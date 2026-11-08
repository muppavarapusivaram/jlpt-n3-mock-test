import sys, fitz, re, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('books/Fill in the stars for JLPT N3 2019 December.pdf')

# 1. Parse answers
p10 = doc[9].get_text('text')
ans_pattern = re.compile(r'(\d+)\.\s*([A-D]{4})-([A-D])')
answers = {}
for m in ans_pattern.finditer(p10):
    q_num = int(m.group(1))
    order = m.group(2)
    star_opt = m.group(3)
    answers[q_num] = {'order': order, 'star': star_opt, 'ans_int': 'ABCD'.index(star_opt) + 1}

# 2. Extract full text
full_text = ''
page_map = {}
for page_idx in range(9):
    t = doc[page_idx].get_text('text')
    full_text += f'\n<<<PAGE_{page_idx+1}>>>\n' + t

# Split into questions
blocks = re.split(r'\n\s*(\d+)\.\s*', full_text)

# We want to skip the 6 exact duplicates that are already in 2018.12 and 2019.12
duplicate_qnums = {76, 79, 80, 87, 89, 90}

questions = []
current_page = 1

for i in range(1, len(blocks), 2):
    q_num = int(blocks[i])
    body = blocks[i+1].strip()

    # Track current page
    # Look back in preceding block or body
    m_page = re.search(r'<<<PAGE_(\d+)>>>', blocks[i-1] + body)
    if m_page:
        current_page = int(m_page.group(1))

    if q_num in duplicate_qnums:
        continue

    # Clean body: remove any stray <<<PAGE_X>>>
    clean_body = re.sub(r'<<<PAGE_\d+>>>', '', body).strip()

    m = re.search(r'A\.\s*(.+?)\s*B\.\s*(.+?)\s*C\.\s*(.+?)\s*D\.\s*(.+)$', clean_body, re.DOTALL)
    if not m:
        print(f"ERROR: Cannot parse Q{q_num}")
        continue

    raw_prompt = clean_body[:m.start()].strip()
    # Normalize underline/star blanks to standard JLPT style: ＿＿ ＿＿ ★ ＿＿
    prompt = re.sub(r'[＿_]\s*[＿_]\s*★\s*[＿_]', '＿＿ ＿＿ ★ ＿＿', raw_prompt)
    prompt = re.sub(r'[\r\n]+', '\n', prompt).strip()

    opt_a = ' '.join(m.group(1).strip().split())
    opt_b = ' '.join(m.group(2).strip().split())
    opt_c = ' '.join(m.group(3).strip().split())
    opt_d = ' '.join(m.group(4).strip().split())
    options = [opt_a, opt_b, opt_c, opt_d]

    ans = answers[q_num]
    order_letters = list(ans['order']) # e.g. ['A', 'D', 'C', 'B']
    order_opts = [options['ABCD'.index(ch)] for ch in order_letters]
    order_str = ' → '.join([f'{ch}「{opt}」' for ch, opt in zip(order_letters, order_opts)])
    correct_opt_text = options[ans['ans_int'] - 1]

    explanation = (
        f"文脈に合わせて語句を並べ替えると、「{order_str}」となります。"
        f"★の位置（3番目）に入るのは {ans['ans_int']}（{correct_opt_text}）です。"
    )

    q_obj = {
        "id": f"jlpt_n3_stars_q{q_num:02d}",
        "book": "JLPT N3 文の組み立て 公式過去問集 (2010-2019)",
        "book_code": "jlpt_n3_stars_collection",
        "unit": "文の組み立て",
        "page": current_page,
        "pdf_page": current_page,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": prompt,
        "options": options,
        "answer": ans["ans_int"],
        "explanation": explanation,
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    }
    questions.append(q_obj)

print(f"Generated {len(questions)} clean star-order questions.")
out_dir = Path("bank/jlpt_n3_stars_collection")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "grammar.json"
out_file.write_text(json.dumps({"questions": questions}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved to {out_file}")
