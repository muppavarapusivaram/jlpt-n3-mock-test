# scripts/build_2021_07.py
# -*- coding: utf-8 -*-
import os, json

os.makedirs('bank/jlpt_n3_2021_07', exist_ok=True)

# ------------------------------------------------------------------
# 1. SECTION 1: 言語知識（文字・語彙） (35 questions)
# ------------------------------------------------------------------
vocab_questions = [
  # 問題1: 漢字読み (8)
  {
    "id": "jlpt_n3_2021_07_v_q01", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このビルの【裏】に小さなレストランがあります。",
    "options": ["そば", "よこ", "かげ", "うら"], "answer": 4,
    "grammar_points": ["漢字読み: 裏 (うら)"], "difficulty": 1,
    "explanation": "「裏」の読み方は「うら」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q02", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "それではゆっくり【呼吸】をしてください。",
    "options": ["こぎゅう", "こきゅう", "よぎゅう", "よきゅう"], "answer": 2,
    "grammar_points": ["漢字読み: 呼吸 (こきゅう)"], "difficulty": 1,
    "explanation": "「呼吸」の読み方は「こきゅう」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q03", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "あの少年の【悲しそうな】顔が忘れられない。",
    "options": ["やさしそう", "かなしそう", "きびしそう", "さびしそう"], "answer": 2,
    "grammar_points": ["漢字読み: 悲しい (かなしい)"], "difficulty": 1,
    "explanation": "「悲しい」の読み方は「かなしい」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q04", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このあたりに【駐車】しましょう。",
    "options": ["しゅしゃ", "しゅうし", "ちゅしゃ", "ちゅうしゃ"], "answer": 4,
    "grammar_points": ["漢字読み: 駐車 (ちゅうしゃ)"], "difficulty": 1,
    "explanation": "「駐車」の読み方は「ちゅうしゃ」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q05", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "もう【逃げて】しまったようだ。",
    "options": ["にげて", "なげて", "こげて", "あげて"], "answer": 1,
    "grammar_points": ["漢字読み: 逃げる (にげる)"], "difficulty": 1,
    "explanation": "「逃げる」の読み方は「にげる」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q06", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【努力】することは大切だと思います。",
    "options": ["どうりょく", "とうりょく", "どりょく", "とりょく"], "answer": 3,
    "grammar_points": ["漢字読み: 努力 (どりょく)"], "difficulty": 1,
    "explanation": "「努力」の読み方は「どりょく」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q07", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "それは【過去】のことです。",
    "options": ["かこ", "かこう", "かきょ", "かきょう"], "answer": 1,
    "grammar_points": ["漢字読み: 過去 (かこ)"], "difficulty": 1,
    "explanation": "「過去」の読み方は「かこ」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q08", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "彼は話し方も【動作】もゆっくりしている。",
    "options": ["とうさ", "とうさく", "どうさ", "どうさん"], "answer": 3,
    "grammar_points": ["漢字読み: 動作 (どうさ)"], "difficulty": 1,
    "explanation": "「動作」の読み方は「どうさ」です。"
  },

  # 問題2: 表記 (6)
  {
    "id": "jlpt_n3_2021_07_v_q09", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "昨日、友達が家に【とまり】にきた。",
    "options": ["停まり", "留まり", "泊まり", "止まり"], "answer": 3,
    "grammar_points": ["漢字表記: 泊まる (とまる)"], "difficulty": 1,
    "explanation": "客が宿や人の家に宿泊することは「泊まる」と書きます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q10", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "書類にはこの学校の【きそく】が書かれていた。",
    "options": ["現販", "規則", "規販", "現則"], "answer": 2,
    "grammar_points": ["漢字表記: 規則 (きそく)"], "difficulty": 1,
    "explanation": "「きそく」の漢字は「規則」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q11", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "ここには【あたたかい】ですね。",
    "options": ["明かいし", "暑かい", "暖かい", "熱かい"], "answer": 3,
    "grammar_points": ["漢字表記: 暖かい (あたたかい)"], "difficulty": 1,
    "explanation": "気候・場所の温もりの「あたたかい」は「暖かい」と書きます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q12", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【やっきょく】がなかなか見つかりません。",
    "options": ["薬局", "薬曲", "楽局", "楽曲"], "answer": 1,
    "grammar_points": ["漢字表記: 薬局 (やっきょく)"], "difficulty": 1,
    "explanation": "「やっきょく」の漢字は「薬局」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q13", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "お皿は【かさねて】その棚にしまってください。",
    "options": ["整ねて", "死ねて", "階ねて", "重ねて"], "answer": 4,
    "grammar_points": ["漢字表記: 重ねる (かさねる)"], "difficulty": 1,
    "explanation": "皿などを積み重ねる動詞は「重ねる」と書きます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q14", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "机の上に【でんごん】のメモがあった。",
    "options": ["伝記", "伝言", "転記", "転々"], "answer": 2,
    "grammar_points": ["漢字表記: 伝言 (でんごん)"], "difficulty": 1,
    "explanation": "「でんごん」の漢字は「伝言」です。"
  },

  # 問題3: 文脈規定 (11)
  {
    "id": "jlpt_n3_2021_07_v_q15", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "マラソン大会は台風で（　）されることになりました。",
    "options": ["遅刻", "運休", "延期", "早退"], "answer": 3,
    "grammar_points": ["語彙: 延期される"], "difficulty": 1,
    "explanation": "大会や行事の日程を先に延ばすのは「延期（えんき）」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q16", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "毎日水をやらないと花が（　）しまう。",
    "options": ["とめて", "きめて", "やせて", "かれて"], "answer": 4,
    "grammar_points": ["語彙: 枯れる (かれる)"], "difficulty": 1,
    "explanation": "植物や花が水分不足などで生命を失う動詞は「枯れる（かれる）」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q17", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この犬は子供のころから（　）されているので、人が大勢いてもおとなしい。",
    "options": ["工夫", "用意", "計画", "訓練"], "answer": 3,
    "grammar_points": ["語彙: 訓練"], "difficulty": 2,
    "explanation": "犬や動物にしつけや能力を教え込む動作を表す語彙です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q18", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "明日は7時に出かけるので、目覚まし時計を6時に（　）した。",
    "options": ["スタート", "セット", "ストップ", "マーク"], "answer": 2,
    "grammar_points": ["外来語: セットする"], "difficulty": 1,
    "explanation": "時計や機器の時間を設定することを「セットする」といいます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q19", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "忙しいのにこんなに待たされて時間が（　）。",
    "options": ["だらしない", "しょうがない", "なさけない", "もったいない"], "answer": 4,
    "grammar_points": ["形容詞: もったいない"], "difficulty": 2,
    "explanation": "貴重な時間や物が無駄に浪費されるのを惜しむ気持ちは「もったいない」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q20", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "友人の家で食べたケーキが美味しかったので（　）と作り方を教えてもらった。",
    "options": ["資源", "材料", "部品", "原因"], "answer": 2,
    "grammar_points": ["語彙: 材料"], "difficulty": 1,
    "explanation": "料理やお菓子を作るもとになるものは「材料（ざいりょう）」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q21", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このソファーの愛用（　）にアンケートをした。",
    "options": ["屋", "人", "者", "員"], "answer": 3,
    "grammar_points": ["接尾辞: 愛用者 (〜しゃ)"], "difficulty": 2,
    "explanation": "好んで日頃から愛用している人を表す接尾辞は「者（しゃ）」で、「愛用者」となります。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q22", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "工事のせいで道路が（　）していて、車がなかなか前に進まない。",
    "options": ["渋滞", "故障", "増加", "集合"], "answer": 1,
    "grammar_points": ["語彙: 渋滞 (じゅうたい)"], "difficulty": 1,
    "explanation": "車が混雑して進まない状態は「渋滞（じゅうたい）」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q23", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "薬の（　）が出て、少し具合はよくなりました。",
    "options": ["成績", "効果", "応援", "価値"], "answer": 2,
    "grammar_points": ["語彙: 効果が出る"], "difficulty": 1,
    "explanation": "薬や治療の効き目・結果が現れることを「効果が出る」といいます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q24", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "彼は日本にまだ一年しか住んでいないのに、日本語が（　）だ。",
    "options": ["さらさら", "ばらばら", "ふらふら", "ペラペラ"], "answer": 4,
    "grammar_points": ["オノマトペ: ペラペラ"], "difficulty": 1,
    "explanation": "外国語を流暢に話す様子を表す副詞・オノマトペは「ペラペラ」です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q25", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この学校で一生懸命に勉強して、知識や技術を（　）と思っている。",
    "options": ["身につけたい", "気に入りたい", "押し込みたい", "取り上げたい"], "answer": 1,
    "grammar_points": ["慣用句: 身につける"], "difficulty": 1,
    "explanation": "技術や学問・習慣を習得して自分のものにすることを「身につける」といいます。"
  },

  # 問題4: 言い換え類義語 (5)
  {
    "id": "jlpt_n3_2021_07_v_q26", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今日の会議では【さまざまな】意見が出た。",
    "options": ["とくべつ", "すばらしい", "いろいろな", "あたらしい"], "answer": 3,
    "grammar_points": ["類義語: さまざまな＝いろいろな"], "difficulty": 1,
    "explanation": "「さまざまな」は種類や様子が多い「いろいろな」と同義です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q27", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "できるだけ早めに【報告して】ください。",
    "options": ["頼んで", "知らせて", "尋ねて", "探して"], "answer": 2,
    "grammar_points": ["類義語: 報告する＝知らせる"], "difficulty": 1,
    "explanation": "「報告する」は相手に状況や結果を伝える「知らせる」と言い換えられます。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q28", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "山田さんは【絶対に】来ると思います。",
    "options": ["あとで", "すぐに", "たぶん", "かならず"], "answer": 4,
    "grammar_points": ["類義語: 絶対に＝かならず"], "difficulty": 1,
    "explanation": "「絶対に（ぜったいに）」は確信をもって例外のないことを表す「かならず」と同義です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q29", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この話は【おしまい】です。",
    "options": ["おわり", "すごい", "はじめて", "おもしろい"], "answer": 1,
    "grammar_points": ["類義語: おしまい＝おわり"], "difficulty": 1,
    "explanation": "「おしまい」は物事の結末・終了を意味する「おわり」と同義です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q30", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "先週、学校を【サボって】しまった。",
    "options": [
      "病気になって学校を辞めてしまった",
      "病気になって学校を休んでしまった",
      "遊びたくて学校を辞めてしまった",
      "遊びたくて、学校を休んでしまった"
    ],
    "answer": 4,
    "grammar_points": ["類義語: サボる＝遊びたくて休む"], "difficulty": 2,
    "explanation": "「サボる」は正当な理由がなく怠けて義務や授業を休むことを意味します。"
  },

  # 問題5: 用法 (5)
  {
    "id": "jlpt_n3_2021_07_v_q31", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【オーバー】",
    "options": [
      "飛行機の出発時間がオーバーになった。",
      "安いのがなくて、1万円もオーバーしてしまった。",
      "考えすぎて、頭がオーバーになった。",
      "料理がオーバーして、もう食べられない。"
    ],
    "answer": 2,
    "grammar_points": ["外来語用法: オーバーする (超過)"], "difficulty": 2,
    "explanation": "「オーバーする」は一定の基準や予算の限度を超えることです。2の「1万円もオーバーしてしまった」が自然です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q32", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【欠点】",
    "options": [
      "ここは景色のいい場所だが、駅から遠いという欠点がある。",
      "栄養に欠点が出ないように、食事のメニューを考えている。",
      "カードレールぶつけて、車に欠点が付いてしまった。",
      "メールを送る前に、メールアドレスに欠点がないか確認しよう。"
    ],
    "answer": 1,
    "grammar_points": ["語彙用法: 欠点 (けってん)"], "difficulty": 2,
    "explanation": "「欠点」は不十分なところ、短所を表します。1の「駅から遠いという欠点がある」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q33", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【親しい】",
    "options": [
      "私は学生のころ、数学より料理の方が親しかった彼女。",
      "彼女はとても親しい道を教えてください。",
      "久しぶりに友達と会って、親しかった。",
      "引っ越してきたばかりで、近くにまだ親しい人はいない。"
    ],
    "answer": 4,
    "grammar_points": ["形容詞用法: 親しい (したしい)"], "difficulty": 2,
    "explanation": "「親しい」は人間関係の間柄が近い・仲が良いことを表します。4の「親しい人」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q34", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【詰める】",
    "options": [
      "明日帰国するので、カバンに洋服やお土産を詰めた。",
      "テーブルに食器を2枚詰めて、朝食の準備をして。",
      "忘れないように、大切なことをノートに詰めた。",
      "ジャケットのポケットに手を詰めて、切符を出した。"
    ],
    "answer": 1,
    "grammar_points": ["動詞用法: 詰める (つめる)"], "difficulty": 2,
    "explanation": "「詰める」は容器やカバンなどに隙間なく物を入れ込むことです。1が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_v_q35", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【支給】",
    "options": [
      "母の誕生日何かプレゼントを支給しようと思う。",
      "これから先生にレポートを支給しに行く。",
      "この会社は家から会社までの交通費を支給してくれる。",
      "会議が始まる前に、この資料を支給してください。"
    ],
    "answer": 3,
    "grammar_points": ["語彙用法: 支給 (しきゅう)"], "difficulty": 2,
    "explanation": "「支給する」はお金や物品を給与・手当として払い出すことです。3の「交通費を支給してくれる」が正解です。"
  }
]

# ------------------------------------------------------------------
# 2. SECTION 2: 言語知識（文法） (22 questions)
# ------------------------------------------------------------------
grammar_questions = [
  # 問題1: 文法形式の判断 (13)
  {
    "id": "jlpt_n3_2021_07_g_q01", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "両親に買ってもらった着物（　）大学の卒業式に出席した。",
    "options": ["を", "が", "で", "に"], "answer": 3,
    "grammar_points": ["助詞: で (手段・装い)"], "difficulty": 1,
    "explanation": "身につける衣服を手段・状態として表す助詞「で」（着物で出席した）が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q02", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "本を読んでいたら（　）5時間も経ってしまった。",
    "options": ["そろそろ", "だんだん", "ようやく", "いつのまにか"], "answer": 4,
    "grammar_points": ["副詞: いつのまにか"], "difficulty": 1,
    "explanation": "本に熱中して気づかないうちに時間が経過した様子を表す「いつのまにか」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q03", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私に（　）今一番大切なものは飼っている犬です。",
    "options": ["対して", "比べて", "おいて", "とって"], "answer": 4,
    "grammar_points": ["文法: 〜にとって"], "difficulty": 1,
    "explanation": "「〜の立場や視点から見ると」という評価の基準を表す「〜にとって」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q04", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "A「部長の田中とお会いになるのは今日が初めてですか。」\nB「はい。山下課長（　）お目にかかったことがございませんので。」",
    "options": ["にだけ", "にしか", "でしか", "でだけ"], "answer": 2,
    "grammar_points": ["文法: 〜にしか〜ない"], "difficulty": 2,
    "explanation": "対象を表す格助詞「に」＋限定否定の「しか」で「山下課長にしかお会いしたことがない」となります。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q05", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この図書館は入り口の近くに、返す本を入れるためのブックポストがあり、図書館が閉まっている（　）、本を返すことができます。",
    "options": ["ときでも", "ままで", "間だから", "ところなら"], "answer": 1,
    "grammar_points": ["文法: 〜ときでも (逆接・譲歩)"], "difficulty": 2,
    "explanation": "「閉まっているときであっても可能」という譲歩条件を表す「ときでも」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q06", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "A「今夜は晴れているから星がよく見えるよ。」\nB「わあ、本当だ。（　）きれいなんだろうか。」",
    "options": ["何とか", "なんか", "なんて", "何でも"], "answer": 3,
    "grammar_points": ["感嘆表現: なんて〜だろう"], "difficulty": 2,
    "explanation": "強い感嘆や驚きを表す構文「なんて〜なんだろうか」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q07", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "展覧会に知り合いの絵が飾られるので、わたしも見に（　）と思う。",
    "options": ["行こうか", "行かないか", "行くのか", "行ったか"], "answer": 1,
    "grammar_points": ["文法: 〜ようかと思う (意志の検討)"], "difficulty": 2,
    "explanation": "自分の計画・意志をやわらかく表す「〜ようかと思う」の形です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q08", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "夏は食べ物が悪く（　）ので、注意してください。",
    "options": ["なりにくい", "しやすい", "しにくい", "なりやすい"], "answer": 4,
    "grammar_points": ["文法: 〜やすい (傾向)"], "difficulty": 1,
    "explanation": "「悪くなる」に「〜しやすい・なりやすい」がつき、「悪くなりやすい」となります。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q09", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "乗っていた電車が急に止まって、隣に立っている人に新しい白い靴を（　）。",
    "options": ["踏んでしまった", "踏んでおいた", "踏まれてしまった", "踏ませておいた"], "answer": 3,
    "grammar_points": ["迷惑受け身: 〜てしまう"], "difficulty": 2,
    "explanation": "他人の動作によって自分が被害を受けた迷惑の受身「踏まれてしまった」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q10", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "明日からテニスの国際大会が始まる。参加する8名は皆、過去に国際大会での優勝経験があり、今回の大会は誰が（　）。",
    "options": [
      "優勝しても不思議ではない",
      "優勝したらいい",
      "優勝するに違いない",
      "優勝するのではないだろうか"
    ],
    "answer": 1,
    "grammar_points": ["文法: 〜ても不思議ではない"], "difficulty": 2,
    "explanation": "全員の実力が高いため「誰が優勝しても当然である・おかしくない」という意味の「優勝しても不思議ではない」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q11", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（駅の改札口で）\n妻「あ、もう10時だよ。急がないと新幹線が出発（　）。」\n夫「本当だ。急ごう。」",
    "options": ["してる", "しとく", "しちゃう", "しなきゃ"], "answer": 3,
    "grammar_points": ["縮約表現: 〜ちゃう (〜てしまう)"], "difficulty": 2,
    "explanation": "意図しない残念な結果になってしまうことを口語で表す「出発しちゃう（出発してしまう）」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q12", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "山田「あ、課長。昨日はどうもごちそうさまでした。おいしい食べ物をたくさん（　）。」\n課長「それはよかった。またうちで食事しよう。」",
    "options": [
      "いただいていました",
      "いただきました",
      "めしあがっていました",
      "めしあがりました"
    ],
    "answer": 2,
    "grammar_points": ["敬語: いただく (謙譲語)"], "difficulty": 2,
    "explanation": "相手にごちそうになった自分の動作をへりくだって言う過去形の謙譲語「いただきました」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q13", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "妻「明日食べに行くラーメン屋、11時半ごろから込むらしいよ。」\n夫「じゃあ、11時過ぎに店に着けるように早めに家を（　）ね。」\n妻「うん、そうだね、早めに出よう。」",
    "options": [
      "出るつもりかもしれない",
      "出たほうがいいかもしれない",
      "出てはいけなそうだ",
      "出なくてもよさそうだ"
    ],
    "answer": 2,
    "grammar_points": ["提案・助言: 〜ほうがいいかもしれない"], "difficulty": 2,
    "explanation": "混雑を避けるための控えめな提案を表す「出たほうがいいかもしれない」が適切です。"
  },

  # 問題2: 文の組み立て (5)
  {
    "id": "jlpt_n3_2021_07_g_q14", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "先生「みなさんは、一度 ＿＿ ★ ＿＿ ＿＿ と思う人はいますか。」",
    "options": ["会ってみたい", "いい", "で", "から"], "answer": 2,
    "grammar_points": ["文法星並べ: 〜でいいから〜てみたい"], "difficulty": 2,
    "explanation": "正しい並び順：一度 [3 で] ★[2 いい] [4 から] [1 会ってみたい] と思う人はいますか。★に入るのは 2 です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q15", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "A「パーティーの料理はどうでしたか。」\nB「おいしかったです。＿＿ ＿＿ ★ ＿＿ わかりませんが、お刺身がおいしかったです。」",
    "options": ["という", "何", "か", "魚"], "answer": 4,
    "grammar_points": ["文法星並べ: 何という魚かわかりませんが"], "difficulty": 2,
    "explanation": "正しい並び順：[2 何] [1 という] ★[4 魚] [3 か] わかりませんが。★に入るのは 4 です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q16", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "A「京都旅行の写真を早く送って」\nB「送る ＿＿ ＿＿ ★ ＿＿ から、もう少し待って。」",
    "options": ["選んでいる", "写真を", "今", "ところだ"], "answer": 1,
    "grammar_points": ["文法星並べ: 〜ているところだから"], "difficulty": 2,
    "explanation": "正しい並び順：送る [2 写真を] [3 今] ★[1 選んでいる] [4 ところだ] から。★に入るのは 1 です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q17", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私は料理が ＿＿ ＿＿ ★ ＿＿ ほとんどない。",
    "options": ["苦手で", "料理は", "作れる", "レシピを見ずに"], "answer": 3,
    "grammar_points": ["文法星並べ: 苦手でレシピを見ずに作れる料理は"], "difficulty": 2,
    "explanation": "正しい並び順：私は料理が [1 苦手で] [4 レシピを見ずに] ★[3 作れる] [2 料理は] ほとんどない。★に入るのは 3 です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q18", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この島は、空から ＿＿ ＿＿ ★ ＿＿「耳島」と呼ばれています。",
    "options": ["形に", "見えることから", "人の耳のような", "見ると"], "answer": 1,
    "grammar_points": ["文法星並べ: 〜と〜に見えることから"], "difficulty": 2,
    "explanation": "正しい並び順：この島は、空から [4 見ると] [3 人の耳のような] ★[1 形に] [2 見えることから]「耳島」と呼ばれています。★に入るのは 1 です。"
  },

  # 問題3: 文章の文法 (4)
  {
    "id": "jlpt_n3_2021_07_g_q19", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p07_m3", "question": "【 19 】に入るものを選びなさい。",
    "options": [
      "するだろうと思いました",
      "させるだろうと思いました",
      "するようにしていました",
      "させるようにしていました"
    ],
    "answer": 3,
    "grammar_points": ["文法: 〜ようにしていた (習慣・方針)"], "difficulty": 2,
    "explanation": "自分の方針として意識的に心がけて継続していた動作を表す「するようにしていました」が適切です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q20", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p07_m3", "question": "【 20 】に入るものを選びなさい。",
    "options": ["ただ", "そのうえ", "つまり", "やはり"], "answer": 1,
    "grammar_points": ["接続詞: ただ (補足的な制限)"], "difficulty": 2,
    "explanation": "前文の楽しさを認めた上で、「しかし疲れてくると大変」という制限・補足を導入する「ただ」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q21", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p07_m3", "question": "【 21 】に入るものを選びなさい。",
    "options": [
      "わかってほしいのです",
      "わかっているからです",
      "わかりそうにありません",
      "わからなければなりません"
    ],
    "answer": 2,
    "grammar_points": ["文末表現: 〜からです (理由説明)"], "difficulty": 2,
    "explanation": "安心できる理由としてチェーン店ならメニューや注文方法が既知であると説明する「わかっているからです」が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_g_q22", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p07_m3", "question": "【 22 】に入るものを選びなさい。",
    "options": ["店", "この店", "ある店", "そういう店"], "answer": 4,
    "grammar_points": ["指示詞: そういう店 (属性の総称)"], "difficulty": 2,
    "explanation": "「どこにでもある全国チェーンのような店」という前述のタイプの店を指すため「そういう店」が適切です。"
  }
]

# ------------------------------------------------------------------
# 3. SECTION 3: 読解 (16 questions)
# ------------------------------------------------------------------
reading_questions = [
  # 問題4: 短文読解 (4)
  {
    "id": "jlpt_n3_2021_07_r_q01", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p08_1", "question": "このメモを読んで、たかしさんがしなければならないことは何か。",
    "options": [
      "おじいちゃんの所へ行く。",
      "昨日のカレーの残りを温めて食べる。",
      "洗濯物を取り込む。",
      "ケーキを買って帰る。"
    ],
    "answer": 3,
    "grammar_points": ["短文読解: 伝言メモの必須指示"], "difficulty": 1,
    "explanation": "「洗濯物が干したままになっているから、取り込んでおいてね」と指示されており、必ずしなければならないことです。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q02", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p08_2", "question": "東京ホテルのサービスについて、どんなことがわかるか。",
    "options": [
      "インターネットで予約すると、1泊料金と朝食が10%割引になる場合がある。",
      "インターネットで2月中に予約すると、朝食が10%割引になる場合がある。",
      "インターネットで予約し、2月中に泊まると、1泊料金が10%割引され、朝食が無料になる場合がある。",
      "インターネット、電話、ファックスので予約しても、2月中は朝食だけ無料になる場合がある。"
    ],
    "answer": 3,
    "grammar_points": ["短文読解: キャンペーン条件の確認"], "difficulty": 2,
    "explanation": "「インターネットで予約され、2月28日までにお泊まりの方は、1泊の料金を10％割引し、ご朝食を無料にいたします（1日10室限定）」と書かれているため、3が正解です。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q03", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p09_3", "question": "がっかりしてしまったのはなぜか。",
    "options": [
      "自分では歩くのが速くなったと思っていたが、実はそうではなかったから",
      "せっかく走って渡れるようになったのに、その必要がなくなったから",
      "自分は時間内に歩いて渡れるのに、歩行者用信号の青の時間が長くなったから",
      "警察が、歩行者用信号の青の時間を少ししか長くしてくれなかったから。"
    ],
    "answer": 1,
    "grammar_points": ["短文読解: 心理・理由の把握"], "difficulty": 2,
    "explanation": "自分が速く歩けるようになったと思って喜んでいたが、実際は警察が青信号の時間を延ばしただけだったと知ったためです。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q04", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p09_4", "question": "朝の歯磨きについて、この文章からわかることは何か。",
    "options": [
      "男性は「食前」に磨く人が「食後」に磨く人より多い。",
      "女性は「食前と食後」に磨く人が「食前」に磨く人より多い。",
      "性別に関係なく、「食前」に歯を磨いている人が60％以上いる。",
      "年齢が高くなると、「食後」に磨く人より「食前」に磨く人が多くなる。"
    ],
    "answer": 2,
    "grammar_points": ["短文読解: アンケートデータの読み取り"], "difficulty": 2,
    "explanation": "女性の順位は「食後」が1位、次は「食前と食後」と書かれており、「食前」よりも「食前と食後」に磨く人の方が多いことがわかります。"
  },

  # 問題5: 中文読解 (6)
  {
    "id": "jlpt_n3_2021_07_r_q05", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p10_m5_1", "question": "【①店の思い出はそのまま子どものころの思い出と重なる】とあるが、それはどんな思い出か。",
    "options": [
      "わたしが小学校に入学した時に、この花屋が開店したこと",
      "小学校を卒業する時に、先生といっしょにこの花屋で花を買ったこと",
      "特別なことがある時には、よくこの店で花を買っていたこと",
      "おじさんが大好きだったので、よくこの店で花を買っていたこと。"
    ],
    "answer": 3,
    "grammar_points": ["中文読解: 指示内容の把握"], "difficulty": 2,
    "explanation": "直後に「家族の誕生日や家にお客さんが来る時などには、母といっしょにこの店で花を買っていた」と具体的に説明されています。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q06", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p10_m5_1", "question": "【②わたしたちはどきどきしながら】とあるが、どうしてどきどきしたのか。",
    "options": [
      "もうすぐ閉店する花屋のおじさんに、無理なお願いをするから",
      "いやそうな顔をしているおじさんに、無理なお願いをするから",
      "お店に花があまりないのに、おじさんに無理なお願いをするから",
      "お金が少ししかないのに、おじさんに無理なお願いをするから。"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 感情の原因"], "difficulty": 2,
    "explanation": "「小学生のおこづかいの中から集まったお金は少しだけだった。それで、わたしたちはどきどきしながら『できるだけ大きい花束を作ってください』とお願いした」とあるためです。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q07", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p10_m5_1", "question": "この文章を書いていた人が一番伝えたいことは何か。",
    "options": [
      "小学校時代にとてもお世話になった先生へのお礼の気持ち",
      "良い思い出を作ってくれた花屋のおじさんへの感謝の気持ち",
      "大好きだった花屋さんが閉店するので、寂しいという気持ち",
      "近所の花屋さんが閉店したので、とても不便だという気持ち。"
    ],
    "answer": 2,
    "grammar_points": ["中文読解: 筆者の主眼・感謝の対象"], "difficulty": 2,
    "explanation": "最後の文で「30年以上もきれいな花束を作り続け、あたたかい思い出を作ってくれたおじさんに、『ありがとう、お疲れ様でした』と言いたい」と花屋のおじさんへの感謝を結んでいます。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q08", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p11_m5_2", "question": "【①面白いのは】とあるが、どうして「面白い」と言っているか。",
    "options": [
      "暑い夏に冷たいものを食べると、体が涼しく感じるから",
      "寒い冬に冷たいものを食べると、おいしく感じられるから",
      "季節に関係なく一年中アイスクリームが売られているから",
      "よく売れるアイスクリームの種類は季節によって違うから"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 注目点の把握"], "difficulty": 2,
    "explanation": "「面白いのは夏と冬ではよく売れるアイスの種類が違うことです」と直後に明記されています。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q09", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p11_m5_2", "question": "【②氷はとても大事なものでした】とあるが、それはどうしてか。",
    "options": [
      "冬に特別な部屋で作った氷だったし、とけないように運ぶのも大変だったから",
      "冬に作った氷は特別な味がしたし、時間がたつととけてなくなってしまうから",
      "夏に作った氷はとてもめずらしかったし、暑さですぐとけてしまうものだったから",
      "夏の氷はめずらしかったし、町まで運ぶ途中でとけて小さくなってしまうから。"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 因果関係の理解"], "difficulty": 2,
    "explanation": "町まで遠く運ぶ間に少しずつ溶けて小さくなるため、貴重で大事なものだったと述べられています。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q10", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "次の1から2の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p11_m5_2", "question": "【③夏の氷は特別なごちそうだったのでしょう】とあるが、ここで言いたいことはどのようなことか。",
    "options": [
      "氷は昔は冬の食べ物だったので、夏に食べることはとても珍しいことだった。",
      "まだアイスクリームを買うことは難しかった、みんな氷でがまんしていた",
      "暑い夏に氷を食べて涼しさを感じることは、日常的にできることではなかった",
      "涼しくなるように氷を食べることは、そのころ人々がよくやっていたことだった。"
    ],
    "answer": 1,
    "grammar_points": ["中文読解: 筆者の推論の趣旨"], "difficulty": 2,
    "explanation": "現代と異なり、昔は夏に氷を口にすること自体が大変希少で特別な贅沢であったことを表しています。"
  },

  # 問題6: 長文読解 (4)
  {
    "id": "jlpt_n3_2021_07_r_q11", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p12_m6", "question": "【①印象的なテレビのコマーシャル（CM）】とあるが、どのような点が印象的だったのか。",
    "options": [
      "洗濯洗剤のCMに女性が登場している点",
      "洗濯洗剤なのに、いい香りがついている点",
      "洗濯洗剤が汚れをよく落とすことを強く言っている点",
      "洗濯洗剤なのに、汚れを落とすことについて全く言っていない点。"
    ],
    "answer": 4,
    "grammar_points": ["長文読解: 特徴の把握"], "difficulty": 2,
    "explanation": "「洗濯洗剤を使う目的は汚れを落とすことなのに、そのCMでは香りのことばかり言っていて、汚れをよく落とすことは全く言っていなかった」とあります。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q12", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p12_m6", "question": "洗濯洗剤「X」を作った会社が伝えたかった、「X」の特長は何か。",
    "options": [
      "シーツを洗うための洗濯洗剤であること",
      "洗濯洗剤「A」より値段がとても安いこと",
      "どんな洗濯洗剤よりも汚れをよく落とすこと",
      "香りを楽しめる洗濯洗剤であること。"
    ],
    "answer": 4,
    "grammar_points": ["長文読解: 商品の差別化ポイント"], "difficulty": 2,
    "explanation": "「『X』は、『A』と値段はあまり変わらないが、汚れを落とすだけでなく、香りも楽しめるのが特長だった」と書かれています。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q13", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p12_m6", "question": "洗濯洗剤「X」は、どのように売れたか。",
    "options": [
      "初めはあまり売れなかったが、よく売れるようになった。",
      "初めはよく売れたが、あまり売れなくなった。",
      "初めからずっとよく売れていた。",
      "初めからずっとあまり売れなかった。"
    ],
    "answer": 1,
    "grammar_points": ["長文読解: 経緯の把握"], "difficulty": 2,
    "explanation": "「最初、『X』は期待していたようには売れなかった...それ以降、『X』もよく売れるようになったそうだ」とあります。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q14", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "次の文章を読んで、後の問いに対する答えとして最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p12_m6", "question": "【②私が見たCM】について、「私」は今、どのようなことを考えているか。",
    "options": [
      "「私」には意味がわからなかったし、多くの消費者にも宣伝効果がなかったのだ。",
      "「私」は変なCMだと思っていたが、多くの消費者には宣伝効果があったのだ。",
      "「私」は効果的なCMだと思っていたし、多くの消費者にも宣伝効果があったのだ。",
      "「私」には印象的だったが、多くの消費者には宣伝効果がなかったのだ。"
    ],
    "answer": 2,
    "grammar_points": ["長文読解: 筆者の認識の変化"], "difficulty": 2,
    "explanation": "最後の文で「私がちょっと変だと感じたあのCMは、実は十分に宣伝効果があったのだ」と述べています。"
  },

  # 問題7: 情報検索 (2)
  {
    "id": "jlpt_n3_2021_07_r_q15", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "次の文章は「山中さくらまつりに協力してくれる人を募集するための案内」である。次の質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p14_m7", "question": "太郎君は山中市に住む17歳の高校生で、さくらまつりの協力者になりたいと思っている。土曜日はいつも朝から夕方まで、クラブ活動がある。太郎君が応募できるのはどれか。",
    "options": ["①と②", "②と③", "④と⑤", "⑤と⑥"], "answer": 3,
    "grammar_points": ["情報検索: 年齢制限と曜日時間の絞り込み"], "difficulty": 2,
    "explanation": "土曜日は部活があるため①②は不可。17歳なので③と⑥（20歳以上限定）は不可。したがって日曜日（4月5日）の④（午前9時〜午後1時）と⑤（午後1時〜午後6時）に応募できます。"
  },
  {
    "id": "jlpt_n3_2021_07_r_q16", "book": "JLPT N3 2021年7月 過去問", "book_code": "jlpt_n3_2021_07",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "次の文章は「山中さくらまつりに協力してくれる人を募集するための案内」である。次の質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2021_07_p14_m7", "question": "さくらまつりの協力者になるためには、どうすればよいか。",
    "options": [
      "3月27日までになるべく早く市役所に郵便かファックスで申し込む。",
      "3月27日までの平日の午前9時から午後5時の間に電話で申し込む。",
      "できるだけ早く山中市役所の市民課広田さんにEメールで申し込む。",
      "市役所ホームページの応募用紙を使ってインターネットで申し込む。"
    ],
    "answer": 1,
    "grammar_points": ["情報検索: 申込方法と締切の照合"], "difficulty": 2,
    "explanation": "申し込み方法欄に「別紙の応募用紙に必要なことを記入して、ファックスまたは郵送してください（先着順）」とあり、締切は3月27日です。電話やメールは問い合わせ専用、HPは用紙入手のみです。"
  }
]

# ------------------------------------------------------------------
# 4. PASSAGES (9 passages)
# ------------------------------------------------------------------
passages = {
  "jlpt_n3_2021_07_p07_m3": {
    "id": "jlpt_n3_2021_07_p07_m3",
    "title": "日本の飲食店",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 7,
    "type": "bunshou_bunpou",
    "content": "以下は、留学生の作文である。\n\n日本の飲食店\n\n　私は子供のときから旅行が大好きです。日本でもいろいろなところへ旅行に行きました。日本では、違う町に行っても、ファミレスや定食屋、ファストフード店など、同じような飲食店が多いと感じます。日本各地にはおいしい食べ物がたくさんあるのだから、そこにしかない飲食店に行くほうがいいと思いました。それで、旅行のときはずっと、その土地にしかない店で食事を【 19 】。\n　旅行先で行ったことがない店に行くのはたのしいです。【 20 】、旅行を続けていると、途中で疲れてきます。疲れているとき、慣れない店に行くのは少し大変です。そんなとき、家の近くにもあるファミレスや定食屋が旅行先にもあるのはいいことだと思うようになりました。メニューも注文方法も【 21 】。私は旅行中に疲れたとき、近所にもあるレストランに入るようになりました。\n　どこでもある同じような店行くことは旅行先だけでできる特別な経験ではありませんが、安心感があります。【 22 】の、今まで知らなかったいいところを見つけることができました。"
  },
  "jlpt_n3_2021_07_p08_1": {
    "id": "jlpt_n3_2021_07_p08_1",
    "title": "母からのメモ",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（１）\nたかしさんの家のテーブルの上に、このメモがある。\n\nたかしへ\n　急な用事で、ちょっとおじいちゃんの所へ行かなければならなくなりました。7時までには帰れると思うけど、おなかがすいて、待てなかったら、昨日のカレーの残りを温めて食べてください。\n　それから、洗濯物が干したままになっているから、取り込んでおいてね。時間があったら、たたんでおいてください。\n　おいしいケーキでも買って帰るね。\n母"
  },
  "jlpt_n3_2021_07_p08_2": {
    "id": "jlpt_n3_2021_07_p08_2",
    "title": "東京ホテル 料金割引のご案内",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（２）\nこれは、あるホテルから山田さんに届いたメールである。\n\nあて先：QUATJLPT @232mail.com\n件名：東京ホテル 料金割引のご案内\n送信日時：2月1日 16:20\n\n山田真二 様\nいつもご利用ありがとうございます。\n現在、東京ホテルでは、インターネット予約割引サービスを行っております。インターネットで予約され、2月28日までにお泊まりの方は、1泊の料金を10％割引し、ご朝食を無料にいたします。\nこの割引をご利用になれるお部屋は一日10室だけですので、お早めにご予約ください。\nなお、このサービスは、電話、ファックスでご予約の場合はご利用できません。\nご予約を心よりお待ちしております。\n東京ホテル お客様サービス係"
  },
  "jlpt_n3_2021_07_p09_3": {
    "id": "jlpt_n3_2021_07_p09_3",
    "title": "歩行者用信号",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 9,
    "type": "dokkai_tandun",
    "content": "（３）\n　駅前の交差点の信号は赤になるのが早く、少し遅れると、途中から走って渡らなければならないことも多かった。しかし、一か月ぐらい前からは走らなくても時間内に渡れるようになった。それで、歩くのが速くなったと思って喜んでいたのだが、今朝の新聞を読んで本当の理由がわかった。あの歩行者用信号は時間内に渡れない人が多かったので、警察が青の時間を少し長くしたのだそうだ。それを知って、ちょっとがっかりしてしまった。"
  },
  "jlpt_n3_2021_07_p09_4": {
    "id": "jlpt_n3_2021_07_p09_4",
    "title": "朝の歯磨きアンケート",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 9,
    "type": "dokkai_tandun",
    "content": "（４）\nこれはある雑誌の記事である。\n\n　あるアンケートで、朝、歯を磨く人3,000人に、磨くのは「食前」「食後」「食前と食後」のどれかを聞いた。性別でみると、男性も女性も「食後」に磨く人が最も多く（男性64％、女性72％）、次は、男性が「食前」で、女性が「食前と食後」だった。年齢でみても、各年齢で一番多いのはやはり「食後」だった。\n　しかし、その割合は、年齢が高くなるにしたがって「食後」が減り、「食前」が増えていく。なるほど、うちでは私と両親は食後に、祖父は食前に磨いている。"
  },
  "jlpt_n3_2021_07_p10_m5_1": {
    "id": "jlpt_n3_2021_07_p10_m5_1",
    "title": "町の花屋さんの思い出",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 10,
    "type": "dokkai_chuubun",
    "content": "問題５：\n（１）\n　近所の花屋が閉店した。30年以上も「町の花屋さん」として愛されてきた店だ。この店がオープンしたのは、私が小学校に入る前だった。わたしにとって、①店の思い出はそのまま子どものころの思い出と重なる。家族の誕生日や家にお客さんが来る時などには、母といっしょにこの店で花を買っていた。\n　小学校を卒業する時には、こんなことがあった。クラス全員でお金を出し合い担任の先生に花束をおくることになった。「お礼の気持ちを表すために、見たこともないほど大きいのをおくろう」とわたしたちは話し合った。しかし、小学生のおこづかいの中から集まったお金は少しだけだった。それで、②わたしたちはどきどきしながら「大好きな先生にあげるから、できるだけ大きい花束を作ってください」とお願いした。おじさんはいやな顔もしないで、特別大きなバラの花束を作ってくれた。30年以上もきれいな花束を作り続け、あたたかい思い出を作ってくれたおじさんに、「ありがとう、お疲れ様でした」と言いたい。"
  },
  "jlpt_n3_2021_07_p11_m5_2": {
    "id": "jlpt_n3_2021_07_p11_m5_2",
    "title": "アイスクリームと夏の氷",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 11,
    "type": "dokkai_chuubun",
    "content": "（２）\n　先ずあなたはアイスクリームが好きですか、甘く冷たいアイスクリームは暑い夏に食べると、体が涼しくなるし、寒い冬に暖かい部屋で食べるのも、おいしいものです。今ではアイスクリームは一年中いつでも食べられますが、①面白いのは夏と冬ではよく売れるアイスの種類が違うことです。夏にレモン味のシャーベットなどが、冬にチョコレート味などの濃い味のものがよく売れるそうです。\n　アイスクリームは150年ぐらい前から食べられるようになったのですが実は日本で「氷」を楽しむ習慣は10世紀にはじまったようです。そのころは冬に作った氷を「氷室（ひむろ）」と呼ばれる特別な部屋に運んで、とけないようにしておきました。夏になると、そこから大きな氷を取り出して町まで運びます。町までは遠く、運ぶ間に少しずつとけて小さくなりますから、②氷はとても大事なものでした。そのころは氷をけずって、さとう水をかけて食べていました。今とは違い、③夏の氷は特別なごちそうだったのでしょう。"
  },
  "jlpt_n3_2021_07_p12_m6": {
    "id": "jlpt_n3_2021_07_p12_m6",
    "title": "洗剤XのCM",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 12,
    "type": "dokkai_choubun",
    "content": "問題６：\n　10年近く前、①印象的なテレビのコマーシャル（CM）があった。ある洗濯洗剤「X」のCMなのだが、洗ったシーツの香りを女性が楽しんでいるだけなのだ。洗濯洗剤を使う目的は汚れを落とすことなのに、そのCMでは香りのことばかり言っていて、汚れをよく落とすことは全く言っていなかった。この洗濯洗剤を作っている会社は、どうしてこんなCMにしたのだろうかと思ったが、最近ある本を読んで、その理由がわかった。\n　その本には、次のようなことが書かれていた。この会社には昔から汚れをよく落とす洗濯洗剤「A」という人気商品があったが、会社の売り上げをもっと伸ばすために、新しいタイプの洗濯洗剤を作ることにした。それが「X」だった。「X」は、「A」と値段はあまり変わらないが、汚れを落とすだけでなく、香りも楽しめるのが特長だった。ところが、最初、「X」は期待していたようには売れなかった。初めのころに作ったCMでは、消費者に「X」の特長がうまく伝わらなかったのだ。\n　そこで、この会社はそれまでのCMを大きく変えて、「この商品を使えば、いい香りが楽しめて、とてもいい気分で洗濯ができる」というメッセージを強く伝えることにした。そうして新しく作られたのが、②私が見たCMだったのだ。\n　そのCMによって、「X」の特長が多くの消費者に伝わったようで、それ以降、「X」もよく売れるようになったそうだ。私がちょっと変だと感じたあのCMは、実は十分に宣伝効果があったのだ。"
  },
  "jlpt_n3_2021_07_p14_m7": {
    "id": "jlpt_n3_2021_07_p14_m7",
    "title": "さくら祭りの協力者募集",
    "book": "JLPT N3 2021年7月 過去問",
    "page": 14,
    "type": "dokkai_jouhou_kensaku",
    "content": "さくら祭りの協力者募集\n\n毎年たくさんの人が集まる「このさくら祭り」に協力者として参加してみませんか\n\n【係の各名と仕事内容】\n1. 案内係：会場の案内と各種プログラムに参加する人を行います\n2. 会場係：場内の整備・見回りを行います。\n\n【場所(会場)】\n場所(会場)\n\n【時間】\n① 4月4日(土)：午前9時 - 午後1時\n② 4月4日(土)：午後1時 - 午後6時\n③ 4月4日(土)：午後6時 - 午後9時\n④ 4月5日(日)：午前9時 - 午後1時\n⑤ 4月5日(日)：午後1時 - 午後6時\n⑥ 4月5日(日)：午後6時 - 午後8時\n\n【応募資格】\n市内に住んでいる16歳以上で、2回以上参加が可能な方。\n（③と⑥は20歳以上の方だけです）\n\n【募集人数】\n①〜⑥につき\n・案内係：各10名\n・会場係：各10名\n\n【募集しめ切り】\n3月27日(金)午後5時\nただし、先着順とし、募集人数になったらしめきります\n\n【申し込み方法】\n別紙の応募用紙に必要なことを記入して、ファックスまたは郵送してください。\n応募用紙は市役所ホームページにもございます。\n・ファックス: 0038-26-1870 (山中市役所市民課)\n・郵送: 〒000-8787 山中市本町1-1 山中市役所市民課\n\n【問い合わせ先】\n山中市役所市民課(広田)\n電話: 0038-26-1877\nEメール: hirota@yamanaka-shi.jp"
  }
}

# ------------------------------------------------------------------
# WRITE JSON FILES
# ------------------------------------------------------------------
with open('bank/jlpt_n3_2021_07/vocab.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2021年7月 過去問", "unit": "文字・語彙", "questions": vocab_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2021_07/grammar.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2021年7月 過去問", "unit": "文法", "questions": grammar_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2021_07/reading.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2021年7月 過去問", "unit": "読解", "questions": reading_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2021_07/passages.json', 'w', encoding='utf-8') as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)

print(f"Extraction for 2021 July completed:")
print(f"  Vocab: {len(vocab_questions)} Qs")
print(f"  Grammar: {len(grammar_questions)} Qs")
print(f"  Reading: {len(reading_questions)} Qs")
print(f"  Passages: {len(passages)} passages")
print(f"  Total: {len(vocab_questions) + len(grammar_questions) + len(reading_questions)} Qs")
