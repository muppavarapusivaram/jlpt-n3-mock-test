import sys
import fitz, re, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('books/Fill in the stars for JLPT N3 2019 December.pdf')
p10 = doc[9].get_text('text')
ans_pattern = re.compile(r'(\d+)\.\s*([A-D]{4})-([A-D])')
answers = {}
for m in ans_pattern.finditer(p10):
    q_num = int(m.group(1))
    order = m.group(2)
    star_opt = m.group(3)
    answers[q_num] = {'order': order, 'star': star_opt, 'ans_int': 'ABCD'.index(star_opt) + 1}

full_text = ''
for i in range(9):
    full_text += '\n' + doc[i].get_text('text')

blocks = re.split(r'\n\s*(\d+)\.\s*', full_text)
parsed = []
for i in range(1, len(blocks), 2):
    q_num = int(blocks[i])
    body = blocks[i+1].strip()
    m = re.search(r'A\.\s*(.+?)\s*B\.\s*(.+?)\s*C\.\s*(.+?)\s*D\.\s*(.+)$', body, re.DOTALL)
    prompt = body[:m.start()].strip()
    opts = [' '.join(m.group(idx).strip().split()) for idx in range(1, 5)]
    ans = answers[q_num]
    parsed.append({
        'q_num': q_num,
        'prompt': prompt,
        'options': opts,
        'ans_int': ans['ans_int'],
        'order': ans['order'],
        'star': ans['star']
    })

bank = json.loads(Path('app/src/data/questionBank.json').read_text(encoding='utf-8'))
all_existing = {q['id']: ''.join(q['question'].split()) for q in bank['questions']}

duplicates = []
for item in parsed:
    norm = ''.join(item['prompt'].split())
    for qid, text in all_existing.items():
        for start in range(0, max(1, len(norm)-15), 5):
            chunk = norm[start:start+15]
            if len(chunk) == 15 and chunk in text:
                duplicates.append((item['q_num'], qid, item['prompt'][:30], text[:30]))
                break

seen_qnums = set()
unique_dupes = []
for d in duplicates:
    if d[0] not in seen_qnums:
        seen_qnums.add(d[0])
        unique_dupes.append(d)

print(f'Total matches found: {len(unique_dupes)}')
for d in unique_dupes:
    print(f'Q{d[0]} matches {d[1]}: "{d[2]}" <-> "{d[3]}"')
