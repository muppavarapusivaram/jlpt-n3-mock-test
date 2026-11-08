#!/usr/bin/env python3
"""
validate_bank.py
Validates all question files and passage files in the JLPT question bank (`bank/`).
Enforces schema completeness, 4-option requirement, answer bounds, passage referential integrity,
and non-listening constraints.
"""

import sys
import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

VALID_SECTIONS = {
    # Official Japanese Section Names
    "言語知識（文字・語彙）",
    "言語知識（文法）",
    "読解",
    "言語知識（文字・語彙・文法）・読解",
    "言語知識（文法）・読解",
    # English aliases (if needed)
    "Language Knowledge (Vocabulary)",
    "Language Knowledge (Grammar)",
    "Reading",
    "Language Knowledge (Vocabulary / Grammar) & Reading"
}

VALID_MONDAI_TYPES = {
    # Vocabulary
    "kanji_reading",
    "orthography",
    "word_formation",
    "contextual_defining",
    "paraphrases",
    "usage",
    # Grammar
    "bunpou_keishiki",
    "bun_kumitate",
    "bunshou_bunpou",
    # Reading
    "dokkai_tandun",
    "dokkai_chuubun",
    "dokkai_choubun",
    "dokkai_jouhou_kensaku"
}

def validate_bank(bank_dir: Path) -> bool:
    print(f"=== Validating Question Bank at '{bank_dir.resolve()}' ===")
    
    # 1. Load all passages
    passages = {}
    passage_files = list(bank_dir.glob("**/passages.json"))
    for pf in passage_files:
        try:
            with open(pf, "r", encoding="utf-8") as f:
                data = json.load(f)
                for pid, pdata in data.items():
                    if pid in passages:
                        print(f"ERROR: Duplicate passage ID '{pid}' in {pf}")
                        return False
                    passages[pid] = pdata
        except Exception as e:
            print(f"ERROR reading passage file {pf}: {e}")
            return False
            
    print(f"Loaded {len(passages)} passages from {len(passage_files)} passage files.")

    # 2. Load and validate question files
    question_files = [
        f for f in bank_dir.glob("**/*.json")
        if f.name != "page_map.json"
        and f.name != "passages.json"
        and f.name != "grammar_points.json"
    ]

    total_questions = 0
    errors = []
    seen_ids = set()
    mondai_counts = {}
    difficulty_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    needs_review_count = 0

    for qf in question_files:
        try:
            with open(qf, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Failed to parse JSON in {qf}: {e}")
            continue

        questions = data.get("questions", [])
        if not questions:
            errors.append(f"{qf} has no 'questions' list.")
            continue

        for i, q in enumerate(questions):
            qid = q.get("id")
            context = f"[{qf.name} #q{i+1} id={qid}]"

            # Check ID
            if not qid or not isinstance(qid, str):
                errors.append(f"{context} Missing or invalid 'id'")
            elif qid in seen_ids:
                errors.append(f"{context} Duplicate ID '{qid}'")
            else:
                seen_ids.add(qid)

            # Check required string metadata
            for field in ["book", "book_code", "unit"]:
                if not q.get(field):
                    errors.append(f"{context} Missing required field '{field}'")

            # Check page numbers
            for pfield in ["page", "pdf_page"]:
                if not isinstance(q.get(pfield), int) or q.get(pfield) <= 0:
                    errors.append(f"{context} Missing or invalid '{pfield}'")

            # Check Section
            section = q.get("section")
            if section not in VALID_SECTIONS:
                errors.append(f"{context} Invalid section '{section}'. Must be one of: {VALID_SECTIONS}")
            
            # Check No Listening
            if "listening" in str(section).lower() or "choukai" in str(q.get("mondai_type")).lower():
                errors.append(f"{context} Listening questions are forbidden in this bank.")

            # Check Mondai Type
            mtype = q.get("mondai_type")
            if mtype not in VALID_MONDAI_TYPES:
                errors.append(f"{context} Invalid mondai_type '{mtype}'. Must be one of: {sorted(VALID_MONDAI_TYPES)}")
            else:
                mondai_counts[mtype] = mondai_counts.get(mtype, 0) + 1

            # Check Question Text
            if not q.get("question") or not isinstance(q.get("question"), str):
                errors.append(f"{context} Question text must be a non-empty string.")

            # Check Options (Strictly 4)
            options = q.get("options")
            if not isinstance(options, list) or len(options) != 4:
                errors.append(f"{context} Options must be a list of exactly 4 strings. Found: {len(options) if isinstance(options, list) else type(options)}")
            else:
                for opt_idx, opt in enumerate(options):
                    if not isinstance(opt, str) or not opt.strip():
                        errors.append(f"{context} Option {opt_idx+1} is empty or not a string.")

            # Check Answer (1, 2, 3, or 4)
            answer = q.get("answer")
            if answer not in [1, 2, 3, 4]:
                errors.append(f"{context} Invalid answer '{answer}'. Must be 1, 2, 3, or 4.")

            # Check Difficulty (1-5)
            diff = q.get("difficulty")
            if diff not in [1, 2, 3, 4, 5]:
                errors.append(f"{context} Invalid difficulty '{diff}'. Must be integer 1 to 5.")
            else:
                difficulty_counts[diff] += 1

            # Check Passage reference
            pid = q.get("passage_id")
            if pid is not None:
                if pid not in passages:
                    errors.append(f"{context} References passage_id '{pid}' which was not found in passages.json.")

            # Check Grammar points
            gps = q.get("grammar_points")
            if not isinstance(gps, list):
                errors.append(f"{context} 'grammar_points' must be a list.")

            # Check needs_review
            if q.get("needs_review") is True:
                needs_review_count += 1

            total_questions += 1

    # Report results
    print(f"\n--- Validation Summary ---")
    print(f"Total files checked: {len(question_files)}")
    print(f"Total questions validated: {total_questions}")
    print(f"Questions flagged with needs_review: {needs_review_count}")
    
    print("\nBreakdown by Mondai Type:")
    for mt, cnt in sorted(mondai_counts.items()):
        print(f"  - {mt:25}: {cnt:3} questions")

    print("\nBreakdown by Difficulty:")
    for d in range(1, 6):
        pct = (difficulty_counts[d] / total_questions * 100) if total_questions > 0 else 0
        print(f"  - Level {d}: {difficulty_counts[d]:3} questions ({pct:5.1f}%)")

    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for err in errors[:20]:
            print(f"  [ERROR] {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
        return False

    print("\nPASSED! All questions and metadata conform strictly to specification.")
    return True

if __name__ == "__main__":
    bank_path = Path("bank")
    success = validate_bank(bank_path)
    sys.exit(0 if success else 1)
