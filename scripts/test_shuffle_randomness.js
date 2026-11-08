// scripts/test_shuffle_randomness.js
const fs = require('fs');
const path = require('path');

const bankPath = path.resolve(__dirname, '../app/src/data/questionBank.json');
const questionBank = JSON.parse(fs.readFileSync(bankPath, 'utf8'));

// Mock localStorage
const storage = {};
global.localStorage = {
  getItem: (key) => storage[key] || null,
  setItem: (key, val) => { storage[key] = String(val); },
  removeItem: (key) => { delete storage[key]; },
  clear: () => { Object.keys(storage).forEach(k => delete storage[k]); }
};

// Cryptographic random float
function secureRandom() {
  if (typeof crypto !== 'undefined' && crypto.getRandomValues) {
    const buffer = new Uint32Array(1);
    crypto.getRandomValues(buffer);
    return buffer[0] / (0xffffffff + 1);
  }
  return Math.random();
}

function fisherYatesShuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(secureRandom() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

const SEEN_QUESTIONS_KEY = 'jlpt_seen_questions_v1';
const RECENT_SIGNATURES_KEY = 'jlpt_recent_signatures_v1';

function getSeenQuestionCounts() {
  try {
    const raw = localStorage.getItem(SEEN_QUESTIONS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch { return {}; }
}

function getRecentSignatures() {
  try {
    const raw = localStorage.getItem(RECENT_SIGNATURES_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch { return []; }
}

function recordRecentSignature(questionIds) {
  const list = getRecentSignatures();
  list.unshift([...questionIds].sort());
  if (list.length > 8) list.pop();
  localStorage.setItem(RECENT_SIGNATURES_KEY, JSON.stringify(list));
}

function sampleWeighted(pool, count, seenCounts, targetDifficulty = null) {
  if (pool.length <= count) return fisherYatesShuffle(pool);
  const shuffledPool = fisherYatesShuffle(pool);

  let candidates = shuffledPool.map(item => {
    const seen = seenCounts[item.id] || 0;
    let weight = seen === 0 ? 50 : seen === 1 ? 6 : seen === 2 ? 1 : 0.2;
    weight *= (0.85 + secureRandom() * 0.3);
    if (targetDifficulty && item.difficulty) {
      const diffDelta = Math.abs(item.difficulty - targetDifficulty);
      if (diffDelta === 0) weight *= 2.5;
      else if (diffDelta === 1) weight *= 1.0;
      else weight *= 0.3;
    }
    return { item, weight };
  });

  const selected = [];
  const chosenIds = new Set();
  while (selected.length < count && candidates.length > 0) {
    const totalWeight = candidates.reduce((sum, c) => sum + c.weight, 0);
    let r = secureRandom() * totalWeight;
    let pickedIdx = 0;
    for (let i = 0; i < candidates.length; i++) {
      r -= candidates[i].weight;
      if (r <= 0) {
        pickedIdx = i;
        break;
      }
    }
    const picked = candidates[pickedIdx].item;
    if (!chosenIds.has(picked.id)) {
      chosenIds.add(picked.id);
      selected.push(picked);
    }
    candidates.splice(pickedIdx, 1);
  }
  return fisherYatesShuffle(selected);
}

function generateTest() {
  const seenCounts = getSeenQuestionCounts();
  const recentSigs = getRecentSignatures();
  const allQuestions = questionBank.questions;
  const allPassages = questionBank.passages;

  const questionsByType = {};
  const questionsByPassage = {};
  allQuestions.forEach(q => {
    const m = q.mondai_type;
    if (!questionsByType[m]) questionsByType[m] = [];
    questionsByType[m].push(q);
    if (q.passage_id) {
      if (!questionsByPassage[q.passage_id]) questionsByPassage[q.passage_id] = [];
      questionsByPassage[q.passage_id].push(q);
    }
  });

  function runSingle() {
    const selectedPassages = {};
    const usedQuestionIds = new Set();
    const usedPassageIds = new Set();

    function pickStandalone(mtype, targets) {
      const targetDiffs = Array.isArray(targets) ? targets : Array(targets).fill(2);
      const shuffledDiffs = fisherYatesShuffle(targetDiffs);
      const picked = [];
      shuffledDiffs.forEach(diffTarget => {
        const pool = (questionsByType[mtype] || []).filter(q => !q.passage_id && !usedQuestionIds.has(q.id));
        const sampled = sampleWeighted(pool.length > 0 ? pool : (questionsByType[mtype] || []), 1, seenCounts, diffTarget);
        if (sampled.length > 0) {
          usedQuestionIds.add(sampled[0].id);
          picked.push(sampled[0]);
        }
      });
      return fisherYatesShuffle(picked);
    }

    function pickPassageUnit(mtype, numPassages, exactQsPerPassage = null) {
      let candidatePassageIds = Object.keys(questionsByPassage).filter(pid => {
        if (usedPassageIds.has(pid)) return false;
        const qs = questionsByPassage[pid];
        if (qs.length === 0 || qs[0].mondai_type !== mtype) return false;
        if (exactQsPerPassage && qs.length !== exactQsPerPassage) return false;
        return true;
      });

      if (candidatePassageIds.length < numPassages) {
        candidatePassageIds = Object.keys(questionsByPassage).filter(pid => {
          if (usedPassageIds.has(pid)) return false;
          const qs = questionsByPassage[pid];
          return qs.length > 0 && qs[0].mondai_type === mtype;
        });
      }

      candidatePassageIds = fisherYatesShuffle(candidatePassageIds);
      const scoredPassages = candidatePassageIds.map(pid => {
        const qs = questionsByPassage[pid];
        const unseenCount = qs.filter(q => (seenCounts[q.id] || 0) === 0).length;
        const weight = (unseenCount * 12 + 1) * (0.85 + secureRandom() * 0.3);
        return { pid, weight };
      });

      const pool = [...scoredPassages];
      const chosenPids = [];
      while (chosenPids.length < numPassages && pool.length > 0) {
        const totalWeight = pool.reduce((sum, p) => sum + p.weight, 0);
        let r = secureRandom() * totalWeight;
        let pickedIdx = 0;
        for (let i = 0; i < pool.length; i++) {
          r -= pool[i].weight;
          if (r <= 0) {
            pickedIdx = i;
            break;
          }
        }
        chosenPids.push(pool[pickedIdx].pid);
        pool.splice(pickedIdx, 1);
      }

      const shuffledPids = fisherYatesShuffle(chosenPids);
      const questionsPicked = [];
      shuffledPids.forEach(pid => {
        usedPassageIds.add(pid);
        if (allPassages[pid]) selectedPassages[pid] = allPassages[pid];
        let qs = questionsByPassage[pid] || [];
        if (exactQsPerPassage && qs.length > exactQsPerPassage) {
          qs = qs.slice(0, exactQsPerPassage);
        }
        qs.forEach(q => {
          usedQuestionIds.add(q.id);
          questionsPicked.push(q);
        });
      });
      return { questionsPicked, pids: shuffledPids };
    }

    const v1 = pickStandalone('kanji_reading', [1, 2, 2, 2, 2, 2, 3, 3]);
    const v2 = pickStandalone('orthography', [1, 2, 2, 2, 2, 3]);
    const v3 = pickStandalone('contextual_defining', [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3]);
    const v4 = pickStandalone('paraphrases', [1, 2, 2, 2, 3]);
    const v5 = pickStandalone('usage', [2, 2, 2, 3, 3]);

    const g1 = pickStandalone('bunpou_keishiki', [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]);
    const g2 = pickStandalone('bun_kumitate', [2, 2, 2, 3, 3]);
    const g3 = pickPassageUnit('bunshou_bunpou', 1, 4);

    const r4 = pickPassageUnit('dokkai_tandun', 4, 1);
    const r5 = pickPassageUnit('dokkai_chuubun', 2, 3);
    const r6 = pickPassageUnit('dokkai_choubun', 1, 4);
    const r7 = pickPassageUnit('dokkai_jouhou_kensaku', 1, 2);

    const all = [
      ...v1, ...v2, ...v3, ...v4, ...v5,
      ...g1, ...g2, ...g3.questionsPicked,
      ...r4.questionsPicked, ...r5.questionsPicked, ...r6.questionsPicked, ...r7.questionsPicked
    ];

    return { all, r4Pids: r4.pids, v1FirstQ: v1[0].id };
  }

  let gen = runSingle();
  let ids = gen.all.map(q => q.id);

  if (recentSigs.length > 0) {
    const lastSig = new Set(recentSigs[0]);
    let overlap = ids.filter(id => lastSig.has(id)).length;
    let attempts = 0;
    while (overlap > 18 && attempts < 3) {
      gen = runSingle();
      ids = gen.all.map(q => q.id);
      overlap = ids.filter(id => lastSig.has(id)).length;
      attempts++;
    }
  }

  recordRecentSignature(ids);
  return { all: gen.all, ids, r4Pids: gen.r4Pids, v1FirstQ: gen.v1FirstQ };
}

console.log('\n======================================================');
console.log('   SHUFFLE RANDOMNESS & COLLISION AVOIDANCE TEST');
console.log('======================================================\n');

const runs = [];
for (let i = 1; i <= 6; i++) {
  const t = generateTest();
  runs.push(t);
  console.log(`[Shuffle ${i}] Generated 73 Qs. Kanji Q1 ID: ${t.v1FirstQ}, Short Passages: [${t.r4Pids.join(', ')}]`);
}

console.log('\n--- Overlap Matrix between Consecutive Shuffles ---');
let maxConsecutiveOverlap = 0;
for (let i = 0; i < runs.length - 1; i++) {
  const setA = new Set(runs[i].ids);
  const setB = runs[i + 1].ids;
  const overlap = setB.filter(id => setA.has(id)).length;
  if (overlap > maxConsecutiveOverlap) maxConsecutiveOverlap = overlap;
  const uniqueness = Math.round(((73 - overlap) / 73) * 100);
  console.log(`  Shuffle ${i + 1} ➔ Shuffle ${i + 2}: ${overlap} overlapping questions (${uniqueness}% unique new questions)`);
}

console.log(`\nMax Overlap observed: ${maxConsecutiveOverlap} / 73`);
console.log(`Collision Avoidance Guard: ${maxConsecutiveOverlap <= 18 ? 'PASSED (Strictly <= 18)' : 'FAILED'}`);

// Test passage order randomness
const passageOrders = runs.map(r => r.r4Pids.join(';'));
const uniquePassageOrders = new Set(passageOrders).size;
console.log(`Unique short-passage presentation orders: ${uniquePassageOrders} / ${runs.length}`);

console.log('\n======================================================\n');
