# scripts/build_2020_12.py
# -*- coding: utf-8 -*-
import os, json

os.makedirs('bank/jlpt_n3_2020_12', exist_ok=True)

# ------------------------------------------------------------------
# 1. SECTION 1: 言語知識（文字・語彙） (35 questions)
# ------------------------------------------------------------------
vocab_questions = [
  # 問題1: 漢字読み (8)
  {
    "id": "jlpt_n3_2020_12_v_q01", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "まず、この問題を【調査】します。",
    "options": ["ちょうさ", "ちょうさつ", "ちょさ", "ちょさつ"], "answer": 1,
    "grammar_points": ["漢字読み: 調査 (ちょうさ)"], "difficulty": 1,
    "explanation": "「調査」の読み方は「ちょうさ」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q02", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "どんな【種類】がありますか。",
    "options": ["しゅれい", "じゅれい", "しゅるい", "じゅるい"], "answer": 3,
    "grammar_points": ["漢字読み: 種類 (しゅるい)"], "difficulty": 1,
    "explanation": "「種類」の読み方は「しゅるい」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q03", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "この辺は【岩】が多い場所だ。",
    "options": ["かい", "いわ", "すな", "どろ"], "answer": 2,
    "grammar_points": ["漢字読み: 岩 (いわ)"], "difficulty": 1,
    "explanation": "「岩」の読み方は「いわ」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q04", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "たくさんの人と【交流】する。",
    "options": ["ごうりゅ", "ごうりゅう", "こうりゅ", "こうりゅう"], "answer": 4,
    "grammar_points": ["漢字読み: 交流 (こうりゅう)"], "difficulty": 1,
    "explanation": "「交流」の読み方は「こうりゅう」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q05", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "荷物はフロントに【預けて】おきました。",
    "options": ["とどけて", "あすけて", "あずけて", "ととけて"], "answer": 3,
    "grammar_points": ["漢字読み: 預ける (あずける)"], "difficulty": 2,
    "explanation": "「預ける」の読み方は「あずける」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q06", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "わたしは、【普通】、7時に起きます。",
    "options": ["ふうだん", "ふうつう", "ふだん", "ふつう"], "answer": 4,
    "grammar_points": ["漢字読み: 普通 (ふつう)"], "difficulty": 1,
    "explanation": "「普通」の読み方は「ふつう」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q07", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "理由もなく【疑って】はいけないと思う。",
    "options": ["ことわって", "うたがって", "きらって", "おこって"], "answer": 2,
    "grammar_points": ["漢字読み: 疑う (うたがう)"], "difficulty": 2,
    "explanation": "「疑う」の読み方は「うたがう」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q08", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿のことばの読み方として最もよいものを、１・２・３・４から一つえらんでください。",
    "passage_id": None, "question": "来週は旅行で家を【留守】にします。",
    "options": ["るす", "るしゅ", "りゅうす", "りゅうしゅ"], "answer": 1,
    "grammar_points": ["漢字読み: 留守 (るす)"], "difficulty": 1,
    "explanation": "「留守」の読み方は「るす」です。"
  },

  # 問題2: 表記 (6)
  {
    "id": "jlpt_n3_2020_12_v_q09", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "それは【ぎゃく】ですよ。",
    "options": ["途", "迅", "逆", "造"], "answer": 3,
    "grammar_points": ["漢字表記: 逆 (ぎゃく)"], "difficulty": 1,
    "explanation": "「ぎゃく」の漢字は「逆」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q10", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "あしたの朝は気温が【ひくく】なるそうです。",
    "options": ["冷く", "低く", "底く", "令く"], "answer": 2,
    "grammar_points": ["漢字表記: 低い (ひくい)"], "difficulty": 1,
    "explanation": "気温や位置の「ひくい」の漢字は「低い」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q11", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "授業で花の形や色を【かんさつ】しました。",
    "options": ["観祭", "視察", "観察", "視祭"], "answer": 3,
    "grammar_points": ["漢字表記: 観察 (かんさつ)"], "difficulty": 1,
    "explanation": "「かんさつ」の漢字は「観察」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q12", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "田村さんが手紙を読んで【ないて】いた。",
    "options": ["恋いて", "涙いて", "悲いて", "泣いて"], "answer": 4,
    "grammar_points": ["漢字表記: 泣く (なく)"], "difficulty": 1,
    "explanation": "「なく（涙を流す）」の漢字は「泣く」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q13", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "夜の11時【いこう】は、料金が高くなる。",
    "options": ["以降", "以向", "移降", "移向"], "answer": 1,
    "grammar_points": ["漢字表記: 以降 (いこう)"], "difficulty": 2,
    "explanation": "「いこう」の漢字は「以降」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q14", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今は【ふくざつ】な気持ちだ。",
    "options": ["復推", "復雑", "複推", "複雑"], "answer": 4,
    "grammar_points": ["漢字表記: 複雑 (ふくざつ)"], "difficulty": 1,
    "explanation": "「ふくざつ」の漢字は「複雑」です。"
  },

  # 問題3: 文脈規定 (11)
  {
    "id": "jlpt_n3_2020_12_v_q15", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "旅行中に町を歩いていたら、（　）学生時代の友人に会い、とても驚いた。",
    "options": ["あんがい", "せっかく", "ついでに", "ぐうぜん"], "answer": 4,
    "grammar_points": ["副詞: 偶然 (ぐうぜん)"], "difficulty": 1,
    "explanation": "予期せず思いがけず出会ったことを表す「偶然（ぐうぜん）」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q16", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "森さんは明るくて（　）のある人だから、一緒に話していると、とても楽しい。",
    "options": ["カロリー", "アップ", "ユーモア", "レジャー"], "answer": 3,
    "grammar_points": ["外来語: ユーモア"], "difficulty": 1,
    "explanation": "人を笑わせる面白みやしゃれっ気を表す外来語は「ユーモア」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q17", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今度の旅行は、みんなから行きたい場所の（　）を聞いて、どこに行くかを決めます。",
    "options": ["感覚", "希望", "意識", "決心"], "answer": 2,
    "grammar_points": ["語彙: 希望 (きぼう)"], "difficulty": 1,
    "explanation": "こうあってほしいという望みを聞くので「希望」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q18", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この物語に（　）する人たちは、全員女性だ。",
    "options": ["登場", "発生", "外出", "入門"], "answer": 1,
    "grammar_points": ["語彙: 登場する (とうじょう)"], "difficulty": 1,
    "explanation": "劇や小説などの作中に現れることを「登場する」といいます。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q19", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "さっき履いてみた靴は少し大きかったけど、この靴は（　）している。",
    "options": ["はっきり", "しっかり", "ぴったり", "そっくり"], "answer": 3,
    "grammar_points": ["オノマトペ: ぴったり"], "difficulty": 1,
    "explanation": "サイズや寸法がすき間なくちょうどよく合っている様子は「ぴったり」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q20", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "たくさん買い物したので、買った商品を家まで（　）してもらった。",
    "options": ["配達", "報告", "送信", "訪問"], "answer": 1,
    "grammar_points": ["語彙: 配達 (はいたつ)"], "difficulty": 1,
    "explanation": "品物などを指定の場所・家に届けることは「配達」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q21", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "友人に頼まれたので、結婚式の司会を（　）。",
    "options": ["引き出した", "受け取った", "取り付けた", "引き受けた"], "answer": 4,
    "grammar_points": ["複合動詞: 引き受ける (ひきうける)"], "difficulty": 2,
    "explanation": "頼まれた仕事や役目を「承知して自分の責任でやる」動詞は「引き受ける」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q22", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "二つの会社の仕事内容や給料を（　）して、いいと思ったほうの会社に決めた。",
    "options": ["競争", "選択", "区別", "比較"], "answer": 4,
    "grammar_points": ["語彙: 比較する (ひかく)"], "difficulty": 2,
    "explanation": "二つ以上のものを並べて違いや優劣を比べる動作は「比較（ひかく）」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q23", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "朝まで寝ないで本を読んでいたので、今日は眠くて何度も（　）が出た。",
    "options": ["あくび", "くしゃみ", "せき", "しゃっくり"], "answer": 1,
    "grammar_points": ["語彙: あくびが出る"], "difficulty": 1,
    "explanation": "眠いときや退屈なときに無意識に大きく口を開けて息を吸い込む生理現象は「あくび」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q24", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "料理を運ぶのが遅かったので、お客さんから（　）を言われた。",
    "options": ["失礼", "文句", "我慢", "反対"], "answer": 2,
    "grammar_points": ["語彙: 文句を言う (もんく)"], "difficulty": 1,
    "explanation": "不平や不満の言葉を述べる慣用句は「文句を言う」です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q25", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "試合会場に着いた田中選手は、待っていた大勢のファンに（　）。",
    "options": ["うめられた", "つつまれた", "かこまれた", "まぜられた"], "answer": 3,
    "grammar_points": ["動詞受身: 囲まれる (かこまれる)"], "difficulty": 2,
    "explanation": "周囲を人などでぐるりと取り巻かれる状態を表す動詞受身は「囲まれた」です。"
  },

  # 問題4: 言い換え類義語 (5)
  {
    "id": "jlpt_n3_2020_12_v_q26", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "店員に【価格】を聞いてみた。",
    "options": ["結果", "返事", "都合", "値段"], "answer": 4,
    "grammar_points": ["類義語: 価格＝値段"], "difficulty": 1,
    "explanation": "「価格（かかく）」は品物の価値を金銭で表した「値段（ねだん）」と同義です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q27", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "これは【らくな】仕事ではない。",
    "options": ["安全な", "危険な", "簡単な", "大変な"], "answer": 3,
    "grammar_points": ["類義語: 楽な＝簡単な"], "difficulty": 1,
    "explanation": "「楽な（らくな）」は苦労や骨折りがいらず平易である「簡単な」に最も近いです。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q28", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この用紙はあとで【回収します】。",
    "options": ["あつめます", "おくります", "わたします", "すてます"], "answer": 1,
    "grammar_points": ["類義語: 回収する＝集める"], "difficulty": 1,
    "explanation": "「回収する（かいしゅう）」は一度配った物などを取り集める「集めます」と同義です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q29", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私の【めい】はみんな海外に住んでいます。",
    "options": ["兄弟の娘", "兄弟の息子", "両親の姉", "両親の兄"], "answer": 1,
    "grammar_points": ["親族語彙: 姪 (めい)＝兄弟姉妹の娘"], "difficulty": 2,
    "explanation": "「めい（姪）」は自分の兄弟・姉妹の産んだ女の子（娘）を指します。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q30", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿の言葉に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "おばあちゃんから【おこづかい】をもらった。",
    "options": ["お菓子", "お金", "おもちゃ", "おみやげ"], "answer": 2,
    "grammar_points": ["類義語: お小遣い＝自由なお金"], "difficulty": 1,
    "explanation": "「おこづかい（お小遣い）」は個人が自由に使える小額の「お金」のことです。"
  },

  # 問題5: 用法 (5)
  {
    "id": "jlpt_n3_2020_12_v_q31", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【割引】",
    "options": [
      "若者が都会に出ていくので、村の人口が割引になっている。",
      "この美術館は団体で見学を申し込むと、料金が割引になる。",
      "ジョギングを始めてから、体重が少し割引になってきた。",
      "最近、仕事が忙しくて、眠る時間が割引になっている。"
    ],
    "answer": 2,
    "grammar_points": ["語彙用法: 割引 (わりびき)"], "difficulty": 1,
    "explanation": "「割引」は代金・料金を本来の金額から一定割合引くことです。2が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q32", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【気づく】",
    "options": [
      "この絵を見ると、ふるさとの景色に気づいて、懐かしくなる。",
      "隣の部屋がにぎやかで、昨日の夜は声に気づいて眠れなかった。",
      "家に着いたとき、電車に忘れ物をしたことに気づいた。",
      "来月から始まる大学生活に気づくと、とても楽しみだ。"
    ],
    "answer": 3,
    "grammar_points": ["動詞用法: 気づく (きづく)"], "difficulty": 1,
    "explanation": "「気づく」はそれまで知らなかった事実を意識する・発見することです。3が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q33", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【栄養】",
    "options": [
      "栄養が足りないと風邪をひきやすくなるから、食事には気をつけている。",
      "わたしの会社は新商品の発売が成功し、どんどん栄養が増えている。",
      "この飛行機は、スピードは速いが、とても多くの栄養がかかる。",
      "大学の講義は難しいけど、栄養が多いので、がんばっています。"
    ],
    "answer": 1,
    "grammar_points": ["語彙用法: 栄養 (えいよう)"], "difficulty": 1,
    "explanation": "「栄養」は生命や健康を維持するために摂取する滋養成分のことです。1が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q34", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【ふらふら】",
    "options": [
      "暑い日が続いたので、畑の野菜がふらふらだ。",
      "熱があるから、立って歩くと少し体がふらふらする。",
      "今日はピアノを一日中弾いていたので、指がふらふらだ。",
      "緊張して声がふらふらしたから、うまくスピーチできなかった。"
    ],
    "answer": 2,
    "grammar_points": ["オノマトペ用法: ふらふらする"], "difficulty": 2,
    "explanation": "「ふらふら」は足元がよろめいて体の安定を失う様子を表します。2が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_v_q35", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文字・語彙", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【滞在】",
    "options": [
      "特急電車は、出発の10分前からホームに滞在している。",
      "少し疲れたので、しばらく喫茶店に滞在しませんか。",
      "わたしの車は、来週まで修理のため工場に滞在しています。",
      "あしたから一週間、仕事で東京に滞在します。"
    ],
    "answer": 4,
    "grammar_points": ["語彙用法: 滞在 (たいざい)"], "difficulty": 2,
    "explanation": "「滞在」はある土地や外国に一定期間とどまり生活することです。4が自然で正確です。"
  }
]

# ------------------------------------------------------------------
# 2. SECTION 2: 言語知識（文法） (22 questions)
# ------------------------------------------------------------------
grammar_questions = [
  # 問題1: 文法形式の判断 (13)
  {
    "id": "jlpt_n3_2020_12_g_q01", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今年の夏は去年（　）暑くない。",
    "options": ["から", "ほど", "まで", "しか"], "answer": 2,
    "grammar_points": ["文法: 〜ほど〜ない (比較否定)"], "difficulty": 1,
    "explanation": "「AはBほど〜ない」で、Bほどその程度が高くないことを表します。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q02", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今朝、電車で隣に座った人から、シャンプー（　）何（　）わからないが、とにかくいい香りがしてきた。",
    "options": ["か／か", "は／は", "が／が", "で／で"], "answer": 1,
    "grammar_points": ["助詞: か何か (不確定例示)"], "difficulty": 2,
    "explanation": "はっきり断定できないものを例示する「シャンプーか何か」の形です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q03", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "課長「林さん、急で悪いんだけど、出張のレポートと明日の会議の資料、今日のお昼ごろまでにできる？」\n林「両方は難しそうです。会議の資料（　）できると思いますが。」",
    "options": ["とでも", "となら", "だけでも", "だけなら"], "answer": 4,
    "grammar_points": ["とりたて助詞: だけなら (限定条件)"], "difficulty": 2,
    "explanation": "「両方は無理だが、その部分に限れば可能である」という限定条件を表す「だけなら」が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q04", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このごろ、朝、早く起こしても、息子が（　）私の言うことを聞かないので困っている。",
    "options": ["やっと", "きっと", "ちっとも", "せっかく"], "answer": 3,
    "grammar_points": ["副詞: ちっとも〜ない (完全否定)"], "difficulty": 2,
    "explanation": "後ろに否定「〜ない」を伴って「少しも〜ない」を強調する「ちっとも」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q05", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "私たちの生活は、技術の進歩の（　）とても便利になった。",
    "options": ["おかげで", "ようで", "ことで", "ほかで"], "answer": 1,
    "grammar_points": ["文法: 〜のおかげで (好結果の原因)"], "difficulty": 1,
    "explanation": "望ましい良い結果をもたらした原因を表す「〜のおかげで」が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q06", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今度の旅行で泊まるYホテルは駅前にあるので、夜遅く駅に（　）、安心だ。",
    "options": ["着いたり", "着いたため", "着いたとしても", "着いたかどうか"], "answer": 3,
    "grammar_points": ["文法: 〜としても (仮定逆接・譲歩)"], "difficulty": 2,
    "explanation": "「たとえ夜遅くに駅に着いた場合であっても（駅前だから安心だ）」という譲歩仮定を表す「着いたとしても」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q07", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "日本に来たのは今回が2度目だ。前に来たのは20年前だが、そのときに人った喫茶店がまだ（　）驚いた。",
    "options": ["営業して", "営業しなくて", "営業していて", "営業していなくて"], "answer": 3,
    "grammar_points": ["て形・理由接続: 〜て驚いた"], "difficulty": 1,
    "explanation": "驚いた直接の原因を表す「まだ営業していて驚いた」が自然です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q08", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "子供のころ、いつも親に絵本を（　）寝ていた。",
    "options": [
      "読んでくれてから",
      "読んでもらってから",
      "読んでくれるから",
      "読んでもらうから"
    ],
    "answer": 2,
    "grammar_points": ["授受表現・時間順序: 〜てもらってから"], "difficulty": 2,
    "explanation": "「親に絵本を読んでもらう」＋その完了後に寝る順序「〜てから」で「読んでもらってから」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q09", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（料理番組で）\n「まず、フライパンで肉をいためます。肉の色が（　）、野菜を入れてください」",
    "options": ["変わっていって", "変わってくるのに", "変わっていくと", "変わってきたら"], "answer": 4,
    "grammar_points": ["文法: 〜てきたら (変化の完了条件)"], "difficulty": 2,
    "explanation": "肉の色が変化してきたそのタイミングを条件として次に移るため「変わってきたら」が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q10", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "赤ちゃんがなかなか寝ない時は、赤ちゃんにクラシック音楽を（　）とよく寝ると聞いた。",
    "options": ["聞かせる", "聞かれる", "聞かされる", "聞いている"], "answer": 1,
    "grammar_points": ["使役形: 聞かせる"], "difficulty": 1,
    "explanation": "他者（赤ちゃん）に音楽を聞くように仕向ける使役動詞「聞かせる」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q11", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（電話で）\n森先生:「はい、北山日本語学校です。」\nリー:「もしもし、中級クラスのリーですが、森先生は（　）か」\n森先生:「あ、リーさん。森です、どうしましたか。」",
    "options": ["ございます", "いらっしゃいます", "拝見します", "お目にかかりまし"], "answer": 2,
    "grammar_points": ["敬語: いらっしゃる (尊敬語)"], "difficulty": 2,
    "explanation": "先生がその場所に居るかどうかを尋ねる尊敬語「いらっしゃいますか」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q12", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "A:「子供が来週から水泳教室に通うんだけど、いろいろ心配なんだよね。」\nB:「始める前から心配（　）しかたないでしょう。大丈夫だよ」",
    "options": [
      "よりしていれば",
      "よりしていても",
      "ばかりしていれば",
      "ばかりしていても"
    ],
    "answer": 4,
    "grammar_points": ["文法: 〜てばかりいても仕方がない"], "difficulty": 2,
    "explanation": "「心配ばかりしていても（何も解決しないので）仕方がない」という逆接・無意味を表す構文です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q13", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の（　）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "夫:「これから会社に行ってくるよ。」\n妻:「あれ、今日は休みでしょう？」\n夫:「さっき会社から電話があって、急に出勤（　）」",
    "options": [
      "しなきゃならなくなった",
      "しちゃいけなくなった",
      "するつもりでいる",
      "しないようにしている"
    ],
    "answer": 1,
    "grammar_points": ["口語義務表現: 〜なきゃならなくなった"], "difficulty": 2,
    "explanation": "予定外の電話連絡により出勤する必要が生じたため「出勤しなきゃならなくなった」が自然です。"
  },

  # 問題2: 文の組み立て (5)
  {
    "id": "jlpt_n3_2020_12_g_q14", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この喫茶店は、コーヒー ＿＿ ＿＿ ★ ＿＿ おいしい。",
    "options": ["などの", "スパゲティ", "料理も", "だけでなく"], "answer": 1,
    "grammar_points": ["文法星並べ: 〜だけでなく〜などの〜も"], "difficulty": 2,
    "explanation": "正しい並び順：コーヒー [4 だけでなく] [2 スパゲティ] ★[1 などの] [3 料理も] おいしい。★に入るのは 1 です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q15", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "（映画館で）\n妻「私、ちょっとジュース買いに行ってくるね。」\n夫「うん。あ、でも、映画が ＿＿ ＿＿ ★ ＿＿ よ。急いでね。」",
    "options": ["しかない", "始まる", "あと3分", "まで"], "answer": 3,
    "grammar_points": ["文法星並べ: 〜まであと〜しかない"], "difficulty": 2,
    "explanation": "正しい並び順：映画が [2 始まる] [4 まで] ★[3 あと3分] [1 しかない] よ。★に入るのは 3 です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q16", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今度の日曜日に友人の結婚式がある。＿＿ ＿＿ ★ ＿＿ が。",
    "options": ["の", "いい", "晴れる", "と"], "answer": 2,
    "grammar_points": ["文法星並べ: 〜といいのだが (願望)"], "difficulty": 2,
    "explanation": "正しい並び順：[3 晴れる] [4 と] ★[2 いい] [1 の] が。★に入るのは 2 です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q17", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "息子は、サッカークラブの練習がきついと ＿＿ ＿＿ ★ ＿＿ 好きだからだと思う。",
    "options": ["よく言っているが", "やっぱりサッカーが", "続けているのは", "それでもやめずに"], "answer": 3,
    "grammar_points": ["文法星並べ: 〜が〜続けているのは"], "difficulty": 2,
    "explanation": "正しい並び順：きついと [1 よく言っているが] [4 それでもやめずに] ★[3 続けているのは] [2 やっぱりサッカーが] 好きだからだと思う。★に入るのは 3 です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q18", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 8, "pdf_page": 8, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "つぎの文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "うちから学校まで自転車で40分かかる。電車なら20分だが、朝の ＿＿ ＿＿ ★ ＿＿ 自転車で通っている。",
    "options": ["こんでいる電車は", "よい運動になるから", "嫌いだし", "自転車で行けば"], "answer": 4,
    "grammar_points": ["文法星並べ: 〜は〜だし〜ば〜から"], "difficulty": 2,
    "explanation": "正しい並び順：朝の [1 こんでいる電車は] [3 嫌いだし] ★[4 自転車で行けば] [2 よい運動になるから] 自転車で通っている。★に入るのは 4 です。"
  },

  # 問題3: 文章の文法 (4)
  {
    "id": "jlpt_n3_2020_12_g_q19", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 9, "pdf_page": 9, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p09_m3", "question": "【 19 】に入るものを選びなさい。",
    "options": ["待つことです", "待ちにくいからです", "待ったところです", "待っているのです"], "answer": 4,
    "grammar_points": ["文脈説明: 〜ているのです (状況の説明)"], "difficulty": 2,
    "explanation": "行列を作って並んでいる人たちの行動理由を説明する「店に入るために待っているのです」が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q20", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 9, "pdf_page": 9, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p09_m3", "question": "【 20 】に入るものを選びなさい。",
    "options": ["でも", "また", "つもり", "そのうえ"], "answer": 1,
    "grammar_points": ["接続詞: でも (逆接)"], "difficulty": 1,
    "explanation": "大勢並んでいたが、友達と話しながら待っていたので苦にならなかったという逆接の「でも」が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q21", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 9, "pdf_page": 9, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p09_m3", "question": "【 21 】に入るものを選びなさい。",
    "options": ["言えて", "言われて", "言ってきて", "言ってくれて"], "answer": 2,
    "grammar_points": ["受動態: 言われて (他者からの発言)"], "difficulty": 2,
    "explanation": "先輩から「いいなあ」とその言葉をかけられた受動の立場を表す「言われて」が適切です。"
  },
  {
    "id": "jlpt_n3_2020_12_g_q22", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "文法", "page": 9, "pdf_page": 9, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、19から22の中に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p09_m3", "question": "【 22 】に入るものを選びなさい。",
    "options": ["その", "どの", "別の", "チーズケーキの"], "answer": 3,
    "grammar_points": ["連体詞: 別の (他の同類)"], "difficulty": 1,
    "explanation": "今回の店とはまた違う「ほかの人気店」という意味を表す「別の」が正解です。"
  }
]

# ------------------------------------------------------------------
# 3. SECTION 3: 読解 (16 questions)
# ------------------------------------------------------------------
reading_questions = [
  # 問題4: 短文読解 (4)
  {
    "id": "jlpt_n3_2020_12_r_q01", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p10_1", "question": "この文章を書いた人が、旅行先で、まずスーパーに入るのはなぜか。",
    "options": [
      "懐かしいふるさとに戻ってきたような気持ちになるから。",
      "魚売り場の広さと、魚の種類の多さを見てみたいから。",
      "ふだんよく利用しているスーパーと広さを比べたいから。",
      "売り場を見て、自分の日常生活との違いを感じたいから。"
    ],
    "answer": 4,
    "grammar_points": ["短文読解: 行動理由の把握"], "difficulty": 2,
    "explanation": "「いつも見ているのとは違う売り場の景色から、自分の日常生活との距離が感じられて、楽しくなるからだ」と明記されています。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q02", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p10_2", "question": "【私の最も好きな時間】とあるが、それはどのような時間か。",
    "options": [
      "月のない暗い夜、電灯で明るい道を、懐中電灯をつけないで歩く時間。",
      "月のない暗い夜、電灯のない道を、懐中電灯をつけて歩く時間。",
      "満月が輝く夜に、電灯のない道を、懐中電灯をつけないで歩く時間。",
      "満月が輝く夜に、昼間は歩かない道を、懐中電灯をつけて歩く時間。"
    ],
    "answer": 3,
    "grammar_points": ["短文読解: 情景の正確な照合"], "difficulty": 2,
    "explanation": "「大きな丸い月が出る満月の夜...明るく輝く月の下では、懐中電灯がなくても周りの景色がわかるのだ...私の最も好きな時間だ」とあります。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q03", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p11_3", "question": "「ゴミゼロ活動」に参加したい全員が、必ずしなければならないことは何か。",
    "options": [
      "前日までにメールで申し込み、当日の9時に手袋を持って第一公園に行く。",
      "前日までにメールで申し込み、当日の9時に手袋とゴミ袋を持って第一公園に行く。",
      "当日の9時に手袋を持って第一公園に行く。",
      "当日の9時に手袋とゴミ袋を持って第一公園に行く。"
    ],
    "answer": 3,
    "grammar_points": ["短文読解: 条件・必須項目の識別"], "difficulty": 2,
    "explanation": "申し込みは「不要」、ゴミ袋は「こちらでも用意します（自宅にあれば持参）」なので任意、手袋だけが「必ず持ってきてください」とあるため、3が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q04", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p11_4", "question": "【この案】とあるが、何か。",
    "options": [
      "中村さんのためにお別れ会をすること。",
      "中村さんにみんなでプレゼントをあげること。",
      "中村さんの好きな物をそれぞれが買って贈ること。",
      "中村さんにどんなプレゼントをもらいたいか聞くこと。"
    ],
    "answer": 2,
    "grammar_points": ["短文読解: 指示語の内容把握"], "difficulty": 1,
    "explanation": "「中村さんに花束と記念品を差し上げたいと思いますが、いかがでしょうか...この案に賛成の方は」とあり、退職する中村さんに贈り物をすることを指します。"
  },

  # 問題5: 中文読解 (6)
  {
    "id": "jlpt_n3_2020_12_r_q05", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p12_m5_1", "question": "【①同じようなこと】とあるが、どのような点が同じなのか。",
    "options": [
      "いつもよりバナナを買う客が多くなること。",
      "一度にいろいろな食べ物を買う客が多くなること。",
      "ある食べ物が、ある日急に売れ出すこと。",
      "果物が、ある時期だけたくさん売れること。"
    ],
    "answer": 3,
    "grammar_points": ["中文読解: 共通点・指示語の把握"], "difficulty": 2,
    "explanation": "直後に「それはトマトだったり魚の缶詰だったりするのですが、ある食べ物が突然大量に売れ出すのです」と説明されています。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q06", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p12_m5_1", "question": "【②理由がわかりました】とあるが、理由は何だったのか。",
    "options": [
      "スーパーがテレビで、その食べ物が健康にいいと宣伝したこと。",
      "店長が売り場にテレビを置いて、売れそうな食べ物を宣伝したこと。",
      "その食べ物が、テレビでおいしいと紹介されてうわさになったこと。",
      "テレビで、その食べ物が健康にいいと紹介されたこと。"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 原因と理由の特定"], "difficulty": 2,
    "explanation": "「テレビ番組で、ある食べ物について、『体にいい』とか『病気を防ぐ効果がある』などと放送されると、翌日はそうなるのだそうです」とあります。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q07", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p12_m5_1", "question": "【③テレビの力は大きいのだな】とあるが、この文章を書いた人はなぜそう思ったのか。",
    "options": [
      "テレビ番組が、人々の行動に影響を与えていると知ったから。",
      "自分の疑問が、テレビ番組を見たことで解決できたと感じたから。",
      "テレビが、スーパーで売れている食べ物をチェックしていると知ったから。",
      "自分が今まで、テレビに影響されていろいろなものを買っていたと気づいたから。"
    ],
    "answer": 1,
    "grammar_points": ["中文読解: 筆者の感想の背景"], "difficulty": 2,
    "explanation": "「テレビ番組1つで、客の買うものが変わり、店で用意する商品も変わると知り」と述べており、人々の行動を変える影響力の大きさに感銘を受けています。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q08", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p13_m5_2", "question": "「私」は、ハンバーガー屋に行ったとき、何を買うと言っているか。",
    "options": [
      "ハンバーガーだけ。",
      "ハンバーガーとポテトだけ。",
      "ポテトと飲み物だけ。",
      "ハンバーガーとポテトと飲み物。"
    ],
    "answer": 1,
    "grammar_points": ["中文読解: 筆者の行動パターンの読み取り"], "difficulty": 1,
    "explanation": "「いつも店員に『ご一緒にポテトやお飲み物はいかがですか。』と聞かれますが、私は『けっこうです。』と言って断っています」とあるため、ハンバーガーのみです。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q09", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 14, "pdf_page": 14, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p13_m5_2", "question": "【①その店】で店員は、どう言うようになったか。",
    "options": [
      "「ありがとうございます。」と言わずに「ご一緒にポテトはいかがですか。」と言う。",
      "「ありがとうございます。」と言った後で、「ご一緒にポテトはいかがですか。」と言う。",
      "「ご一緒にポテトはいかがですか」と言わずに「ありがとうございます。」と言う。",
      "「ご一緒にポテトはいかがですか」と言った後で「ありがとうございます。」と言う。"
    ],
    "answer": 2,
    "grammar_points": ["中文読解: 発話順序の確認"], "difficulty": 2,
    "explanation": "「『ご一緒にポテトはいかがですか』と聞く前に、必ず『ありがとうございます。』と店員に言わせるようにしました」とあるため、2が正解です。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q10", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 14, "pdf_page": 14, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p13_m5_2", "question": "【②「ありがとう」という言葉には、不思議な力があるなと思いました】とあるが、「私」はどうしてそう思ったのか。",
    "options": [
      "ハンバーガー屋に来る客が増えたと聞いたから。",
      "ハンバーガーだけを注文する客が増えたと聞いたから。",
      "ハンバーガーとポテトが好きな客が増えたと聞いたから。",
      "ハンバーガーと一緒にポテトを頼む客が増えたと聞いたから。"
    ],
    "answer": 4,
    "grammar_points": ["中文読解: 心情と結論の理由"], "difficulty": 2,
    "explanation": "「ありがとうございます」と言われると、客が気分をよくして本来買う予定のなかったポテトまで追加注文するようになるからです。"
  },

  # 問題6: 長文読解 (4)
  {
    "id": "jlpt_n3_2020_12_r_q11", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 15, "pdf_page": 15, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p14_m6", "question": "「私」がS市の包丁を使うのはなぜか。",
    "options": [
      "料理がおいしく作れるのに、値段が安いから。",
      "職人が丁寧に作ったもので、よく切れるから。",
      "大量に生産されたもので、売っている店が多いから。",
      "多くの料理人が使っているものを、自分も使いたいから。"
    ],
    "answer": 2,
    "grammar_points": ["長文読解: 主人公の選好理由"], "difficulty": 2,
    "explanation": "「高い技術を持っている人たちが、一本ずつ丁寧に作っているので...料理のおいしさは包丁がよく切れるか、切れないかで大きく変わる」と述べています。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q12", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 15, "pdf_page": 15, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p14_m6", "question": "S市の包丁産業について説明で、合っているものはどれか。",
    "options": [
      "包丁を作る職人の数が減っている。",
      "包丁を作る職人の技術が下がっている。",
      "包丁が工場で大量に生産できるようになった。",
      "包丁が昔と比べて売れなくなった。"
    ],
    "answer": 1,
    "grammar_points": ["長文読解: 業界の現状把握"], "difficulty": 2,
    "explanation": "「職人が年を取って辞めていく一方で、職人になりたいと考える若い人が見つからず、職人の数が減っているのだ」と書かれています。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q13", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 15, "pdf_page": 15, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p14_m6", "question": "【あるコース】の目的は何か。",
    "options": [
      "包丁産業団体にS市の包丁の良さを知ってもらい、もっと海外で売ってもらうこと。",
      "若い料理人にS市の包丁の素晴らしさを知ってもらい、もっと買ってもらうこと。",
      "年を取った職人に包丁作りの指導方法を学んでもらい、若い職人を育ててもらうこと。",
      "若い人に包丁の作り方を学んでもらい、S市で包丁職人になってもらうこと。"
    ],
    "answer": 4,
    "grammar_points": ["長文読解: 施策の目的"], "difficulty": 2,
    "explanation": "後継者不足を解決するため、若い人を全国から募集して1年かけて包丁作りを教え、市内の包丁会社に就職してもらう目的で開かれました。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q14", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 15, "pdf_page": 15, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p14_m6", "question": "今後のS市の包丁産業について、「私」はどう思っているか。",
    "options": [
      "一流の料理人のための包丁だけを作るようにしてほしい。",
      "包丁を工場で大量に生産する方法に変えたほうがいい。",
      "これまでと変わらないやり方で包丁を作っていってほしい。",
      "これまでと違う新しい技術で包丁を作ったほうがいい。"
    ],
    "answer": 3,
    "grammar_points": ["長文読解: 筆者の希望・総括"], "difficulty": 2,
    "explanation": "「若い職人たちにも頑張ってもらって、ずっと続いてきたS市の素晴らしい包丁作りの技術を守っていってほしい」と結んでいます。"
  },

  # 問題7: 情報検索 (2)
  {
    "id": "jlpt_n3_2020_12_r_q15", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 16, "pdf_page": 16, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "右のページは、文化会館の案内である。これを読んで、下の質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p17_m7", "question": "田中さんの高校生の娘は、この会館で踊りを習うことにした。田中さんは、毎回車で娘を会館に送っていくので、週に一回だけ、娘と同じ日時、時間に何か別のものを習いたいと思っている。田中さんはどの教室だったら参加できるか。",
    "options": ["折り紙", "お茶", "お花", "日本料理"], "answer": 1,
    "grammar_points": ["情報検索: 日時と開講回数のマッチング"], "difficulty": 2,
    "explanation": "娘が習う「踊り」は火・土の18:30〜20:00です。田中さんが週1回だけ同じ時間帯に受講できるのは、火曜18:30〜20:00に開講している「折り紙（週1回）」です。"
  },
  {
    "id": "jlpt_n3_2020_12_r_q16", "book": "JLPT N3 2020年12月 過去問", "book_code": "jlpt_n3_2020_12",
    "unit": "読解", "page": 16, "pdf_page": 16, "section": "読解",
    "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
    "instruction": "右のページは、文化会館の案内である。これを読んで、下の質問に答えなさい。答えは、１・２・３・４から最もよいものを一つ選びなさい。",
    "passage_id": "jlpt_n3_2020_12_p17_m7", "question": "山田大学の留学生リーさんは、この会館で柔道の教室に参加したいと思っているが、柔道着を持っていない。リーさんは、参加料と柔道着をどうしたらいいか。",
    "options": [
      "参加料7000円を払い、柔道着は文化会館で借りる。",
      "参加料5000円を払い、柔道着は文化会館で借りる。",
      "参加料7000円を払い、柔道着は自分で買う。",
      "参加料5000円を払い、柔道着は自分で買う。"
    ],
    "answer": 4,
    "grammar_points": ["情報検索: 区分料金と備品条件の確認"], "difficulty": 2,
    "explanation": "柔道は月・木の「週2回の教室」で、大学生のリーさんは「学生（高校生以上）」料金の5,000円が適用されます。また柔道着は貸出がなく「自分で準備してください。会館でも売っています」とあるため、自分で購入します。"
  }
]

# ------------------------------------------------------------------
# 4. PASSAGES (9 passages)
# ------------------------------------------------------------------
passages = {
  "jlpt_n3_2020_12_p09_m3": {
    "id": "jlpt_n3_2020_12_p09_m3",
    "title": "人気の店で並ぶこと",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 9,
    "type": "bunshou_bunpou",
    "content": "以下は、留学生の作文である。\n\n人気の店で並ぶこと\nディビス ソフィア\n\n　東京の街を歩いていると、飲食店の前にたくさんの人が並んでいるのをよく見ます。店に入るために【 19 】。有名な店なのかもしれませんが、長い時間待つのは時間がもったいないので、私はいつもすぐに人れる店を選んでいました。\n　先週友達に、おいしいチーズケーキ屋があるから一緒に行こうと誘われました。人気がある店で、1時間ぐらい並ぶこともあるそうです。並ぶのは嫌でしたが、暇だったし、私はチーズケーキが大好きなので、一緒に行くことにしました。店に着くと、やはりたくさんの人が並んでいました。【 20 】、友達と話しながら待っていたら、長い時間待ったとは感じませんでした。チーズケーキはとてもおいしかったです。翌日、ゼミの先輩に、人気のチーズケーキを食べたことを話しました。先輩に「いいなあ。私も今度行ってみよう。」と、【 21 】、うれしかったです。\n　私が食べたチーズケーキは本当においしかったです。人気の店に並んで待つ気持ちが少しわかりました。また機会があったら、【 22 】人気店でも並んでみたいです。"
  },
  "jlpt_n3_2020_12_p10_1": {
    "id": "jlpt_n3_2020_12_p10_1",
    "title": "旅先のスーパー",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 10,
    "type": "dokkai_tandun",
    "content": "（１）\n　私のふるさとには、海がなかった。だから、ふるさとを出て、海があるこの町に引っ越してきたときの驚きは、今でも忘れられない。スーパーの魚売り場の広さと、そこに並んでいる魚の種類の多さが、比較にならなかったからだ。場所が違えば、そこに違った生活がある。それ以来、旅行で初めての土地を訪ねた時には、まずスーパーに入ることが癖になってしまった。いつも見ているのとは違う売り場の景色から、自分の日常生活との距離が感じられて、楽しくなるからだ。"
  },
  "jlpt_n3_2020_12_p10_2": {
    "id": "jlpt_n3_2020_12_p10_2",
    "title": "満月の夜の散歩",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 10,
    "type": "dokkai_tandun",
    "content": "（２）\n　夜の散歩は、数年続いている私たち夫婦の習慣だ。私はいつも夕食後、辺りが暗くなってから外に出る。近所には電灯もあるが、少し歩くと、家も減り、明かりもなくなるので、持ってきた懐中電灯をつける。だが、大きな丸い月が出る満月の夜はちょっと違う。明るく輝く月の下では、懐中電灯がなくても周りの景色がわかるのだ。道には私たちの黒い影がはっきり見え、昼間と違う不思議な世界にいる気分になれる。私の最も好きな時間だ。"
  },
  "jlpt_n3_2020_12_p11_3": {
    "id": "jlpt_n3_2020_12_p11_3",
    "title": "ゴミゼロ活動のお知らせ",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 11,
    "type": "dokkai_tandun",
    "content": "（３）\n町の掲示板に、このお知らせがはってある。\n\n＊9 時に集合してください\n集合場所：第一公園\n活動内容：町内のゴミ拾い\n持ち物：手袋(掃除用に必ず持ってきてください)\n＊ゴミ袋はこちらでも用意しますが、ご自宅にあれば、お持ちください。\n参加方法:当日、直接集合場所に来てください。申し込みは不要です。\n＊大雨などで中止する場合の連絡を希望する方は、前日までに、メールでお申し込みください。\n活動完了後、お茶、ジュースをお配りします。\n\n帯川町町内会\n電話:222－333(森口)\nobikawacho@xxmail.com"
  },
  "jlpt_n3_2020_12_p11_4": {
    "id": "jlpt_n3_2020_12_p11_4",
    "title": "中村さんへのプレゼントの提案",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 11,
    "type": "dokkai_tandun",
    "content": "（４）\n営業部の皆様\nお疲れ様です。\n皆さんもご存知のように、中村さんが来月でお辞めになります。そこで、中村さんに花束と記念品を差し上げたいと思いますが、いかがでしょうか。\n中村さんのお好きなものなど、ご存知の方がいらっしゃったら、アドバイスをいただければうれしいです。\nこの案に賛成の方は、今週中にご返信ください。代金などについては、また後で連絡いたします。\nよろしくお願いいたします。\n石田"
  },
  "jlpt_n3_2020_12_p12_m5_1": {
    "id": "jlpt_n3_2020_12_p12_m5_1",
    "title": "テレビの影響とスーパーの売れ行き",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 12,
    "type": "dokkai_chuubun",
    "content": "問題５：\n（１）\n　「どうして今日はバナナを買うお客さんがこんなに多いんだろう」日本でスーパーのアルバイトを始めたばかりのころ。驚いたことがあります。その日は朝からバナナがどんどん売れて、すぐに棚から消えてしまったのです。\n　それからも時々①同じようなことがありました。それはトマトだったり魚の缶詰だったりするのですが、ある食べ物が突然大量に売れ出すのです。店長に聞いて②理由がわかりました。テレビ番組で、ある食べ物について、「体にいい」とか「病気を防ぐ効果がある」などと放送されると、翌日はそうなるのだそうです。\n　よく売れるのは長くても二ヶ月くらいなのですが、健康を気にして、テレビでいいと言われたことをやってみようと思う人が多いのでしょう。スーパーでは最近、テレビで紹介される食べ物をチェックして、売れそうな商品は多めに注文しているそうです。\n　テレビ番組1つで、客の買うものが変わり、店で用意する商品も変わると知り、③テレビの力は大きいのだなと思いました。"
  },
  "jlpt_n3_2020_12_p13_m5_2": {
    "id": "jlpt_n3_2020_12_p13_m5_2",
    "title": "「ありがとう」の不思議な力",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 13,
    "type": "dokkai_chuubun",
    "content": "（２）\n　私はハンバーガーが好きで、よく近所の店にハンバーガーを買いに行きます。注文をすると、いつも店員に「ご一緒にポテトやお飲み物はいかがですか。」と聞かれますが、私は「けっこうです。」と言って断っています。\n　以前、こんな話を聞きました。あるハンバーガー屋で、「ご一緒にポテトはいかがですか」と聞く前に、必ず「ありがとうございます。」と店員に言わせるようにしました。すると、①その店では、何も言わずに「ご一緒にポテトはいかがですか。」と聞いたときより、ポテトを注文する客が増えたそうです。違いは、「ありがとうございます。」という言葉を言うか言わないかだけです。\n　でも、「ありがとうございます。」と言われると、つい「それじゃ、お願いします。」と言ってしまう人が多いらしいです。本当は買うつもりがなくても、ちょっと気分がよくなって頼んでしまうのでしょう。私はこの話を聞いて、②「ありがとう」という言葉には、不思議な力があるなと思いました。"
  },
  "jlpt_n3_2020_12_p14_m6": {
    "id": "jlpt_n3_2020_12_p14_m6",
    "title": "S市の伝統的な包丁作り",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 14,
    "type": "dokkai_choubun",
    "content": "問題６：\n　料理のおいしさは包丁がよく切れるか、切れないかで大きく変わる。\n　私は日本料理の料理人をしているが、私の包丁はS市で作られたものだ。S市の包丁は職人、つまり物を作る高い技術を持っている人たちが、一本ずつ丁寧に作っているので、値段は高いが、工場で大量に生産された包丁とは全く違うのだ。\n　S市は昔から、包丁作りで有名な町だ。料理人が使うプロ用の包丁の90％以上を生産していて、最近では海外への輸出も増えてきた。ただ、最近読んだ新聞の記事によると、S市の包丁生産には大きな問題があるらしい。職人が年を取って辞めていく一方で、職人になりたいと考える若い人が見つからず、職人の数が減っているのだ。\n　この問題を解決するために、S市の包丁産業団体が、市と協力して、数年前に一度、あるコースを開いた。あるコースでは、全国から職人になりたい若い人を募集して、一年かけて包丁作りの基本的な技術を教えた。10〜30代の男女13人が参加し、最終的に8人が市内の五つの包丁作りの会社に就職した。その中の一人は、記事の中のインタビューで「いつか自分の作った包丁を、一流の料理人に使ってもらいたい。」と話していた。\n　この若い職人たちにも頑張ってもらって、ずっと続いてきたS市の素晴らしい包丁作りの技術を守っていってほしい。私は、次に買う包丁もS市の包丁を選ぶつもりである。"
  },
  "jlpt_n3_2020_12_p17_m7": {
    "id": "jlpt_n3_2020_12_p17_m7",
    "title": "日本文化教室のご案内",
    "book": "JLPT N3 2020年12月 過去問",
    "page": 17,
    "type": "dokkai_jouhou_kensaku",
    "content": "日本文化教室のご案内\n\n【開講】4月13日(月)〜7月31日(金)\n【場所】山田市文化会館\n【教室の内容】\n・柔道：月・木 18:30〜20:00 (定員20名)\n・踊り：火・土 18:30〜20:00 (定員20名)\n・折り紙：火 18:30〜20:00 (定員20名)\n・お茶：金 18:30〜20:00 (定員35名)\n・お花：土 14:30〜15:30 (定員35名)\n・日本料理：第一・第三日曜日 15:00〜18:00 (定員20名)\n\n※週2回ある教室は両方の曜日に参加してください。\n\n【参加料】\n・週2回の教室：大人 7000円 / 学生(高校生以上) 5000円\n・週1回の教室：大人 4000円 / 学生(高校生以上) 3000円\n・お花・日本料理教室：8000円（材料費込み）\n※この料金は一月分（ひと月分）の合一（合計）です。\n\n【申し込み期間・方法】\n・3月2日(月)〜4月2日(木)（定員になれば受付終了）\n・文化会館事務室で申し込み用紙に記入して、参加料を支払ってください。\n\n【その他】\n・教室で使用する道具は、文化会館に用意してあります。\n・柔道の教室で着る柔道着は自分で準備してください。会館でも売っています。\n\n山田市文化会館\n〒987-4543 山田市わかば1-2-3\n電話:012-345-6789"
  }
}

# ------------------------------------------------------------------
# WRITE JSON FILES
# ------------------------------------------------------------------
with open('bank/jlpt_n3_2020_12/vocab.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2020年12月 過去問", "unit": "文字・語彙", "questions": vocab_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2020_12/grammar.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2020年12月 過去問", "unit": "文法", "questions": grammar_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2020_12/reading.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2020年12月 過去問", "unit": "読解", "questions": reading_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2020_12/passages.json', 'w', encoding='utf-8') as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)

print(f"Extraction for 2020 December completed:")
print(f"  Vocab: {len(vocab_questions)} Qs")
print(f"  Grammar: {len(grammar_questions)} Qs")
print(f"  Reading: {len(reading_questions)} Qs")
print(f"  Passages: {len(passages)} passages")
print(f"  Total: {len(vocab_questions) + len(grammar_questions) + len(reading_questions)} Qs")
