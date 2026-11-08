# -*- coding: utf-8 -*-
"""
mock_test_generator.py
Algorithm & engine for assembling authentic, balanced JLPT N3 Mock Exams
conforming strictly to the official JLPT N3 blueprint:

Section 1: 言語知識（文字・語彙） (30 minutes)
  - 問題1 (漢字読み): 8 questions (kanji_reading)
  - 問題2 (表記): 6 questions (orthography)
  - 問題3 (文脈規定): 11 questions (contextual_defining)
  - 問題4 (言い換え類義): 5 questions (paraphrases)
  - 問題5 (用法): 5 questions (usage)
  Total Section 1 = 35 questions

Section 2: 言語知識（文法）・読解 (70 minutes)
  文法:
    - 問題1 (文法形式の判断): 13 questions (bunpou_keishiki)
    - 問題2 (文の組み立て ★): 5 questions (bun_kumitate)
    - 問題3 (文章の文法): 4 questions (bunshou_bunpou, 1 passage)
  読解:
    - 問題4 (短文読解): 4 questions (dokkai_tandun, 4 passages)
    - 問題5 (中文読解): 6 questions (dokkai_chuubun, 2 passages of 3 questions each)
    - 問題6 (長文読解): 4 questions (dokkai_choubun, 1 passage of 4 questions)
    - 問題7 (情報検索): 2 questions (dokkai_jouhou_kensaku, 1 notice/flyer with 2 questions)
  Total Section 2 = 38 questions

Total Exam = Exactly 73 questions (Listening excluded per specification).
"""

import os
import sys
import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional

BANK_DIR = Path("bank")

class JLPTMockTestGenerator:
    def __init__(self, bank_dir: Path = BANK_DIR):
        self.bank_dir = bank_dir
        self.passages: Dict[str, Any] = {}
        self.questions_by_type: Dict[str, List[Dict[str, Any]]] = {}
        self.passages_by_type: Dict[str, List[str]] = {}
        self.questions_by_passage: Dict[str, List[Dict[str, Any]]] = {}
        self.load_bank()

    def load_bank(self):
        """Loads all questions and passages from the bank directory."""
        # 1. Load Passages
        for pfile in self.bank_dir.glob("**/passages.json"):
            try:
                data = json.loads(pfile.read_text(encoding="utf-8"))
                for pid, pdata in data.items():
                    self.passages[pid] = pdata
            except Exception as e:
                print(f"Warning: Failed to load passage file {pfile}: {e}")

        # 2. Load Questions
        qfiles = [
            f for f in self.bank_dir.glob("**/*.json")
            if f.name not in ["page_map.json", "passages.json", "grammar_points.json", "bank_data.js"]
        ]

        total_loaded = 0
        for qf in qfiles:
            try:
                data = json.loads(qf.read_text(encoding="utf-8"))
                for q in data.get("questions", []):
                    mtype = q.get("mondai_type")
                    if not mtype:
                        continue
                    self.questions_by_type.setdefault(mtype, []).append(q)
                    total_loaded += 1

                    pid = q.get("passage_id")
                    if pid:
                        self.questions_by_passage.setdefault(pid, []).append(q)
            except Exception as e:
                print(f"Warning: Failed to load question file {qf}: {e}")

        # Index passages by question mondai_type
        for pid, qlist in self.questions_by_passage.items():
            if qlist:
                mtype = qlist[0].get("mondai_type")
                if mtype:
                    self.passages_by_type.setdefault(mtype, []).append(pid)

        print(f"Loaded {total_loaded} questions and {len(self.passages)} passages into generator.")

    def sample_standalone(self, mtype: str, count: int, exclude_ids: set, rng: random.Random) -> List[Dict[str, Any]]:
        """Samples questions of a given mondai_type without passages."""
        pool = [q for q in self.questions_by_type.get(mtype, []) if q["id"] not in exclude_ids and not q.get("passage_id")]
        if len(pool) < count:
            # If not enough non-passage, allow any
            pool = [q for q in self.questions_by_type.get(mtype, []) if q["id"] not in exclude_ids]
        
        if len(pool) < count:
            print(f"Notice: Pool for {mtype} has {len(pool)} items; requested {count}. Sampling with replacement or available.")
            chosen = pool[:]
            pool_all = self.questions_by_type.get(mtype, [])
            while len(chosen) < count and pool_all:
                chosen.append(rng.choice(pool_all))
            return chosen

        chosen = rng.sample(pool, count)
        for c in chosen:
            exclude_ids.add(c["id"])
        return chosen

    def sample_passage_group(self, mtype: str, expected_q_count: int, num_passages: int, exclude_passages: set, exclude_ids: set, rng: random.Random) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Samples complete passage units with all their associated questions.
        """
        available_pids = [
            pid for pid in self.passages_by_type.get(mtype, [])
            if pid not in exclude_passages
        ]
        
        if len(available_pids) < num_passages:
            available_pids = self.passages_by_type.get(mtype, [])
        
        selected_pids = rng.sample(available_pids, min(num_passages, len(available_pids)))
        chosen_questions = []
        chosen_passages = {}

        for pid in selected_pids:
            exclude_passages.add(pid)
            chosen_passages[pid] = self.passages[pid]
            qs = [q for q in self.questions_by_passage.get(pid, [])]
            for q in qs:
                exclude_ids.add(q["id"])
                chosen_questions.append(q)

        return chosen_questions, chosen_passages

    def generate_exam(self, test_id: str, title: str, seed: Optional[int] = None) -> Dict[str, Any]:
        """
        Generates a complete JLPT N3 Mock Exam conforming to official blueprint.
        """
        rng = random.Random(seed)
        exclude_ids = set()
        exclude_passages = set()
        test_passages = {}

        # ---------------------------------------------------------
        # Section 1: 言語知識（文字・語彙） (30 minutes, 35 questions)
        # ---------------------------------------------------------
        v_q1 = self.sample_standalone("kanji_reading", 8, exclude_ids, rng)
        v_q2 = self.sample_standalone("orthography", 6, exclude_ids, rng)
        v_q3 = self.sample_standalone("contextual_defining", 11, exclude_ids, rng)
        v_q4 = self.sample_standalone("paraphrases", 5, exclude_ids, rng)
        v_q5 = self.sample_standalone("usage", 5, exclude_ids, rng)

        vocab_list = []
        q_counter = 1
        for group, m_num, m_type, m_lbl, instr in [
            (v_q1, 1, "kanji_reading", "問題1", "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。"),
            (v_q2, 2, "orthography", "問題2", "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。"),
            (v_q3, 3, "contextual_defining", "問題3", "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。"),
            (v_q4, 4, "paraphrases", "問題4", "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。"),
            (v_q5, 5, "usage", "問題5", "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。")
        ]:
            for item in group:
                q_copy = dict(item)
                q_copy["exam_number"] = q_counter
                q_copy["mondai_number"] = m_num
                q_copy["mondai_label"] = m_lbl
                q_copy["mondai_type"] = m_type
                q_copy["instruction"] = instr
                q_copy["section"] = "言語知識（文字・語彙）"
                vocab_list.append(q_copy)
                q_counter += 1

        # ---------------------------------------------------------
        # Section 2: 言語知識（文法）・読解 (70 minutes, 38 questions)
        # ---------------------------------------------------------
        # Grammar
        g_q1 = self.sample_standalone("bunpou_keishiki", 13, exclude_ids, rng)
        g_q2 = self.sample_standalone("bun_kumitate", 5, exclude_ids, rng)
        g_q3, p_g3 = self.sample_passage_group("bunshou_bunpou", 4, 1, exclude_passages, exclude_ids, rng)
        test_passages.update(p_g3)

        grammar_list = []
        g_counter = 1
        for group, m_num, m_type, m_lbl, instr in [
            (g_q1, 1, "bunpou_keishiki", "問題1", "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。"),
            (g_q2, 2, "bun_kumitate", "問題2", "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。"),
            (g_q3, 3, "bunshou_bunpou", "問題3", "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。")
        ]:
            for item in group:
                q_copy = dict(item)
                q_copy["exam_number"] = g_counter
                q_copy["mondai_number"] = m_num
                q_copy["mondai_label"] = m_lbl
                q_copy["mondai_type"] = m_type
                q_copy["instruction"] = instr
                q_copy["section"] = "言語知識（文法）"
                grammar_list.append(q_copy)
                g_counter += 1

        # Reading
        r_q4, p_r4 = self.sample_passage_group("dokkai_tandun", 4, 4, exclude_passages, exclude_ids, rng)
        r_q5, p_r5 = self.sample_passage_group("dokkai_chuubun", 6, 2, exclude_passages, exclude_ids, rng)
        r_q6, p_r6 = self.sample_passage_group("dokkai_choubun", 4, 1, exclude_passages, exclude_ids, rng)
        r_q7, p_r7 = self.sample_passage_group("dokkai_jouhou_kensaku", 2, 1, exclude_passages, exclude_ids, rng)

        test_passages.update(p_r4)
        test_passages.update(p_r5)
        test_passages.update(p_r6)
        test_passages.update(p_r7)

        reading_list = []
        r_counter = 23 # Reading questions in Section 2 start at 23 following grammar 1..22
        for group, m_num, m_type, m_lbl, instr in [
            (r_q4, 4, "dokkai_tandun", "問題4", "つぎの (1) から (4) の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。"),
            (r_q5, 5, "dokkai_chuubun", "問題5", "つぎの (1) と (2) の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。"),
            (r_q6, 6, "dokkai_choubun", "問題6", "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。"),
            (r_q7, 7, "dokkai_jouhou_kensaku", "問題7", "右のページのお知らせ（資料）を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。")
        ]:
            for item in group:
                q_copy = dict(item)
                q_copy["exam_number"] = r_counter
                q_copy["mondai_number"] = m_num
                q_copy["mondai_label"] = m_lbl
                q_copy["mondai_type"] = m_type
                q_copy["instruction"] = instr
                q_copy["section"] = "読解"
                reading_list.append(q_copy)
                r_counter += 1

        exam_data = {
            "test_id": test_id,
            "title": title,
            "seed": seed,
            "level": "N3",
            "sections": [
                {
                    "section_id": "sec_vocab",
                    "title": "言語知識（文字・語彙）",
                    "time_limit_minutes": 30,
                    "question_count": len(vocab_list),
                    "questions": vocab_list
                },
                {
                    "section_id": "sec_grammar_reading",
                    "title": "言語知識（文法）・読解",
                    "time_limit_minutes": 70,
                    "question_count": len(grammar_list) + len(reading_list),
                    "grammar_questions": grammar_list,
                    "reading_questions": reading_list,
                    "questions": grammar_list + reading_list
                }
            ],
            "passages": test_passages,
            "scoring": {
                "total_questions": len(vocab_list) + len(grammar_list) + len(reading_list),
                "passing_score": 95,
                "max_score": 180,
                "section_threshold": 19,
                "score_distribution": {
                    "language_knowledge": {"max": 60, "min_pass": 19, "weight_per_q": 60 / (len(vocab_list) + len(grammar_list))},
                    "reading": {"max": 60, "min_pass": 19, "weight_per_q": 60 / len(reading_list)}
                }
            }
        }
        return exam_data

def generate_mock_tests(count: int = 3, out_dir: str = "mock_tests"):
    os.makedirs(out_dir, exist_ok=True)
    generator = JLPTMockTestGenerator()
    generated = []

    for i in range(1, count + 1):
        test_id = f"mock_n3_{i:02d}"
        title = f"JLPT N3 総合実戦模試 第{i}回 (公式基準)"
        seed = 1000 + i * 77
        exam = generator.generate_exam(test_id, title, seed=seed)
        out_path = os.path.join(out_dir, f"{test_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(exam, f, ensure_ascii=False, indent=2)
        print(f"Generated {out_path}: {exam['scoring']['total_questions']} questions, {len(exam['passages'])} passages.")
        generated.append(exam)

    # Export JS bundle for standalone browser usage without CORS
    bundle_path = os.path.join(out_dir, "mock_test_data.js")
    bundle_data = {ex["test_id"]: ex for ex in generated}
    with open(bundle_path, "w", encoding="utf-8") as f:
        f.write("window.MOCK_TEST_DATA = " + json.dumps(bundle_data, ensure_ascii=False) + ";")
    print(f"Exported interactive mock tests bundle to {bundle_path}")

if __name__ == "__main__":
    generate_mock_tests(count=3)
