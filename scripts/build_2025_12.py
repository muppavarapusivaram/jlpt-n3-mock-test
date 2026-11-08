"""
Extracts and structures JLPT N3 2025-12 practice exam questions into the validated bank schema:
- bank/jlpt_n3_2025_12/vocab.json (35 Qs)
- bank/jlpt_n3_2025_12/grammar.json (22 Qs)
- bank/jlpt_n3_2025_12/reading.json (16 Qs)
- bank/jlpt_n3_2025_12/passages.json (9 passages)
"""
import json
from pathlib import Path

def build_2025_12():
    out_dir = Path("bank/jlpt_n3_2025_12")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # -------------------------------------------------------------
    # PASSAGES (9 authentic passages)
    # -------------------------------------------------------------
    passages = {
        "jlpt_n3_2025_12_p08": {
            "passage_id": "jlpt_n3_2025_12_p08",
            "book_id": "jlpt_n3_2025_12",
            "unit": "問題3 文章の文法",
            "page": 8,
            "pdf_page": 8,
            "mondai_number": 3,
            "title": "コンビニ",
            "author": "留学生の作文 (ウイルソン リサ)",
            "content": (
                "私は日本のコンビニが好きです。家の近くや大学の近くにいろいろなコンビニがあるのですが、24時間営業なので、とても便利です。\n"
                "日本に来たばかりのころ、コンビニに行くとき、コンビニの会社の違いはあまり気にしていませんでした。会社が違っても、売っている商品は同じだと[19]。"
                "売っている商品が会社によって少し違うことに気がついたのは、日本に来て1か月ぐらいたったところでした。飲み物、食べ物、生活用品、雑誌などが売られているのは同じです。[20]、それぞれの会社のコンビニに、ほかの会社のコンビニにはないデザートやパンや弁当などがあるのです。"
                "会社ごとにおいしいデザートやパンや弁当を考えて、自分たちだけの新しい商品を作っているようです。いつ行っても店には新しい商品がたくさん並んでいます。"
                "見ているだけでも楽しいし、[21]会社もいい商品を売ろうとがんばっているようで、応援したくなります。\n"
                "私にとってコンビニは買い物をするだけの場所ではありません。食べてみたい商品や新商品がたくさん並んでいて、行くと楽しい気分になれる[22]。"
            )
        },
        "jlpt_n3_2025_12_p09": {
            "passage_id": "jlpt_n3_2025_12_p09",
            "book_id": "jlpt_n3_2025_12",
            "unit": "短文 1",
            "page": 9,
            "pdf_page": 9,
            "mondai_number": 4,
            "title": "野菜の皮のだし",
            "author": "エッセイ",
            "content": (
                "先日、友人の家に遊びに行ったとき、カレーライスとスープをごちそうになった。"
                "とてもおいしかったと言うと、友人は「スープは、カレーに使った野菜の皮を煮て、だしを取って作ったんだ。栄養もあるんだよ。」と教えてくれた。"
                "30分ぐらい煮るだけで、たまねぎの茶色の薄い皮やにんじんの皮から栄養があるだしが取れるそうだ。"
                "今まで私は、野菜の皮は何も考えないで捨てていたが、今度、私もやってみようと思った。"
            )
        },
        "jlpt_n3_2025_12_p10": {
            "passage_id": "jlpt_n3_2025_12_p10",
            "book_id": "jlpt_n3_2025_12",
            "unit": "短文 2",
            "page": 10,
            "pdf_page": 10,
            "mondai_number": 4,
            "title": "春のピクニックのお知らせ",
            "author": "東山大学 国際交流クラブ",
            "content": (
                "国際交流クラブ 春のピクニックのお知らせ\n"
                "国際交流クラブの会員でない方も参加できます。留学生も日本人学生も、ぜひ参加してください。\n"
                "【日時】4月20日(土) 14時〜16時\n"
                "【場所】花森公園 北広場\n"
                "【参加費】300円 (当日集めます。会員は無料です。)\n"
                "【その他】お菓子は準備しますが、飲み物は持参してください。\n"
                "参加の連絡は不要ですが、質問がある方はメールをください。\n"
                "希望する方は、当日、年会費(2,000円)を払えば、会員になることができます。その場合、参加費は無料になります。\n"
                "東山大学 国際交流クラブ 代表：丸川良子 r_marukawa@higashiyamayuukibui.ac.jp"
            )
        },
        "jlpt_n3_2025_12_p11": {
            "passage_id": "jlpt_n3_2025_12_p11",
            "book_id": "jlpt_n3_2025_12",
            "unit": "短文 3",
            "page": 11,
            "pdf_page": 11,
            "mondai_number": 4,
            "title": "旅館からの空室確認メール",
            "author": "中雲山旅館 森田",
            "content": (
                "サンディ・シン様\n"
                "ご質問のメールをくださり、ありがとうございました。\n"
                "3月25日の「和室」のお部屋が空いているかというお尋ねでしたが、「和室」は全室予約が入っております。大変申し訳ございません。\n"
                "ただ、ベッド付きの「和洋室」のお部屋でしたら、ご予約になれます。ホームページで、お部屋の写真などもごらんになれますので、ぜひご検討ください。\n"
                "なお、桜の時期は、毎年たくさんのお客様がいらっしゃいます。ご予約になる場合は、お早めにお願いいたします。\n"
                "＜和洋室のお部屋の情報＞\n"
                "広さ：20m²＋6畳\n"
                "設備：ベッド2台、風呂、トイレ、冷蔵庫、テレビ\n"
                "2名様、夕朝食付き 料金合計 42,000円（税込み）\n"
                "中雲山旅館 森田\n"
                "ホームページ https://www.nakagumoyamaYuukiBui.co.jp\n"
                "電話 013-109-4475\n"
                "メールアドレス morita@nakagumoyamaYuukiBui.co.jp"
            )
        },
        "jlpt_n3_2025_12_p12_1": {
            "passage_id": "jlpt_n3_2025_12_p12_1",
            "book_id": "jlpt_n3_2025_12",
            "unit": "短文 4",
            "page": 12,
            "pdf_page": 12,
            "mondai_number": 4,
            "title": "東京の地下鉄と省エネルギーの工夫",
            "author": "交通コラム",
            "content": (
                "東京の地下鉄は、できるだけ、駅を地下の浅いところに作り、駅と駅の間は中心部分が深くなるように掘ってある。これは、少ないエネルギーで電車を走らせるための工夫だ。"
                "こうしておくと、電車は駅を出てすぐに、坂を下っていくことになるので、自然にスピードが出るし、次の駅に近づく(注)と、坂を上がっていくことになるので、止まりやすくなる。"
                "東京では、毎日数多くの電車が走るので、減らせるエネルギーの量はかなり大きい。\n"
                "(注) 次の駅に近づく：次の駅の近くに行く"
            )
        },
        "jlpt_n3_2025_12_p12_2": {
            "passage_id": "jlpt_n3_2025_12_p12_2",
            "book_id": "jlpt_n3_2025_12",
            "unit": "中文 1",
            "page": 12,
            "pdf_page": 12,
            "mondai_number": 5,
            "title": "スーパーでの買い物の価値",
            "author": "エッセイ",
            "content": (
                "スーパーは、多くの人にとって、必要な物を買うだけの場所かもしれません。週に2、3回、近所のスーパーに夫と行く私も、今までは①そう思っていました。でも、最近少し考えが変わりました。\n"
                "去年、一人暮らしをしている息子が、自分が使っているインターネットスーパーを紹介してくれました。インターネットで注文すると、当日か次の日までに品物が届きます。「簡単に注文できるし、出かけなくてもいいから、便利だよ。」と息子が言うので、使ってみました。確かに簡単で便利でしたが、1か月ぐらいで②やめてしまいました。\n"
                "それは、こんなことに気がついたからです。私は、夫と一緒にスーパーに行って、店に並んでいる野菜を手にとっておいしそうな物を選んだり、自分たちの目で見て新鮮な魚を見つけたりするのが、楽しかったのです。それがわかってから、スーパーでの時間は、私の大切な時間だと思うようになりました。"
            )
        },
        "jlpt_n3_2025_12_p13": {
            "passage_id": "jlpt_n3_2025_12_p13",
            "book_id": "jlpt_n3_2025_12",
            "unit": "中文 2",
            "page": 13,
            "pdf_page": 13,
            "mondai_number": 5,
            "title": "分散型ホテルの広がり",
            "author": "旅行経済コラム",
            "content": (
                "普通、「ホテル」と聞いたら、泊まる部屋や受付、食事会場などが一つの建物の中にあるものをイメージするだろう。実際、今まで日本では、そのようなホテルでないと営業できなかった。しかし、最近、法律が変わり、各部屋や受付などが別々の建物に分散して(注)いても、一つのホテルとして営業できるようになった。このようなホテルは「分散型ホテル」と呼ばれている。\n"
                "分散型ホテルは、歴史のある古い町に多い。そして、ホテルの部屋、受付、食事会場などに使われている建物の多くは、歴史的な価値がある古い家を直したものだ。\n"
                "それらは町のあちこちにあるので、ホテルに泊まる客は、人々が生活している町の中を、行ったり来たりすることになる。すると、町のあちこちの店を客が利用するようになるので、町の経済に良い影響が出る。客には不便なようにも思えるが、町の日常を見たり、その町らしい店を見つけたりしたい客にとっては、これが価値になるのだ。\n"
                "(注) 分散する：分かれる"
            )
        },
        "jlpt_n3_2025_12_p15": {
            "passage_id": "jlpt_n3_2025_12_p15",
            "book_id": "jlpt_n3_2025_12",
            "unit": "長文",
            "page": 15,
            "pdf_page": 15,
            "mondai_number": 6,
            "title": "娘のクラスでの絵本読み聞かせ",
            "author": "父親のエッセイ",
            "content": (
                "「来月の絵本の読み聞かせ活動、やってみない？」と妻が言った。小学校1年生の娘のクラスでは、毎月1回、生徒の親の一人が、自分で選んだ絵本を教室で子供たちに読んであげている。子供を本に慣れさせるための活動なのだが、参加できる親が少なくて先生が困っているそうだ。妻は、「あなたが行ったら、きっと京子は喜ぶよ。」と言った。私は、娘が喜ぶならと思って、やってみることにした。\n"
                "絵本は、私が子供のころに好きだった本を選んだ。とても面白い本だったから、今の子供たちも興味を持ってくれると思ったのだ。前の晩、妻と娘の前で読む練習をしてみた。読み始めると、娘が「パパ、違うよ。」と言った。学校の読み聞かせでは、絵が見えるように、本を子供たちに向けて読むそうだ。やってみたが、本の横から字を読まなければならないので、思ったより大変だった。①娘の前で練習してよかったと思った。\n"
                "当日、教室の外で待っていると、娘が呼びに来た。子供たちは教室の前の方に集まって座っていて、その前に置かれた小さないすに、娘が私を連れて行ってくれた。私は立って読んだほうが絵を見せやすいと思ったので、いすには座らなかった。練習のおかげで、絵本は問題なく読めた。それに、②予想が当たり、内容にも興味を持ってもらえたようだ。みんなが「面白かった。」などと言ってくれた。\n"
                "うちで娘に感想を聞いてみたが、自分が用意したいすに座らなかったのが不満だったそうだ。でも、「次は座ってね。」とも言っていた。「次は」と言うのだから、③娘はきっとうれしかったのだろうと思う。"
            )
        },
        "jlpt_n3_2025_12_p18": {
            "passage_id": "jlpt_n3_2025_12_p18",
            "book_id": "jlpt_n3_2025_12",
            "unit": "情報検索",
            "page": 18,
            "pdf_page": 18,
            "mondai_number": 7,
            "title": "鳥山図書館 図書館内の席の利用について",
            "author": "鳥山図書館",
            "content": (
                "鳥山図書館 図書館内の席の利用について\n"
                "鳥山図書館には4種類の席があります。目的に合わせてご利用ください。\n\n"
                "■ 席の種類について\n"
                "・読書席A（30席）：図書館の資料を読む席です。パソコンを使うことはできません。【利用の回数と時間の制限：制限なし】\n"
                "・読書席B（15席）：図書館の資料を読んだり、持ってきた資料を使って勉強したりする席です。自分のパソコンを持ってきて使うことができます。【利用の回数と時間の制限：1日1回、1時間30分まで】\n"
                "・学習席（15席）：学生や生徒の方が、図書館の資料を読んだり、持ってきた資料を使って勉強したりする席です。自分のパソコンを持ってきて使うことができます。【利用の回数と時間の制限：1日1回、3時間まで】\n"
                "・インターネット席（5席）：インターネットが利用できるパソコンが置いてある席です。図書館のパソコンを使って、情報を集めたい方が利用できます。【利用の回数と時間の制限：1日1回、1時間まで】\n\n"
                "■ 席の利用可能時間（図書館の開館・閉館時間と同じ）\n"
                "平日 9:00〜20:00 ／ 土日祝日 9:00〜18:00\n"
                "※読書席A以外は、利用の回数と時間の制限があります。上の表をご確認ください。\n\n"
                "■ 席の利用方法\n"
                "・読書席Aは申し込み不要です。空いている席をご利用ください。\n"
                "・読書席Bと学習席とインターネット席の利用には、申し込みが必要です。利用を希望する方は、図書館の貸し出しカードを受付にお持ちください。"
            )
        }
    }
    (out_dir / "passages.json").write_text(json.dumps(passages, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 1. VOCABULARY (35 questions)
    # -------------------------------------------------------------
    vocab = [
        # 問題1 (漢字読み 1〜8)
        {"id": "jlpt_n3_2025_12_v_q01", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "これは西洋の建物の写真です。", "options": ["せよう", "せいゆう", "せいよう", "せゆう"], "answer": 3, "explanation": "「西洋」は「せいよう」と読みます。", "grammar_points": ["漢字読み: 西洋 (せいよう)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q02", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今回はとても苦しい試合だった。", "options": ["おしい", "くるしい", "くやしい", "きびしい"], "answer": 2, "explanation": "「苦しい」は「くるしい」と読みます。", "grammar_points": ["漢字読み: 苦しい (くるしい)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q03", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この手紙は他人に見せないでください。", "options": ["たんじん", "たじん", "たんにん", "たにん"], "answer": 4, "explanation": "「他人」は「たにん」と読みます。", "grammar_points": ["漢字読み: 他人 (たにん)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q04", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日は腹痛で学校を休みました。", "options": ["ふくつう", "ふくつ", "ずつう", "ずつ"], "answer": 1, "explanation": "「腹痛」は「ふくつう」と読みます。", "grammar_points": ["漢字読み: 腹痛 (ふくつう)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q05", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "次の駅が終点です。", "options": ["しゅうでん", "しゅうてん", "じゅうてん", "じゅうでん"], "answer": 2, "explanation": "「終点」は「しゅうてん」と読みます。", "grammar_points": ["漢字読み: 終点 (しゅうてん)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q06", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "もう少しこちらでお待ちください。", "options": ["おうち", "おたち", "おまち", "おもち"], "answer": 3, "explanation": "「お待ち」は「おまち」と読みます。", "grammar_points": ["漢字読み: 待つ (まつ)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q07", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この着物の帯は美しいです。", "options": ["おび", "えり", "そで", "いと"], "answer": 1, "explanation": "「帯」は「おび」と読みます。", "grammar_points": ["漢字読み: 帯 (おび)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q08", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "＿＿のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日母から郵便が届いた。", "options": ["ようべん", "ようびん", "ゆうべん", "ゆうびん"], "answer": 4, "explanation": "「郵便」は「ゆうびん」と読みます。", "grammar_points": ["漢字読み: 郵便 (ゆうびん)"], "difficulty": 1, "needs_review": False},

        # 問題2 (表記 9〜14)
        {"id": "jlpt_n3_2025_12_v_q09", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "このあたりはマンションが多い", "options": ["通り", "辺り", "返り", "迎り"], "answer": 2, "explanation": "「あたり」の漢字表記は「辺り」です。", "grammar_points": ["漢字表記: 辺り (あたり)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q10", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "次のずを見てください。", "options": ["絵", "図", "表", "例"], "answer": 2, "explanation": "「ず」の漢字表記は「図」です。", "grammar_points": ["漢字表記: 図 (ず)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q11", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "貯金が少しへりました。", "options": ["細りました", "低りました", "消りました", "減りました"], "answer": 4, "explanation": "「へる」の漢字表記は「減る」です。", "grammar_points": ["漢字表記: 減る (へる)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q12", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "来年、ここにほどうができるそうだ。", "options": ["歩動", "走道", "歩道", "走動"], "answer": 3, "explanation": "「ほどう」の漢字表記は「歩道」です。", "grammar_points": ["漢字表記: 歩道 (ほどう)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q13", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "パソコンのキーボードをうつ音が聞こえる。", "options": ["打つ", "押つ", "指つ", "折つ"], "answer": 1, "explanation": "キーボードを「うつ」の漢字表記は「打つ」です。", "grammar_points": ["漢字表記: 打つ (うつ)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q14", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "＿＿のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "山田さんは、まじめなせいかくだ。", "options": ["姓格", "性各", "性格", "姓各"], "answer": 3, "explanation": "「せいかく」の漢字表記は「性格」です。", "grammar_points": ["漢字表記: 性格 (せいかく)"], "difficulty": 1, "needs_review": False},

        # 問題3 (文脈規定 15〜25)
        {"id": "jlpt_n3_2025_12_v_q15", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私の国と日本は（　）が12時間あるので、昼と夜が反対だ。", "options": ["時代", "時期", "時速", "時差"], "answer": 4, "explanation": "国と国の間の標準時の差は「時差（じさ）」です。", "grammar_points": ["文脈規定: 時差"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q16", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "自転車が壊れてしまい、（　）ので歩いて家に帰りました。", "options": ["くわしい", "だらしない", "しかたない", "うらやましい"], "answer": 3, "explanation": "他に方法や手段がない状況を表す「仕方ない（しかたない）」が適切です。", "grammar_points": ["イ形容詞的連語: 仕方ない"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q17", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "病気の人を治したくて、高校生のときに医者になることを（　）した。", "options": ["予想", "決心", "証明", "仮定"], "answer": 2, "explanation": "将来の目標に向けて自分の意志を固めることは「決心（けっしん）する」と言います。", "grammar_points": ["名詞・スル動詞: 決心"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q18", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "彼は、いつも（　）を言って、みんなを笑わせる面白い人だ。", "options": ["感想", "文句", "冗談", "自慢"], "answer": 3, "explanation": "人を笑わせるためのふざけた言葉やユーモアは「冗談（じょうだん）」です。「冗談を言う」で用います。", "grammar_points": ["名詞: 冗談"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q19", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "ホテルに到着したが、まだ部屋に入れなかったので、受付に荷物を（　）出かけた。", "options": ["預けて", "泊めて", "配って", "与えて"], "answer": 1, "explanation": "品物や荷物を他人に頼んで保管してもらうことは「預ける（あずける）」と言います。", "grammar_points": ["動詞: 預ける (あずける)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q20", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "空港に着いたとき、飛行機の出発が遅れるという（　）が聞こえた。", "options": ["ガイダンス", "アナウンス", "コマーシャル", "スピーチ"], "answer": 2, "explanation": "公共の場や空港などの館内放送による連絡案内は「アナウンス（announcement）」です。", "grammar_points": ["外来語: アナウンス"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q21", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "休日で渋滞すると思いましたが、（　）道はすいていました。", "options": ["突然", "当然", "年中", "案外"], "answer": 4, "explanation": "予想や期待に反して事態が意外な結果になることを表す副詞は「案外（あんがい）」です。", "grammar_points": ["副詞: 案外 (予想に反して)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q22", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "彼は若いとき非常に苦労したが、一生懸命（　）して、立派な政治家になった。", "options": ["努力", "納得", "期待", "注意"], "answer": 1, "explanation": "目標に向かって力を尽くして励むことは「努力（どりょく）」です。", "grammar_points": ["名詞・スル動詞: 努力"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q23", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "時間がなくて、朝も昼もご飯を食べられなかったので、おなかが（　）だ。", "options": ["ぺらぺら", "からから", "ぺこぺこ", "どきどき"], "answer": 3, "explanation": "空腹で激しくお腹が空いている状態を表すオノマトペは「ぺこぺこ」です。", "grammar_points": ["オノマトペ: おなかがぺこぺこ"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q24", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "林さんが会社を辞めるというのは、林さんから直接聞いたので（　）情報です。", "options": ["満足な", "正常な", "完全な", "確実な"], "answer": 4, "explanation": "本人から直接確認した間違いのない確かな情報は「確実な（かくじつな）」情報です。", "grammar_points": ["ナ形容詞: 確実だ"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q25", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "電気の工事の人が来て、部屋の壁にエアコンを（　）くれた。", "options": ["取り付けて", "取り上げて", "受け入れて", "引き受けて"], "answer": 1, "explanation": "器具や装置をしかるべき場所に据え付けることは「取り付ける」と言います。", "grammar_points": ["複合動詞: 取り付ける"], "difficulty": 2, "needs_review": False},

        # 問題4 (言い換え類義 26〜30)
        {"id": "jlpt_n3_2025_12_v_q26", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "清潔なタオルで拭いてください。", "options": ["柔らかい", "ぬれた", "乾いた", "きれいな"], "answer": 4, "explanation": "「清潔な（せいけつな）」は汚れがなく衛生的で「きれいな」と同義です。", "grammar_points": ["類義語: 清潔な ＝ きれいな"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q27", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "さっきご飯を食べました。", "options": ["急いで", "少し遅れて", "少し前に", "ゆっくり"], "answer": 3, "explanation": "「さっき」は現在から少し前の時間を指すので「少し前に」と同義です。", "grammar_points": ["副詞・類義語: さっき ＝ 少し前に"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q28", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "これはキッチンに置いてください。", "options": ["居間", "台所", "廊下", "風呂"], "answer": 2, "explanation": "外来語「キッチン（kitchen）」は和語の「台所（だいどころ）」と同義です。", "grammar_points": ["類義語: キッチン ＝ 台所"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q29", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今、野口さんが指導しています。", "options": ["調べて", "答えて", "聞いて", "教えて"], "answer": 4, "explanation": "「指導する（しどうする）」は教え導くことなので「教えて」と同義です。", "grammar_points": ["類義語: 指導する ＝ 教える"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q30", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "＿＿に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "そろそろお休みにしましょう。", "options": ["休みましょう", "食事にしましょう", "終わりにしましょう", "寝ましょう"], "answer": 3, "explanation": "作業や会議などの場面で「そろそろお休みにしましょう」と言う場合、その日の活動を「終わりにしましょう（切り上げましょう）」という意味で使われます。", "grammar_points": ["慣用表現・類義語: お休みにする ＝ 終わりにする"], "difficulty": 2, "needs_review": False},

        # 問題5 (用法 31〜35)
        {"id": "jlpt_n3_2025_12_v_q31", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "にぎる", "options": [
            "昨日の引っ越しで何度も重い家具をにぎったので体が痛い。",
            "お祭りで弟が迷子にならないように、弟の手をしっかりとにぎった。",
            "風で帽子が飛ばされたが、石原さんが走ってにぎってくれた。",
            "母親が、生まれたばかりの赤ちゃんを大事そうににぎっている。"
        ], "answer": 2, "explanation": "「にぎる（握る）」は手や指で包むように強く持つ動作を表します。「手をしっかりとにぎる」が最も自然です。重い家具は「運んだ/持ち上げた」、帽子は「つかまえて/拾って」、赤ちゃんは「抱いて（だいて）」を用います。", "grammar_points": ["動詞の用法: 握る (手をとる・つかむ)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q32", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "修理", "options": [
            "今朝、妻とけんかしたので、早く仲を修理したい。",
            "腕をけがしたとき、この病院で修理してもらった。",
            "自転車が壊れたので、買ったお店で修理してもらった。",
            "私が間違えた漢字を、先生が赤いペンで修理してくれた。"
        ], "answer": 3, "explanation": "「修理（しゅうり）」は壊れた機械や道具・車両などを直して再び使えるようにすることです。「自転車を修理してもらう」が正しい用法です。人間関係は「仲直り」、けがは「治療/手当て」、文字の間違いは「訂正/直して」を用います。", "grammar_points": ["語の用法: 修理 (機械・道具の修繕)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q33", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "目的", "options": [
            "今日はたくさん商品が売れて、目的の10万円を超えました。",
            "お店を予約するとき、窓側の席がいいと目的を伝えた。",
            "来週から1か月海外に出張する目的なので、準備に忙しい。",
            "この研究の目的は、新しい薬の効果を調べることです。"
        ], "answer": 4, "explanation": "「目的（もくてき）」は目指す事柄や行動の意図を表し、「〜の目的は〜することだ」という文型で用います。1は「目標の（金額）」、2は「希望/要望」、3は「予定なので」が適切です。", "grammar_points": ["語の用法: 目的 (研究・行動の目指す的)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q34", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "懐かしい", "options": [
            "子どものときの写真を見て、懐かしい気持ちになった。",
            "ここは800年前に建てられた懐かしい寺なので、見学の人が多い。",
            "結婚して30年たったので、妻とは懐かしい関係だ。",
            "私と田村さんは、会ってすぐに懐かしい友達になった。"
        ], "answer": 1, "explanation": "「懐かしい（なつかしい）」は過去の出来事や人を思い出して心が温かく慕わしくなる感情を表します。「子どものときの写真を見て懐かしい気持ちになる」が適切です。2は「歴史ある」、3は「親密な/深い」、4は「親しい」を用います。", "grammar_points": ["イ形容詞: 懐かしい (過去を追想する感情)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_v_q35", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文字・語彙）", "page": 5, "pdf_page": 5, "section": "言語知識（文字・語彙）", "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "変化", "options": [
            "友達の都合が悪くなって、食事の約束が来週に変化してしまった。",
            "引っ越して住所が変化したので、みんなに知らせた。",
            "インターネットが登場して、人々の生活は大きく変化した。",
            "会議の司会は、水野さんから高橋さんに変化するそうだ。"
        ], "answer": 3, "explanation": "「変化（へんか）」はある状態から別の状態へ大きく変わる現象全般を表し、「生活が大きく変化した」が最適です。1は「変更になって」、2は「変わったので」、4は「交代する/変わる」を用います。", "grammar_points": ["名詞・スル動詞: 変化 (状態・情勢の推移)"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "vocab.json").write_text(json.dumps({"questions": vocab}, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 2. GRAMMAR (22 questions)
    # -------------------------------------------------------------
    grammar = [
        # 問題1 (文法形式の判断 1〜13)
        {"id": "jlpt_n3_2025_12_g_q01", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "友人の田中さんは京都が大好きで、今までに何度（　）行ったことがあるそうだ。", "options": ["も", "は", "など", "ぐらい"], "answer": 1, "explanation": "回数・数量を表す語に「も」を後接させて、回数が極めて多いことを強調する「何度（も）」が適切です。", "grammar_points": ["助詞: も (数量・回数の多さの強調)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q02", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "A「ねぇ、お昼ご飯、一緒に行かない？」\nB「うん、行こう。何食べる？」\nA「寒いから、温かいうどん（　）どう？」", "options": ["に", "だけ", "まで", "なんか"], "answer": 4, "explanation": "一つの例を控えめに提案する口語表現「〜なんか（どう？）」が最も自然です。", "grammar_points": ["とりたて助詞: なんか (控えめな例示・提案)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q03", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私は両親の誕生日にいつも手紙を書く。手紙（　）、普段は恥ずかしくてなかなか言えない感謝の気持ちを伝えられるからだ。", "options": ["でなら", "になら", "でしか", "にしか"], "answer": 1, "explanation": "手紙という手段・方法を取り上げて「その方法であれば実現できる」という条件を示す「手段＋でなら」が適切です。", "grammar_points": ["助詞の複合: でなら (手段の仮定限定)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q04", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "いつもは雨でも自転車で大学に行くが、今朝は（　）雨が強かったので、バスで行った。", "options": ["ちっとも", "あまりに", "次第に", "今にも"], "answer": 2, "explanation": "程度が度を越して甚だしいことを表し原因・理由につながる副詞「あまりに（雨が強かったので）」が正解です。", "grammar_points": ["副詞: あまりに (過度の程度)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q05", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "先週、登山をした。暑い日だったが、登っていく（　）風が冷たくなって、とても気持ちがよかった。", "options": ["とすると", "のと比べると", "にしたがって", "に対して"], "answer": 3, "explanation": "一方の変化（登っていく）と並行して他方の変化（風が冷たくなる）が進む比例関係を表す「動詞辞書形＋にしたがって」が適切です。", "grammar_points": ["〜にしたがって (並行変化・比例)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q06", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（姉の部屋で）\n妹「お姉ちゃん、この漫画、もう読んで？借りてもいい？」\n姉「あ、それ、まだ途中なんだ。（　）、貸してあげるね。」", "options": ["読んでいたら", "読み続けたら", "読んでおいたら", "読み終わったら"], "answer": 4, "explanation": "現在途中まで読んでいる行為が完全に完了した時点で相手に貸すという条件を示す「読み終わったら」が正解です。", "grammar_points": ["複合動詞: 〜終わる ＋ たら"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q07", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "来月、留学生の友達が日本での留学生活を終えて国に帰る。友達が国に（　）、いろいろなことを一緒にしたい。", "options": ["帰っていて", "帰ってしまえば", "帰っている間", "帰ってしまう前に"], "answer": 4, "explanation": "完全に帰国して取り返しがつかなくなる前という時間の限界を表す「〜てしまう前に」が正解です。", "grammar_points": ["〜てしまう前に (完了・不可逆的事態の前の時間枠)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q08", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この寺は、県内で最も古い寺で、（　）今から1000年以上前だそうだ。", "options": ["建てられてからは", "建てられたのは", "建てさせるまでは", "建てさせたときは"], "answer": 2, "explanation": "主語を取り立てて時を説明する分裂文表現「〜のは（今から1000年以上前だ）」が適切です。寺は受動態「建てられた」になります。", "grammar_points": ["分裂文構文: 〜受身＋のは〜だ"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q09", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "兄「駅前にドーナツ屋ができたらしいね。知ってる？」\n弟「うん。人気がある（　）よ。昨日店の前を通ったけど、たくさんの人が並んでたよ。」", "options": ["ことだ", "せいだ", "みたいだ", "つもりだ"], "answer": 3, "explanation": "「たくさんの人が並んでいた」という直前の観察証拠に基づき推量・判断する比況・推定の「〜みたいだ」が適切です。", "grammar_points": ["推量表現: 〜みたいだ"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q10", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（会社で）\n森「すみません、大下さん。この近くで、いい眼科を知っていたら（　）。朝から目がかゆくて。」\n大下「え、大丈夫ですか。駅前のABC眼科はよかったですよ。」", "options": ["教えたんですが", "教えてもいいですか", "教えてもらうんですか", "教えてほしいんですが"], "answer": 4, "explanation": "相手に対して情報を教えてもらうことを丁寧に希望・依頼する前置き表現「〜てほしいんですが」が最適です。", "grammar_points": ["依頼・希望表現: 〜てほしいんですが"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q11", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "林さんは、会議で資料のグラフについて質問されたときに、わからないと言っていたが、林さんが作ったグラフなのだから、（　）と思う。", "options": ["わからないに違いない", "わからないはずがない", "わからないかもしれない", "わからなくてもかまわない"], "answer": 2, "explanation": "「林さんが自分で作った」という強い根拠があるため、わからないということはあり得ないという強い確信・否定「〜ないはずがない」が適切です。", "grammar_points": ["二重否定・確信: 〜ないはずがない"], "difficulty": 3, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q12", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "父は、出張に行くと、母と私に必ずお土産を（　）。", "options": ["買ってきてあげる", "買っていってあげる", "買ってきてくれる", "買っていってくれる"], "answer": 3, "explanation": "父が出先から母と私（話し手側の身内）に対して品物を買って戻ってくる行為なので、「買ってきてくれる」が正解です。", "grammar_points": ["授受動詞・移動: 〜てきてくれる"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q13", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（　）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "風邪をひいて、今日は授業を休んでしまったが、一日家で寝ていたら、かなりよくなってきた。明日は授業に（　）。", "options": ["出られそうだ", "出られるそうだ", "出そうだ", "出るそうだ"], "answer": 1, "explanation": "現在の回復具合を見て、明日は出席することができそうだという話者の主観的・見込みの様態推量「可能動詞連用形＋そうだ（出られそうだ）」が適切です。", "grammar_points": ["様態の助動詞: 可能動詞 ＋ そうだ"], "difficulty": 2, "needs_review": False},

        # 問題2 (文の組み立て 14〜18)
        {"id": "jlpt_n3_2025_12_g_q14", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日、本屋で小説2冊 ＿＿ ＿＿ ★ ＿＿ 本を1冊買った。", "options": ["と", "の", "について", "レポートの書き方"], "answer": 3, "explanation": "正しい語順は「と(1) → レポートの書き方(4) → について(3) → の(2)」となります。★に入るのは 3（について）です。", "grammar_points": ["文の組み立て: 〜についての＋名詞"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q15", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "（道で）\nA「あの喫茶店、＿＿ ＿＿ ★ ＿＿ があるよ。入ってみない？」\nB「いいね。」", "options": ["で", "か何か", "テレビ", "見たこと"], "answer": 1, "explanation": "正しい語順は「テレビ(3) → か何か(2) → で(1) → 見たこと(4) があるよ」となります。★に入るのは 1（で）です。", "grammar_points": ["文の組み立て: 不特定の例示「〜か何か」＋場所・媒体「で」＋経験「見たことがある」"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q16", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "半年前からギターを習い始めてから、毎日練習している。弾けば ＿＿ ＿＿ ★ ＿＿ 自分でもわかり、とても楽しい。", "options": ["上手に", "弾くほど", "なっていくのが", "弾けるように"], "answer": 4, "explanation": "正しい語順は「弾くほど(2) → 上手に(1) → 弾けるように(4) → なっていくのが(3)」となります。★に入るのは 4（弾けるように）です。", "grammar_points": ["文の組み立て: 〜ば〜ほど (比例相関) ＋ 〜ようになる"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q17", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "今の会社に就職したときに、北町で一人暮らしを始めた。会社から遠い ＿＿ ＿＿ ★ ＿＿ からだ。", "options": ["北町を選んだ", "のは", "ずっと北町に住んでみたかった", "のに"], "answer": 2, "explanation": "正しい語順は「のに(4) → 北町を選んだ(1) → のは(2) → ずっと北町に住んでみたかった(3) からだ」となります。★に入るのは 2（のは）です。", "grammar_points": ["文の組み立て: 逆接「〜のに」＋ 分裂文「〜のは〜からだ」"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q18", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "つぎの文の ★ に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "お風呂は家の中でも特にかびが生えやすい場所だ。かびを防ぐ ＿＿ ＿＿ ★ ＿＿ 重要らしい。", "options": ["ことが", "使った後", "ぬれたままにしない", "ためには"], "answer": 3, "explanation": "正しい語順は「ためには(4) → 使った後(2) → ぬれたままにしない(3) → ことが(1) 重要らしい」となります。★に入るのは 3（ぬれたままにしない）です。", "grammar_points": ["文の組み立て: 目的「〜ためには」＋ 状態継続「〜ままにしない」＋ 主語化「〜ことが重要だ」"], "difficulty": 2, "needs_review": False},

        # 問題3 (文章の文法 19〜22)
        {"id": "jlpt_n3_2025_12_g_q19", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p08", "question": "（19）に入る最もよいものをえらびなさい。", "options": ["思います", "思ってしまいます", "思っていたからです", "思ったことです"], "answer": 3, "explanation": "直前の「会社の違いはあまり気にしていませんでした」という理由を述べる文末表現「〜思っていたからです」が最も自然につながります。", "grammar_points": ["文章の文法: 理由説明の文末 (〜からだ)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q20", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 8, "pdf_page": 8, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p08", "question": "（20）に入る最もよいものをえらびなさい。", "options": ["つまり", "ところで", "ちなみに", "でも"], "answer": 4, "explanation": "一般的な品揃えは共通しているという事実から、会社ごとの独自商品の存在へと対比・転換する逆接の接続詞「でも」が適切です。", "grammar_points": ["文章の文法: 逆接接続詞 (でも)"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q21", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p08", "question": "（21）に入る最もよいものをえらびなさい。", "options": ["どの", "その", "この", "あの"], "answer": 1, "explanation": "特定の1社ではなく、各コンビニ会社「どの会社も（＝いずれの会社も）」努力しているという意味で全般を取り立てる「どの」が適切です。", "grammar_points": ["文章の文法: 疑問詞＋も (全面肯定・全般化)"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_g_q22", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "言語知識（文法）", "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、（19）から（22）の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p08", "question": "（22）に入る最もよいものをえらびなさい。", "options": ["場所にしたのです", "場所なのです", "場所にするのでしょう", "場所なのでしょうか"], "answer": 2, "explanation": "文章全体の結論として、自分にとってコンビニとはどういう場所であるかを読者に説明・断定する「〜場所なのです」が最適です。", "grammar_points": ["文章の文法: 説明の終結表現 (〜のです)"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "grammar.json").write_text(json.dumps({"questions": grammar}, ensure_ascii=False, indent=2), encoding="utf-8")

    # -------------------------------------------------------------
    # 3. READING (16 questions)
    # -------------------------------------------------------------
    reading = [
        # 問題4 (短文 23〜26)
        {"id": "jlpt_n3_2025_12_r_q23", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "短文 1", "page": 10, "pdf_page": 10, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p09", "question": "やってみようと思ったとあるが、何をしようと思ったのか。", "options": [
            "だしを使わないで料理すること。",
            "野菜の皮からだしを取ること。",
            "30分ぐらい煮てから野菜の皮をむくこと。",
            "皮をむいていない野菜でスープを作ること。"
        ], "answer": 2, "explanation": "友人が「カレーに使った野菜の皮を煮て、だしを取って作ったんだ」と教えてくれたことを受け、「今まで捨てていたが、今度、私もやってみようと思った」と述べているため、野菜の皮からだしを取ることです。", "grammar_points": ["読解（短文）: 指示内容の把握"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q24", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "短文 2", "page": 10, "pdf_page": 10, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p10", "question": "ピクニックに参加するときに会員になろうと思っている人は、どうしなければならないか。", "options": [
            "メールで参加の連絡をして、当日、年会費と飲み物を持っていく。",
            "当日、年会費とお菓子と飲み物を持っていく。",
            "当日、年会費と参加費と飲み物を持っていく。",
            "当日、年会費と飲み物を持っていく。"
        ], "answer": 4, "explanation": "「参加の連絡は不要」「当日、年会費(2,000円)を払えば会員になれ、その場合参加費は無料」「お菓子は準備するが飲み物は持参」とあるため、当日に年会費と飲み物を持っていけばよいです。", "grammar_points": ["読解（短文）: 条件・持参物の照合"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q25", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "短文 3", "page": 11, "pdf_page": 11, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p11", "question": "旅館の人が、このメールで伝えたいことはどれか。", "options": [
            "3月25日の「和室」は空いているが、「和洋室」も検討してほしい。",
            "3月25日の「和室」は予約できないので、「和洋室」を検討してほしい。",
            "3月25日はどの部屋も予約できないので、別の日を検討してほしい。",
            "「和室」は人気があって予約が取りにくいので、早めに予約してほしい。"
        ], "answer": 2, "explanation": "「『和室』は全室予約が入っております。ただ、ベッド付きの『和洋室』のお部屋でしたら、ご予約になれます。ぜひご検討ください」と代替の部屋を提案しています。", "grammar_points": ["読解（短文）: ビジネスメールの主旨把握"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q26", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "短文 4", "page": 12, "pdf_page": 12, "section": "読解", "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（1）から（4）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p12_1", "question": "この文章では、東京の地下鉄はどのような工夫をしていると言っているか。", "options": [
            "駅と駅の間に坂を作り、電車が使用するエネルギーが少なくなるようにしてある。",
            "少ないエネルギーで坂を走れる電車を使用するようにしている。",
            "坂を減らして、少ないエネルギーで電車のスピードが出せるようにしてある。",
            "走る電車の数をできるだけ少なくして、使用するエネルギーを減らしている。"
        ], "answer": 1, "explanation": "「駅を地下の浅いところに作り、駅と駅の間は中心部分が深くなるように掘ってある。これは、少ないエネルギーで電車を走らせるための工夫だ」と明記されています。", "grammar_points": ["読解（短文）: 説明文の要旨把握"], "difficulty": 2, "needs_review": False},

        # 問題5 (中文 27〜32)
        {"id": "jlpt_n3_2025_12_r_q27", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 1", "page": 13, "pdf_page": 13, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p12_2", "question": "①そう思っていましたとあるが、どう思っていたのか。", "options": [
            "スーパーは、必要な物を買うだけの場所だ。",
            "多くの人にとって必要な物を売っている場所が、スーパーだ。",
            "多くの人が買い物できるスーパーが、近所にもっと必要だ。",
            "近所のスーパーは、週に2、3回行く場所だ。"
        ], "answer": 1, "explanation": "直前の第1文に「スーパーは、多くの人にとって、必要な物を買うだけの場所かもしれません」とあり、それに同意して「私も、今まではそう思っていました」と述べています。", "grammar_points": ["読解（中文）: 指示語の指す内容"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q28", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 1", "page": 13, "pdf_page": 13, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p12_2", "question": "②やめてしまいましたとあるが、何をやめたのか。", "options": [
            "夫と二人で近所のスーパーに行くこと。",
            "息子にインターネットスーパーで買い物をしてもらうこと。",
            "インターネットスーパーの使い方を息子に教えてもらうこと。",
            "息子が紹介してくれたインターネットスーパーを利用すること。"
        ], "answer": 4, "explanation": "息子に勧められて1か月使ってみた「インターネットスーパー」の利用をやめたことが直前の文脈から明確です。", "grammar_points": ["読解（中文）: 行動の文脈把握"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q29", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 1", "page": 13, "pdf_page": 13, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p12_2", "question": "「私」は今、どんなことを大切だと思っているか。", "options": [
            "夫と息子と一緒に、家族みんなで近所のスーパーで買い物をすること。",
            "夫と相談しながら、インターネットスーパーで買いたい物を選ぶこと。",
            "近所のスーパーで、夫と一緒に実物を見て、品物を選んだり探したりすること。",
            "おいしそうな品物や新鮮な品物がたくさんあるスーパーを、夫と探すこと。"
        ], "answer": 3, "explanation": "本文末尾に「夫と一緒にスーパーに行って、店に並んでいる野菜を手にとっておいしそうな物を選んだり、自分たちの目で見て新鮮な魚を見つけたりするのが、楽しかった」「スーパーでの時間は、私の大切な時間だと思うようになりました」とあります。", "grammar_points": ["読解（中文）: 心情・価値観の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q30", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 2", "page": 14, "pdf_page": 14, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p13", "question": "この文章によると、最近、日本で営業できるようになったのは、どのようなホテルか。", "options": [
            "泊まる部屋と受付はあるが、食事会場がないホテル。",
            "泊まる部屋だけがあって、受付や食事会場がないホテル。",
            "泊まる部屋や受付、食事会場などが、同じ建物の中にあるホテル。",
            "泊まる部屋や受付、食事会場などが、それぞれ違う建物にあるホテル。"
        ], "answer": 4, "explanation": "「各部屋や受付などが別々の建物に分散していても、一つのホテルとして営業できるようになった。このようなホテルは『分散型ホテル』と呼ばれている」とあります。", "grammar_points": ["読解（中文）: 定義の正確な把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q31", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 2", "page": 14, "pdf_page": 14, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p13", "question": "分散型ホテルは、どのような客に合っているか。", "options": [
            "泊まる部屋、受付、食事会場などの間の移動を、なるべく少なくしたい客。",
            "歴史のある町に興味があるが、泊まるのは最近建てられた建物がいいと思う客。",
            "歴史のある町を歩き回ったり、ふだんの町のようすを見たりしたい客。",
            "ホテルに泊まっているほかの客たちとの交流を大切にしたい客。"
        ], "answer": 3, "explanation": "本文に「町の日常を見たり、その町らしい店を見つけたりしたい客にとっては、これが価値になるのだ」と書かれています。", "grammar_points": ["読解（中文）: ターゲット層・利用価値の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q32", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "中文 2", "page": 15, "pdf_page": 15, "section": "読解", "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（1）と（2）の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p13", "question": "この文章全体のテーマは何か。", "options": [
            "歴史のあるホテルとその価値。",
            "新しいタイプのホテルとその良さ。",
            "日本のホテルに泊まる客の行動の変化。",
            "新しく建てられたホテルが町の経済に与える影響。"
        ], "answer": 2, "explanation": "文章全体を通して、法律改正により可能となった「分散型ホテル」という新しい宿泊形態の仕組みとそのメリット（良さ）を解説しています。", "grammar_points": ["読解（中文）: 全体主旨・テーマの把握"], "difficulty": 2, "needs_review": False},

        # 問題6 (長文 33〜36)
        {"id": "jlpt_n3_2025_12_r_q33", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p15", "question": "「私」は、なぜ絵本の読み聞かせ活動に参加することにしたのか。", "options": [
            "いい絵本が見つけられなくて困っている先生を助けたかったから。",
            "絵本を読むことになって困っている妻を助けたかったから。",
            "「私」が絵本を読んだら娘が喜ぶと、妻が言ったから。",
            "子供たちに絵本の良さを伝えたかったから。"
        ], "answer": 3, "explanation": "本文に「妻は、『あなたが行ったら、きっと京子は喜ぶよ。』と言った。私は、娘が喜ぶならと思って、やってみることにした」とあります。", "grammar_points": ["読解（長文）: 参加動機の把握"], "difficulty": 1, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q34", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p15", "question": "①娘の前で練習してよかったと思ったとあるが、なぜか。", "options": [
            "娘が絵本の内容に興味を持ってくれたから。",
            "違う絵本のほうがいいと娘が言ってくれたから。",
            "学校での読み聞かせのやり方を知ることができたから。",
            "本の横からでも字がうまく読める方法を娘が教えてくれたから。"
        ], "answer": 3, "explanation": "娘から「学校の読み聞かせでは、絵が見えるように、本を子供たちに向けて読む」と実際のルールややり方を教えてもらい、事前に横から読む難しさを把握できたからです。", "grammar_points": ["読解（長文）: 理由の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q35", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "長文", "page": 16, "pdf_page": 16, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p15", "question": "②予想とあるが、どのような予想か。", "options": [
            "先生が選んでくれた絵本なので、子供たちは興味を持つだろう。",
            "生徒の親たちが選んだ絵本なので、子供たちも好きになるだろう。",
            "今の子供たちに人気がある絵本なので、子供たちはとても喜ぶだろう。",
            "自分が昔読んでとても面白かった絵本なので、今の子供たちも興味を持つだろう。"
        ], "answer": 4, "explanation": "第2段落に「私が子供のころに好きだった本を選んだ。とても面白い本だったから、今の子供たちも興味を持ってくれると思ったのだ」とあり、その予想が当たったと述べています。", "grammar_points": ["読解（長文）: 照応関係の把握"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q36", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "長文", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p15", "question": "③娘はきっとうれしかったのだろうとあるが、「私」はなぜそう思ったのか。", "options": [
            "娘が「面白かった。」と言ってくれたから。",
            "娘が、ほかの子供たちの感想をうれしそうに伝えてくれたから。",
            "娘が、いすを用意して「私」を歓迎していたとわかったから。",
            "娘の言葉から、また読み聞かせに来てほしいという気持ちを感じたから。"
        ], "answer": 4, "explanation": "末尾に「『次は座ってね。』とも言っていた。『次は』と言うのだから、娘はきっとうれしかったのだろうと思う」とあり、次回の参加を前提にした娘の言葉から再訪を望む気持ちを感じ取ったためです。", "grammar_points": ["読解（長文）: 心理・推論の把握"], "difficulty": 2, "needs_review": False},

        # 問題7 (情報検索 37〜38)
        {"id": "jlpt_n3_2025_12_r_q37", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "情報検索", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、ある図書館のホームページに書かれた、席の利用案内である。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p18", "question": "会社員の森山さんは、水曜日か土曜日の17時以降に、鳥山図書館にある資料を読みに行こうと思っている。同じ席を2時間利用したいが、何曜日に、どの席を利用すればいいか。", "options": [
            "水曜日に、読書席Aを利用する。",
            "水曜日に、読書席Aか読書席Bを利用する。",
            "土曜日に、読書席Aを利用する。",
            "土曜日に、読書席Aか読書席Bを利用する。"
        ], "answer": 1, "explanation": "閉館時間を確認すると、平日は20:00まで、土日祝日は18:00までです。17時以降に2時間利用するには平日（水曜日）でなければならず（土曜日は1時間しか利用できない）、読書席Bは制限時間1時間30分までのため、時間制限のない読書席Aを利用する必要があります。したがって「水曜日に、読書席Aを利用する」が正解です。", "grammar_points": ["情報検索: 開館時間・制限時間の照合"], "difficulty": 2, "needs_review": False},
        {"id": "jlpt_n3_2025_12_r_q38", "book": "JLPT N3 2025年12月 実戦問題集", "book_code": "jlpt_n3_2025_12", "unit": "情報検索", "page": 17, "pdf_page": 17, "section": "読解", "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、ある図書館のホームページに書かれた、席の利用案内である。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2025_12_p18", "question": "高校生のクレアさんは、鳥山図書館で、平日の15時ごろから1時間勉強をしたいと思っている。勉強には自分のパソコンを使いたい。クレアさんはどうすればいいか。", "options": [
            "貸し出しカードを持って受付に行き、読書席Bか学習席の申し込みをする。",
            "貸し出しカードを持って受付に行き、学習席かインターネット席の申し込みをする。",
            "読書席Bか学習席を利用する。申し込みは必要ない。",
            "学習席かインターネット席を利用する。申し込みは必要ない。"
        ], "answer": 1, "explanation": "高校生が自分のパソコンを持ち込んで勉強できる席は「読書席B」または「学習席」です。そして「読書席Bと学習席とインターネット席の利用には、申し込みが必要です。利用を希望する方は、図書館の貸し出しカードを受付にお持ちください」とあるため、1が正解です。", "grammar_points": ["情報検索: 利用条件・持参機器・手続方法の複合照合"], "difficulty": 2, "needs_review": False}
    ]
    (out_dir / "reading.json").write_text(json.dumps({"questions": reading}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Extraction for 2025-12 practice exam completed:")
    print(f"  Vocab: {len(vocab)} Qs")
    print(f"  Grammar: {len(grammar)} Qs")
    print(f"  Reading: {len(reading)} Qs")
    print(f"  Passages: {len(passages)} passages")
    print(f"  Total: {len(vocab) + len(grammar) + len(reading)} Qs")

if __name__ == "__main__":
    build_2025_12()
