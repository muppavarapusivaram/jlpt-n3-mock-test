# scripts/build_2019_12.py
import os, json

os.makedirs('bank/jlpt_n3_2019_12', exist_ok=True)

# ------------------------------------------------------------------
# 1. SECTION 1: 言語知識（文字・語彙） (35 questions)
# ------------------------------------------------------------------
vocab_questions = [
  # 問題1: 漢字読み (8)
  {
    "id": "jlpt_n3_2019_12_v_q01", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "１０時に【予約】をお願いします。",
    "options": ["ようやく", "よやく", "よよく", "ようやく"], "answer": 2,
    "grammar_points": ["漢字読み: 予約 (よやく)"], "difficulty": 1,
    "explanation": "「予約」の読み方は「よやく」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q02", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "あの頃は私も【若かった】。",
    "options": ["わるかった", "さむかった", "こわかった", "わかかった"], "answer": 4,
    "grammar_points": ["漢字読み: 若い (わかい)"], "difficulty": 1,
    "explanation": "「若い」の読み方は「わかい」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q03", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【上品な】人ですね。",
    "options": ["じょうひん", "じょうびん", "じょひん", "じょびん"], "answer": 1,
    "grammar_points": ["漢字読み: 上品 (じょうひん)"], "difficulty": 2,
    "explanation": "「上品」の読み方は「じょうひん」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q04", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "山田さんに【助けて】もらった。",
    "options": ["とどけて", "たすけて", "うけて", "かたづけて"], "answer": 2,
    "grammar_points": ["漢字読み: 助ける (たすける)"], "difficulty": 1,
    "explanation": "「助ける」の読み方は「たすける」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q05", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【未来】を考えてみる。",
    "options": ["しょらい", "しょうらい", "みらい", "みいらい"], "answer": 3,
    "grammar_points": ["漢字読み: 未来 (みらい)"], "difficulty": 1,
    "explanation": "「未来」の読み方は「みらい」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q06", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この電車は【各駅】に止まります。",
    "options": ["かくえき", "がくえき", "きゃくえき", "ぎゃくえき"], "answer": 1,
    "grammar_points": ["漢字読み: 各駅 (かくえき)"], "difficulty": 2,
    "explanation": "「各駅」の読み方は「かくえき」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q07", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "誰が【勝った】んですか？",
    "options": ["かざった", "おった", "のこった", "かった"], "answer": 4,
    "grammar_points": ["漢字読み: 勝つ (かつ)"], "difficulty": 1,
    "explanation": "「勝つ」の過去形は「かった」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q08", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
    "instruction": "＿＿の言葉の読み方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "彼に初めて会ったときの【印象】はどうでしたか？",
    "options": ["いんしょう", "いんそう", "にんしょう", "にんそう"], "answer": 1,
    "grammar_points": ["漢字読み: 印象 (いんしょう)"], "difficulty": 2,
    "explanation": "「印象」の読み方は「いんしょう」です。"
  },

  # 問題2: 表記 (6)
  {
    "id": "jlpt_n3_2019_12_v_q09", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【りゆう】はよくわかりません。",
    "options": ["理有", "利由", "自由", "理由"], "answer": 4,
    "grammar_points": ["表記: 理由"], "difficulty": 1,
    "explanation": "「りゆう」は漢字で「理由」と書きます。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q10", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この【しま】には、初めて来ました。",
    "options": ["寺", "村", "島", "庭"], "answer": 3,
    "grammar_points": ["表記: 島"], "difficulty": 1,
    "explanation": "「しま」は漢字で「島」と書きます。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q11", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "卒業の【きねん】に写真を撮りました。",
    "options": ["気念", "祈念", "木念", "記念"], "answer": 4,
    "grammar_points": ["表記: 記念"], "difficulty": 1,
    "explanation": "「きねん」は漢字で「記念」と書きます。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q12", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "これが【いっぱんてき】な方法です。",
    "options": ["一藩的", "一番的", "一般的", "一番適"], "answer": 3,
    "grammar_points": ["表記: 一般的"], "difficulty": 2,
    "explanation": "「いっぱんてき」は漢字で「一般的」と書きます。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q13", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "今日も【かならず】行きます。",
    "options": ["必ず", "必らず", "要ず", "心ず"], "answer": 1,
    "grammar_points": ["表記: 必ず"], "difficulty": 1,
    "explanation": "「かならず」は漢字で「必ず」と書きます。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q14", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
    "instruction": "＿＿の言葉を漢字で書くとき、最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "効果が【あらわれた】ようですよ。",
    "options": ["改れた", "現れた", "表た", "現た"], "answer": 2,
    "grammar_points": ["表記: 現れた"], "difficulty": 2,
    "explanation": "効果などが出現する場合は「現れた」と書きます。"
  },

  # 問題3: 文脈規定 (11)
  {
    "id": "jlpt_n3_2019_12_v_q15", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "おじさんの会社を（ ）するつもりだ。",
    "options": ["登場", "進行", "就職", "同席"], "answer": 3,
    "grammar_points": ["語彙: 就職"], "difficulty": 2,
    "explanation": "会社に勤めることを「会社に就職する」と言います。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q16", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "この店の帽子は全部私が色や形などの（ ）を考えています。",
    "options": ["レシピ", "デザイン", "サイン", "ミックス"], "answer": 2,
    "grammar_points": ["語彙: デザイン"], "difficulty": 1,
    "explanation": "色や形などを構想することを「デザイン（を考える）」と言います。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q17", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "申し込みの（ ）は来週の月曜日ですから、それまでに申込書を出してください。",
    "options": ["あて先", "合図", "締め切り", "合計"], "answer": 3,
    "grammar_points": ["語彙: 締め切り"], "difficulty": 1,
    "explanation": "期日・期限のことを「締め切り」と言います。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q18", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "英語で会議をするときは、英語がわかる佐藤さんが英語を日本語に（ ）してくれる。",
    "options": ["通訳", "案内", "伝言", "連絡"], "answer": 1,
    "grammar_points": ["語彙: 通訳"], "difficulty": 1,
    "explanation": "ある言語で話された言葉を別の言語に訳して伝えることを「通訳」と言います。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q19", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "部屋の電気が（ ）消えて、驚いた。",
    "options": ["突然", "急いで", "結構", "庭"], "answer": 1,
    "grammar_points": ["語彙: 突然"], "difficulty": 1,
    "explanation": "予告なく急に起きる様子を表す「突然」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q20", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "誰も木村さんはうそをついていると思うが、私は彼が言ったことを（ ）。",
    "options": ["手伝います", "褒めます", "守ります", "信じます"], "answer": 4,
    "grammar_points": ["語彙: 信じる"], "difficulty": 2,
    "explanation": "「言ったことを信じる」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q21", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "このホテル慎重に清掃されているために部屋はとても（ ）だ。",
    "options": ["新鮮", "清潔", "正常", "丁寧"], "answer": 2,
    "grammar_points": ["語彙: 清潔"], "difficulty": 2,
    "explanation": "汚れがなく綺麗な状態を表す「清潔」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q22", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "仕事で遅くなってしまい、今日はご飯を作るのが（ ）ので、お弁当を買うことにしました。",
    "options": ["にくらしい", "だらしない", "しょうがない", "面倒臭い"], "answer": 4,
    "grammar_points": ["語彙: 面倒臭い"], "difficulty": 2,
    "explanation": "手間がかかって億劫な様子を表す「面倒臭い」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q23", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "みんなの前でスピーチをしたときは、緊張して胸が（ ）しました。",
    "options": ["こんこん", "だぶだぶ", "どきどき", "ちかちか"], "answer": 3,
    "grammar_points": ["オノマトペ: どきどき"], "difficulty": 1,
    "explanation": "心臓が速く脈打つ様子を表す「どきどき（する）」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q24", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "とても暑かったので、スーパーで買ったアイスクリームが家に着く前に（ ）しまった。",
    "options": ["もえて", "とけて", "さめて", "かれて"], "answer": 2,
    "grammar_points": ["語彙: 溶ける"], "difficulty": 1,
    "explanation": "熱で固体が液体になることを「溶ける（とける）」と言います。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q25", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）",
    "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
    "instruction": "（ ）に入れるのに最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "アパートの鍵をなくしてしまったので、大家さんに（ ）を話して、鍵を開けてもらった。",
    "options": ["秘密", "歴史", "具合", "事情"], "answer": 4,
    "grammar_points": ["語彙: 事情"], "difficulty": 2,
    "explanation": "物事のいきさつ・理由を説明することを「事情を話す」と言います。"
  },

  # 問題4: 類義 (5)
  {
    "id": "jlpt_n3_2019_12_v_q26", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "鈴木さんへ【感謝】の手紙を送った。",
    "options": ["お願い", "お礼", "お見舞い", "お知らせ"], "answer": 2,
    "grammar_points": ["類義語: 感謝 ≒ お礼"], "difficulty": 1,
    "explanation": "「感謝の手紙」に最も近い意味は「お礼」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q27", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "子どもたちは【キッチン】にいます。",
    "options": ["廊下", "居間", "玄関", "台所"], "answer": 4,
    "grammar_points": ["類義語: キッチン ≒ 台所"], "difficulty": 1,
    "explanation": "「キッチン」は「台所」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q28", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【不安なので】、私は行かないことにした。",
    "options": ["時間がない", "お金がない", "危険な", "心配な"], "answer": 4,
    "grammar_points": ["類義語: 不安 ≒ 心配"], "difficulty": 1,
    "explanation": "「不安」に最も近い意味は「心配」です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q29", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "おなかが【ぺこぺこだ】。",
    "options": ["痛い", "すいている", "かゆい", "いっぱい"], "answer": 2,
    "grammar_points": ["オノマトペ: ぺこぺこ ≒ すいている"], "difficulty": 1,
    "explanation": "「おなかがぺこぺこ」は「すいている」という意味です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q30", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
    "instruction": "＿＿に意味が最も近いものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "兄は【黙って】ずっと漫画を読んでいる。",
    "options": ["何も話さないで", "何も食べないで", "勉強しないで", "寝ないで"], "answer": 1,
    "grammar_points": ["語彙: 黙る ≒ 何も話さない"], "difficulty": 2,
    "explanation": "「黙って」は言葉を発しない様子、「何も話さないで」です。"
  },

  # 問題5: 用法 (5)
  {
    "id": "jlpt_n3_2019_12_v_q31", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【健康】",
    "options": [
      "弟の成績がいつもより健康だったので、両親は喜んだ。",
      "祖父は毎日運動をしているから、今でもとても健康だ。",
      "前にある大きなビルは、古いけど健康だそうだ。",
      "最近パソコンが健康ではないみたいので、ときどき変な音がする。"
    ], "answer": 2,
    "grammar_points": ["用法: 健康"], "difficulty": 2,
    "explanation": "「健康」は体や精神が健やかな状態を表します。「祖父は今でもとても健康だ」が正しい用法です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q32", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【参加】",
    "options": [
      "高橋さんは今度の留学セミナーに参加しますか。",
      "林の中に参加したら、涼しくて気持ちがいいですよ。",
      "昨日タクシーに乗ったとき、渋滞に参加してしまった。",
      "猫が私の家族に参加しました。"
    ], "answer": 1,
    "grammar_points": ["用法: 参加"], "difficulty": 1,
    "explanation": "「セミナーに参加する」が自然で正しい用法です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q33", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【中旬】",
    "options": [
      "その本は本棚の中旬にあります。",
      "今日のサッカーは試合の中旬に点に入りました。",
      "来月の中旬に国へ帰るつもりです。",
      "私は三人兄弟の中旬です。"
    ], "answer": 3,
    "grammar_points": ["用法: 中旬"], "difficulty": 2,
    "explanation": "「中旬」は月の11日〜20日頃を指し、「来月の中旬」が正しい用法です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q34", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【落ち着く】",
    "options": [
      "この店は人気があるので、朝早くから店の前に大勢の人が落ち着いている。",
      "買った本が袋に入ったまま、床に落ち着いている。",
      "好きな音楽を聞いているとき、気持ちが落ち着いている。",
      "祭りの後はいつも道にゴミがたくさん落ち着いている。"
    ], "answer": 3,
    "grammar_points": ["用法: 落ち着く"], "difficulty": 2,
    "explanation": "「気持ちが落ち着く」が正しい用法です。"
  },
  {
    "id": "jlpt_n3_2019_12_v_q35", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文字・語彙", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）",
    "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
    "instruction": "つぎの言葉の使い方として最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None, "question": "【ほえる】",
    "options": [
      "祖父の家の近くの森は、いろいろな種類の鳥がほえている。",
      "夜になると、隣さんの犬がほえていて、うるさい。",
      "私は毎晩、目覚まし時計がほえる音で起きる。",
      "この店は、いつもにぎやかな音楽がほえている。"
    ], "answer": 2,
    "grammar_points": ["用法: 吠える"], "difficulty": 2,
    "explanation": "「犬がほえていて」が正しい用法です。"
  }
]

# ------------------------------------------------------------------
# 2. SECTION 2: 言語知識（文法） (23 questions)
# ------------------------------------------------------------------
grammar_questions = [
  # 問題1: 文法形式の判断 (13)
  {
    "id": "jlpt_n3_2019_12_g_q01", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "高校時代の友人と京都で楽しい一日（ ）過ごした。",
    "options": ["と", "を", "も", "が"], "answer": 2,
    "grammar_points": ["助詞: を（過ごす）"], "difficulty": 1,
    "explanation": "「楽しい一日を過ごした」のように、過ごす対象を表す格助詞「を」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q02", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "A「このケーキ、どこで買ったの？すごくおいしいね。」\nB「『リボン』（ ）店なんだけど、知ってる？」",
    "options": ["って", "とか", "だって", "なんか"], "answer": 1,
    "grammar_points": ["引用・呼称: 〜っていう／〜って店"], "difficulty": 1,
    "explanation": "「リボンという店」の口語的表現である「『リボン』って店」の「って」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q03", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "私が電車に乗ったとき、車内がすいていたが、集中して本を読んでいたら、（ ）満員になった。",
    "options": ["もっと", "いまにも", "もしかしたら", "いつのまにか"], "answer": 4,
    "grammar_points": ["副詞: いつのまにか"], "difficulty": 2,
    "explanation": "気づかないうちに変化が起きていたことを表す「いつのまにか（満員になった）」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q04", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "うちには大きさの違うフライパンが（ ）あるが、使っているのは一番小さいサイズのだけだ。",
    "options": ["どれ", "いくつ", "どれか", "いくつか"], "answer": 4,
    "grammar_points": ["不定数量: いくつか（複数ある）"], "difficulty": 1,
    "explanation": "フライパンが何個か存在することを表す「いくつか」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q05", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "森田「石山さん、見たいって言ってたDVD、持ってきたよ。」\n石山「ありがとう。」\n森田「林さんも見たがってたから、（ ）林さんに渡してくれる？」",
    "options": ["見たあったら", "見ていたら", "見終わったら", "見続けたら"], "answer": 3,
    "grammar_points": ["複合動詞: 〜終わる＋たら"], "difficulty": 1,
    "explanation": "DVDをすべて見終えた後の条件を表す「見終わったら」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q06", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "私は毎年誕生日にそのとき読みたいと思った本を一冊（ ）、本棚に並べているが、自分が好きな本の変化が分かって面白い。",
    "options": ["買うはずだ", "買うことにしている", "買うところだ", "買うようになっている"], "answer": 2,
    "grammar_points": ["習慣・決定: 〜ことにしている"], "difficulty": 2,
    "explanation": "自分で決めて毎年続けている個人的な習慣を表す「買うことにしている」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q07", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "A「昨日携帯電話をなくしたって言ったけど、見つかった？」\nB「うん、実は車の中に落ちていたんだ。」\nA「そうなんだ。（ ）ね。」",
    "options": ["見つかってよかった", "見つかるほうがいい", "見つかったようだ", "見つかりそうだった"], "answer": 1,
    "grammar_points": ["安堵・共感: 〜てよかった"], "difficulty": 1,
    "explanation": "無事に見つかったことに対する安堵・お祝いの表現「見つかってよかったね」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q08", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "先生「Yuukiさんが留学すると言ったとき、ご両親は何と（ ）。」\nYuukiさん「頑張れと応援してくれた。」",
    "options": ["うかがいましたか？", "もうしあげましたか？", "おっしゃいましたか？", "お聞きになりましたか？"], "answer": 3,
    "grammar_points": ["尊敬語: おっしゃる（言う）"], "difficulty": 2,
    "explanation": "相手（Yuukiさん）の両親の発言について尋ねているため、「言う」の尊敬語である「おっしゃいましたか？」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q09", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "乗客「すみません、この車は花仙駅に行きますか。」\n運転手「いいえ、この車は次の停車地に行く（ ）です。」",
    "options": ["だけ", "しか", "まで", "から"], "answer": 1,
    "grammar_points": ["限定: 〜だけ（〜のみ）"], "difficulty": 2,
    "explanation": "花仙駅までは行かず、次の停車地までしか行かないことを限定して説明する「行く（だけ）です」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q10", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "授業の後、昼ご飯を（ ）大学の食堂に行ったが、とても込んでいたので、大学の近くのラーメン屋に食べに行った。",
    "options": ["食べていて", "食べているのに", "食べようと思って", "食べようと思うのに"], "answer": 3,
    "grammar_points": ["意図・意志: 〜ようと思って"], "difficulty": 2,
    "explanation": "「昼ご飯を食べようという意図を持って食堂に行った」ことを表す「食べようと思って」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q11", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "うちの近くにある美容院は9時まで営業しているから、仕事が（ ）行けて便利だ。",
    "options": ["終わる前は", "終わってからは", "終わる前でも", "終わってからでも"], "answer": 4,
    "grammar_points": ["逆接・条件: 〜てからでも"], "difficulty": 2,
    "explanation": "仕事が終わった後の遅い時間であっても行くことができることを表す「終わってからでも」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q12", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "高校生のとき、ギター教室に（ ）が、難しく３ヶ月でやめてしまった。",
    "options": ["通ってみたところだ", "通ってみたことがある", "通っておいたところだ", "通っておいたことがある"], "answer": 2,
    "grammar_points": ["試み・経験: 〜てみたことがある"], "difficulty": 2,
    "explanation": "過去に実際に試してみた経験があることを表す「通ってみたことがある」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q13", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
    "instruction": "つぎの文の ( ) に入れるのに最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": None,
    "question": "子供のころ、私は将来歌手に（ ）。",
    "options": ["なりたそうだ", "なることができた", "なっていたと思う", "なりたいと思っていた"], "answer": 4,
    "grammar_points": ["希望の継続: 〜たいと思っていた"], "difficulty": 2,
    "explanation": "子供の頃にずっと抱いていた希望・夢を表す「なりたいと思っていた」が入ります。"
  },

  # 問題2: 文の組み立て ★ (5)
  {
    "id": "jlpt_n3_2019_12_g_q14", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None,
    "question": "昨日父に、来週友達と旅行に行く __ __ ★ __ 頼んだが、断られてしまった。",
    "options": ["と", "車を", "ので", "使わせてほしい"], "answer": 4,
    "grammar_points": ["使役・許可要求: 使わせてほしいと頼む"], "difficulty": 2,
    "explanation": "正しい並び順は「旅行に行く [ので (3)] [車を (2)] [★ 使わせてほしい (4)] [と (1)] 頼んだ」です。★は4です。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q15", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None,
    "question": "桜大学は学生 __ __ ★ __ についてアンケート調査を行った。",
    "options": ["に対する", "の", "考え方", "働くこと"], "answer": 1,
    "grammar_points": ["対象: 〜に対する考え方"], "difficulty": 2,
    "explanation": "正しい並び順は「学生 [の (2)] [働くこと (4)] [★ に対する (1)] [考え方 (3)] について」です。★は1です。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q16", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None,
    "question": "食事の __ __ ★ __ を汚してしまった。",
    "options": ["ときに", "ばかりの", "白いＴシャツ", "買った"], "answer": 2,
    "grammar_points": ["完了直後: 〜たばかりのN"], "difficulty": 2,
    "explanation": "正しい並び順は「食事の [ときに (1)] [買った (4)] [★ ばかりの (2)] [白いＴシャツ (3)] を」です。★は2です。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q17", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None,
    "question": "昨日初めて花川駅に行った。花川駅まで __ __ ★ __ 電車に乗る前に駅員に聞いた。",
    "options": ["わからなくて", "どの電車で", "一番早く着くのか", "行けば"], "answer": 3,
    "grammar_points": ["疑問節: 〜のかわからなくて"], "difficulty": 2,
    "explanation": "正しい並び順は「花川駅まで [どの電車で (2)] [行けば (4)] [★ 一番早く着くのか (3)] [わからなくて (1)]」です。★は3です。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q18", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）",
    "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
    "instruction": "次の文の ★ に入る最もよいものを、１・２・３・４から一つ選びなさい。",
    "passage_id": None,
    "question": "A「ねえ、昨日のパーティーに行く？会場のレストランが駅から遠くてちょっと不便だから行こうか迷っているんだけど」\nB「私、車で __ __ ★ __ 」",
    "options": ["もし", "乗せていってあげる", "行くんだったら", "行くつもりだから"], "answer": 3,
    "grammar_points": ["仮定・提案: 〜んだったら、〜てあげる"], "difficulty": 3,
    "explanation": "正しい並び順は「車で [行くつもりだから (4)]、[もし (1)] [★ 行くんだったら (3)] [乗せていってあげる (2)]」です。★は3です。"
  },

  # 問題3: 文章の文法 (5) (大掃除, p07)
  {
    "id": "jlpt_n3_2019_12_g_q19", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p07",
    "question": "【 19 】に入る最もよいものを選びなさい。",
    "options": ["ある", "この", "その", "あの"], "answer": 2,
    "grammar_points": ["指示詞: この状態"], "difficulty": 2,
    "explanation": "直前に述べた「掃除ができない状態」を直視して指す指示詞「この（状態）」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q20", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p07",
    "question": "【 20 】に入る最もよいものを選びなさい。",
    "options": ["まず", "または", "すると", "ところが"], "answer": 1,
    "grammar_points": ["順序・手順: まず〜そして〜"], "difficulty": 2,
    "explanation": "大掃除の手順として最初に行ったことを表す「まず（不要品を全部捨てました）」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q21", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p07",
    "question": "【 21 】に入る最もよいものを選びなさい。",
    "options": ["なら", "でも", "まで", "ばかり"], "answer": 3,
    "grammar_points": ["助詞: まで（極端な例の提示）"], "difficulty": 2,
    "explanation": "普段はやらない奥まった換気扇にまで及んだことを表す「換気扇まで掃除したのは初めてでした」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q22", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p07",
    "question": "【 22 】に入る最もよいものを選びなさい。",
    "options": [
      "迎えることができそうです",
      "迎えることができたらしいです",
      "迎えることができればいいです",
      "迎えることができたと思います"
    ], "answer": 3,
    "grammar_points": ["希望・期待: 〜ばいいです"], "difficulty": 3,
    "explanation": "大掃除が終わり、これから来る新年に対する前向きな希望を表す「迎えることができればいいです」が入ります。"
  },
  {
    "id": "jlpt_n3_2019_12_g_q23", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "文法", "page": 7, "pdf_page": 7, "section": "言語知識（文法）",
    "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
    "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、１・２・３・４から一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p07",
    "question": "【 23 】に入る最もよいものを選びなさい。",
    "options": ["決めた", "決められた", "決めさせた", "決めさせられた"], "answer": 1,
    "grammar_points": ["受動 vs 能動: （社会で慣習として）決めた時期"], "difficulty": 2,
    "explanation": "文章の前半の「誰かが決めた時期」と呼応し、「決めた時期に何かをする」が入ります。"
  }
]

# ------------------------------------------------------------------
# 3. SECTION 2: 読解 (14 questions) & PASSAGES (8)
# ------------------------------------------------------------------
reading_questions = [
  # 問題4: 短文読解 (4)
  {
    "id": "jlpt_n3_2019_12_r_q24", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p08",
    "question": "家庭教師について、高島さんの希望に合っているものはどれか。",
    "options": [
      "医学部の学生で、火曜と土曜に教えられること。",
      "受験生に数学を教えた経験があり、週に2回教えられること。",
      "数学が専門の学生で、週に2時間教えられること。",
      "明るい性格で、土曜と日曜の19時から21時まで教えられること"
    ], "answer": 2,
    "grammar_points": ["短文読解: 条件の照合"], "difficulty": 2,
    "explanation": "お知らせに「回数：週2回」「受験生に数学の指導をしたことがある」「数学が専門でなくてもけっこう」とあるため、2が合致します。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q25", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p09_1",
    "question": "足りないものは何か。",
    "options": [
      "コピー用紙1箱と、プリンタの黒のインク2箱と青のインク1箱",
      "コピー用紙1箱と、プリンターの黒のインク1箱",
      "プリンタの黒のインク2箱",
      "プリンタの黒のインク1箱"
    ], "answer": 3,
    "grammar_points": ["短文読解: 注文内容と納品内容の差分計算"], "difficulty": 2,
    "explanation": "注文したのは黒のインク3箱でしたが、届いたのは1箱だったので、足りないものは「黒のインク2箱」です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q26", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p09_2",
    "question": "隣の席の人によると、先輩が私と話すときは笑顔ではなくなるのはなぜか。",
    "options": [
      "会社に入ったばかりの「私」と話すのは緊張するから。",
      "会社に入ったばかりのは「私」を心配しているから。",
      "先輩のことを怖がっている「私」と話したくないから。",
      "先輩のことを怖がっている「私」を嫌っているから。"
    ], "answer": 1,
    "grammar_points": ["短文読解: 理由の把握"], "difficulty": 2,
    "explanation": "隣の席の人は「あの人は、初めて会う人が苦手で、緊張しちゃって笑えなくなるんだよ」と答えているため、1が正解です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q27", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解",
    "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p10",
    "question": "何をやってみたくなったのか。",
    "options": [
      "10万円以上するイヤホンを一つかって、スビーカーの音と比べて音楽を楽しむこと",
      "10万円以上するイヤホンを一つ買って、いろいろな音楽を楽しむこと",
      "聴く音楽に合わせて複数のスビーカーを買って、音楽を楽しむこと",
      "聴く音楽に合わせて複数のイヤホンを買って、音楽を楽しむこと"
    ], "answer": 4,
    "grammar_points": ["短文読解: 心情・意欲の把握"], "difficulty": 2,
    "explanation": "「最近は、複数のイヤホンを持ち、ロックやクラシックなど聴く音楽に合わせて、使うイヤホンを変える人もいるそうだ...同じようにやってみたくなった」とあるので、4が正解です。"
  },

  # 問題5: 中文読解 (6)
  # Passage 1: プロの写真屋 (3 Qs)
  {
    "id": "jlpt_n3_2019_12_r_q28", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p10_11",
    "question": "なぜ「私」はカメラマンに頼むことにしたのか。",
    "options": [
      "娘の写真を使って、ポスターを作りたいから",
      "娘がプロのカメラマンに撮ってもらいたいといったから",
      "娘が公園で写真を撮ってもらうのが好きだから",
      "娘の自然な笑顔の写真が、自分ではうまく撮れないから"
    ], "answer": 4,
    "grammar_points": ["中文読解: 動機の把握"], "difficulty": 2,
    "explanation": "「娘の自然な笑顔が撮りたいのですが、自分ではなかなかうまくいかなくて、困っていたので」と明確に書かれています。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q29", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p10_11",
    "question": "そんなやり方とあるが、何か。",
    "options": [
      "ブランコで遊んでいる娘を撮り続けたこと",
      "娘と一緒にブランコで遊びながら撮り始めたこと",
      "カメラを気にしている娘のすぐ近くで撮り始めたこと",
      "20分近くも娘を撮り続けていたこと"
    ], "answer": 3,
    "grammar_points": ["中文読解: 指示語の内容把握"], "difficulty": 2,
    "explanation": "「娘のすぐ近くで撮り始めました。娘がカメラをかなり気にしていたので、私はそんなやり方でいい写真が撮れるのだろうかと思いました」とあるため、3です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q30", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p10_11",
    "question": "工夫とあるが、どのようなことか。",
    "options": [
      "子供が知らない場所で緊張しないように、慣れている場所で撮ること",
      "子供が飽きてしまわないように、なるべく時間をかけないで撮ること",
      "子供がカメラマンに慣れるように、カメラマンが笑顔で撮り続けること",
      "子供が撮られることに慣れるように、写真を撮り続けること"
    ], "answer": 4,
    "grammar_points": ["中文読解: 詳細把握"], "difficulty": 3,
    "explanation": "カメラマンは「カメラに慣れて意識しなくなってからなんです。はじめの20分はそのための準備です」と述べており、4が正解です。"
  },

  # Passage 2: 右と左の伝え方 (3 Qs)
  {
    "id": "jlpt_n3_2019_12_r_q31", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p11_12",
    "question": "自分の思っている「右」を相手に正しく伝えるのが難しいといったのはなぜか。",
    "options": [
      "ソースをつけていたほほは、「私」から見ても、友達にとっても「右」だったから",
      "ソースをつけていたほほは、「私」から見ても、友達にとっても「左」だったから",
      "ソースをつけていたほほは、「私」から見て「右」だったが、友だちにとっては「左」だったから",
      "ソースをつけていたほほは、「私」から見て「左」だったが、友だちにとっては「右」だったから"
    ], "answer": 3,
    "grammar_points": ["中文読解: 視点と位置関係の把握"], "difficulty": 2,
    "explanation": "向かい合っている相手に対して「私から見て右」と言ったため、相手自身にとっては左側だったという食い違いが原因です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q32", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p11_12",
    "question": "正しく伝わったかもしれないとあるが、ここで「私」が正しく伝わると考えたのはどのような説明か。",
    "options": [
      "どんな人にとっても変わらないものを使った説明",
      "インターネットで広く紹介されている説明",
      "体の一部分を表す言葉を使った説明",
      "人によって変わるものを使った説明"
    ], "answer": 1,
    "grammar_points": ["中文読解: 筆者の思考の読み取り"], "difficulty": 2,
    "explanation": "「方角なら誰にとってもどんな場所でも変わらない...『西側のほほ』といえば、正しく伝わったかもしれない」とあるため、1が正解です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q33", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解",
    "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p11_12",
    "question": "先日と同じことがあったとき、間違いなく確実に伝えるためには、「私」は今後、どのような言い方をすると考えられるか。",
    "options": [
      "「右のほほにソースがついているよ。」",
      "「心臓がある側のほほにソースがついているよ」",
      "「西側のほほにソースがついているよ」",
      "「私から見て右のほほにソースがついているよ」"
    ], "answer": 4,
    "grammar_points": ["中文読解: 結論の推論"], "difficulty": 3,
    "explanation": "筆者は最後に「相手と自分の位置関係を考えながら、『右』『左』という言葉を使う以外の方法はないだろう」と述べており、4が合致します。"
  },

  # 問題6: 長文読解 (4)
  # Passage: 立ったり座ったりして仕事をする
  {
    "id": "jlpt_n3_2019_12_r_q34", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p12_13",
    "question": "面白いサイトから、わかったことはどれか。",
    "options": [
      "ずっと座っていた人は、足はどこも疲れていなかった",
      "ずっと立っていた人は、体が全体的に疲れていた",
      "どんな姿勢をしていた人も皆、足は全体的に疲れていた",
      "立ったり座ったりしていた人は、体からだがどこもあまり疲れていなかった"
    ], "answer": 4,
    "grammar_points": ["長文読解: 実験結果の把握"], "difficulty": 2,
    "explanation": "「体全体があまり疲れていなかったのは、立ったり座ったりして姿勢を変えていた人だった」と明確に述べられています。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q35", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p12_13",
    "question": "ある会社で起きた変化として、合っているのはどれか。",
    "options": [
      "体が調子が悪くなった社員が増えた",
      "社員の間でコミュニケーションが増えた",
      "時間をかけて話し合う会議が増えた",
      "姿勢がよい社員が増えた"
    ], "answer": 2,
    "grammar_points": ["長文読解: 具体例の把握"], "difficulty": 2,
    "explanation": "「体の調子が悪いと言う人が減り、そのうえ、以前より社員の間でよくコミュニケーションをとるようになったそうだ」とあるため、2が正解です。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q36", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p12_13",
    "question": "私たちの会社もこのような机にしてほしいとあるが、現在「私」の会社では、どのように仕事をしているか。",
    "options": [
      "立ったり座ったりして仕事をしている",
      "長い時間、座ったままで仕事をしている",
      "ふだんは立って仕事をしていたが、会議は座ってしている",
      "普段は座って仕事をしていたが、会議はたってしている"
    ], "answer": 2,
    "grammar_points": ["長文読解: 現状把握"], "difficulty": 2,
    "explanation": "第1段落で「私の会社では、毎日何時間もいすに座って仕事をするので、首や肩や腰が痛くなると言う人が多い」と書かれています。"
  },
  {
    "id": "jlpt_n3_2019_12_r_q37", "book": "JLPT N3 2019年12月 過去問", "book_code": "jlpt_n3_2019_12",
    "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解",
    "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
    "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。",
    "passage_id": "jlpt_n3_2019_12_p12_13",
    "question": "この文章のテーマは何か。",
    "options": [
      "机の高さといすの関係",
      "体の調子とお金の関係",
      "姿勢が体や仕事に与える影響",
      "社員の意見が会社に与える影響"
    ], "answer": 3,
    "grammar_points": ["長文読解: 全体の主題把握"], "difficulty": 2,
    "explanation": "働くときの姿勢（座りっぱなし vs 立つ/座るの切り替え）が体調や仕事の効率・コミュニケーションに与える影響を論じています。"
  }
]

# ------------------------------------------------------------------
# 4. PASSAGES (8)
# ------------------------------------------------------------------
passages = {
  "jlpt_n3_2019_12_p07": {
    "id": "jlpt_n3_2019_12_p07",
    "title": "大掃除",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 7,
    "type": "bunshou_bunpou",
    "content": "以下は留学生の作文である\n\n大掃除\n\n日本では、１２月の終わりに大掃除するという習慣がある。家の中の普段あまり掃除しないところをきれいにすることです。１２月になると、テレビで掃除用具や洗剤の宣伝をよく見ます。\n\n日本に来て最初の年の終わり、私は大掃除しませんでした。誰かが決めた時期に掃除をするというのが嫌だったのです。けれども、ずっと忙しくて大掃除ができず、そのまま、また１２月になってしまいました。「［ 19 ］状態が続くといつまでたっても掃除をしないところが残ったままだ。」と思いました。それで、去年は１２月に大掃除をすることにしました。\n\n［ 20 ］、家の中の不要品を全部捨てました。そして、窓の汚れやキッチンの油汚れをきれいにしました。換気扇［ 21 ］掃除したのは初めてでした。カーテンも洗濯しました。家の中が明るくなったような気がしました。家がきれいになって、いつもより気持ちよく新しい年［ 22 ］。\n\nいつ何をするか、自分で考えて決めることは重要です。それでも、たまには［ 23 ］時期に何かをするのも悪くないと思いました。"
  },
  "jlpt_n3_2019_12_p08": {
    "id": "jlpt_n3_2019_12_p08",
    "title": "家庭教師募集",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 8,
    "type": "dokkai_tandun",
    "content": "（１）これは大学の掲示板にはってあるお知らせである。\n\n家庭教師募集\n\n医学部受験のため、高校３年生の息子に数学を教えてくれる大学生の方を探しています。\n\n回数：週２回\n時間：１回２時間\n平日（火曜以外）…１９時から２１時まで\n土曜、日曜…９時から１９時の間で都合のいい時間をお知らせください。\n時給：3,000円（交通費もお支払いします）\n\n学部の希望は特にありませんが、受験生に数学の指導をしたことがある、明るい性格の方にお願いしたいです。数学が専門でなくてもけっこうです。\nお電話をお待ちしています。\n\n今泉市曇田町\n091-021-4678\n高島"
  },
  "jlpt_n3_2019_12_p09_1": {
    "id": "jlpt_n3_2019_12_p09_1",
    "title": "文房具店へのメール",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 9,
    "type": "dokkai_tandun",
    "content": "（２）これは、本田さんが文房具店に送ったメールである。\n\n中野文房具\n中野様\n\n注文した商品が昨日届いたのですが、足りないものがありました。\n注文したのは、コピー用紙１箱とプリンターの黒のインク３箱と青のインク１箱でしたが、黒のインクは１箱しか入ってしませんでした。確かめていただけないでしょうか。よろしくお願いします。\n\n本田みどり"
  },
  "jlpt_n3_2019_12_p09_2": {
    "id": "jlpt_n3_2019_12_p09_2",
    "title": "会社の怖い先輩",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 9,
    "type": "dokkai_tandun",
    "content": "（３）\n私は先週から新しい会社で働いているのだが、怖い先輩が一人いる。ほかの人と話すときは笑顔なのに、私と話すときは笑顔ではなくなるのだ。渡した先輩に嫌われているかもしれないと思って、隣の席の人に相談してみた。すると、「あの人は、初めて会う人が苦手で、緊張しちゃって笑えなくなるんだよ。もう少ししたらなれると思うから、緊張しないで。」と言われました。自分が嫌われているのではないらしいことがわかって、安心した。"
  },
  "jlpt_n3_2019_12_p10": {
    "id": "jlpt_n3_2019_12_p10",
    "title": "イヤホン売り場",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 10,
    "type": "dokkai_tandun",
    "content": "（４）\n先日、大型電気店に行ったとき、久しぶりにイヤホン売り場を通りかかって驚いた。種類がかなり増えていて、10万円以上するものもあった。いくつかのイヤホンで音を聞いてみたが、それほど高くないものでも、十分によい音だった。店の人によると、最近は、複数のイヤホンを持ち、ロックやクラシックなど聴く音楽に合わせて、使うイヤホンを変える人もいるそうだ。私は今まではスピーカーでしか聞いていなかったが、同じようにやってみたくなった。"
  },
  "jlpt_n3_2019_12_p10_11": {
    "id": "jlpt_n3_2019_12_p10_11",
    "title": "プロの写真屋の工夫",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 10,
    "type": "dokkai_chuubun",
    "content": "問題５：\n（１）\n近所の写真屋で「お子様の自然な笑顔を残しませんか」というポスターを見ました。プロのカメラマンが近くの公園で写真を撮ってくれるそうなので、頼んでみることにしました。私には４歳の娘がいます。娘の自然な笑顔が撮りたいのですが、自分ではなかなかうまくいかなくて、困っていたので。\n\n当日、カメラマンは公園のブランコで遊ぶ娘のすぐ近くで撮り始めました。娘がカメラをかなり気にしていたので、私はそんなやり方でいい写真が撮れるのだろうかと思いました。しかし、カメラマンは、その後もしばらくそのまま撮り続けていました。２０分ぐらい経つと、娘はカメラマンがそばにいることを気にしなくなっていきました。\n\n１時間撮ったあと、見せてくれた写真には、娘のいい笑顔が何枚も写っていました。「自然な笑顔が撮れるのは、カメラに慣れて意識しなくなってからなんです。はじめの２０分はそのための準備です。」と教えてくれました。プロの工夫を聞いて、なるほどと感心しました。"
  },
  "jlpt_n3_2019_12_p11_12": {
    "id": "jlpt_n3_2019_12_p11_12",
    "title": "右と左の伝え方",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 11,
    "type": "dokkai_chuubun",
    "content": "（２）\n先日、友だちと向かい合って食事をしていて、友達のほほにソースがついているのに気づいた。私が右のほほにソースがついているよ」と教えたら、友達は反対側のほほをふいた。「あ、そっちじゃなくて、私から見て右だよ。」といったら、「こっちか」と友達は笑った。自分の思っている「右」を相手に正しく伝えるのが難しい。\n\nインターネットで「右」を調べたら「人体の心臓のない側」とあった。しかし、これは向かい合っていると、相手の心臓か私の心臓かで逆になってしまう。それに、心臓に右がある人もいるそうだ。「はしを持つ方」と言う説明もあるが、これも同じことだ。\n\nでは、誰にとっても変わらないものは何だろう。方角なら誰にとってもどんな場所でも変わらない。先日も、「西側のほほ」といえば、正しく伝わったかもしれない。\n\nしかし、私たちはいつも方角を考えて生活してはいないので、実際にはこのような言い方はできそうにない。結局、相手と自分の位置関係を考えながら、「右」「左」という言葉を使う以外の方法はないだろう。"
  },
  "jlpt_n3_2019_12_p12_13": {
    "id": "jlpt_n3_2019_12_p12_13",
    "title": "立ったり座ったりして仕事をする机",
    "book": "JLPT N3 2019年12月 過去問",
    "page": 12,
    "type": "dokkai_choubun",
    "content": "問題６：\n私の会社では、毎日何時間もいすに座って仕事をするので、首や肩や腰が痛くなると言う人が多い。私も腰の痛みに悩んでいる。先日インターネットを見ていたら、面白いサイトがあった。腰の痛みを治すには、まず、仕事は座ってするという考え方を変えたほうがいいと書いてあったのだ。\n\nそのサイトによると、姿勢による疲れ方の違いを調べた結果、ずっと座って仕事をしていた人は、「首から上」と「足のひざから上」が特に疲れていたことがわかったそうだ。ずっと立っていた人は「足のひざから下」はとても疲れていたが、「首から上」はあまり疲れていなかった。体全体があまり疲れていなかったのは、立ったり座ったりして姿勢を変えていた人だった。\n\n実際に、ある会社では社員が立ったり座ったりして仕事をしているそうだ。その会社では、自分で高さが変えられる机を使い始めたのだ。その結果、体の調子が悪いと言う人が減り、そのうえ、以前より社員の間でよくコミュニケーションをとるようになったそうだ。立っていると、移動しやすいし、ほかの社員にも話しかけやすいらしい。会議室にも同じ机を置いて、たって会議ができるようにしてみたら、意見やアイデアがたくさん出て、会議が早く終わることが多くなったそうだ。\n\nお金はかかるかもしれないが、私たちの会社もこのような机にしてほしい。今度、会社に意見を出してみようと思う。"
  }
}

with open('bank/jlpt_n3_2019_12/vocab.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2019年12月 過去問", "unit": "文字・語彙", "questions": vocab_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2019_12/grammar.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2019年12月 過去問", "unit": "文法", "questions": grammar_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2019_12/reading.json', 'w', encoding='utf-8') as f:
    json.dump({"book": "JLPT N3 2019年12月 過去問", "unit": "読解", "questions": reading_questions}, f, ensure_ascii=False, indent=2)

with open('bank/jlpt_n3_2019_12/passages.json', 'w', encoding='utf-8') as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)

print(f"Extraction for 2019 December completed:")
print(f"  Vocab: {len(vocab_questions)} Qs")
print(f"  Grammar: {len(grammar_questions)} Qs")
print(f"  Reading: {len(reading_questions)} Qs")
print(f"  Passages: {len(passages)} passages")
print(f"  Total: {len(vocab_questions) + len(grammar_questions) + len(reading_questions)} Qs")
