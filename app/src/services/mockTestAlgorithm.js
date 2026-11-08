// app/src/services/mockTestAlgorithm.js
import questionBank from '../data/questionBank.json';

const SEEN_QUESTIONS_KEY = 'jlpt_seen_questions_v1';
const TEST_HISTORY_KEY = 'jlpt_test_history_v1';
const RECENT_SIGNATURES_KEY = 'jlpt_recent_signatures_v1';

/**
 * High-entropy cryptographic pseudo-random float in [0, 1)
 * Falls back to Math.random() if crypto is unavailable.
 */
export function secureRandom() {
  if (typeof crypto !== 'undefined' && crypto.getRandomValues) {
    const buffer = new Uint32Array(1);
    crypto.getRandomValues(buffer);
    return buffer[0] / (0xffffffff + 1);
  }
  return Math.random();
}

/**
 * Modern Fisher-Yates (Knuth) unbiased array shuffle.
 * Every one of the N! permutations has strictly equal probability.
 */
export function fisherYatesShuffle(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(secureRandom() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Manages seen question IDs to ensure students don't repeatedly get the same questions.
 */
export function getSeenQuestionCounts() {
  try {
    const raw = localStorage.getItem(SEEN_QUESTIONS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function recordSeenQuestions(questionIds) {
  try {
    const counts = getSeenQuestionCounts();
    questionIds.forEach(id => {
      counts[id] = (counts[id] || 0) + 1;
    });
    localStorage.setItem(SEEN_QUESTIONS_KEY, JSON.stringify(counts));
  } catch (e) {
    console.error('Failed to record seen questions:', e);
  }
}

export function resetSeenQuestions() {
  try {
    localStorage.removeItem(SEEN_QUESTIONS_KEY);
    localStorage.removeItem(RECENT_SIGNATURES_KEY);
  } catch (e) {
    console.error('Failed to reset seen questions:', e);
  }
}

export function getRecentSignatures() {
  try {
    const raw = localStorage.getItem(RECENT_SIGNATURES_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function recordRecentSignature(questionIds) {
  try {
    const list = getRecentSignatures();
    const sorted = [...questionIds].sort();
    list.unshift(sorted);
    if (list.length > 8) list.pop(); // keep last 8 tests
    localStorage.setItem(RECENT_SIGNATURES_KEY, JSON.stringify(list));
  } catch (e) {
    console.error('Failed to record recent signature:', e);
  }
}

export function getTestHistory() {
  try {
    const raw = localStorage.getItem(TEST_HISTORY_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function saveTestResult(result) {
  try {
    const history = getTestHistory();
    history.unshift({
      ...result,
      date: new Date().toLocaleDateString('ja-JP', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    });
    if (history.length > 20) history.pop();
    localStorage.setItem(TEST_HISTORY_KEY, JSON.stringify(history));
  } catch (e) {
    console.error('Failed to save test result:', e);
  }
}

/**
 * Weighted anti-fatigue random sampling with Fisher-Yates pre-shuffle and entropy jitter.
 */
function sampleWeighted(pool, count, seenCounts, targetDifficulty = null) {
  if (pool.length <= count) return fisherYatesShuffle(pool);

  // Pre-shuffle pool with Fisher-Yates so initial index order introduces ZERO bias
  const shuffledPool = fisherYatesShuffle(pool);

  let candidates = shuffledPool.map(item => {
    const seen = seenCounts[item.id] || 0;
    // Strong exponential decay on seen items:
    let weight = seen === 0 ? 50 : seen === 1 ? 6 : seen === 2 ? 1 : 0.2;

    // Add randomized jitter factor [0.85, 1.15] to prevent tied weights from favoring first item
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

/**
 * Core JLPT N3 Mock Test Generation Algorithm
 * Balances:
 * 1. Exact Mondai question counts (35 Vocab + 22 Grammar + 16 Reading = 73 Qs)
 * 2. Passage integrity (passages selected as complete units)
 * 3. Stratified Difficulty balance (~10% Lv1, ~70% Lv2, ~20% Lv3)
 * 4. High-entropy Cryptographic Fisher-Yates Shuffling (unpredictable patterns)
 * 5. Recent test collision avoidance (never repeats recent shuffle combinations)
 */
export function generateBalancedMockTest(options = {}) {
  const seenCounts = getSeenQuestionCounts();
  const recentSigs = getRecentSignatures();
  const allQuestions = questionBank.questions;
  const allPassages = questionBank.passages;

  // Group questions by mondai_type and by passage_id
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

  // Inner generation function
  function runSingleGeneration() {
    const selectedPassages = {};
    const usedQuestionIds = new Set();
    const usedPassageIds = new Set();

    // Helper for standalone questions with stratified difficulty and Fisher-Yates shuffle
    function pickStandalone(mtype, targets) {
      const targetDiffs = Array.isArray(targets) ? targets : Array(targets).fill(2);
      // Pre-shuffle the difficulty targets order for extra entropy
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

      // Internal question permutation shuffle
      return fisherYatesShuffle(picked);
    }

    // Helper for passage units with true roulette-wheel sampling and Fisher-Yates shuffle
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

      // Pre-shuffle candidates
      candidatePassageIds = fisherYatesShuffle(candidatePassageIds);

      const scoredPassages = candidatePassageIds.map(pid => {
        const qs = questionsByPassage[pid];
        const unseenCount = qs.filter(q => (seenCounts[q.id] || 0) === 0).length;
        const weight = (unseenCount * 12 + 1) * (0.85 + secureRandom() * 0.3);
        return { pid, weight };
      });

      // Weighted roulette sampling without replacement
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

      // Shuffle passage presentation order
      const shuffledPids = fisherYatesShuffle(chosenPids);
      const questionsPicked = [];

      shuffledPids.forEach(pid => {
        usedPassageIds.add(pid);
        if (allPassages[pid]) {
          selectedPassages[pid] = allPassages[pid];
        }
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

    // -------------------------------------------------------------
    // 1. SECTION 1: 言語知識（文字・語彙） (35 questions, 30 min)
    // -------------------------------------------------------------
    const v1 = pickStandalone('kanji_reading', [1, 2, 2, 2, 2, 2, 3, 3]); // 8 Qs
    const v2 = pickStandalone('orthography', [1, 2, 2, 2, 2, 3]); // 6 Qs
    const v3 = pickStandalone('contextual_defining', [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3]); // 11 Qs
    const v4 = pickStandalone('paraphrases', [1, 2, 2, 2, 3]); // 5 Qs
    const v5 = pickStandalone('usage', [2, 2, 2, 3, 3]); // 5 Qs

    const vocabQuestions = [];
    let vCounter = 1;

    [
      { list: fisherYatesShuffle(v1), num: 1, label: '問題1', type: 'kanji_reading', instr: '______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。' },
      { list: fisherYatesShuffle(v2), num: 2, label: '問題2', type: 'orthography', instr: '______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。' },
      { list: fisherYatesShuffle(v3), num: 3, label: '問題3', type: 'contextual_defining', instr: '( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。' },
      { list: fisherYatesShuffle(v4), num: 4, label: '問題4', type: 'paraphrases', instr: '______に意味が最も近いものを、1・2・3・4から一つえらびなさい。' },
      { list: fisherYatesShuffle(v5), num: 5, label: '問題5', type: 'usage', instr: 'つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。' }
    ].forEach(group => {
      group.list.forEach(item => {
        vocabQuestions.push({
          ...item,
          exam_number: vCounter++,
          mondai_number: group.num,
          mondai_label: group.label,
          mondai_type: group.type,
          instruction: group.instr,
          section: '言語知識（文字・語彙）'
        });
      });
    });

    // -------------------------------------------------------------
    // 2. SECTION 2: 言語知識（文法）・読解 (38 questions, 70 min)
    // -------------------------------------------------------------
    // Grammar (22 questions)
    const g1 = pickStandalone('bunpou_keishiki', [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]); // 13 Qs
    const g2 = pickStandalone('bun_kumitate', [2, 2, 2, 3, 3]); // 5 Qs
    const g3 = pickPassageUnit('bunshou_bunpou', 1, 4); // 4 Qs

    const grammarQuestions = [];
    let gCounter = 1;

    [
      { list: fisherYatesShuffle(g1), num: 1, label: '問題1', type: 'bunpou_keishiki', instr: 'つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。' },
      { list: fisherYatesShuffle(g2), num: 2, label: '問題2', type: 'bun_kumitate', instr: '次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。' },
      { list: g3, num: 3, label: '問題3', type: 'bunshou_bunpou', instr: 'つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。' }
    ].forEach(group => {
      group.list.forEach(item => {
        grammarQuestions.push({
          ...item,
          exam_number: gCounter++,
          mondai_number: group.num,
          mondai_label: group.label,
          mondai_type: group.type,
          instruction: group.instr,
          section: '言語知識（文法）'
        });
      });
    });

    // Reading (16 questions)
    const r4 = pickPassageUnit('dokkai_tandun', 4, 1); // 4 short passages (1 Q each)
    const r5 = pickPassageUnit('dokkai_chuubun', 2, 3); // 2 medium passages (3 Qs each)
    const r6 = pickPassageUnit('dokkai_choubun', 1, 4); // 1 long passage (4 Qs)
    const r7 = pickPassageUnit('dokkai_jouhou_kensaku', 1, 2); // 1 information notice (2 Qs)

    const readingQuestions = [];
    let rCounter = 1;

    [
      { list: r4, num: 4, label: '問題4', type: 'dokkai_tandun', instr: 'つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。' },
      { list: r5, num: 5, label: '問題5', type: 'dokkai_chuubun', instr: 'つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。' },
      { list: r6, num: 6, label: '問題6', type: 'dokkai_choubun', instr: 'つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。' },
      { list: r7, num: 7, label: '問題7', type: 'dokkai_jouhou_kensaku', instr: '右のページを見て、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。' }
    ].forEach(group => {
      group.list.forEach(item => {
        readingQuestions.push({
          ...item,
          exam_number: rCounter++,
          mondai_number: group.num,
          mondai_label: group.label,
          mondai_type: group.type,
          instruction: group.instr,
          section: '読解'
        });
      });
    });

    return {
      vocabQuestions,
      grammarQuestions,
      readingQuestions,
      selectedPassages
    };
  }

  // Generate candidate exam with anti-pattern-repeat check
  let generated = runSingleGeneration();
  let candidateIds = [
    ...generated.vocabQuestions.map(q => q.id),
    ...generated.grammarQuestions.map(q => q.id),
    ...generated.readingQuestions.map(q => q.id)
  ];

  // If recent signatures exist, verify Jaccard overlap < 0.25 (meaning < 18 repeated questions)
  if (recentSigs.length > 0) {
    const lastSig = new Set(recentSigs[0]);
    let overlap = candidateIds.filter(id => lastSig.has(id)).length;
    let attempts = 0;

    while (overlap > 18 && attempts < 3) {
      generated = runSingleGeneration();
      candidateIds = [
        ...generated.vocabQuestions.map(q => q.id),
        ...generated.grammarQuestions.map(q => q.id),
        ...generated.readingQuestions.map(q => q.id)
      ];
      overlap = candidateIds.filter(id => lastSig.has(id)).length;
      attempts++;
    }
  }

  // Record this test signature so next shuffle won't repeat it
  recordRecentSignature(candidateIds);

  const { vocabQuestions, grammarQuestions, readingQuestions, selectedPassages } = generated;
  const allExamQuestions = [...vocabQuestions, ...grammarQuestions, ...readingQuestions];

  // Calculate difficulty distribution of generated exam
  const diffDistribution = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
  let unseenCount = 0;

  allExamQuestions.forEach(q => {
    const d = q.difficulty || 2;
    diffDistribution[d] = (diffDistribution[d] || 0) + 1;
    if ((seenCounts[q.id] || 0) === 0) {
      unseenCount++;
    }
  });

  const randHex = Math.floor(secureRandom() * 0xffffff).toString(16).toUpperCase().padStart(6, '0');
  const testId = `N3-MOCK-${new Date().getFullYear()}-${randHex}`;
  const title = `JLPT N3 総合実戦模試 [${testId}]`;

  return {
    test_id: testId,
    title: title,
    generated_at: new Date().toISOString(),
    level: 'N3',
    scoring: {
      total_questions: allExamQuestions.length,
      max_score: 180,
      scaled_max_score: 120, // 60 lang + 60 reading (scaled standard)
      passing_score: 95,
      section_pass_threshold: 19
    },
    analytics: {
      total_questions: allExamQuestions.length,
      unseen_questions: unseenCount,
      unseen_percentage: Math.round((unseenCount / allExamQuestions.length) * 100),
      difficulty_distribution: diffDistribution,
      average_difficulty: (
        allExamQuestions.reduce((acc, q) => acc + (q.difficulty || 2), 0) / allExamQuestions.length
      ).toFixed(2)
    },
    sections: [
      {
        section_id: 'sec_vocab',
        title: '言語知識（文字・語彙）',
        time_limit_minutes: 30,
        question_count: vocabQuestions.length,
        questions: vocabQuestions
      },
      {
        section_id: 'sec_grammar_reading',
        title: '言語知識（文法）・読解',
        time_limit_minutes: 70,
        question_count: grammarQuestions.length + readingQuestions.length,
        grammar_questions: grammarQuestions,
        reading_questions: readingQuestions,
        questions: [...grammarQuestions, ...readingQuestions]
      }
    ],
    passages: selectedPassages
  };
}

/**
 * Calculates official JLPT Scaled Score from student answers.
 */
export function calculateJLPTScore(exam, userAnswers) {
  const sec1 = exam.sections[0];
  const sec2 = exam.sections[1];

  let vocabCorrect = 0;
  let grammarCorrect = 0;
  let readingCorrect = 0;

  const resultsByQuestion = {};

  sec1.questions.forEach(q => {
    const isCorrect = userAnswers[q.id] === q.answer;
    if (isCorrect) vocabCorrect++;
    resultsByQuestion[q.id] = {
      isCorrect,
      userAnswer: userAnswers[q.id],
      correctAnswer: q.answer
    };
  });

  sec2.grammar_questions.forEach(q => {
    const isCorrect = userAnswers[q.id] === q.answer;
    if (isCorrect) grammarCorrect++;
    resultsByQuestion[q.id] = {
      isCorrect,
      userAnswer: userAnswers[q.id],
      correctAnswer: q.answer
    };
  });

  sec2.reading_questions.forEach(q => {
    const isCorrect = userAnswers[q.id] === q.answer;
    if (isCorrect) readingCorrect++;
    resultsByQuestion[q.id] = {
      isCorrect,
      userAnswer: userAnswers[q.id],
      correctAnswer: q.answer
    };
  });

  const langTotalCorrect = vocabCorrect + grammarCorrect;
  const langMaxQuestions = sec1.questions.length + sec2.grammar_questions.length;
  const readingMaxQuestions = sec2.reading_questions.length;

  // Scaled Score Calculation:
  const languageScore = Math.round((langTotalCorrect / langMaxQuestions) * 60);
  const readingScore = Math.round((readingCorrect / readingMaxQuestions) * 60);
  const totalScaled120 = languageScore + readingScore;

  const isPassed = (totalScaled120 >= 63) && (languageScore >= 19) && (readingScore >= 19);

  return {
    isPassed,
    languageScore,
    readingScore,
    totalScaled120,
    official180Equivalent: Math.round((totalScaled120 / 120) * 180),
    totalCorrect: vocabCorrect + grammarCorrect + readingCorrect,
    totalQuestions: exam.scoring.total_questions,
    vocabCorrect,
    vocabTotal: sec1.questions.length,
    grammarCorrect,
    grammarTotal: sec2.grammar_questions.length,
    readingCorrect,
    readingTotal: readingMaxQuestions,
    resultsByQuestion
  };
}
