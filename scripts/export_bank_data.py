"""
Generates:
1. bank/bank_data.js for review.html
2. app/src/data/questionBank.json for the React Mock Test Simulator
"""
import json
from pathlib import Path

def export_data():
    bank_dir = Path("bank")
    
    # 1. Soumatome N3 Bunpou
    sm_dir = bank_dir / "soumatome_n3_bunpou"
    w1 = json.loads((sm_dir / "week_01.json").read_text(encoding="utf-8"))
    w2 = json.loads((sm_dir / "week_02.json").read_text(encoding="utf-8"))
    w3 = json.loads((sm_dir / "week_03.json").read_text(encoding="utf-8"))
    w4 = json.loads((sm_dir / "week_04.json").read_text(encoding="utf-8"))
    w5 = json.loads((sm_dir / "week_05.json").read_text(encoding="utf-8"))
    w6 = json.loads((sm_dir / "week_06.json").read_text(encoding="utf-8"))
    p_sm = json.loads((sm_dir / "passages.json").read_text(encoding="utf-8"))

    # 2. 2018 December
    j18d_dir = bank_dir / "jlpt_n3_2018_12"
    v18d = json.loads((j18d_dir / "vocab.json").read_text(encoding="utf-8"))
    g18d = json.loads((j18d_dir / "grammar.json").read_text(encoding="utf-8"))
    r18d = json.loads((j18d_dir / "reading.json").read_text(encoding="utf-8"))
    p_18d = json.loads((j18d_dir / "passages.json").read_text(encoding="utf-8"))

    # 3. 2019 December
    j19d_dir = bank_dir / "jlpt_n3_2019_12"
    v19d = json.loads((j19d_dir / "vocab.json").read_text(encoding="utf-8"))
    g19d = json.loads((j19d_dir / "grammar.json").read_text(encoding="utf-8"))
    r19d = json.loads((j19d_dir / "reading.json").read_text(encoding="utf-8"))
    p_19d = json.loads((j19d_dir / "passages.json").read_text(encoding="utf-8"))

    # 4. 2020 December
    j20d_dir = bank_dir / "jlpt_n3_2020_12"
    v20d = json.loads((j20d_dir / "vocab.json").read_text(encoding="utf-8"))
    g20d = json.loads((j20d_dir / "grammar.json").read_text(encoding="utf-8"))
    r20d = json.loads((j20d_dir / "reading.json").read_text(encoding="utf-8"))
    p_20d = json.loads((j20d_dir / "passages.json").read_text(encoding="utf-8"))

    # 5. 2021 July
    j21_dir = bank_dir / "jlpt_n3_2021_07"
    v21 = json.loads((j21_dir / "vocab.json").read_text(encoding="utf-8"))
    g21 = json.loads((j21_dir / "grammar.json").read_text(encoding="utf-8"))
    r21 = json.loads((j21_dir / "reading.json").read_text(encoding="utf-8"))
    p_21 = json.loads((j21_dir / "passages.json").read_text(encoding="utf-8"))
    
    # 3. 2022 July
    j22_dir = bank_dir / "jlpt_n3_2022_07"
    v22 = json.loads((j22_dir / "vocab.json").read_text(encoding="utf-8"))
    g22 = json.loads((j22_dir / "grammar.json").read_text(encoding="utf-8"))
    r22 = json.loads((j22_dir / "reading.json").read_text(encoding="utf-8"))
    p_22 = json.loads((j22_dir / "passages.json").read_text(encoding="utf-8"))

    # 4. 2023 July
    j23_dir = bank_dir / "jlpt_n3_2023_07"
    v23 = json.loads((j23_dir / "vocab.json").read_text(encoding="utf-8"))
    g23 = json.loads((j23_dir / "grammar.json").read_text(encoding="utf-8"))
    r23 = json.loads((j23_dir / "reading.json").read_text(encoding="utf-8"))
    p_23 = json.loads((j23_dir / "passages.json").read_text(encoding="utf-8"))
    
    # 5. 2023 December
    j23d_dir = bank_dir / "jlpt_n3_2023_12"
    v23d = json.loads((j23d_dir / "vocab.json").read_text(encoding="utf-8"))
    g23d = json.loads((j23d_dir / "grammar.json").read_text(encoding="utf-8"))
    r23d = json.loads((j23d_dir / "reading.json").read_text(encoding="utf-8"))
    p_23d = json.loads((j23d_dir / "passages.json").read_text(encoding="utf-8"))

    # 6. 2024 July
    j24_dir = bank_dir / "jlpt_n3_2024_07"
    v24 = json.loads((j24_dir / "vocab.json").read_text(encoding="utf-8"))
    g24 = json.loads((j24_dir / "grammar.json").read_text(encoding="utf-8"))
    r24 = json.loads((j24_dir / "reading.json").read_text(encoding="utf-8"))
    p_24 = json.loads((j24_dir / "passages.json").read_text(encoding="utf-8"))

    # 7. Stars Collection (2010-2019)
    stars_dir = bank_dir / "jlpt_n3_stars_collection"
    g_stars = json.loads((stars_dir / "grammar.json").read_text(encoding="utf-8"))

    # 8. 2025 July (Practice / Simulation Exam)
    j25_dir = bank_dir / "jlpt_n3_2025_07"
    v25 = json.loads((j25_dir / "vocab.json").read_text(encoding="utf-8"))
    g25 = json.loads((j25_dir / "grammar.json").read_text(encoding="utf-8"))
    r25 = json.loads((j25_dir / "reading.json").read_text(encoding="utf-8"))
    p_25 = json.loads((j25_dir / "passages.json").read_text(encoding="utf-8"))

    # 9. 2025 December (Practice / Simulation Exam)
    j25d_dir = bank_dir / "jlpt_n3_2025_12"
    v25d = json.loads((j25d_dir / "vocab.json").read_text(encoding="utf-8"))
    g25d = json.loads((j25d_dir / "grammar.json").read_text(encoding="utf-8"))
    r25d = json.loads((j25d_dir / "reading.json").read_text(encoding="utf-8"))
    p_25d = json.loads((j25d_dir / "passages.json").read_text(encoding="utf-8"))
    
    all_passages = {**p_sm, **p_18d, **p_19d, **p_20d, **p_21, **p_22, **p_23, **p_23d, **p_24, **p_25, **p_25d}
    
    data = {
        'w1': {'questions': w1['questions'], 'passages': all_passages},
        'w2': {'questions': w2['questions'], 'passages': all_passages},
        'w3': {'questions': w3['questions'], 'passages': all_passages},
        'w4': {'questions': w4['questions'], 'passages': all_passages},
        'w5': {'questions': w5['questions'], 'passages': all_passages},
        'w6': {'questions': w6['questions'], 'passages': all_passages},
        '2018_12_v': {'questions': v18d['questions'], 'passages': all_passages},
        '2018_12_g': {'questions': g18d['questions'], 'passages': all_passages},
        '2018_12_r': {'questions': r18d['questions'], 'passages': all_passages},
        '2019_12_v': {'questions': v19d['questions'], 'passages': all_passages},
        '2019_12_g': {'questions': g19d['questions'], 'passages': all_passages},
        '2019_12_r': {'questions': r19d['questions'], 'passages': all_passages},
        '2020_12_v': {'questions': v20d['questions'], 'passages': all_passages},
        '2020_12_g': {'questions': g20d['questions'], 'passages': all_passages},
        '2020_12_r': {'questions': r20d['questions'], 'passages': all_passages},
        '2021_07_v': {'questions': v21['questions'], 'passages': all_passages},
        '2021_07_g': {'questions': g21['questions'], 'passages': all_passages},
        '2021_07_r': {'questions': r21['questions'], 'passages': all_passages},
        '2022_07_v': {'questions': v22['questions'], 'passages': all_passages},
        '2022_07_g': {'questions': g22['questions'], 'passages': all_passages},
        '2022_07_r': {'questions': r22['questions'], 'passages': all_passages},
        '2023_07_v': {'questions': v23['questions'], 'passages': all_passages},
        '2023_07_g': {'questions': g23['questions'], 'passages': all_passages},
        '2023_07_r': {'questions': r23['questions'], 'passages': all_passages},
        '2023_12_v': {'questions': v23d['questions'], 'passages': all_passages},
        '2023_12_g': {'questions': g23d['questions'], 'passages': all_passages},
        '2023_12_r': {'questions': r23d['questions'], 'passages': all_passages},
        '2024_07_v': {'questions': v24['questions'], 'passages': all_passages},
        '2024_07_g': {'questions': g24['questions'], 'passages': all_passages},
        '2024_07_r': {'questions': r24['questions'], 'passages': all_passages},
        '2025_07_v': {'questions': v25['questions'], 'passages': all_passages},
        '2025_07_g': {'questions': g25['questions'], 'passages': all_passages},
        '2025_07_r': {'questions': r25['questions'], 'passages': all_passages},
        '2025_12_v': {'questions': v25d['questions'], 'passages': all_passages},
        '2025_12_g': {'questions': g25d['questions'], 'passages': all_passages},
        '2025_12_r': {'questions': r25d['questions'], 'passages': all_passages},
        'stars_collection': {'questions': g_stars['questions'], 'passages': all_passages}
    }
    
    # Export bank_data.js
    out_file = bank_dir / "bank_data.js"
    out_file.write_text("window.BANK_DATA = " + json.dumps(data, ensure_ascii=False) + ";", encoding="utf-8")
    print(f"Exported bundle to {out_file} ({out_file.stat().st_size} bytes)")

    # Collect all questions into React application bundle
    all_questions = []
    for k, v in data.items():
        all_questions.extend(v['questions'])

    react_bank_file = Path("app/src/data/questionBank.json")
    react_bank_data = {
        "version": "1.2.0",
        "total_questions": len(all_questions),
        "total_passages": len(all_passages),
        "passages": all_passages,
        "questions": all_questions
    }
    react_bank_file.write_text(json.dumps(react_bank_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported React question bank to {react_bank_file} ({len(all_questions)} questions, {len(all_passages)} passages)")

if __name__ == "__main__":
    export_data()
