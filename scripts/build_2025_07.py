"""
Extracts and structures JLPT N3 2025-07 practice exam questions into the validated bank schema:
- bank/jlpt_n3_2025_07/vocab.json (35 Qs)
- bank/jlpt_n3_2025_07/grammar.json (22 Qs)
- bank/jlpt_n3_2025_07/reading.json (16 Qs)
- bank/jlpt_n3_2025_07/passages.json (9 passages)
"""
import json
from pathlib import Path

def build_2025_07():
    out_dir = Path("bank/jlpt_n3_2025_07")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # -------------------------------------------------------------
    # PASSAGES (9 authentic passages)
    # -------------------------------------------------------------
    passages = {
        "jlpt_n3_2025_07_p09": {
            "passage_id": "jlpt_n3_2025_07_p09",
            "book_id": "jlpt_n3_2025_07",
            "unit": "問題3 文章の文法",
            "page": 9,
            "pdf_page": 9,
            "mondai_number": 3,
            "title": "スキー旅行",
            "author": "留学生の作文 (ユーキブイ)",
            "content": (
                "冬になると、駅の広告や旅行会社のちらしでスキー旅行の案内をよく見ます。"
                "去年の冬、私はスキーが上手な友達からスキー旅行に誘われました。"
                "私は寒いのが苦手だし、スキーもしたことがなかったので迷いました。でも、友達と旅行には行きたかったので、スキーにチャレンジしてみることにしました。\n"
                "私たちはバスでスキー旅行に行きました。その日は晴れていましたが、バスを降りたらとても寒くて、私は暖かいところにいたいと思いました。[19]、せっかく来たのだからと思って、スキーの練習を始めました。"
                "スキーの練習をしていると、すぐに寒さを感じなくなりました。スキーは難しかったですが、面白かったです。半日で、あまり転ばずに[20]。山の上から滑って降りるときのスピードにどきどきしました。\n"
                "今は駅でスキーの広告を見るたびに、[21]スキー旅行を思い出します。一度スキーの面白さを知ってしまうと、また行きたくなります。"
                "自分でもスキーをしてみて、日本でスキーが冬の代表的なスポーツになっている理由がよく[22]。"
            )
        },
        "jlpt_n3_2025_07_p10": {
            "passage_id": "jlpt_n3_2025_07_p10",
            "book_id": "jlpt_n3_2025_07",
            "unit": "短文 1",
            "page": 10,
            "pdf_page": 10,
            "mondai_number": 4,
            "title": "英語資料のチェック依頼",
            "author": "木村",
            "content": (
                "ジョンさん\n"
                "先週は、製品発表会の英語資料のチェックをしてくれて、ありがとうございました。\n"
                "チェックしてもらったあと、少し文章を書き加えました。それから、直したほうがいいとアドバイスをもらったのでグラフも作り直しました。直した資料をこのメールと一緒に送りますので、もう一度見てもらえませんか。新しく書き加えた部分は、赤い字になっています。\n"
                "すみませんが、今週中にご返信をお願いいたします。\n"
                "木村"
            )
        },
        "jlpt_n3_2025_07_p11_1": {
            "passage_id": "jlpt_n3_2025_07_p11_1",
            "book_id": "jlpt_n3_2025_07",
            "unit": "短文 2",
            "page": 11,
            "pdf_page": 11,
            "mondai_number": 4,
            "title": "図書館の休館と特別窓口のお知らせ",
            "author": "緑図書館",
            "content": (
                "緑図書館 1月25日\n"
                "図書館の休館と特別窓口のお知らせ\n"
                "緑図書館は、4月1日から9月30日まで、工事のため休館することになりました。この期間は、水森駅の駅ビル「グラン」3階に特別窓口を開きます。\n"
                "特別窓口では、予約した本を借りることと本を返すことができます。本や新聞を読む場所はありません。なお、本の予約は、インターネットでの予約が便利ですが、特別窓口でも可能です。\n"
                "ご利用可能時間は、決まりましたら、ホームページでお知らせします。\n"
                "ご不便をおかけしますが、よろしくお願いいたします。"
            )
        },
        "jlpt_n3_2025_07_p11_2": {
            "passage_id": "jlpt_n3_2025_07_p11_2",
            "book_id": "jlpt_n3_2025_07",
            "unit": "短文 3",
            "page": 11,
            "pdf_page": 11,
            "mondai_number": 4,
            "title": "紙から作られた靴下",
            "author": "雑誌記事読者",
            "content": (
                "昨日、雑誌で「紙から作られた靴下」という記事を読んだ。そのタイトルを見たとき、私は、紙コップのように、一度使ったら捨ててしまう物なのだろうと思った。"
                "しかし、記事によると、その靴下は、特別な紙で作った丈夫な糸でできているそうだ。紙なのに水に強く、洗濯をして何度も使えると書かれていた。予想と違っていて、意外だった。"
                "よく汗を吸ってすぐ乾くので、長い時間靴をはく人にいいそうだ。今度、買ってみようと思う。"
            )
        },
        "jlpt_n3_2025_07_p12": {
            "passage_id": "jlpt_n3_2025_07_p12",
            "book_id": "jlpt_n3_2025_07",
            "unit": "短文 4",
            "page": 12,
            "pdf_page": 12,
            "mondai_number": 4,
            "title": "体と痛みについての考察",
            "author": "医学コラム",
            "content": (
                "体が痛くて病院に通っている患者が、悪いところが治ってきたときに、「別のところが痛くなってきた。今度はそっちが悪いみたいだ。」と言うことがある。"
                "このような場合、実は、その人には最初から悪いところがいくつかあった可能性がある。人の体は、同じときに一つの痛みしか感じない。そのときにいちばん強い痛みだけを感じるのである。"
                "この患者は、最も悪かったところが治ってきたので、次の痛みを感じるようになってきたと考えられる。"
            )
        },
        "jlpt_n3_2025_07_p12_c": {
            "passage_id": "jlpt_n3_2025_07_p12_c",
            "book_id": "jlpt_n3_2025_07",
            "unit": "中文 1",
            "page": 12,
            "pdf_page": 12,
            "mondai_number": 5,
            "title": "夏休みの宿題と思い出",
            "author": "エッセイ",
            "content": (
                "私と妹は、顔はとても似ていると言われますが、嫌いな物や嫌なことに対する姿勢は逆です。例えば、食事で苦手な物があったとき、私は最後に食べますが、妹は最初に食べてしまいます。\n"
                "もう一つ①例があります。私たちが通っていた小学校では、毎年夏休みに宿題がたくさん出ました。妹はいつもすぐに終わらせましたが、私は夏休みが終わる数日前になって慌ててやり始めました。それで、毎年、私だけ両親にしかられました。\n"
                "しかし、ある年、②妹もしかられたことがありました。その年も、妹は夏休みが始まってすぐに、すべての宿題をやってしまいました。そのときは、両親は妹を褒めていました。\n"
                "でも、両親は、その中に「今年の夏休みの思い出」という作文の宿題があったことに、気がついていなかったのです。夏休みの最後の日、母は作文の内容がうそであることに気づいて、書き直させました。\n"
                "その日は、私も妹も、しかられながら机に向かいました。"
            )
        },
        "jlpt_n3_2025_07_p14": {
            "passage_id": "jlpt_n3_2025_07_p14",
            "book_id": "jlpt_n3_2025_07",
            "unit": "中文 2",
            "page": 14,
            "pdf_page": 14,
            "mondai_number": 5,
            "title": "カラス侵入禁止の紙",
            "author": "ニュース読者",
            "content": (
                "カラスは、人間の食べ物を奪ったりするので、嫌われることが多い鳥だ。そのカラスについて、ある問題を解決した人のニュースを見た。\n"
                "ある大学の研究所の建物に、倉庫として使っている場所がある。そこに、カラスが入ってきて物を壊したり汚したりするので、研究所の人は困っていた。それで、カラスの研究者に相談したら、「カラス侵入禁止(注)」と書いた紙をはったらどうかと言われた。最初は①冗談だと思ったが、実際にやってみると、②本当に来なくなったそうだ。\n"
                "カラスに文字が読めるはずがないのに、なぜこの紙に効果があったのだろうか。\n"
                "この研究者によると、まず、そこを通って紙を見た人が不思議に思って、近くにいるカラスをよく見る。すると、カラスは危険を感じて来なくなる。カラスは人間に見られるのを嫌うのだそうだ。\n"
                "ニュースを見て私は、この研究者がカラスの行動だけでなく、人間の行動についても、しっかり③予想できていたのだろうと感じた。\n"
                "(注) 侵入禁止：立ち入り禁止"
            )
        },
        "jlpt_n3_2025_07_p15": {
            "passage_id": "jlpt_n3_2025_07_p15",
            "book_id": "jlpt_n3_2025_07",
            "unit": "長文",
            "page": 15,
            "pdf_page": 15,
            "mondai_number": 6,
            "title": "未利用魚と魚料理レストラン",
            "author": "エッセイ",
            "content": (
                "先週、実家に帰ったとき、両親が、近所に新しくできた魚料理のレストランに連れて行ってくれた。両親はもう何回か行ったのだそうだ。\n"
                "メニューには、よく知られた魚を使った料理はほとんどなく、聞いたことのない魚の料理が並んでいた。いろいろな料理を食べたが、どれもおいしかった。両親は、この店では日本で今まで一般的に売られていなかった種類の魚を扱っているのだと教えてくれた。最近、そのような魚は「未利用魚」と呼ばれ、関心を持つ人が増えているそうだ。\n"
                "食事のあと、店長がテーブルに来て、いろいろ説明してくれた。日本では、魚がとれる量が減り続けていて、多いときの半分以下になっている。日本人がよく食べている魚は80種類ぐらいだが、実は、日本の近くの海では3,000種類以上の魚がとれる。そこで、未利用魚を食べる人を増やそうという動きが広がってきた。食べる人が増えれば、今まで商品としての価値がなかった魚が売れるようになるので、漁業(注)を応援することになるのだ。\n"
                "未利用魚のことを知らない人は多い。それで、この店では、未利用魚のおいしさや、食べることの意味を知ってもらうことが重要だと考えているそうだ。私もなるほどと思ったし、実は、両親も同じように感じて私を誘ったらしい。\n"
                "この話を聞いたあと、私は自分でも買いたいと思って近所のスーパーを見てみたが、未利用魚は売っていなかった。レストランの店長は、最近は未利用魚を缶詰などにしたものがインターネットで買えると言っていた。せっかく興味を持ったのだから、どういうものが買えるのか調べてみようと思う。\n"
                "(注) 漁業：魚をとる仕事"
            )
        },
        "jlpt_n3_2025_07_p17": {
            "passage_id": "jlpt_n3_2025_07_p17",
            "book_id": "jlpt_n3_2025_07",
            "unit": "情報検索",
            "page": 17,
            "pdf_page": 17,
            "mondai_number": 7,
            "title": "青葉市 市民スポーツセンター 利用のご案内",
            "author": "青葉市 市民スポーツセンター",
            "content": (
                "青葉市 市民スポーツセンター 利用のご案内\n"
                "【営業時間と休館日】\n"
                "営業時間 10:00〜20:00（利用受付は 19:30 まで） ／ 休館日 毎週月曜日\n\n"
                "【利用方法】\n"
                "・券売機で利用券を買って、窓口へお出しください。\n"
                "・利用するには、室内用の靴が必要です。\n"
                "・18 時以降、小学生と中学生は、18 歳以上の大人の方とご一緒にご利用ください。\n"
                "・1枚の利用券で利用できる時間は、2 時間までです。2 時間以上利用する場合は、必要な時間分の利用券を買ってください。\n\n"
                "料金表（一人 2 時間までの利用料金）\n"
                "・体育館：一般（大人） 380 円 ／ 高校生 190 円 ／ 小学生・中学生※ 130 円\n"
                "・卓球室：一般（大人） 200 円 ／ 高校生 150 円 ／ 小学生・中学生※ 100 円\n"
                "※ 火、木曜日は、小学生と中学生の体育館と卓球室の料金が無料になります。\n\n"
                "【体育館の利用について】\n"
                "火曜日から金曜日の 14 時から 20 時までの間、決められたスポーツができます。毎月の体育館のスケジュール表をご確認ください。\n"
                "【卓球室の利用について】\n"
                "開館日（火曜日〜日曜日）の 10 時から 20 時まで利用できます。\n\n"
                "9月の体育館のスケジュール表\n"
                "・火曜日：14時〜16時 バレーボール ／ 16時〜18時 ★バスケットボール ／ 18時〜20時 ×\n"
                "・水曜日：14時〜16時 × ／ 16時〜18時 バドミントン ／ 18時〜20時 バドミントン\n"
                "・木曜日：14時〜16時 × ／ 16時〜18時 ★バドミントン ／ 18時〜20時 バスケットボール\n"
                "・金曜日：14時〜16時 バスケットボール ／ 16時〜18時 バレーボール ／ 18時〜20時 バレーボール\n"
                "・×の時間は決まった団体等が利用する時間のため、利用はできません。\n"
                "・★の時間は小学生と中学生だけが利用可能です。"
            )
        }
    }
    (out_dir / "passages.json").write_text(json.dumps(passages, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 1. VOCABULARY (35 questions)
    # -------------------------------------------------------------
    vocab = [
        # 問題1 (漢字読み 1〜8)
        {"id": "jlpt_n3_2025_07_v_q01", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "急に涙が出てしまいました。", "options": ["なみだ", "あせ", "せき", "くしゃみ"], "answer": 1, "explanation": "「涙」は「なみだ」と読みます。", "grammar_points": ["漢字読み: 涙 (なみだ)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q02", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "けがは完全に治りました。", "options": ["かんぜん", "かんたん", "けんぜん", "けんたん"], "answer": 1, "explanation": "「完全」は「かんぜん」と読みます。", "grammar_points": ["漢字読み: 完全 (かんぜん)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q03", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "雨で地面がぬれている。", "options": ["ちめい", "ちめん", "じめい", "じめん"], "answer": 4, "explanation": "「地面」は「じめん」と読みます。", "grammar_points": ["漢字読み: 地面 (じめん)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q04", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "お金はあの箱に移したほうがいいですか。", "options": ["もどした", "かくした", "のこした", "うつした"], "answer": 4, "explanation": "「移した」は「うつした」と読みます。", "grammar_points": ["漢字読み: 移す (うつす)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q05", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "おいしくて有名なケーキを買うために行列ができている。", "options": ["ぎょうれい", "ぎょうれつ", "こうれい", "こうれつ"], "answer": 2, "explanation": "「行列」は「ぎょうれつ」と読みます。", "grammar_points": ["漢字読み: 行列 (ぎょうれつ)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q06", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "ここに身長を書いてください。", "options": ["せんちょう", "しんちょう", "じんちょう", "ぜんちょう"], "answer": 2, "explanation": "「身長」は「しんちょう」と読みます。", "grammar_points": ["漢字読み: 身長 (しんちょう)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q07", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "ユーキさんは困っているようだ。", "options": ["まよって", "おこって", "こまって", "だまって"], "answer": 3, "explanation": "「困っている」は「こまっている」と読みます。", "grammar_points": ["漢字読み: 困る (こまる)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q08", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "近くに薬局はありますか。", "options": ["やっきょ", "やきょく", "やっきょく", "やきょ"], "answer": 3, "explanation": "「薬局」は「やっきょく」と読みます。", "grammar_points": ["漢字読み: 薬局 (やっきょく)"], "difficulty": 2, "needs_review": False},

        # 問題2 (表記 9〜14)
        {"id": "jlpt_n3_2025_07_v_q09", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この町で子どもをそだてたいと思っている。", "options": ["産てたい", "育てたい", "愛てたい", "幸てたい"], "answer": 2, "explanation": "「そだてる」の漢字表記は「育てる」です。", "grammar_points": ["漢字表記: 育てる (そだてる)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q10", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "物が燃えるときに、けむりが出ます。", "options": ["煙", "燥", "焼", "爆"], "answer": 1, "explanation": "「けむり」の漢字表記は「煙」です。", "grammar_points": ["漢字表記: 煙 (けむり)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q11", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ここからしんりんが見えます。", "options": ["森村", "森林", "山林", "山村"], "answer": 2, "explanation": "「しんりん」の漢字表記は「森林」です。", "grammar_points": ["漢字表記: 森林 (しんりん)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q12", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "朝、シャワーをあびました。", "options": ["流びました", "洗びました", "清びました", "浴びました"], "answer": 4, "explanation": "「あびる」の漢字表記は「浴びる」です。", "grammar_points": ["漢字表記: 浴びる (あびる)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q13", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "文字の色を変えることはかのうでしょうか。", "options": ["可能", "可態", "化能", "化態"], "answer": 1, "explanation": "「かのう」の漢字表記は「可能」です。", "grammar_points": ["漢字表記: 可能 (かのう)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q14", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今からメールをそうしんします。", "options": ["返信", "送真", "送信", "返真"], "answer": 3, "explanation": "「そうしん」の漢字表記は「送信」です。", "grammar_points": ["漢字表記: 送信 (そうしん)"], "difficulty": 1, "needs_review": False},

        # 問題3 (文脈規定 15〜25)
        {"id": "jlpt_n3_2025_07_v_q15", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "山の上から見た景色が素晴らしくて、とても（　）した。", "options": ["拝見", "歓迎", "応答", "感動"], "answer": 4, "explanation": "素晴らしい景色に心を強く動かされたので「感動」が適切です。", "grammar_points": ["文脈規定: 感動する"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q16", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この店では、以前誰かが使っていた（　）の車を売っている。", "options": ["後半", "中年", "中古", "後期"], "answer": 3, "explanation": "以前誰かが使用していたものは「中古（ちゅうこ）」と言います。「中古の車」で中古車を意味します。", "grammar_points": ["文脈規定: 中古"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q17", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "来週の旅行に持っていく物の（　）を作った。", "options": ["スケジュール", "リスト", "カタログ", "プログラム"], "answer": 2, "explanation": "持っていく品物を書き並べた一覧表なので「リスト」が適切です。", "grammar_points": ["外来語: リスト (list)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q18", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この前は試合に負けて（　）が、今回は勝てたので、本当にうれしい。", "options": ["くやしかった", "まずしかった", "ゆるかった", "ずるかった"], "answer": 1, "explanation": "勝負に負けて残念で悔しい感情を表すのは「くやしかった」です。", "grammar_points": ["イ形容詞: 悔しい (くやしい)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q19", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ここから市役所までの（　）はどのくらいですか。", "options": ["途中", "徒歩", "方向", "距離"], "answer": 4, "explanation": "二つの地点の間の長さを尋ねているので「距離（きょり）」が最も適切です。", "grammar_points": ["文脈規定: 距離"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q20", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "シャワーの後は、このタオルで体を（　）ください。", "options": ["ほして", "ふいて", "張って", "直して"], "answer": 2, "explanation": "タオルで水気を取る動作は「拭く（ふく）」です。", "grammar_points": ["動詞: 拭く (ふく)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q21", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "配達が遅れたせいで、お客さんから（　）を言われてしまった。", "options": ["失礼", "命令", "否定", "文句"], "answer": 4, "explanation": "不満や苦情を言うことは「文句（もんく）を言う」とコロケーションで用います。", "grammar_points": ["慣用連語: 文句を言う"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q22", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この問題を解決するために、何かよい方法を（　）人はいませんか。", "options": ["思いついた", "引き受けて", "知り合った", "取り替えた"], "answer": 1, "explanation": "新しいアイデアや考えが頭に浮かぶことは「思いつく」と言います。", "grammar_points": ["複合動詞: 思いつく"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q23", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私の家から駅までは（　）なので、駅まで歩くと疲れます。", "options": ["坂道", "通り道", "片道", "近道"], "answer": 1, "explanation": "傾斜のある道で歩くと疲れるので「坂道（さかみち）」が適しています。", "grammar_points": ["名詞: 坂道"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q24", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この店はとても人気があり、店の前にはいつも、開店を待つ人の長い（　）ができて いる。", "options": ["帯", "線", "列", "壁"], "answer": 3, "explanation": "順番を待つ人の並びを「列（れつ）」と言います。「長い列ができる」の形で使われます。", "grammar_points": ["名詞: 列 (れつ)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q25", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "後でレポートを書くために、実験の結果をノートに（　）した。", "options": ["申請", "記録", "予報", "通知"], "answer": 2, "explanation": "出来事や実験の結果などを将来のために書き残す行為は「記録（きろく）」です。", "grammar_points": ["名詞・スル動詞: 記録"], "difficulty": 2, "needs_review": False},

        # 問題4 (言い換え類義 26〜30)
        {"id": "jlpt_n3_2025_07_v_q26", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "あの仕事は本当に苦労した。", "options": ["危険だった", "大変だった", "つまらなかった", "やりたくなかった"], "answer": 2, "explanation": "「苦労した（くろうした）」は骨が折れて心身ともに「大変だった」という意味に最も近いです。", "grammar_points": ["類義語: 苦労する ＝ 大変だ"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q27", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ユーキさんとモギさんは、部屋からそっと出ていった。", "options": ["静かに", "にぎやかに", "急いで", "二人で"], "answer": 1, "explanation": "「そっと」は物音を立てずに気づかれないようにする様子を表すので、「静かに」が同義です。", "grammar_points": ["副詞・類義語: そっと ＝ 静かに"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q28", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日、田中さんは早退したそうです。", "options": ["早く起きた", "早く来た", "早く寝た", "早く帰った"], "answer": 4, "explanation": "「早退（そうたい）する」は所定の終了時刻より「早く帰る」ことを意味します。", "grammar_points": ["類義語: 早退する ＝ 早く帰る"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q29", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ここに来てから1週間くらいたちました。", "options": ["待ちました", "続けました", "休みました", "過ぎました"], "answer": 4, "explanation": "時が「たつ（経つ）」は時間が「過ぎる」と同義です。", "grammar_points": ["動詞・類義語: 時がたつ ＝ 過ぎる"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q30", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この店ではさまざまな料理が食べられます。", "options": ["きれいな", "有名な", "いろいろな", "特別な"], "answer": 3, "explanation": "「さまざま（様々）」は種類が多様であることを表すので「いろいろな」と同義です。", "grammar_points": ["ナ形容詞・類義語: さまざま ＝ いろいろ"], "difficulty": 1, "needs_review": False},

        # 問題5 (用法 31〜35)
        {"id": "jlpt_n3_2025_07_v_q31", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "減少", "options": [
            "弟はサッカーの試合に負けてから、元気が減少している。",
            "気温が減少しているので、今夜は雪が降ると思う。",
            "調査によると、この国の人口は今後減少するそうだ。",
            "今年はりんごの値段が去年より減少したらしい。"
        ], "answer": 3, "explanation": "「減少（げんしょう）」は数量や人口などの数値が減ることに用います。「人口が減少する」というコロケーションが最も自然です。元気は「なくなる/衰える」、気温は「下がる」、値段は「下がる/安くなる」を用います。", "grammar_points": ["語の用法: 減少 (数量・数値の低下)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q32", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "重大", "options": [
            "子どもたちは重大な顔をして、先生の話を聞いていた。",
            "これは祖母からもらった重大な指輪だ。",
            "外国での一人暮らしは、重大な経験になると思う。",
            "明日、社長から重大な発表があるそうだ。"
        ], "answer": 4, "explanation": "「重大（じゅうだい）」は結果や影響が極めて深刻・重要であることを表し、「重大な発表」「重大な責任」「重大な事件」などの形で使います。1は「真剣な」、2は「大切な/貴重な」、3は「貴重な/大きな」を用います。", "grammar_points": ["語の用法: 重大 (重大な発表・決定)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q33", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ばらばら", "options": [
            "冷凍庫に入れるのを忘れて、アイスクリームがばらばらになってしまった。",
            "床に落としてしまい、資料がばらばらになってしまった。",
            "ドアを開けたので、部屋の暖かい空気がばらばらになってしまった。",
            "コップが倒れて、中のジュースがばらばらになってしまった。"
        ], "answer": 2, "explanation": "「ばらばら」は一つにまとまっていた物が散乱して散り散りになる状態を表します。「資料がばらばらになる」が正しい用法です。アイスクリームは「溶けて」、空気は「逃げて」、ジュースは「こぼれて」を用います。", "grammar_points": ["オノマトペ・副詞: ばらばら (散乱)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q34", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "皮", "options": [
            "じゃがいもは皮をむかないで、そのままゆでます。",
            "机にぶつけて、パソコンの皮に傷がついてしまった。",
            "割った卵の皮はここに捨ててください。",
            "テキストの皮に名前が書いてあるので、誰の物か分かります。"
        ], "answer": 1, "explanation": "「皮（かわ）」は動植物の体や果実・野菜の外側を包む薄い層を表します。「じゃがいもの皮をむく」が自然です。パソコンは「表面/カバー」、卵は「殻（から）」、テキストは「表紙（ひょうし）」を用います。", "grammar_points": ["語の用法: 皮 (野菜や果物の外層)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_v_q35", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "オーダー", "options": [
            "健康のため、毎日運動をするように医者からオーダーされた。",
            "母は妹に部屋の掃除をオーダーした。",
            "レストランで食事の後にデザートをオーダーした。",
            "次の大会で必ず優勝してほしいと選手たちにオーダーした。"
        ], "answer": 3, "explanation": "「オーダー（order）」は主に飲食店で料理などを「注文する」ことや、特注品を発注することに用います。「デザートをオーダーした」が正しい使い方です。1は「指示された」、2は「言いつけた/頼んだ」、4は「要求した/期待した」を用います。", "grammar_points": ["外来語: オーダー (注文)"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "vocab.json").write_text(json.dumps({"questions": vocab}, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 2. GRAMMAR (22 questions)
    # -------------------------------------------------------------
    grammar = [
        # 問題1 (文法形式の判断 1〜13)
        {"id": "jlpt_n3_2025_07_g_q01", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "先月東京で行われたサッカーの国際大会には、世界中（　）多くのサッカーファンが集まった。", "options": ["に", "で", "から", "まで"], "answer": 3, "explanation": "各地を起点として人々が集まってくる移動の起点・出所を表す助詞は「から」です。「世界中から集まる」が正解です。", "grammar_points": ["助詞: から (起点・出所)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q02", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "食事のマナーは国（　）違うので、私は旅行に行く前に、気をつけたほうがいいことはないか調べるようにしている。", "options": ["によって", "に対して", "にとって", "において"], "answer": 1, "explanation": "名詞に応じてそれぞれ異なる多様性・相違を表す「〜によって（違う）」が適切です。", "grammar_points": ["〜によって (相違・多様性)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q03", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "A「もうすぐ（　）この前言ってたけど、準備は進んでる？」\nB「うん。」", "options": ["引っ越す", "引っ越すか", "引っ越すって", "引っ越すのを"], "answer": 3, "explanation": "相手が以前発言した内容を引用・取り上げるくだけた引用表現「〜って（この前言ってた）」が適切です。", "grammar_points": ["〜って (引用の「と」のくだけた口語形)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q04", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "田中「山下さん、映画をよく見るそうですね。映画館で見るんですか。」\n山下「映画館にも行きますが、（　）、家でDVDを見ることが多いですね。」", "options": ["確かに", "まるで", "必ずしも", "どちらかというと"], "answer": 4, "explanation": "二者択一や傾向を問われた際に、強いて選ぶならそちらの傾向が強いと述べる「どちらかというと」が最適です。", "grammar_points": ["副詞表現: どちらかというと"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q05", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（料理番組で）\n「じゃがいもは、ゆでてから皮をむいたほうが、きれいに皮がむけます。ゆでた後、熱い（　）皮をむきましょう。」", "options": ["のに", "うちに", "ことで", "とすると"], "answer": 2, "explanation": "ある状態（熱い状態）が続いている間に動作を行うことを表す「〜うちに」が適切です。", "grammar_points": ["〜うちに (ある状態が継続している間に)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q06", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "少し前にご飯を食べた（　）なのに、もうおなかがすいてきた。", "options": ["せい", "とき", "よう", "ばかり"], "answer": 4, "explanation": "動作が終わってから心理的にまだほとんど時間が経過していないことを表す「〜たばかり（なのに）」が適切です。", "grammar_points": ["〜たばかり (完了直後の心理的近接)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q07", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私は小学生のころ、ゲームが大好きだった。早く家でゲームが（　）、毎日学校から走って帰っていた。", "options": ["したくて", "したくても", "するためで", "するためでも"], "answer": 1, "explanation": "願望（〜たい）の理由・動機を表して後続の行動へとつなげる接続「〜したくて」が最も自然です。", "grammar_points": ["願望接続: 〜たくて (理由・動機)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q08", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "弟の誕生日プレゼントを何にするか考えている。何を（　）、喜ぶだろうか。", "options": ["くれたら", "あげたら", "くれるから", "あげるから"], "answer": 2, "explanation": "話者から身内である弟への授受表現は「あげる」であり、仮定条件をつなぐ「あげたら」が正解です。", "grammar_points": ["授受動詞と条件: 〜てあげる / 〜たら"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q09", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（電話で）\nA「この前借りた小説、もう1回貸してもらえない？」\nB「うん、いいよ。あした、学校に（　）ね。」", "options": ["持っとく", "持ってる", "持ってく", "持っちゃう"], "answer": 3, "explanation": "「持っていく」の口語縮約形「持ってく」が正解です。学校へ本を持って行くという移動を伴う行為を表します。", "grammar_points": ["口語縮約: 〜ていく → 〜てく"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q10", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "A「再来週の登山、楽しみだね。」\nB「うん、（　）ね。」", "options": ["晴れてきた", "晴れるといい", "晴れるんだ", "晴れてよかった"], "answer": 2, "explanation": "将来の望ましい事態を願う表現は「〜といい（ね）」です。", "grammar_points": ["希望・願いの表現: 〜といい"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q11", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（市のホームページで）\n9月30日に絵本作家の坂木みどりさんによる講演会が開かれます。市民の方であれば、どなたでも無料で（　）。", "options": ["ご参加になれます", "参加いたします", "ご参加になっています", "参加できております"], "answer": 1, "explanation": "市民に対する敬語（尊敬語）かつ可能表現です。「ご＋動詞の連用形＋になる」に可能の助動詞がついた「ご参加になれます」が適切です。", "grammar_points": ["敬語 (尊敬可能表現): ご〜になれる"], "difficulty": 3, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q12", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "以前は、会社の窓から海を見ることができたが、隣に高いビルができて、（　）。", "options": ["見えなくてもよくなった", "見られたかもしれない", "見えなくなってしまった", "見られるようにならない"], "answer": 3, "explanation": "以前は見えていたものがビルによって遮られ、残念な結果として視認不可能になった変化を表す「見えなくなってしまった」が適切です。", "grammar_points": ["可能動詞の否定変化と残念の意: 〜なくなる ＋ 〜てしまう"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q13", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（病院で）\n医者「この薬を五日間飲んでください。」\n患者「わかりました。熱が下がっても（　）。」\n医者「はい。五日間必ず飲んでください。」", "options": ["飲んではいけませんか", "飲んでいないんでしょうか", "飲んでみようと思いますか", "飲んだほうがいいでしょうか"], "answer": 4, "explanation": "熱が下がった場合でも服用を継続すべきかどうかを医師に相談・確認する表現「〜たほうがいいでしょうか」が最も適切です。", "grammar_points": ["助言を求める表現: 〜たほうがいいでしょうか"], "difficulty": 2, "needs_review": False},

        # 問題2 (文の組み立て 14〜18)
        {"id": "jlpt_n3_2025_07_g_q14", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今年の夏も暑いが、＿＿ ＿＿ ★ ＿＿ ずっと涼しく感じる。", "options": ["異常な", "に比べると", "暑さだった", "去年の夏"], "answer": 4, "explanation": "正しい語順は「異常な(1) → 暑さだった(3) → 去年の夏(4) → に比べると(2)」となります。★に入るのは 4（去年の夏）です。", "grammar_points": ["文の組み立て: 連体修飾 ＋ 〜に比べると"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q15", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "初めてアルバイトをして、お金を稼ぐ＿＿ ＿＿ ★ ＿＿ わかった。", "options": ["ことか", "大変な", "ことが", "どれだけ"], "answer": 2, "explanation": "正しい語順は「ことが(3) → どれだけ(4) → 大変な(2) → ことか(1)」となります。★に入るのは 2（大変な）です。", "grammar_points": ["文の組み立て: どれだけ〜ことか (感嘆・強調)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q16", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今日、昼食の後、図書館へ行って本を読んでいたら ＿＿ ＿＿ ★ ＿＿。", "options": ["ので", "外が暗くなっていた", "驚いた", "いつの間にか"], "answer": 1, "explanation": "正しい語順は「いつの間にか(4) → 外が暗くなっていた(2) → ので(1) → 驚いた(3)」となります。★に入るのは 1（ので）です。", "grammar_points": ["文の組み立て: 副詞 ＋ 状況変化 ＋ 原因・理由 (〜ので)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q17", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "このチーズケーキの ＿＿ ＿＿ ★ ＿＿、誰でも簡単に作れると思う。", "options": ["だから", "作り方", "だけ", "材料を混ぜて冷やす"], "answer": 3, "explanation": "正しい語順は「作り方は材料を混ぜて冷やす(4) → だけ(3) → だから(1)」(このチーズケーキの作り方は...「作り方(2) → 材料を混ぜて冷やす(4) → だけ(3) → だから(1)」)となります。★に入るのは 3（だけ）です。", "grammar_points": ["文の組み立て: 〜だけだから (限定・理由)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q18", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "A「あさってのサッカーの試合、応援に行くね。天気予報では曇りと言っていたけど、雨だったら中止になる？」\nB「ありがとう。もし ＿＿ ＿＿ ★ ＿＿ 応援には無理して来なくてもいいよ。」", "options": ["雨が降ったら", "試合は", "雨が降ったとしても", "中止にならないんだけど"], "answer": 4, "explanation": "正しい語順は「試合は(2) → 雨が降ったとしても(3) → 中止にならないんだけど(4)、もし雨が降ったら(1) 応援には無理して来なくてもいいよ」となります。★に入るのは 4（中止にならないんだけど）です。", "grammar_points": ["文の組み立て: 〜としても (譲歩条件) ＋ 〜んだけど (前置き)"], "difficulty": 3, "needs_review": False},

        # 問題3 (文章の文法 19〜22)
        {"id": "jlpt_n3_2025_07_g_q19", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p09", "question": "（19）に入る最もよいものをえらびなさい。", "options": ["例えば", "それでも", "実は", "また"], "answer": 2, "explanation": "直前の「暖かいところにいたいと思った」という消極的な思いに反して、「せっかく来たのだから」と気持ちを切り替えて練習を始める逆接の接続詞「それでも」が適切です。", "grammar_points": ["文章の文法: 逆接接続詞 (それでも)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q20", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p09", "question": "（20）に入る最もよいものをえらびなさい。", "options": ["滑れるようになりました", "滑れるようにしてあげました", "滑ってくれました", "滑ってもらえました"], "answer": 1, "explanation": "練習の成果として筆者自身が半日で上達し、転ばずに滑ることができる状態に変化したことを表す「滑れるようになりました」が正解です。", "grammar_points": ["文章の文法: 能力変化表現 (〜ようになる)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q21", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p09", "question": "（21）に入る最もよいものをえらびなさい。", "options": ["あの広告の", "ああいう", "ある", "あの"], "answer": 4, "explanation": "筆者の記憶の中にある「あの（去年のスキー旅行）」を指し示す連体詞「あの」が適切です。", "grammar_points": ["文章の文法: 指示詞のア系列 (追想・共通記憶)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_g_q22", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "言語知識（文法）", "page": 10, "pdf_page": 10, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p09", "question": "（22）に入る最もよいものをえらびなさい。", "options": ["わかっていきます", "わかるのでしょう", "わかりました", "わかったそうです"], "answer": 3, "explanation": "自分でスキーを実際に体験した結果、納得・理解に至った過去の心理的到達点を表す「わかりました」が適切です。", "grammar_points": ["文章の文法: 文末表現 (理解の完了・納得)"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "grammar.json").write_text(json.dumps({"questions": grammar}, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 3. READING (16 questions)
    # -------------------------------------------------------------
    reading = [
        # 問題4 (短文 23〜26)
        {"id": "jlpt_n3_2025_07_r_q23", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "短文 1", "page": 10, "pdf_page": 10, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p10", "question": "ジョンさんがこのメールで頼まれていることはどれか。", "options": [
            "今週中にもう一度、資料のチェックをすること。",
            "今週中に資料のチェックをするために木村さんと会うこと。",
            "今週中に日本語の資料を英語に直すこと。",
            "今週中に新しい資料を作ること。"
        ], "answer": 1, "explanation": "メール本文に「直した資料をこのメールと一緒に送りますので、もう一度見てもらえませんか」「今週中にご返信をお願いいたします」とあり、資料の再チェックを依頼されています。", "grammar_points": ["読解（短文）: 依頼内容の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q24", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "短文 2", "page": 11, "pdf_page": 11, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p11_1", "question": "駅ビルの特別窓口でできることは何か。", "options": [
            "予約した本を借りることと、本を返すことと、本を読むことと、本の予約をすること。",
            "予約した本を借りることと、本を返すことと、本を読むこと。",
            "予約した本を借りることと、本を返すことと、本の予約をすること。",
            "予約した本を借りることと、本を返すことだけ。"
        ], "answer": 3, "explanation": "「特別窓口では、予約した本を借りることと本を返すことができます」「本の予約は、インターネットでの予約が便利ですが、特別窓口でも可能です」とあり、読書スペースはないため、予約本の貸出・返却・予約ができます。", "grammar_points": ["読解（短文）: 施設利用条件の正確な読解"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q25", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "短文 3", "page": 12, "pdf_page": 12, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p11_2", "question": "予想と違っていて、意外だったとあるが、何が意外だったのか。", "options": [
            "紙コップのように、一度使ったら捨てる紙の靴下があること。",
            "記事で紹介されていた靴下は、洗濯ができて、繰り返して使えること。",
            "記事で紹介されていた靴下は、よく汗を吸ってすぐに乾くこと。",
            "長い時間靴をはく人のための靴下があること。"
        ], "answer": 2, "explanation": "筆者は当初「一度使ったら捨ててしまう物」と思っていたのに対し、「紙なのに水に強く、洗濯をして何度も使える」と書かれていたため意外に感じました。", "grammar_points": ["読解（短文）: 対比と心情把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q26", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "短文 4", "page": 12, "pdf_page": 12, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p12", "question": "この文章では、患者が「別のところが痛くなってきた。今度はそっちが悪いみたいだ。」と言うのは、なぜだと言っているか。", "options": [
            "悪いところが治ってきたときに、複数の痛みを感じるようになることがあるから。",
            "悪いところが一つ治ると、次に悪かったところがもっと悪くなることがあるから。",
            "痛いところがいくつかあっても、患者は一つずつしか伝えないことがあるから。",
            "痛かったところがよくなると、別のところの痛みを感じるようになることがあるから。"
        ], "answer": 4, "explanation": "本文に「人の体は、同じときに一つの痛みしか感じない。そのときにいちばん強い痛みだけを感じる」「最も悪かったところが治ってきたので、次の痛みを感じるようになってきた」と書かれています。", "grammar_points": ["読解（短文）: 因果関係の把握"], "difficulty": 2, "needs_review": False},

        # 問題5 (中文 27〜32)
        {"id": "jlpt_n3_2025_07_r_q27", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 1", "page": 13, "pdf_page": 13, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p12_c", "question": "①例とあるが、何についての例か。", "options": [
            "「私」と妹は、顔だけでなく、性格も似ているということ。",
            "「私」と妹は、嫌いな物や嫌なことに対する姿勢が逆だということ。",
            "「私」と妹は、協力し合って夏休みの宿題をしていたということ。",
            "「私」と妹は、毎年夏休みに必ず両親にしかられていたこと。"
        ], "answer": 2, "explanation": "直前の段落に「嫌いな物や嫌なことに対する姿勢は逆です」とあり、苦手な食べ物を食べる順番に続く「もう一つの例」として宿題への取り組み方が挙げられています。", "grammar_points": ["読解（中文）: 指示語と段落構成の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q28", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 1", "page": 13, "pdf_page": 13, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p12_c", "question": "「私」と妹は、毎年の夏休みの宿題をどう思っていたか。", "options": [
            "「私」も妹も好きだった。",
            "「私」も妹も嫌だった。",
            "「私」は好きだったが、妹は嫌だった。",
            "「私」は嫌だったが、妹は好きだった。"
        ], "answer": 2, "explanation": "宿題は二人にとって「嫌なこと」の例として語られており、妹は嫌だからこそ最初に終わらせ、筆者は嫌だから後回しにしていました。したがって二人とも嫌でした。", "grammar_points": ["読解（中文）: 文脈的前提の推論"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q29", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 1", "page": 14, "pdf_page": 14, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p12_c", "question": "②妹もしかられたとあるが、妹はなぜしかられたのか。", "options": [
            "夏休みが終わる数日前になって宿題をやり始めたから。",
            "「私」の作文と同じことを「今年の夏休みの思い出」に書いたから。",
            "「今年の夏休みの思い出」に、実際にはしていないことを書いたから。",
            "「今年の夏休みの思い出」を、夏休みの最後の日まで書かなかったから。"
        ], "answer": 3, "explanation": "本文に「夏休みの最後の日、母は作文の内容がうそであることに気づいて、書き直させました」とあり、夏休みの初めに書いたため実際にはしていない嘘の思い出を書いたからです。", "grammar_points": ["読解（中文）: 理由・エピソードの把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q30", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 2", "page": 14, "pdf_page": 14, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p14", "question": "①冗談だと思ったとあるが、なぜそう思ったのか。", "options": [
            "カラスが文字を読めないと意味がない方法だから。",
            "カラスの研究者でなくても思いつくような方法だから。",
            "カラスの研究者でなければ実行できないような方法だから。",
            "カラスがいながらず、逆に、集まってしまいそうな方法だから。"
        ], "answer": 1, "explanation": "直後に「カラスに文字が読めるはずがないのに」とあるように、鳥であるカラスに対して文字で警告を書いても意味がないと考えたため冗談だと思いました。", "grammar_points": ["読解（中文）: 心理の根拠把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q31", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 2", "page": 15, "pdf_page": 15, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p14", "question": "②本当に来なくなったとあるが、なぜか。", "options": [
            "倉庫が汚くなって、カラスが好きな場所ではなくなったから。",
            "カラスが今までなかった紙を見て、危険な場所になったと感じたから。",
            "研究者が観察しに来るようになったことを、カラスが嫌ったか。",
            "カラスをよく見る人が増えて、カラスが危険を感じたから。"
        ], "answer": 4, "explanation": "本文に「紙を見た人が不思議に思って、近くにいるカラスをよく見る。すると、カラスは危険を感じて来なくなる。カラスは人間に見られるのを嫌うのだそうだ」とあります。", "grammar_points": ["読解（中文）: 仕組み・メカニズムの読解"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q32", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "中文 2", "page": 15, "pdf_page": 15, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p14", "question": "③予想できていたとあるが、人間の行動について、研究者はどのように予想していたと考えられるか。", "options": [
            "ニュースで取り上げられて有名になった場所には、行ってみたくなる。",
            "カラスに入ってほしくない場所には、カラスが入らないような工夫をする。",
            "カラスがいる場所では、危険を感じてカラスの近くに行かないようにする。",
            "「カラス侵入禁止」と書かれた紙を見たら、近くにいるカラスを観察したくなる。"
        ], "answer": 4, "explanation": "研究者は「そこを通って紙を見た人が不思議に思って、近くにいるカラスをよく見る」という人間の心理・行動を巧みに計算して紙を貼るよう提案しました。", "grammar_points": ["読解（中文）: 意図の把握"], "difficulty": 2, "needs_review": False},

        # 問題6 (長文 33〜36)
        {"id": "jlpt_n3_2025_07_r_q33", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p15", "question": "先週、「私」が行ったレストランは、どのようなレストランか。", "options": [
            "普通の魚を使った料理も珍しい魚を使った料理も多い。",
            "普通の魚を使った料理がとても多く、珍しい魚を使った料理が少ない。",
            "普通の魚を使った料理がとても少なく、珍しい魚を使った料理が多い。",
            "珍しい魚を使った料理しかない。"
        ], "answer": 3, "explanation": "本文に「よく知られた魚を使った料理はほとんどなく、聞いたことのない魚の料理が並んでいた」とあり、一般に知られた普通の魚料理は極めて少なく、珍しい未利用魚の料理が並んでいます。", "grammar_points": ["読解（長文）: 特徴・概況の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q34", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p15", "question": "説明してくれたとあるが、説明の内容として合っているのはどれか。", "options": [
            "日本でとれる魚の量が減ったことで、未利用魚を食べる人を増やす動きが進んだ。",
            "日本ではたくさんの種類の魚がとれるが、日本人の食べる魚の種類は減っている。",
            "未利用魚を食べる人が増えると、未利用魚以外の魚が売れなくなる。",
            "今までに同じ種類の魚を食べ続けることが、魚をとる仕事を応援することになる。"
        ], "answer": 1, "explanation": "店長の説明として「魚がとれる量が減り続けていて、多いときの半分以下になっている。（中略）そこで、未利用魚を食べる人を増やそうという動きが広がってきた」とあります。", "grammar_points": ["読解（長文）: 本文内容合致判断"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q35", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p15", "question": "両親が「私」をレストランに連れて行ったのはなぜか。", "options": [
            "未利用魚のおいしさや食べることの意味を、「私」にも知ってほしかったから。",
            "未利用魚を食べながら、「私」から未利用魚についての話を聞きたかったから。",
            "未利用魚以外にもおいしい魚がたくさんあると、「私」に教えたかったから。",
            "「私」が未利用魚に関心を持っていることを知っていたから。"
        ], "answer": 1, "explanation": "本文に「未利用魚のおいしさや、食べることの意味を知ってもらうことが重要だと考えているそうだ。私もなるほどと思ったし、実は、両親も同じように感じて私を誘ったらしい」と書かれています。", "grammar_points": ["読解（長文）: 人物の意図把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q36", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "長文", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p15", "question": "「私」は、これからどうしようと思っているか。", "options": [
            "自分の家の近所にも、未利用魚の料理を扱うレストランがないか調べてみよう。",
            "自分の家の近所のスーパーで、未利用魚を売っていないか見てみよう。",
            "自分でも買うことができる未利用魚をインターネットで探してみよう。",
            "インターネットで買える未利用魚にどういうものがあるのか、店長に聞いてみよう。"
        ], "answer": 3, "explanation": "本文末尾に「最近は未利用魚を缶詰などにしたものがインターネットで買えると言っていた。せっかく興味を持ったのだから、どういうものが買えるのか調べてみようと思う」とあります。", "grammar_points": ["読解（長文）: 結び・今後の意向把握"], "difficulty": 2, "needs_review": False},

        # 問題7 (情報検索 37〜38)
        {"id": "jlpt_n3_2025_07_r_q37", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "情報検索", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、ある市のスポーツセンターのホームページに載っている利用案内である。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p17", "question": "高校生のモギさんは、小学生の妹と一緒に卓球室を利用したいと思っている。木曜日に1時間利用する場合、モギさんたちの料金はいくらになるか。", "options": [
            "モギさんも妹も無料。",
            "モギさんは150円、妹は無料。",
            "モギさんは150円、妹は100円。",
            "モギさんは190円、妹は130円。"
        ], "answer": 2, "explanation": "卓球室の高校生料金は150円です。小学生は通常100円ですが、「※火、木曜日は、小学生と中学生の体育館と卓球室の料金が無料になります」とあるため、木曜日は妹が無料になります。したがってモギさんは150円、妹は無料です。", "grammar_points": ["情報検索: 条件絞り込み（曜日割引の適用）"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_07_r_q38", "book": "JLPT N3 2025年7月 実戦問題集", "book_code": "jlpt_n3_2025_07", "unit": "情報検索", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、ある市のスポーツセンターのホームページに載っている利用案内である。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_07_p17", "question": "大学生のユーキさんは、9月に体育館でバスケットボールの練習をしようと思っている。16時から20時の間で、1時間練習したい。ユーキさんが練習できるのはどの曜日か。", "options": [
            "火曜日か木曜日か金曜日。",
            "火曜日か木曜日。",
            "木曜日か金曜日。",
            "木曜日。"
        ], "answer": 4, "explanation": "大学生のユーキさんは一般（大人）です。スケジュール表のバスケットボールを確認すると、火曜16時〜18時は★印（小学生と中学生限定）、金曜は14時〜16時（時間帯外）です。木曜日は18時〜20時がバスケットボールで大人も利用可能なため、利用できるのは「木曜日」のみです。", "grammar_points": ["情報検索: 条件照合（一般対象・種目・時間帯）"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "reading.json").write_text(json.dumps({"questions": reading}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Extraction for 2025-07 practice exam completed:")
    print(f"  Vocab: {len(vocab)} Qs")
    print(f"  Grammar: {len(grammar)} Qs")
    print(f"  Reading: {len(reading)} Qs")
    print(f"  Passages: {len(passages)} passages")
    print(f"  Total: {len(vocab) + len(grammar) + len(reading)} Qs")

if __name__ == "__main__":
    build_2025_07()
