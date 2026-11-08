# scripts/build_2018_12.py
# -*- coding: utf-8 -*-
import os, json

os.makedirs('bank/jlpt_n3_2018_12', exist_ok=True)

# ------------------------------------------------------------------
# 1. SECTION 1: 言語知識（文字・語彙） (35 questions)
# ------------------------------------------------------------------
vocab_questions = [
  # 問題1: 漢字読み (8)
  {
    "id": "jlpt_n3_2018_12_v_q01", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "息子は来年【卒業】します。",
    "options": ["さつきょう", "そつぎょう", "そつきょう", "さつぎょう"], "answer": 2,
    "grammar_points": ["漢字読み: 卒業 (そつぎょう)"], "difficulty": 1,
    "explanation": "「卒業」の読み方は「そつぎょう」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q02", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "留学について先生に【相談】した。",
    "options": ["しょうたん", "しょうだん", "そうたん", "そうだん"], "answer": 4,
    "grammar_points": ["漢字読み: 相談 (そうだん)"], "difficulty": 1,
    "explanation": "「相談」の読み方は「そうだん」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q03", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【確かに】かばんにしまいました。",
    "options": ["たしかに", "しずかに", "たじかに", "しすかに"], "answer": 1,
    "grammar_points": ["漢字読み: 確か (たしか)"], "difficulty": 1,
    "explanation": "「確かに」の読み方は「たしかに」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q04", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "子どもたちが【遊ぶ】声が聞こえます。",
    "options": ["よぶ", "あそぶ", "まなぶ", "さけぶ"], "answer": 2,
    "grammar_points": ["漢字読み: 遊ぶ (あそぶ)"], "difficulty": 1,
    "explanation": "「遊ぶ」の読み方は「あそぶ」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q05", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "店の人はみんな同じ【制服】を着ていた。",
    "options": ["ようふく", "せいふう", "せいふく", "ようふう"], "answer": 3,
    "grammar_points": ["漢字読み: 制服 (せいふく)"], "difficulty": 2,
    "explanation": "「制服」の読み方は「せいふく」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q06", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "鈴木さんが【換えて】くれました。",
    "options": ["かえて", "くわえて", "つかまえて", "つたえて"], "answer": 1,
    "grammar_points": ["漢字読み: 換える (かえる)"], "difficulty": 2,
    "explanation": "「換える」の読み方は「かえる」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q07", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【血圧】が前よりも高かったようです。",
    "options": ["ちど", "けつど", "けつあつ", "ちあつ"], "answer": 3,
    "grammar_points": ["漢字読み: 血圧 (けつあつ)"], "difficulty": 2,
    "explanation": "「血圧」の読み方は「けつあつ」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q08", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【改札】の前で会いましょう。",
    "options": ["けいせつ", "けいさつ", "かいせつ", "かいさつ"], "answer": 4,
    "grammar_points": ["漢字読み: 改札 (かいさつ)"], "difficulty": 2,
    "explanation": "「改札」の読み方は「かいさつ」です。"
  },

  # 問題2: 表記 (6)
  {
    "id": "jlpt_n3_2018_12_v_q09", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "高橋さんに【しゅうかんし】を買ってきてもらった。",
    "options": ["週完誌", "週刊記", "週刊誌", "週完記"], "answer": 3,
    "grammar_points": ["漢字表記: 週刊誌 (しゅうかんし)"], "difficulty": 2,
    "explanation": "「しゅうかんし」の漢字は「週刊誌」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q10", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このドラマの【つづき】が楽しみだ。",
    "options": ["総き", "統き", "続き", "績き"], "answer": 3,
    "grammar_points": ["漢字表記: 続き (つづき)"], "difficulty": 1,
    "explanation": "「つづき」の漢字は「続き」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q11", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "毎日【ねっしん】に勉強している。",
    "options": ["熱心", "燃心", "熱身", "燃身"], "answer": 1,
    "grammar_points": ["漢字表記: 熱心 (ねっしん)"], "difficulty": 1,
    "explanation": "「ねっしん」の漢字は「熱心」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q12", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "中村さんは一週間前に【たいいん】したそうです。",
    "options": ["帰院", "退院", "退員", "帰員"], "answer": 2,
    "grammar_points": ["漢字表記: 退院 (たいいん)"], "difficulty": 1,
    "explanation": "「たいいん」の漢字は「退院」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q13", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "もうちょっと【あつい】のが欲しいです。",
    "options": ["丸い", "厚い", "細い", "浅い"], "answer": 2,
    "grammar_points": ["漢字表記: 厚い (あつい)"], "difficulty": 1,
    "explanation": "「あつい（物が厚い）」の漢字は「厚い」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q14", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "あしたは９時に【しゅっきん】します。",
    "options": ["出勧", "出勘", "出働", "出勤"], "answer": 4,
    "grammar_points": ["漢字表記: 出勤 (しゅっきん)"], "difficulty": 2,
    "explanation": "「しゅっきん」の漢字は「出勤」です。"
  },

  # 問題3: 文脈規定 (11)
  {
    "id": "jlpt_n3_2018_12_v_q15", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "森選手は、全国で1位になることを（　）にしてがんばっている。",
    "options": ["指定", "満点", "一流", "目標"], "answer": 4,
    "grammar_points": ["語彙: 目標にする"], "difficulty": 1,
    "explanation": "「〜を目標にする」で、目指すところとして努力する意味になります。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q16", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "玄関の電気は、スイッチを押さなくても、暗くなると（　）つきます。",
    "options": ["人工的に", "自動的に", "積極的に", "具体的に"], "answer": 2,
    "grammar_points": ["語彙: 自動的"], "difficulty": 2,
    "explanation": "人の手を加えずに自然・機械の働きで点灯するので「自動的に」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q17", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "掃除をするので、この（　）に水を入れてきてください。",
    "options": ["ロッカー", "バケツ", "ブラシ", "タオル"], "answer": 2,
    "grammar_points": ["語彙: バケツ"], "difficulty": 1,
    "explanation": "掃除で水を入れる道具は「バケツ」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q18", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この国は雨が少ないので、いつも空気が（　）している。",
    "options": ["乾燥", "縮小", "沸騰", "減少"], "answer": 1,
    "grammar_points": ["語彙: 乾燥する"], "difficulty": 1,
    "explanation": "雨が少なくて水分がない状態を表すのは「乾燥（かんそう）」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q19", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この町は昔から貿易が盛んで、経済の中心地として（　）してきた。",
    "options": ["進歩", "出発", "発展", "開始"], "answer": 3,
    "grammar_points": ["語彙: 発展する"], "difficulty": 2,
    "explanation": "経済や都市の規模が広がり栄えることを「発展（はってん）」といいます。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q20", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "どちらのパソコンを買おうか、まだ（　）います。",
    "options": ["おどろいて", "こわがって", "まよって", "うたがって"], "answer": 3,
    "grammar_points": ["語彙: 迷う"], "difficulty": 1,
    "explanation": "選択肢の間で決めかねている状態を表すのは「迷って（まよって）」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q21", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "駅のホームで、小学校のときの同級生に（　）会ってびっくりした。",
    "options": ["ぜひ", "一応", "ついでに", "偶然"], "answer": 4,
    "grammar_points": ["語彙: 偶然"], "difficulty": 2,
    "explanation": "予期せず思いがけず会うことを「偶然（ぐうぜん）」といいます。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q22", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "その映画は面白いと友達から聞いていたから、（　）していたのに、実際はあまり面白くなかった。",
    "options": ["期待", "歓迎", "満足", "感激"], "answer": 1,
    "grammar_points": ["語彙: 期待する"], "difficulty": 2,
    "explanation": "楽しみにあらかじめ良い結果を望むことは「期待（きたい）」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q23", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "寝坊して慌てて家を出たので、（　）携帯電話を忘れてきてしまった。",
    "options": ["そっと", "ぐっすり", "うっかり", "どっと"], "answer": 3,
    "grammar_points": ["語彙: うっかり"], "difficulty": 2,
    "explanation": "不注意で思わず過ちをしてしまう様子を表すオノマトペは「うっかり」です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q24", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "会社に届いた郵便の中に、あて先が違う手紙が一通（　）いた。",
    "options": ["交ざって", "寄って", "固まって", "合って"], "answer": 1,
    "grammar_points": ["語彙: 交ざる (まざる)"], "difficulty": 2,
    "explanation": "他の物の中に別のものが入り込むことを「交ざる（まざる）」といいます。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q25", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この皿の上に同じ皿をどんどん（　）ください。",
    "options": ["そそいで", "あずけて", "むかえて", "かさねて"], "answer": 4,
    "grammar_points": ["語彙: 重ねる (かさねる)"], "difficulty": 2,
    "explanation": "物を上に次々と積み上げることは「重ねる（かさねる）」です。"
  },

  # 問題4: 言い換え類義語 (5)
  {
    "id": "jlpt_n3_2018_12_v_q26", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "山口さんに【指導して】もらいました。",
    "options": ["教えて", "探して", "調べて", "決めて"], "answer": 1,
    "grammar_points": ["類義語: 指導する＝教える"], "difficulty": 1,
    "explanation": "「指導する」は「教える（おしえる）」と言い換えられます。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q27", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "もっと【トレーニング】をしたほうがいい。",
    "options": ["準備", "競争", "質問", "練習"], "answer": 4,
    "grammar_points": ["類義語: トレーニング＝練習"], "difficulty": 1,
    "explanation": "「トレーニング」は身体や技能を鍛える「練習（れんしゅう）」と同義です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q28", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "どんな【手段】があるか考えてみた。",
    "options": ["連絡", "楽しみ", "やり方", "理由"], "answer": 3,
    "grammar_points": ["類義語: 手段＝やり方"], "difficulty": 2,
    "explanation": "「手段（しゅだん）」は目的を達成するための「やり方」を指します。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q29", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "リーさんは日本語が【ぺらぺら】です。",
    "options": ["あまり書けません", "上手に書けます", "あまり話せません", "上手に話せます"], "answer": 4,
    "grammar_points": ["類義語: ぺらぺら＝上手に話せる"], "difficulty": 1,
    "explanation": "「ぺらぺら」は外国語などを流暢に「上手に話せる」様子を表します。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q30", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "その歌手は【ようやく】有名になった。",
    "options": ["とても", "やっと", "なぜか", "やっぱり"], "answer": 2,
    "grammar_points": ["類義語: ようやく＝やっと"], "difficulty": 2,
    "explanation": "「ようやく」は長い時間や苦労の末に実現する「やっと」と同義です。"
  },

  # 問題5: 用法 (5)
  {
    "id": "jlpt_n3_2018_12_v_q31", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【建築】",
    "options": [
      "有名な画家によって建築された絵がデパートの入り口に飾られていた。",
      "昨日見学した工場では、毎日自動車が100台以上建築されているそうだ。",
      "この会社が人気があるのは、働きやすい環境が建築されているからだ。",
      "この図書館は50年前に建築されたそうで、現在修理が行われている。"
    ],
    "answer": 4,
    "grammar_points": ["語彙用法: 建築 (けんちく)"], "difficulty": 2,
    "explanation": "「建築する」は家やビルなどの建造物を建てることに使います。4の「図書館が建築された」が自然で正確です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q32", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【埋める】",
    "options": [
      "この子はまだ2歳なのに、上手にシャツのボタンを埋めた。",
      "私の家では、生ごみは庭に穴を掘って埋めている。",
      "花壇に埋めたばらの木にもうすぐ花が咲きそうだ。",
      "店で箱にケーキを六つ埋めてもらって、家に持って帰った。"
    ],
    "answer": 2,
    "grammar_points": ["語彙用法: 埋める (うめる)"], "difficulty": 2,
    "explanation": "「埋める」は穴を掘って土などを上からかぶせる動作です。2の「庭に穴を掘って埋めている」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q33", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【重大】",
    "options": [
      "両親は慣れない町で、重大な苦労をして私たちを育ててくれた。",
      "K社のパソコンに重大な問題が見つかり、回収することになったらしい。",
      "重大な時間を使ってアンケートに協力してくださり、ありがとうございました。",
      "今年の夏休みは、私にとって重大な思い出となりました。"
    ],
    "answer": 2,
    "grammar_points": ["語彙用法: 重大 (じゅうだい)"], "difficulty": 2,
    "explanation": "「重大」は結果や影響が非常に大きいこと。「重大な問題」「重大な責任」などの形で用います。2が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q34", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【延期】",
    "options": [
      "台風が来るので、明日の試合は来週に延期するそうだ。",
      "今朝は具合が悪かったので、会社に行く時間を少し延期した。",
      "いつもより延期して勉強したので、今回のテストはよくできた。",
      "スピーチの時間は5分という決まりですから、延期しないでください。"
    ],
    "answer": 1,
    "grammar_points": ["語彙用法: 延期 (えんき)"], "difficulty": 2,
    "explanation": "「延期」は決められていた期日や日程を先に延ばすことです。1の「試合は来週に延期する」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_v_q35", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【知り合う】",
    "options": [
      "林さんに手を振ったけれど、林さんは知り合わなかった。",
      "木村さんが優勝したことは、テレビのニュースで知り合った。",
      "佐藤さんとは、10年前に旅行先で知り合った。",
      "この機械は説明をよく読んで知り合ってから使ってください。"
    ],
    "answer": 3,
    "grammar_points": ["語彙用法: 知り合う (しりあう)"], "difficulty": 2,
    "explanation": "「知り合う」は互いに面識を持つ関係になることです。3の「旅行先で知り合った」が正解です。"
  }
]

# ------------------------------------------------------------------
# 2. SECTION 2: 言語知識（文法） (23 questions)
# ------------------------------------------------------------------
grammar_questions = [
  # 問題1: 文法形式の判断 (13)
  {
    "id": "jlpt_n3_2018_12_g_q01", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "昨日の夜はとても疲れていたので、夕飯の後、電気（　）消さないでソファで寝てしまった。",
    "options": ["も", "と", "が", "で"], "answer": 1,
    "grammar_points": ["助詞: も (否定強調)"], "difficulty": 2,
    "explanation": "「〜も消さないで」で、「消すべき当然の電気さえ消さずに」という強調を表します。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q02", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "隣の席の山田さんは、文句が多い。いつも（　）言っている。",
    "options": [
      "疲れて仕事が多くて",
      "疲れたり仕事が多かったり",
      "疲れたし仕事が多いし",
      "疲れたとか仕事が多いとか"
    ],
    "answer": 4,
    "grammar_points": ["文法: 〜とか〜とか"], "difficulty": 2,
    "explanation": "「〜とか〜とか言う」で、不満や例などを並べて挙げる表現です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q03", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "最近できたケーキ屋に今日初めて行ってみたが、（　）込んでいたので、何も買わずに帰ってきた。",
    "options": ["ちっとも", "せっかく", "ようやく", "あまりにも"], "answer": 4,
    "grammar_points": ["副詞: あまりにも"], "difficulty": 2,
    "explanation": "「あまりにも」は程度が非常に甚だしく度を越えている様子を表します。「あまりにも込んでいたので」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q04", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私の大学の国際政治学部は、他の学部（　）留学生の割合が高い。",
    "options": ["において", "によって", "にくらべて", "にしたがって"], "answer": 3,
    "grammar_points": ["文法: 〜に比べて"], "difficulty": 2,
    "explanation": "比較の基準を表す「〜に比べて」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q05", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "昨日、1か月前から編んでいたセーターが完成した。途中で間違えて、何度か（　）けれど、完成させることができてよかった。",
    "options": ["やりおわった", "やりなおした", "やっておいた", "やってあった"], "answer": 2,
    "grammar_points": ["複合動詞: やり直す (やりなおす)"], "difficulty": 1,
    "explanation": "途中で間違えて改めてもう一度行ったので「やり直した」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q06", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（高校で）\n先生「大学合格おめでとう。よく頑張ったね。」\n生徒「ありがとうございます。先生がいつも丁寧に教えてくださった（　）。」",
    "options": ["ようです", "せいです", "はずです", "おかげです"], "answer": 4,
    "grammar_points": ["文法: 〜おかげで / おかげです"], "difficulty": 1,
    "explanation": "良い結果をもたらした感謝の理由・原因を表す「〜おかげです」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q07", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "祖母は20年以上前に買った掃除機をまだ（　）。壊れて使えなくなるまで、新しいのは買わないと言っていた。",
    "options": ["使った", "使わない", "使っている", "使っていなかった"], "answer": 3,
    "grammar_points": ["文法: ている (状態の継続)"], "difficulty": 1,
    "explanation": "過去から現在まで継続して使い続けていることを表す「使っている」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q08", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（レストランで）\n店員「いらっしゃいませ。2名様ですか。」\n客「はい。」\n店員「こちらへどうぞ。お席にご案内（　）。」",
    "options": ["いたします", "なさいます", "うかがいます", "いらっしゃいます"], "answer": 1,
    "grammar_points": ["敬語: ご案内いたします (謙譲語)"], "difficulty": 2,
    "explanation": "店員が客を案内する自分の動作をへりくだって言う謙譲表現「ご案内いたします」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q09", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私はダンスが大好きで、毎日練習している。私より上手な人はたくさんいるが、ダンスが好きだという気持ちは（　）負けない。",
    "options": ["誰には", "誰にも", "誰かは", "誰かも"], "answer": 2,
    "grammar_points": ["助詞: にも (全面的否定)"], "difficulty": 2,
    "explanation": "「〜には負けない」に全面否定・強調の「も」がつき、「誰にも負けない」となります。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q10", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（さくらホテルのホームページで）\nさくらホテルの会員に（　）、「ホームページからのお申し込み」、または、「郵送でのお申し込み」の二つの方法があります。",
    "options": ["なるには", "するよりは", "なるかどうかは", "することは"], "answer": 1,
    "grammar_points": ["文法: 〜には (目的・条件)"], "difficulty": 2,
    "explanation": "「会員になるためには」という目的・必要条件を表す「なるには」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q11", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "自分のレストランを（　）実際に店をオープンするまで5年以上かかったが、自分の店が持ててとてもうれしい。",
    "options": [
      "開こうと思えば",
      "開こうと思ってから",
      "開くようになれば",
      "開くようになってから"
    ],
    "answer": 2,
    "grammar_points": ["文法: 〜てから (起点の明示)"], "difficulty": 2,
    "explanation": "意志をもった時点を起点として「〜と思ってから〜まで」と表す2が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q12", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（会社で）\n前川「森さん、この書類、ここにもサインを（　）ですか。」\n森「あ、忘れてました。すぐします。」",
    "options": [
      "してあげてもいい",
      "してくれたらいい",
      "してやったらいい",
      "してもらってもいい"
    ],
    "answer": 4,
    "grammar_points": ["授受表現: 〜てもらってもいいですか (依頼)"], "difficulty": 2,
    "explanation": "相手に対して丁寧に依頼・確認を求める表現「〜てもらってもいいですか」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q13", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（会社で）\n青木「南さん、今日はもうお帰りですか。」\n南「ええ、これから子供を保育園に迎えに（　）。お先に失礼します。」",
    "options": [
      "行っているところなんです",
      "行っているところですね",
      "行かなければならないんです",
      "行かなければならないですね"
    ],
    "answer": 3,
    "grammar_points": ["文法: 〜なければならないんです (理由説明)"], "difficulty": 2,
    "explanation": "早く退社する理由を相手に説明しているので、「行かなければならないんです」が適切です。"
  },

  # 問題2: 文の組み立て (5)
  {
    "id": "jlpt_n3_2018_12_g_q14", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "なかなか英語の単語が覚えられないので、英語の得意な友達が ＿＿ ★ ＿＿ ＿＿ した。",
    "options": ["ことに", "やっていた", "ように", "何度も書いてみる"], "answer": 3,
    "grammar_points": ["文法星並べ: 〜ように〜ことにした"], "difficulty": 2,
    "explanation": "正しい並び順：友達が [2. やっていた] ★[3. ように] [4. 何度も書いてみる] [1. ことに] した。★に入るのは 3 です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q15", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "半年前から ＿＿ ＿＿ ★ ＿＿ 終わってしまった。",
    "options": ["とうとう", "見ていた", "毎週", "大好きなドラマが"], "answer": 4,
    "grammar_points": ["文法星並べ: 毎週見ていた大好きなドラマがとうとう"], "difficulty": 2,
    "explanation": "正しい並び順：半年前から [3. 毎週] [2. 見ていた] ★[4. 大好きなドラマが] [1. とうとう] 終わってしまった。★に入るのは 4 です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q16", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "大川橋は ＿＿ ＿＿ ★ ＿＿「めがね橋」とも呼ばれている。",
    "options": ["している", "形を", "ことから", "めがねのような"], "answer": 1,
    "grammar_points": ["文法星並べ: 〜ことから (理由・由来)"], "difficulty": 2,
    "explanation": "正しい並び順：大川橋は [4. めがねのような] [2. 形を] ★[1. している] [3. ことから]「めがね橋」とも呼ばれている。★に入るのは 1 です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q17", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "田中「木村さん、仕事はどうですか。」\n木村「会社に入ってまだ少ししか ＿＿ ＿＿ ★ ＿＿ ですが、毎日楽しいです。」",
    "options": ["ので", "たっていない", "ばかり", "わからないこと"], "answer": 4,
    "grammar_points": ["文法星並べ: 〜ので〜ばかり"], "difficulty": 2,
    "explanation": "正しい並び順：会社に入ってまだ少ししか [2. たっていない] [1. ので] ★[4. わからないこと] [3. ばかり] ですが、毎日楽しいです。★に入るのは 4 です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q18", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（会社で）\n西川「林さん、来週のセミナーのポスター、知りませんか。さっき ＿＿ ＿＿ ★ ＿＿ 入ってたんですけど、気づいたら箱がなくなってて。」\n林「ああ、山下さんがどこかに持っていきましたよ。」",
    "options": ["まで", "あった", "あそこに", "白い段ボール箱に"], "answer": 2,
    "grammar_points": ["文法星並べ: さっきまであそこにあった〜に"], "difficulty": 2,
    "explanation": "正しい並び順：さっき [1. まで] [3. あそこに] ★[2. あった] [4. 白い段ボール箱に] 入ってたんですけど。★に入るのは 2 です。"
  },

  # 問題3: 文章の文法 (5)
  {
    "id": "jlpt_n3_2018_12_g_q19", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から23の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p07_m3", "question": "【 19 】に入るものを選びなさい。",
    "options": ["案内されました", "案内してあげました", "案内していました", "案内させてくれました"], "answer": 1,
    "grammar_points": ["文脈文法: 受け身 (案内されました)"], "difficulty": 2,
    "explanation": "友達の家で自分が案内を受けた受動の立場なので「案内されました」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q20", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から23の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p07_m3", "question": "【 20 】に入るものを選びなさい。",
    "options": ["それに", "一方", "つまり", "ところが"], "answer": 1,
    "grammar_points": ["接続詞: それに (情報の添加)"], "difficulty": 2,
    "explanation": "前の「落ち着きました」に加えてさらに「涼しいと思いました」と良さを付け加えるため、「それに」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q21", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から23の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p07_m3", "question": "【 21 】に入るものを選びなさい。",
    "options": ["部屋", "この部屋", "あの部屋", "その部屋"], "answer": 2,
    "grammar_points": ["指示詞: この部屋 (現場指示)"], "difficulty": 2,
    "explanation": "今実際に二人でいるその場所（畳の部屋）を指して言っているので「この部屋」が適切です。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q22", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から23の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p07_m3", "question": "【 22 】に入るものを選びなさい。",
    "options": ["では", "でなら", "でだけ", "でしか"], "answer": 4,
    "grammar_points": ["文法: でしか〜ない (限定否定)"], "difficulty": 2,
    "explanation": "後ろに「寝たことがなかった」という否定があるため、「ベッドでしか〜ない」の形になります。"
  },
  {
    "id": "jlpt_n3_2018_12_g_q23", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から23の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p07_m3", "question": "【 23 】に入るものを選びなさい。",
    "options": ["住むならいいです", "住むつもりだからです", "住んでみたいです", "住もうとすることです"], "answer": 3,
    "grammar_points": ["文末表現: 〜てみたいです (希望)"], "difficulty": 1,
    "explanation": "畳の良さを知って自分もそうしたいという希望を表す「住んでみたいです」が最も自然です。"
  }
]

# ------------------------------------------------------------------
# 3. SECTION 3: 読解 (16 questions)
# ------------------------------------------------------------------
reading_questions = [
  # 問題4: 短文読解 (4)
  {
    "id": "jlpt_n3_2018_12_r_q01", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p08_1", "question": "「私」は母のどんな点をうらやましいと思っているか。",
    "options": [
      "人の名前をすぐに覚えられる点",
      "町で、知っている人をすぐに見つけられる点",
      "初めて会った人とすぐに親しく話せるようになる点",
      "すぐに人の名前が思い出せなくても慌てない点"
    ],
    "answer": 1,
    "grammar_points": ["短文読解: 人物の特徴と心情"], "difficulty": 2,
    "explanation": "「私の母は、少し話しただけの人でも、一度で名前を覚えてしまう...私はそんな母がとてもうらやましい」と書かれているため、1が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q02", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p08_2", "question": "3月22日に学生が利用できる駐車場はどこか。",
    "options": [
      "第一駐車場だけ",
      "第一駐車場と教師用駐車場",
      "第一駐車場と教師用駐車場とスーパー「東鉄」の駐車場",
      "第二駐車場だけ"
    ],
    "answer": 2,
    "grammar_points": ["短文読解: 日程・条件の確認"], "difficulty": 2,
    "explanation": "3月22日は「第二駐車場」の工事日です。「工事期間中は、工事をしていない他の二つの駐車場のどちらかに車をとめてください（教師用の駐車場も利用できます）」とあるので、工事をしていない「第一駐車場」と「教師用駐車場」が利用できます。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q03", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p08_3", "question": "大西さんが原さんに頼んだことは何か。",
    "options": [
      "新商品発表会の準備を手伝ってくれる人を探すこと",
      "新商品発表会の当日に会場で受付をすること",
      "新商品発表会について、黒川課長に説明すること",
      "新商品発表会での仕事について、木村さんに説明すること"
    ],
    "answer": 2,
    "grammar_points": ["短文読解: ビジネスメールの依頼内容"], "difficulty": 2,
    "explanation": "メール本文に「当日会場で受付をしてくれる人が、あと二人必要になりました。黒川課長に相談した結果、原さんと木村さんに頼もうということになりました」とあり、当日の受付を依頼しています。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q04", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p09_4", "question": "社会を強く生きていく力がいちばん強くなるのは、どのような子供か。",
    "options": [
      "ほめられた経験も、しかられた経験も少ない子供",
      "ほめられた経験は少ないが、しかられた経験は多い子供",
      "ほめられた経験は多いが、しかられた経験は少ない子供",
      "ほめられた経験も、しかられた経験も多い子供"
    ],
    "answer": 4,
    "grammar_points": ["短文読解: 条件の比較"], "difficulty": 2,
    "explanation": "「ほめられた経験が多い人」の方が強く、その中では「しかられた経験が多い人」がより強かったとあるため、両方とも多い子供が一番強くなります。"
  },

  # 問題5: 中文読解 (6)
  {
    "id": "jlpt_n3_2018_12_r_q05", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p09_m5_1", "question": "【あきらめました】とあるが、何をあきらめたか。",
    "options": [
      "来月引っ越しをすること",
      "今の家より広い家に引っ越しをすること",
      "ほとんどの家具を新しい家に持っていくこと",
      "今使っているソファを新しい家に持っていくこと"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 指示内容の把握"], "difficulty": 2,
    "explanation": "直前に「このソファは、夫も私も気に入っているので、本当は持っていきたかったです。でも、今度の家は今の家より狭いので、あきらめました」とあり、現在のソファの持参を諦めたことがわかります。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q06", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p09_m5_1", "question": "夫がソファを選ぶときに、大切だと考えていることは何か。",
    "options": [
      "柔らかいこと",
      "少し硬めであること",
      "よい姿勢で座れること",
      "座ったときに気持ちがいいこと"
    ],
    "answer": 3,
    "grammar_points": ["中文読解: 登場人物の判断基準"], "difficulty": 2,
    "explanation": "「夫は腰が悪いので、よい姿勢で座れることが大事だと考えています」と明記されています。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q07", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p09_m5_1", "question": "「私」は引っ越しをした後、どのように生活するつもりか。",
    "options": [
      "今使っているソファを、これからもずっと使って生活する。",
      "まあまあいいと思えるソファを買って、そのソファを使って生活する。",
      "納得できるソファが見つかるまで、ソファのない状態で生活する。",
      "ソファを買うのをあきらめて、これからはソファのない生活をする。"
    ],
    "answer": 3,
    "grammar_points": ["中文読解: 筆者の今後の予定・意図"], "difficulty": 2,
    "explanation": "最後の文に「やはり私たちにぴったりのソファが見つかるまで、しばらくはソファのない生活で我慢しようと思います」とあります。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q08", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_m5_2", "question": "「私」は父の誕生日に何をプレゼントしたか。",
    "options": [
      "父が生まれた年の誕生日の新聞のコピー",
      "父が中学生になって最初の誕生日の新聞のコピー",
      "父が希望した年の誕生日の新聞のコピー",
      "今年の父の誕生日の新聞のコピー"
    ],
    "answer": 2,
    "grammar_points": ["中文読解: 具体的事実の読み取り"], "difficulty": 2,
    "explanation": "「父が中学生になって最初の誕生日の新聞にしました」と書かれています。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q09", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_m5_2", "question": "父は子供のころ、ファストフード店にどのようなイメージを持っていたか。",
    "options": [
      "お金持ちしか行けない高い店",
      "日本のどこにでもある店",
      "安く食事ができる店",
      "子供でも入りやすい店"
    ],
    "answer": 1,
    "grammar_points": ["中文読解: 過去の認識の把握"], "difficulty": 2,
    "explanation": "「父は『そんな場所にできたのだから、お金持ちしか行けない高いレストランなのだろう。』と思ってあこがれたそうです」とあります。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q10", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_m5_2", "question": "【昔の新聞のおかげです】とあるが、何が昔の新聞のおかげなのか。",
    "options": [
      "父の子供のころの社会についてよくわかったこと",
      "父と自分の子供時代が違うことが初めてわかったこと",
      "父の子供のころの話が聞けて、父を身近に感じたこと",
      "父が「私」の子供時代を思い出して、懐かしがってくれたこと"
    ],
    "answer": 3,
    "grammar_points": ["中文読解: 理由と結びつきの把握"], "difficulty": 2,
    "explanation": "「父から子供時代の話を聞いたのは初めてでした。父が身近に感じられてうれしかったです...昔の新聞のおかげです」と述べています。"
  },

  # 問題6: 長文読解 (4)
  {
    "id": "jlpt_n3_2018_12_r_q11", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_11_m6", "question": "この文章では、校庭が芝生になることでどのような変化があると言っているか。",
    "options": [
      "芝生を見て気持ちがいいと思う子供が増える。",
      "子供たちが校庭に出て、よく遊ぶようになる。",
      "夏に校庭の気温が上がって、子供たちが外に出にくくなる。",
      "校庭の土だけでなく、乾いた芝生も近所に飛ぶようになる。"
    ],
    "answer": 2,
    "grammar_points": ["長文読解: 原因と効果の把握"], "difficulty": 2,
    "explanation": "「芝生にすると、子供たちは土の校庭のときより、積極的に外で遊ぶようになる」と書かれています。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q12", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_11_m6", "question": "【心配になって】とあるが、何について心配になったのか。",
    "options": [
      "土の校庭がなくなることが良いかどうか",
      "校庭を芝生にする動きが日本で広がるかどうか",
      "「私」の家の庭の芝生をうまく育てられるかどうか",
      "広い校庭の芝生がうまく育つかどうか"
    ],
    "answer": 4,
    "grammar_points": ["長文読解: 筆者の懸念点の把握"], "difficulty": 2,
    "explanation": "「私の家の狭い庭も芝生にしてみたことがある。だが、すぐに枯れてしまった。あんなに広い校庭を芝生にして大丈夫なのだろうか。ちょっと心配になって」とあるため、広い校庭の芝生がうまく育つかを心配しています。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q13", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_11_m6", "question": "芝生の特徴について、合っているものはどれか。",
    "options": [
      "育つのが早い種類の芝生は、状態が悪くなると直りにくい。",
      "育つのが早い種類の芝生は、休ませる期間を作らなくてもよい。",
      "育つのが遅い種類の芝生は、芝生を短く切る回数が多い。",
      "育つのが遅い種類の芝生は、世話をする時間とお金があまりかからない。"
    ],
    "answer": 4,
    "grammar_points": ["長文読解: 対比構造の整理"], "difficulty": 2,
    "explanation": "「一方、遅い種類の芝生は、世話をする時間とお金はあまりかからないが、状態が悪くなると中々直らない」とあります。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q14", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p10_11_m6", "question": "家の近くにある小学校の「芝生の校庭」について、「私」は今、どう考えているか。",
    "options": [
      "芝生の世話をするのは大変だと思うので、土の校庭に戻してもらいたい。",
      "「私」だけで芝生の世話をするのは大変なので、協力してくれる人を募集したい。",
      "芝生の世話をするのは大変だと思うので、できれば「私」も手伝いたい。",
      "大人だけで芝生の世話をするのは大変なので、子供たちにも手伝ってもらいたい。"
    ],
    "answer": 3,
    "grammar_points": ["長文読解: 筆者の意見・態度の総括"], "difficulty": 2,
    "explanation": "「きっと、家の近くの小学校でも芝生の世話をしてくれる人を募集しているに違いない。子供たちが元気に遊べる校庭が作れるよう、私も協力できたらいいと思っている」と結ばれています。"
  },

  # 問題7: 情報検索 (2)
  {
    "id": "jlpt_n3_2018_12_r_q15", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "右のページは、マラソン大会の案内である。これを読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p12_m7", "question": "キニーさんは小学生の息子と一緒に二人で走り、そのあとで一人でも走りたいと考えている。キニーさんの希望に合うものはどれか。",
    "options": [
      "「親子で走ろう（1キロ）」と「ハーフマラソン」",
      "「親子で走ろう（1キロ）」と「10キロ」",
      "「親子で走ろう（50メートル）」と「ハーフマラソン」",
      "「親子で走ろう（50メートル）」と「10キロ」"
    ],
    "answer": 2,
    "grammar_points": ["情報検索: スケジュールと参加条件の照合"], "difficulty": 2,
    "explanation": "小学生の息子と走れるのは「親子で走ろう（1キロ）」（9:00スタート）。ハーフマラソンは8:30スタートで親子マラソンより前です。10キロは13:30スタートなので親子マラソンの後に走れます。したがって「親子で走ろう（1キロ）」と「10キロ」が正解です。"
  },
  {
    "id": "jlpt_n3_2018_12_r_q16", "book": "JLPT N3 2018年12月 過去問", "book_code": "jlpt_n3_2018_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "右のページは、マラソン大会の案内である。これを読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2018_12_p12_m7", "question": "島原さんは「10キロ」に参加しようと思っている。島原さんはクレジットカードを持っていないので、参加費をクレジットカードで払うことができない。島原さんに可能な申し込み方法はどれか。",
    "options": [
      "1月23日から2月7日の間に郵便局で申し込む。",
      "1月23日から2月7日の間に電話で申し込む。",
      "1月23日から2月21日の間にインターネットで申し込む。",
      "マラソン大会当日に会場で申し込む。"
    ],
    "answer": 1,
    "grammar_points": ["情報検索: 支払方法と申込期間の絞り込み"], "difficulty": 2,
    "explanation": "「10キロ」は参加費有料（2,000円）です。インターネット申込はクレカ払いが必要。電話は「無料の種目だけ」。当日の会場申込は不可。したがって「郵便局（参加費が有料の種目だけ）」で期間（1月23日〜2月7日）に申し込む必要があります。"
  }
]

# ------------------------------------------------------------------
# 4. PASSAGES (9 passages)
# ------------------------------------------------------------------
passages = {
  "jlpt_n3_2018_12_p07_m3": {
    "id": "jlpt_n3_2018_12_p07_m3",
    "title": "畳の部屋",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 7,
    "type": "bunshou_bunpou",
    "content": "以下は、留学生の作文である。\n\n畳の部屋\nジョーンズ リサ\n\n　私は6月に日本人の友達の家に遊びに行って、泊めてもらいました。友達の家は新しいマンションの9階にありました。最初に、リビングで友達と友達のお母さんと3人でお茶を飲みながら話しました。それから、隣の部屋に【 19 】、そこは畳の部屋でした。畳は古い家にあるものだと思っていたのですが、新しいマンションにあったので驚きました。\n　友達と私は畳の部屋でDVDを見たり、ゲームをしたりして過ごしました。畳に座ると乾いた草のような香りがして、とても落ち着きました。【 20 】、畳の部屋はリビングより少し涼しいと思いました。友達に聞いたら、畳には湿気を吸って湿度を下げる効果があるそうです。\n　夜になって、友達が畳の部屋の押し入れから布団を出しました。そして、今日は【 21 】で寝ようと言いました。私は少し心配になりました。それまで、ベッド【 22 】寝たことがなかったからです。でも、実際に寝てみるととても気持ちがよく、ぐっすり眠れました。\n　畳の部屋で過ごすことで、私は畳のよさを知ることができました。私も畳の部屋がある家に【 23 】。"
  },
  "jlpt_n3_2018_12_p08_1": {
    "id": "jlpt_n3_2018_12_p08_1",
    "title": "母の特技",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（１）\n　私は人の名前がなかなか覚えられない。先日も町で、私を見つけて、私の名前を呼んで話しかけてくれた人がいたのに、私はその人の名前が思い出せなくて慌ててしまった。一方、私の母は、少し話しただけの人でも、一度で名前を覚えてしまう。「何か工夫しているの。」と聞いたら、「なんにも。自然に覚えちゃうのよ。」と笑っていた。私はそんな母がとてもうらやましい。"
  },
  "jlpt_n3_2018_12_p08_2": {
    "id": "jlpt_n3_2018_12_p08_2",
    "title": "大学の駐車場工事のお知らせ",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（２）\nこれは大学にはってあるお知らせである。\n\n自動車通学をしている学生の皆さんへ\n　大学の駐車場の工事を行います。日程は以下のとおりです。\n　工事期間中は、工事をしていない他の二つの駐車場のどちらかに車をとめてください（教師用の駐車場も利用できます）。\n\n　3月18日（月）〜19日（火） 第一駐車場\n　3月20日（水）〜21日（木） 教師用駐車場\n　3月22日（金）〜23日（土） 第二駐車場\n\nなお、以前から注意しているように、スーパー「東鉄」の駐車場には絶対にとめないでください。\n岩村大学"
  },
  "jlpt_n3_2018_12_p08_3": {
    "id": "jlpt_n3_2018_12_p08_3",
    "title": "新商品発表会のお願い",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（３）\n（会社で）これは大西さんが原さんに書いたメールである。\n\n原さん\nお疲れさまです。\n再来週24日の新商品発表会のことで、お願いがあります。\n今、発表会の準備をしているところなのですが、思った以上に参加者が増えてしまい、当日会場で受付をしてくれる人が、あと二人必要になりました。黒川課長に相談した結果、原さんと木村さんに頼もうということになりました。忙しいとは思いますが、お願いします。木村さんには、もう引き受けてもらっています。\n詳しいことは来週説明します。\nよろしくお願いします。\n大西"
  },
  "jlpt_n3_2018_12_p09_4": {
    "id": "jlpt_n3_2018_12_p09_4",
    "title": "社会を強く生きていく力",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 9,
    "type": "dokkai_tandun",
    "content": "（４）\n　どのような子供が、社会を強く生きていく力を持つようになるのだろうか。ある調査によると、子供のころに人から「ほめられた経験が多い人」は、「ほめられた経験が少ない人」より、この力が強かったそうだ。そして、「ほめられた経験が多い人」の中では、「しかられた経験が多い人」が、「しかられた経験が少ない人」より、この力が強かったそうだ。いちばんこの力が弱かったのは、「ほめられた経験も、しかられた経験も少ない人」だった。"
  },
  "jlpt_n3_2018_12_p09_m5_1": {
    "id": "jlpt_n3_2018_12_p09_m5_1",
    "title": "ソファの買い替え",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 9,
    "type": "dokkai_chuubun",
    "content": "問題５：\n（１）\n　わが家は来月引っ越しをします。ほとんどの家具は新しい家に持っていきますが、ソファだけは買い替える予定です。\n　このソファは、夫も私も気に入っているので、本当は持っていきたかったです。でも、今度の家は今の家より狭いので、あきらめました。\n　それで、今新しいものを探しているところです。でも、なかなか二人が納得できるものがなくて困っています。夫は腰が悪いので、よい姿勢で座れることが大事だと考えています。そういうソファは、少し硬めのものが多いのですが、私は柔らかいソファが好きです。今のソファは、柔らかくて気持ちがいいけれど、よい姿勢で座れるので、二人ともとても満足しています。家具店を何軒も回ってやっと見つけたものです。\n　今回も、まあまあいいと思えるソファはありました。一度はそれを買おうかとも思いましたが、やめました。やはり私たちにぴったりのソファが見つかるまで、しばらくはソファのない生活で我慢しようと思います。"
  },
  "jlpt_n3_2018_12_p10_m5_2": {
    "id": "jlpt_n3_2018_12_p10_m5_2",
    "title": "昔の新聞のプレゼント",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 10,
    "type": "dokkai_chuubun",
    "content": "（２）\n　先日、私は昔の新聞のページを印刷するサービスがあるのを知り、父の誕生日にプレゼントしました。初めは父の生まれた日の新聞のコピーにしようと思いましたが、父が中学生になって最初の誕生日の新聞にしました。ふだんはあまりしゃべらない父が、その中の記事を見て、「これ、懐かしいな。」と昔の話を始めました。\n　父によると、一流店が並ぶ東京の中心地に、日本ではまだ珍しかったファストフード店ができたとき、大きなニュースになったらしいのです。実は安い店だったのに、父は「そんな場所にできたのだから、お金持ちしか行けない高いレストランなのだろう。」と思ってあこがれたそうです。「ファストフード店は安いって、今なら小学生でも知っているのに、そんなイメージを持っていたんだから、おかしいだろう。」と笑いました。\n　父から子供時代の話を聞いたのは初めてでした。父が身近に感じられてうれしかったです。また、こんな話が聞けたらいいなと思いました。昔の新聞のおかげです。"
  },
  "jlpt_n3_2018_12_p10_11_m6": {
    "id": "jlpt_n3_2018_12_p10_11_m6",
    "title": "芝生の校庭",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 10,
    "type": "dokkai_choubun",
    "content": "問題６：\n　私の家の近くにある小学校では、最近、校庭が土から芝生に変わった。きれいな緑が広がる芝生の校庭は、とても気持ちがいい。\n　今、日本各地の学校で校庭を芝生にしようという動きがあるそうだ。芝生にすると、子供たちは土の校庭のときより、積極的に外で遊ぶようになる。また、芝生には、暑いときに校庭の気温を上がりにくくしたり、校庭の乾いた土が風で近所の家に飛んでいくのを防いだりする効果もある。\n　実は、私の家の狭い庭も芝生にしてみたことがある。だが、すぐに枯れてしまった。あんなに広い校庭を芝生にして大丈夫なのだろうか。ちょっと心配になって、調べてみた。\n　芝生には、育つのが早い種類と遅い種類がある。そして、それぞれ良い点と悪い点がある。育つのが早い種類の芝生は、状態が悪くなっても直りやすいが、長く伸びすぎないように何度も切らなければならず、世話をする時間とお金がかかる。一方、遅い種類の芝生は、世話をする時間とお金はあまりかからないが、状態が悪くなると中々直らない。また、どちらの種類の芝生でも、1年に1か月ぐらいは誰も踏まない期間を作り、休ませる必要があるそうだ。その間は、子供たちも校庭で遊ぶのを我慢しなければならない。\n　「芝生の校庭」が成功した学校は、町に住む人々に芝生の世話を手伝ってもらっているところが多いようだ。きっと、家の近くの小学校でも芝生の世話をしてくれる人を募集しているに違いない。子供たちが元気に遊べる校庭が作れるよう、私も協力できたらいいと思っている。"
  },
  "jlpt_n3_2018_12_p12_m7": {
    "id": "jlpt_n3_2018_12_p12_m7",
    "title": "わかば市 市民マラソン大会",
    "book": "JLPT N3 2018年12月 過去問",
    "page": 12,
    "type": "dokkai_jouhou_kensaku",
    "content": "わかば市 市民マラソン大会\n\n2019年5月12日（日）\nわかば市で自然を感じながら走りませんか\n\n【種目 / 参加できる人 / スタート予定時間 / 参加費】\n・ハーフマラソン（21.0975キロ） / 高校生以上 / 8:30 / 4,000円\n・10キロ / 高校生以上 / 13:30 / 2,000円\n・2キロ / 小学生・中学生 / 12:30 / 500円\n・親子で走ろう（1キロ） / 小学生1名と親1名 / 9:00 / 無料\n・親子で走ろう（50メートル） / 小学校に入る前の子供1名と親1名 / 11:30 / 無料\n\n【コース】\nわかば公園内のグラウンドをスタートし、わかば市内を走り、グラウンドに戻ります。\n詳しいコースは、下のホームページから確認してください。\n\n【申し込みと参加費の支払いについて】\n①インターネット（すべての種目）\n＜期間＞1月23日（水）から2月21日（木）まで\n下のホームページから申し込んでください。参加費が必要な種目は、クレジットカードで支払ってください。\n\n②郵便局（参加費が有料の種目だけ）\n＜期間＞1月23日（水）から2月7日（木）まで\nパンフレットの中にある指定の用紙を使って参加費を郵便局で振り込み、申し込みをしてください。（パンフレットはわかば市役所、わかば市内の郵便局、わかば市内の学校にあります。）\n\n③電話（参加費が無料の種目だけ）\n＜期間＞1月23日（水）から2月7日（木）まで\n「わかば市 市民マラソン係」に電話をしてください。\n\n※マラソン大会当日に、会場で申し込むことはできません。\n※申し込み後に種目を変えることはできません。\n\nわかば市 市民マラソン係 電話 091-846-8460\nhttp://www.wakaba.lg.jp/hashirou"
  }
}

# ------------------------------------------------------------------
# WRITE JSON FILES
# ------------------------------------------------------------------
with open('bank/jlpt_n3_2018_12/vocab.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2018年12月 過去問", "unit": "文字・語彙", "questions": vocab_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2018_12/grammar.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2018年12月 過去問", "unit": "文法", "questions": grammar_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2018_12/reading.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2018年12月 過去問", "unit": "読解", "questions": reading_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2018_12/passages.json', 'w', encoding='utf-8') as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)

print(f"Extraction for 2018 December completed:")
print(f"  Vocab: {len(vocab_questions)} Qs")
print(f"  Grammar: {len(grammar_questions)} Qs")
print(f"  Reading: {len(reading_questions)} Qs")
print(f"  Passages: {len(passages)} passages")
print(f"  Total: {len(vocab_questions) + len(grammar_questions) + len(reading_questions)} Qs")
