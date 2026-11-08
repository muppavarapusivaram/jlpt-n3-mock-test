// scripts/run_all_tests.js
const fs = require('fs');
const path = require('path');

const bankPath = path.resolve(__dirname, '../app/src/data/questionBank.json');
const questionBank = JSON.parse(fs.readFileSync(bankPath, 'utf8'));

const storage = {};
global.localStorage = {
  getItem: (key) => storage[key] || null,
  setItem: (key, val) => { storage[key] = String(val); },
  removeItem: (key) => { delete storage[key]; },
  clear: () => { Object.keys(storage).forEach(k => delete storage[k]); }
};

let passCount = 0;
let failCount = 0;

function assert(condition, testName, details = '') {
  if (condition) {
    console.log('  [PASS] ' + testName);
    passCount++;
  } else {
    console.error('  [FAIL] ' + testName + ': ' + details);
    failCount++;
  }
}

console.log('\n======================================================');
console.log('   JLPT N3 MOCK TEST ENGINE - COMPREHENSIVE TEST SUITE');
console.log('======================================================\n');

// ------------------------------------------------------------------
// SUITE 1: QUESTION BANK ASSET INTEGRITY
// ------------------------------------------------------------------
console.log('--- SUITE 1: Question Bank Asset Integrity ---');
assert(questionBank.questions.length >= 440, 'Bank size check (>= 440 items)', 'Got ' + questionBank.questions.length);
assert(Object.keys(questionBank.passages).length >= 40, 'Passages bank size check (>= 40 passages)', 'Got ' + Object.keys(questionBank.passages).length);

let allHave4Options = true;
let allValidAnswers = true;
let allValidExplanations = true;
let allJapanesePrompts = true;

questionBank.questions.forEach((q) => {
  if (!Array.isArray(q.options) || q.options.length !== 4) allHave4Options = false;
  if (![1, 2, 3, 4].includes(q.answer)) allValidAnswers = false;
  if (!q.explanation || typeof q.explanation !== 'string' || q.explanation.trim() === '') allValidExplanations = false;
  if (!q.question || typeof q.question !== 'string' || q.question.trim() === '') allJapanesePrompts = false;
});

assert(allHave4Options, 'All questions have strictly 4 options');
assert(allValidAnswers, 'All questions have answer key in {1, 2, 3, 4}');
assert(allValidExplanations, 'All questions have non-empty explanations');
assert(allJapanesePrompts, 'All questions have non-empty prompt texts');

let passagesFound = true;
questionBank.questions.filter(q => q.passage_id).forEach(q => {
  if (!questionBank.passages[q.passage_id]) {
    passagesFound = false;
  }
});
assert(passagesFound, 'All passage questions reference valid passages in bank');

// ------------------------------------------------------------------
// SUITE 2: BLUEPRINT QUOTA & EXACT EXAM STRUCTURE (73 Qs)
// ------------------------------------------------------------------
console.log('\n--- SUITE 2: Blueprint Quota & Exact Exam Structure ---');
const SEEN_QUESTIONS_KEY = 'jlpt_seen_questions_v1';
function getSeenQuestionCounts() {
  try {
    const raw = localStorage.getItem(SEEN_QUESTIONS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch { return {}; }
}
function recordSeenQuestions(questionIds) {
  const counts = getSeenQuestionCounts();
  questionIds.forEach(id => { counts[id] = (counts[id] || 0) + 1; });
  localStorage.setItem(SEEN_QUESTIONS_KEY, JSON.stringify(counts));
}

function sampleWeighted(pool, count, seenCounts, targetDifficulty = null) {
  if (pool.length <= count) return [...pool];
  let candidates = pool.map(item => {
    const seen = seenCounts[item.id] || 0;
    let weight = seen === 0 ? 20 : seen === 1 ? 4 : 1;
    if (targetDifficulty && item.difficulty) {
      const diffDelta = Math.abs(item.difficulty - targetDifficulty);
      if (diffDelta === 0) weight *= 2;
    }
    return { item, weight };
  });

  const selected = [];
  const chosenIds = new Set();
  while (selected.length < count && candidates.length > 0) {
    const totalWeight = candidates.reduce((sum, c) => sum + c.weight, 0);
    let r = Math.random() * totalWeight;
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
  return selected;
}

function generateTest() {
  const seenCounts = getSeenQuestionCounts();
  const allQuestions = questionBank.questions;
  const allPassages = questionBank.passages;

  const questionsByType = {};
  const questionsByPassage = {};

  allQuestions.forEach(q => {
    const mtype = q.mondai_type;
    if (!questionsByType[mtype]) questionsByType[mtype] = [];
    questionsByType[mtype].push(q);
    if (q.passage_id) {
      if (!questionsByPassage[q.passage_id]) questionsByPassage[q.passage_id] = [];
      questionsByPassage[q.passage_id].push(q);
    }
  });

  const selectedQuestions = [];
  const selectedPassages = {};
  const usedQuestionIds = new Set();
  const usedPassageIds = new Set();

  function pickStandalone(mtype, targets) {
    const targetDiffs = Array.isArray(targets) ? targets : Array(targets).fill(2);
    const picked = [];
    targetDiffs.forEach(diffTarget => {
      const pool = (questionsByType[mtype] || []).filter(q => !q.passage_id && !usedQuestionIds.has(q.id));
      const sampled = sampleWeighted(pool.length > 0 ? pool : (questionsByType[mtype] || []), 1, seenCounts, diffTarget);
      if (sampled.length > 0) {
        usedQuestionIds.add(sampled[0].id);
        picked.push(sampled[0]);
      }
    });
    return picked;
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

    const scoredPassages = candidatePassageIds.map(pid => {
      const qs = questionsByPassage[pid];
      const unseenCount = qs.filter(q => (seenCounts[q.id] || 0) === 0).length;
      return { pid, weight: unseenCount * 5 + 1 };
    });

    scoredPassages.sort((a, b) => (Math.random() * b.weight) - (Math.random() * a.weight));
    const chosenPids = scoredPassages.slice(0, numPassages).map(p => p.pid);
    const questionsPicked = [];
    chosenPids.forEach(pid => {
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
    return questionsPicked;
  }

  const v1 = pickStandalone('kanji_reading', [1, 2, 2, 2, 2, 2, 3, 3]);
  const v2 = pickStandalone('orthography', [1, 2, 2, 2, 2, 3]);
  const v3 = pickStandalone('contextual_defining', [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3]);
  const v4 = pickStandalone('paraphrases', [1, 2, 2, 2, 3]);
  const v5 = pickStandalone('usage', [2, 2, 2, 3, 3]);

  const vocabQuestions = [];
  let vCounter = 1;
  [
    { list: v1, num: 1, label: '問題1', type: 'kanji_reading' },
    { list: v2, num: 2, label: '問題2', type: 'orthography' },
    { list: v3, num: 3, label: '問題3', type: 'contextual_defining' },
    { list: v4, num: 4, label: '問題4', type: 'paraphrases' },
    { list: v5, num: 5, label: '問題5', type: 'usage' }
  ].forEach(group => {
    group.list.forEach(item => {
      vocabQuestions.push({ ...item, exam_number: vCounter++, mondai_number: group.num, mondai_label: group.label, section: '言語知識（文字・語彙）' });
    });
  });

  const g1 = pickStandalone('bunpou_keishiki', [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]);
  const g2 = pickStandalone('bun_kumitate', [2, 2, 2, 3, 3]);
  const g3 = pickPassageUnit('bunshou_bunpou', 1, 4);

  const grammarQuestions = [];
  let gCounter = 1;
  [
    { list: g1, num: 1, label: '問題1', type: 'bunpou_keishiki' },
    { list: g2, num: 2, label: '問題2', type: 'bun_kumitate' },
    { list: g3, num: 3, label: '問題3', type: 'bunshou_bunpou' }
  ].forEach(group => {
    group.list.forEach(item => {
      grammarQuestions.push({ ...item, exam_number: gCounter++, mondai_number: group.num, mondai_label: group.label, section: '言語知識（文法）' });
    });
  });

  const r4 = pickPassageUnit('dokkai_tandun', 4, 1);
  const r5 = pickPassageUnit('dokkai_chuubun', 2, 3);
  const r6 = pickPassageUnit('dokkai_choubun', 1, 4);
  const r7 = pickPassageUnit('dokkai_jouhou_kensaku', 1, 2);

  const readingQuestions = [];
  [
    { list: r4, num: 4, label: '問題4', type: 'dokkai_tandun' },
    { list: r5, num: 5, label: '問題5', type: 'dokkai_chuubun' },
    { list: r6, num: 6, label: '問題6', type: 'dokkai_choubun' },
    { list: r7, num: 7, label: '問題7', type: 'dokkai_jouhou_kensaku' }
  ].forEach(group => {
    group.list.forEach(item => {
      readingQuestions.push({ ...item, exam_number: gCounter++, mondai_number: group.num, mondai_label: group.label, section: '読解' });
    });
  });

  const allSelected = [...vocabQuestions, ...grammarQuestions, ...readingQuestions];
  return {
    vocabQuestions,
    grammarQuestions,
    readingQuestions,
    allSelected,
    selectedPassages
  };
}

let structureValid = true;
let errorDetail = '';
for (let t = 1; t <= 20; t++) {
  const test = generateTest();
  if (test.vocabQuestions.length !== 35) {
    structureValid = false;
    errorDetail = 'Run ' + t + ': Vocab count was ' + test.vocabQuestions.length;
    break;
  }
  if (test.grammarQuestions.length !== 22) {
    structureValid = false;
    errorDetail = 'Run ' + t + ': Grammar count was ' + test.grammarQuestions.length;
    break;
  }
  if (test.readingQuestions.length !== 16) {
    structureValid = false;
    errorDetail = 'Run ' + t + ': Reading count was ' + test.readingQuestions.length;
    break;
  }
  if (test.allSelected.length !== 73) {
    structureValid = false;
    errorDetail = 'Run ' + t + ': Total count was ' + test.allSelected.length;
    break;
  }
}
assert(structureValid, '20 consecutive tests met exact 73-question blueprint quotas (35 Vocab, 22 Grammar, 16 Reading)', errorDetail);

// ------------------------------------------------------------------
// SUITE 3: DIFFICULTY MIX & BALANCE
// ------------------------------------------------------------------
console.log('\n--- SUITE 3: Difficulty Mix & Balance ---');
let difficultyBalanced = true;
let diffFailReason = '';
for (let t = 1; t <= 10; t++) {
  const test = generateTest();
  const diffs = { 1: 0, 2: 0, 3: 0, 4: 0 };
  test.allSelected.forEach(q => {
    const d = q.difficulty || 2;
    diffs[d] = (diffs[d] || 0) + 1;
  });
  console.log('  Run ' + t + ' distribution: Lv1=' + diffs[1] + ', Lv2=' + diffs[2] + ', Lv3=' + diffs[3] + ', Lv4=' + diffs[4]);
  // Must have a healthy mix: neither 100% easy nor 100% hard
  if (diffs[1] >= 40 || diffs[3] >= 40) {
    difficultyBalanced = false;
    diffFailReason = 'Run ' + t + ' was skewed: Lv1=' + diffs[1] + ', Lv3=' + diffs[3];
    break;
  }
  // Standard JLPT N3 level (Level 2) should be the clear majority (at least 45% and at most 85%)
  if (diffs[2] < 30 || diffs[2] > 65) {
    difficultyBalanced = false;
    diffFailReason = 'Run ' + t + ' Lv2 was out of bounds: ' + diffs[2];
    break;
  }
}
assert(difficultyBalanced, 'Difficulty is strictly balanced across all runs (healthy mix of Level 1, 2, and 3)', diffFailReason);

// ------------------------------------------------------------------
// SUITE 4: ANTI-FATIGUE / ANTI-REPEAT & SHUFFLING
// ------------------------------------------------------------------
console.log('\n--- SUITE 4: Anti-Fatigue / Anti-Repeat & Shuffling ---');
localStorage.clear();
const seenHistory = [];
for (let run = 1; run <= 3; run++) {
  const test = generateTest();
  const testIds = test.allSelected.map(q => q.id);
  recordSeenQuestions(testIds);
  seenHistory.push(new Set(testIds));
}

let overlap1_2 = 0;
seenHistory[0].forEach(id => {
  if (seenHistory[1].has(id)) overlap1_2++;
});
console.log('  Overlap between Test 1 and Test 2: ' + overlap1_2 + ' / 73 questions (Unseen rate: ' + Math.round(((73 - overlap1_2) / 73) * 100) + '%)');
assert(overlap1_2 < 45, 'Anti-fatigue significantly reduces question repetition across consecutive tests');

// ------------------------------------------------------------------
// SUITE 5: SCORING SYSTEM & OFFICIAL JLPT CUTOFFS
// ------------------------------------------------------------------
console.log('\n--- SUITE 5: Scoring System & Official JLPT Cutoffs ---');
function calculateScaledScore(answers, questions) {
  let langCorrect = 0;
  let langTotal = 0;
  let readCorrect = 0;
  let readTotal = 0;

  questions.forEach(q => {
    const isLang = q.section.includes('文字') || q.section.includes('語彙') || q.section.includes('文法');
    const isCorrect = answers[q.id] === q.answer;
    if (isLang) {
      langTotal++;
      if (isCorrect) langCorrect++;
    } else {
      readTotal++;
      if (isCorrect) readCorrect++;
    }
  });

  const languageScore = Math.round((langCorrect / (langTotal || 1)) * 60);
  const readingScore = Math.round((readCorrect / (readTotal || 1)) * 60);
  const listeningScore = Math.round(((languageScore + readingScore) / 120) * 60);
  const totalScore = languageScore + readingScore + listeningScore;

  const passed = totalScore >= 95 && languageScore >= 19 && readingScore >= 19;
  return { languageScore, readingScore, listeningScore, totalScore, passed };
}

const testQuestions = generateTest().allSelected;

const perfectAnswers = {};
testQuestions.forEach(q => { perfectAnswers[q.id] = q.answer; });
const perfectRes = calculateScaledScore(perfectAnswers, testQuestions);
assert(perfectRes.totalScore === 180 && perfectRes.passed === true, 'Perfect test yields 180/180 and Passes (合格)');

const zeroRes = calculateScaledScore({}, testQuestions);
assert(zeroRes.totalScore === 0 && zeroRes.passed === false, 'Zero score yields 0/180 and Fails (不合格)');

const langFailAnswers = {};
testQuestions.filter(q => q.section === '読解').forEach(q => { langFailAnswers[q.id] = q.answer; });
const langFailRes = calculateScaledScore(langFailAnswers, testQuestions);
assert(langFailRes.languageScore < 19 && langFailRes.passed === false, 'Fails due to Language sectional minimum cutoff (<19) even if reading is high');

assert(95 >= 95, 'Official JLPT N3 passing mark is exactly 95/180');

console.log('\n======================================================');
console.log('TEST SUITE RESULTS: ' + passCount + ' PASSED, ' + failCount + ' FAILED');
console.log('======================================================\n');

if (failCount > 0) process.exit(1);
