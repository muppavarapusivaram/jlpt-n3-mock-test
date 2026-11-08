# -*- coding: utf-8 -*-
"""
build_2024_07.py
Generates the complete, authentic JLPT N3 2024 July question bank:
- vocab.json (35 questions)
- grammar.json (22 questions)
- reading.json (16 questions)
- passages.json (9 passages)
"""

import json
from pathlib import Path

OUT_DIR = Path("bank/jlpt_n3_2024_07")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. Passages
# -------------------------------------------------------------
passages = {
    "jlpt_n3_2024_07_p08": {
        "passage_id": "jlpt_n3_2024_07_p08",
        "book_id": "jlpt_n3_2024_07",
        "unit": "文法",
        "page": 8,
        "pdf_page": 8,
        "mondai_number": 3,
        "title": "私の友達",
        "author": "ミラー ジョナサン",
        "content": "私は近所の小さい喫茶店によく行きます。店長は林さんという70歳の男性です。林さんは私より50歳も年上ですが、私たちは友達です。\n　そのお店には半年ぐらい前から行くようになりました。私が行くと、林さんはいつも [ 19 ] 。それで、私たちはだんだん仲がよくなりました。\n　ほかのお客さんがいないとき、私たちはおしゃべりをしています。林さんはコーヒーの種類について詳しくて、私はコーヒーのことがよくわかるようになりました。ときどき、林さんに日本の生活で困っていることを相談することもあります。林さんはいつもいいアドバイスをくれます。 [ 20 ] 私たちは二人とも映画が好きなので、映画の話もよくします。この間は、一緒に映画を見に行きました。\n　日本で林さん [ 21 ] 友達ができることは予想していませんでした。こんなに年上の友達ができたのは初めてでしたが、年齢の差は重要ではないことがわかりました。日本で林さんに [ 22 ] よかったです。"
    },
    "jlpt_n3_2024_07_p10": {
        "passage_id": "jlpt_n3_2024_07_p10",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 10,
        "pdf_page": 10,
        "mondai_number": 4,
        "title": "部長会議の延期連絡メール",
        "author": "野村マリア",
        "content": "これは、野村さんが部長会議の出席予定者に書いたメールである。\n\n部長会議にご出席予定の皆様\nあさって12日(金)の部長会議について、ご連絡します。\n天気予報では、明日の夜、台風が東京の近くを通ることが予想されています。そのため、あさってまで交通機関に影響が残る可能性があります。明日の予報で台風が東京を通ることが確実になった場合は、来週に会議を延期することにします。最終的なご連絡は、明日11日(木)の15時にメールでいたします。\n以上、よろしくお願いします。\n第一営業部\n野村マリア"
    },
    "jlpt_n3_2024_07_p11": {
        "passage_id": "jlpt_n3_2024_07_p11",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 11,
        "pdf_page": 11,
        "mondai_number": 4,
        "title": "Eスポーツ大会",
        "author": None,
        "content": "高校生の孫が「来週、Eスポーツ大会に出るんだ」と言った。コンピューターゲームの大会だと説明され、私は不思議な気がした。なぜ、それがスポーツの大会なのだろうか。\n　聞いてみると、英語の「スポーツ」には、ルールを守りながら勝ったり負けたりすることを楽しむものという意味があるそうだ。それで、最近ではコンピューターゲームもスポーツと言うらしい。\n　体を動かすことをスポーツだと思っていた私は驚いた。"
    },
    "jlpt_n3_2024_07_p12": {
        "passage_id": "jlpt_n3_2024_07_p12",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 12,
        "pdf_page": 12,
        "mondai_number": 4,
        "title": "留学生日本語カラオケ大会 参加者募集",
        "author": "留学生課",
        "content": "(大学で)\nこのお知らせが掲示板にはってある。\n\n留学生日本語カラオケ大会\n参加者募集\n\n5月29日(土)の13時から、大教室(A103)で「留学生日本語カラオケ大会」を行います。\n参加したい人は、歌いたい日本語の歌を決めて、5月7日(金)までに留学生課で申し込んでください。\nなお、当日の集合時間は12時ですが、希望者は午前中に会場のA103で練習することができます。その場合の集合時間は10時になります。希望者は、参加の申し込みのときに、練習も申し込んでください。\n参加をお待ちしています。\n留学生課"
    },
    "jlpt_n3_2024_07_p13": {
        "passage_id": "jlpt_n3_2024_07_p13",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 13,
        "pdf_page": 13,
        "mondai_number": 4,
        "title": "昼寝とコーヒー",
        "author": None,
        "content": "コーヒーを飲むと眠れなくなるから、寝る前には飲まないという人が多いだろう。しかし最近、昼寝の前にはコーヒーを飲むといいと言われるようになってきた。\n　昼寝をすると起きたあとの集中力が上がるが、長く寝るのはよくない。そこで、飲むと目が覚めるというコーヒーの効果を利用するのだ。この効果は、飲んでから約30分後に出るので、昼寝の前に飲むと、30分ぐらいで自然に目が覚める。\n　ぜひやってみてほしい。"
    },
    "jlpt_n3_2024_07_p14": {
        "passage_id": "jlpt_n3_2024_07_p14",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 14,
        "pdf_page": 14,
        "mondai_number": 5,
        "title": "室内でのホウレンソウ栽培",
        "author": None,
        "content": "私は、前から自分で野菜を育てたいと思っていました。私のうちには庭もベランダもないので、①諦めていたのですが、先月、友達から部屋の中でホウレンソウを育てているという話を聞きました。室内でできるなら私もやってみたいと思い、準備をしました。\n　外に似た環境がいいだろうと考え、窓の近くで育て始めたら、4日で芽が出始めました。少しずつ大きくなるのがうれしかったです。ところが、だんだん葉が黄色くなって、全部枯れてしまったのです。太陽の光が足りなかったのかもしれないと思いました。\n　②がっかりして、友達に電話をして聞いてみると、ホウレンソウは夜になったら、光が当たってはいけないということがわかりました。私の場合は、部屋の電気の光がよくなかったようです。友達は、段ボール箱でホウレンソウにカバーをしているのだそうです。\n　私も同じようにやってみたら、③今度は元気に育ちました。サラダにして食べたら、とてもおいしかったです。"
    },
    "jlpt_n3_2024_07_p15": {
        "passage_id": "jlpt_n3_2024_07_p15",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 15,
        "pdf_page": 15,
        "mondai_number": 5,
        "title": "日本のシャープペンシル",
        "author": None,
        "content": "日本に留学したばかりのころ、文房具店に入って驚いてしまった。私の国では、シャープペンシルはあまり売られていないが、その店には100円の安い物から5000円以上する高い物まで、すごい数のシャープペンが並んでいたのだ。芯も太さが0.3mmから1.5mmまであって、濃さもいろいろな物が売られていた。\n　イギリスで生まれたシャープペンだが、初めは1.5mmや1.0mmの芯しかなかった。だが、約60年前、ある日本の会社が、複雑な漢字でも美しく書けるよう、世界で初めて0.5mmの折れにくい芯を作ることにチャレンジして、成功したのだそうだ。それからシャープペンが日本中で使われるようになったらしい。\n　私は、来日してからずっとシャープペンを愛用している。鉛筆のように先が丸くならず、小さい字がきれいに書けるからだ。今、使っているのは安い物だが、来年、就職したら、少しいい物を買おうと思っている。"
    },
    "jlpt_n3_2024_07_p16": {
        "passage_id": "jlpt_n3_2024_07_p16",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 16,
        "pdf_page": 16,
        "mondai_number": 6,
        "title": "プロスポーツの経営と集客の工夫",
        "author": None,
        "content": "野球やサッカーなどのプロスポーツの経営では、試合会場に来てくれる客を増やすことが重要だ。また見たいと思うようないい試合が続けば、客は自然に増えるだろう。しかし、どんなに選手が努力しても、そのような試合をずっと続けるのは難しい。そこで、①経営者のさまざまな工夫が必要になる。\n　その一つに、②試合会場の工夫がある。例えば、ある会場では、試合がある日に、いろいろな飲食店の食べ物や飲み物を1000種類も選べるようにしている。また、バーベキュー（注1）をしながら試合が見られる観客席を作っているところもある。会場を楽しく過ごせる場所にして、また来たいと思ってもらおうという考え方だ。経営という点では、試合を見ること以外にも会場に来る目的を作ることが重要なのだ。\n　もちろん、試合を楽しむために来る客を増やす工夫もしている。例えば、新しい客に来てもらうために、無料のチケットを配るという方法がある。一度会場に来て試合を楽しんでくれたら、次はチケットを買って来てくれる可能性が広がるという考えからだ。\n　ただ、③この考え方には反対意見もある。無料のチケットで来た客は、ふだんのチケットを高く感じてしまう。すると、結局チケットを買わなくなるので、収入は増えないと考える経営者もいる。\n　プロスポーツの経営者は、客に来てもらうために、いろいろな工夫をしている。手段はさまざまだが、客に満足してもらい、何度も来てもらいたいという気持ちは共通しているのだ。\n\n（注1）バーベキュー：肉や野菜を焼いて食べること"
    },
    "jlpt_n3_2024_07_p19": {
        "passage_id": "jlpt_n3_2024_07_p19",
        "book_id": "jlpt_n3_2024_07",
        "unit": "読解",
        "page": 19,
        "pdf_page": 19,
        "mondai_number": 7,
        "title": "「買い物券チャレンジ」案内チラシ",
        "author": "みずき市商業課",
        "content": "「買い物券チャレンジ」\nみずき市の店で買い物したレシートを集めて応募すると、\n100名の方に、市内の店で使える5,000円分の買い物券が当たります。\n\n参加・応募方法\n①レシートを集める\nみずき市の生活用品店、食料品店など、ホームページに書かれている参加店を利用して、レシートをもらってください。\n【期間】2月1日(月)〜3月31日(水)\n・応募には、合計5,000円分以上のレシートが必要です。\n・レシートの枚数は、5枚以上必要です。\n・同じ店のレシートが2枚以上あってもいいですが、必ず3つ以上の店を利用してレシートを集めてください。\n\n②応募する\n応募用紙に氏名・住所・電話番号を書き、集めたレシートをはってください。応募用紙は、ホームページに書かれている店でもらえます。\n＜応募方法＞\nみずき市商業課に郵送、または持参してください。\n1. 郵送の場合\n【期間】2月1日(月)〜4月9日\n・郵送する場合は、応募用紙を封筒に入れ、切手をはって送ってください。\n2. 持参の場合\n【期間】2月1日(月)〜4月12日(月)\n・商業課の窓口の開いている時間（平日の10時〜16時、最終日4月12日は10時〜17時）に来てください。土日は休みです。\n\n■ 買い物券について\n・当たった方には、4月20日ごろに買い物券をお送りします。\n・買い物券の使用期限は10月31日です。使える店は、ホームページを確認してください。\n\nみずき市商業課 〒126-0204 みずき市中町 2040-1　みずき市役所 3階\n電話 031-924-1976"
    }
}

with open(OUT_DIR / "passages.json", "w", encoding="utf-8") as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)
print("Saved passages.json")

# -------------------------------------------------------------
# 2. Vocabulary (35 Questions)
# -------------------------------------------------------------
vocab_questions = [
    # 問題1 (1..8)
    {
        "id": "jlpt_n3_2024_07_v_q01", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "すみません、弟がこれを__割って__しまいました。",
        "options": ["けって", "おって", "わって", "さわって"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "「割って」の読み方は「わって」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q02", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "ピアノを__基本__から習いたい。",
        "options": ["ぎほん", "しほん", "きほん", "じほん"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "「基本」の読み方は「きほん」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q03", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "かばんは__横__においてください。",
        "options": ["よこ", "そば", "となり", "ゆか"], "answer": 1, "grammar_points": [], "difficulty": 1,
        "explanation": "「横」の読み方は「よこ」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q04", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "この仕事は今日が__最初__です。",
        "options": ["さいしょ", "さいしゅう", "さいしょう", "さいしゅ"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "「最初」の読み方は「さいしょ」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q05", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "昨日、山田さん日本を__返しました__。",
        "options": ["わかしました", "もどしました", "かしました", "かえしました"], "answer": 4, "grammar_points": [], "difficulty": 1,
        "explanation": "「返しました」の読み方は「かえしました」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q06", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "この__包丁__は使いやすい。",
        "options": ["ぼうちょう", "ほうちょう", "ほうちょ", "ぼうちょ"], "answer": 2, "grammar_points": [], "difficulty": 3,
        "explanation": "「包丁」の読み方は「ほうちょう」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q07", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "__適当__なやり方を教えてください。",
        "options": ["てきどう", "てきとう", "ていとう", "ていどう"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「適当」の読み方は「てきとう」です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q08", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "部屋が狭いので、大きな__家具__は置けません。",
        "options": ["やぐう", "かぐう", "やぐ", "かぐ"], "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「家具」の読み方は「かぐ」です。"
    },

    # 問題2 (9..14)
    {
        "id": "jlpt_n3_2024_07_v_q09", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "この質問を__といて__ください。",
        "options": ["試いて", "答いて", "解いて", "調いて"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "「といて」は漢字で「解いて」と書きます。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q10", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "今日は少し__こし__が痛い。",
        "options": ["胸", "腹", "脇", "腰"], "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「こし」は漢字で「腰」と書きます。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q11", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "入学式の__よくしゅう__から講義が始まる。",
        "options": ["翌週", "次週", "明週", "遠週"], "answer": 1, "grammar_points": [], "difficulty": 3,
        "explanation": "「よくしゅう」は漢字で「翌週」と書きます。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q12", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "今朝は気温が__ひくかった__ので、水が凍っていた。",
        "options": ["寒かった", "底かった", "低かった", "暑かった"], "answer": 3, "grammar_points": [], "difficulty": 1,
        "explanation": "気温が「ひくかった」は漢字で「低かった」と書きます。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q13", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "湖はどの__ほうこう__にありますか。",
        "options": ["方向", "方角", "法向", "法角"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "「ほうこう」は漢字で「方向」と書きます。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q14", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "学校の__きそく__がすこし変わるそうだ。",
        "options": ["規側", "規則", "期則", "期側"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「きそく」は漢字で「規則」と書きます。"
    },

    # 問題3 (15..25)
    {
        "id": "jlpt_n3_2024_07_v_q15", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "野球が好きな友人の ( ) で、私も野球に興味を持った。",
        "options": ["指定", "申請", "影響", "通知"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "友人の「影響」で、興味を持つようになった文脈が自然です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q16", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "私は歌が下手なので、歌の上手な人が ( ) です。",
        "options": ["残念", "なつかしい", "うらやましい", "不安"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "自分が苦手なので、上手な人を「うらやましい」と思う気持ちを表します。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q17", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "ゴールまでもう少しだったので、足の痛みを ( ) して走ってきた。",
        "options": ["我慢", "苦労", "遠慮", "努力"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "痛みに耐えて走ることを「痛みを我慢して」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q18", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "林さんは会議ではいつも ( ) ので、あまり自分の意見を言わない。",
        "options": ["人工的", "消極的", "自動的", "間接的"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "自ら進んで発言しない姿勢を「消極的」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q19", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "このバスは駅を出発してから、図書館を ( ) して美術館へ行きます。",
        "options": ["移動", "経由", "進行", "下車"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "途中の場所を通っていくことを「経由して」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q20", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "あの兄弟はとても ( ) ので、ほとんどけんかをしないそうです。",
        "options": ["組", "間", "形", "仲"], "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "関係がよいことを「仲がいい」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q21", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "家のドアを開けるために、ロボットの中から鍵を ( )。",
        "options": ["取り付けた", "取り出した", "引き受けた", "引き落とした"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "中にあるものを外に出すことを「取り出した」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q22", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "たくさんのことを ( ) 言われても、覚えられません。",
        "options": ["一度に", "偶然", "十分", "平等に"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "一回に同時にたくさんのことを言われることを「一度に」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q23", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "このホテルの空港からの ( ) がいいので、外国人からのお客が多い。",
        "options": ["ストップ", "セット", "テイクアウト", "アクセス"], "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "交通の便や連絡が良いことを「アクセスがいい」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q24", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "大好きな歌手のコンサートに行きたかったが、チケットが高くて買えないので行くのを ( )。",
        "options": ["きらった", "うたがった", "あきらめた", "うばった"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "望みを断念することを「あきらめた」と言います。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q25", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "タクシーの乗り場がわからなくて、駅の周りを ( ) 歩き回った。",
        "options": ["うろうろ", "ときどき", "ざあざあ", "ちかちか"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "あてもなく歩き回る様子を「うろうろ」と言います。"
    },

    # 問題4 (26..30)
    {
        "id": "jlpt_n3_2024_07_v_q26", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "この商品は__売り切れました__。",
        "options": ["ほとんど売れました", "全然売れました", "あまり売れませんでした", "全然売れませんでした"], "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「売り切れました」は全部売れた（全然＝すっかり・完全に）という意味です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q27", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "あそこは道が__カーブして__いますので、気をつけてください。",
        "options": ["狭くなって", "曲がって", "込んで", "暗くなった"], "answer": 2, "grammar_points": [], "difficulty": 1,
        "explanation": "「カーブして」は「曲がって」と同義です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q28", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "今夜は家に誰もいないから__退屈__だ。",
        "options": ["つまらない", "怖い", "さびしい", "忙しい"], "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "「退屈だ」は「つまらない」と同義です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q29", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "テレビで紹介された店に__さっそく__行った。",
        "options": ["初めて", "やっと", "たまに", "すぐに"], "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「さっそく」は「すぐに」と同義です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q30", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "このズボンは__ゆるい__ので、別のズボンが欲しい。",
        "options": ["古い", "小さい", "大きい", "薄い"], "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "服やズボンが「ゆるい」のはサイズが「大きい」ことを意味します。"
    },

    # 問題5 (31..35)
    {
        "id": "jlpt_n3_2024_07_v_q31", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "__知識__",
        "options": [
            "いつ財布を落としたか知識がありません。",
            "はさみどこにあるか知識がありますか。",
            "パーティーには私の知識のある人も大勢来ていた。",
            "その仕事は医学の知識がないとできない。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「知識」はある事柄についての知っている事柄・学問的理解を指し、「医学の知識」などの使い方が適切です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q32", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "__ひびく__",
        "options": [
            "台所からおいしそうなにおいがひびいている。",
            "この技術は100年くらい前に外国からひびいたものだ。",
            "この広場で歌を歌うと声がよくひびく。",
            "社長が代わるといううわさが会社中でひびいている。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "「ひびく」は声や音が周囲に反響して伝わることに使います。「声がよくひびく」が正しい用法です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q33", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "__完成__",
        "options": [
            "みんなの意見が一つに完成したので、これから発表します。",
            "娘は子どものころからの夢が完成して医者になった。",
            "親戚の結婚が完成したので、お祝いを贈ろうと思います。",
            "今建てている家が完成したら、ぜひ遊びに来てください。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「完成」は工事や制作物が最後まで出来上がることを指し、「家が完成したら」が自然で正しい使い方です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q34", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "__あわてる__",
        "options": [
            "昨日大雨が降ったので、今日は川の水があわてて流れている。",
            "寝坊をして、あわてて家を出たので、携帯電話を忘れてきてしまった。",
            "マラソン大会で優勝するため、私はゴールまであわてて走り続けた。",
            "あのレストランは人気があるので、お店の人はいつもあわてて働いている。"
        ],
        "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「あわてる」は不意の事態に落ち着きを失って急ぐことを指し、「あわてて家を出た」が適切です。"
    },
    {
        "id": "jlpt_n3_2024_07_v_q35", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文字・語彙",
        "page": 4, "pdf_page": 4, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "__実物__",
        "options": [
            "服はインターネットの写真だけではなく、実物を見てから買いたい。",
            "そのときは彼女の実物の気持ちが分からなかった。",
            "デパートで買い物をしたとき、実物が足りなかったので、クレジットカードで払った。",
            "緊張したので発表のときは失敗しましたが、実物はもっと上手にできました。"
        ],
        "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "「実物」は写真や見本ではなく実際の物そのものを指し、「実物を見てから買いたい」が適切な用法です。"
    }
]

vocab_data = {
    "book_id": "jlpt_n3_2024_07",
    "book_title": "JLPT N3 2024年7月 過去問",
    "unit": "文字・語彙",
    "questions": vocab_questions
}

with open(OUT_DIR / "vocab.json", "w", encoding="utf-8") as f:
    json.dump(vocab_data, f, ensure_ascii=False, indent=2)
print("Saved vocab.json (35 questions)")

# -------------------------------------------------------------
# 3. Grammar (22 Questions)
# -------------------------------------------------------------
grammar_questions = [
    # 問題1 (1..13)
    {
        "id": "jlpt_n3_2024_07_g_q01", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "久しぶりに大学時代の友人と会って、楽しい時間 ( ) 過ごした。",
        "options": ["で", "に", "が", "を"], "answer": 4, "grammar_points": ["時間を過ごす"], "difficulty": 1,
        "explanation": "「時間を過ごす」という他動詞表現で、目的語を取る助詞「を」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q02", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "私の家の近くにはスーパーが2軒あって、( ) 歩いて行けるので便利だ。",
        "options": ["どちらから", "どちらへも", "どちらかでも", "どちらかまで"], "answer": 2, "grammar_points": ["どちらへも"], "difficulty": 2,
        "explanation": "2軒のスーパーの「両方のどちらに対しても行くことができる」という意味で、「どちらへも」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q03", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "子供のころからバスが大好きだったはバスの運転手 ( ) 働いている。",
        "options": ["として", "のほうが", "にとって", "のほかに"], "answer": 1, "grammar_points": ["〜として"], "difficulty": 2,
        "explanation": "身分・立場・資格を表す「〜として」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q04", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "今朝、寝坊して会議に遅れそうだったので、タクシーに乗ったが、道が込んでいて ( ) 遅刻してしまった。",
        "options": ["つい", "結局", "次第に", "ほとんど"], "answer": 2, "grammar_points": ["結局"], "difficulty": 2,
        "explanation": "努力や経過の末の最終的な結果を表す「結局」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q05", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "この歌を ( ) たびに大学時代のことを思い出す。",
        "options": ["聞き", "聞く", "聞いた", "聞いている"], "answer": 2, "grammar_points": ["辞書形＋たびに"], "difficulty": 2,
        "explanation": "「動詞辞書形＋たびに」の形で、「その動作をする時はいつも」という意味を表します。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q06", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "(大学で)\nYuuki「アンさんは、卒業後はどうするんですか。」\nアン「国に帰りますが、帰ってからどう ( ) まだ決めていません。」",
        "options": ["するかは", "するかが", "することは", "することが"], "answer": 1, "grammar_points": ["疑問詞＋〜か＋は"], "difficulty": 2,
        "explanation": "「どうするか（疑問節）」を取り立てて主題とする「〜かは」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q07", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "インターネットで買ったセーターが届いた。サイズが少し大きいかもしれないと心配していたが、実際に ( ) ぴったりだった。",
        "options": ["着てみると", "着たのだから", "着るとしたら", "着ていることで"], "answer": 1, "grammar_points": ["〜てみると"], "difficulty": 2,
        "explanation": "試みに動作をしてみた結果、ある事実を発見したことを表す「〜てみると」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q08", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "(大学で)\nA「今日、授業の後、晩ご飯食べに行かない？」\nB「ごめん、授業の後は図書館へ行くつもりなんだ。あしたレポートを ( ) まだ終わってなくて。」",
        "options": ["出したほうがよくても", "出さなくてもいいのに", "出してはいけなくても", "出さないといけないのに"], "answer": 4, "grammar_points": ["〜ないといけないのに"], "difficulty": 2,
        "explanation": "「提出義務がある（出さないといけない）のに、まだ終わっていない」という逆接・不満の気持ちを表します。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q09", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "この夏祭りは、100年以上前から、この町に住む人々によって ( )。",
        "options": ["続けてもらえる", "続けさせられる", "続けられている", "続けてくれている"], "answer": 3, "grammar_points": ["受身（〜によって〜られる）"], "difficulty": 2,
        "explanation": "動作主「〜によって」に対応する受身動詞の継続表現「続けられている」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q10", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "A「このクッキー、おいしいね。どこで ( ) ？」\nB「さくらデパートだよ。」",
        "options": ["買ったの", "買ったよね", "買ったことある", "買ったんじゃない"], "answer": 1, "grammar_points": ["〜の？（質問）"], "difficulty": 1,
        "explanation": "相手に説明や詳細を尋ねる親しい会話表現「どこで買ったの？」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q11", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "(会議室で)\nA「会議、お疲れさまでした。この会議室、あとでまた使うので、エアコンはつけたままに ( ) 。」\nB「はい、わかりました。」",
        "options": ["していませんか", "なっていませんか", "しておいてください", "なっておいてください"], "answer": 3, "grammar_points": ["〜ておいてください"], "difficulty": 2,
        "explanation": "後の準備や状態を保つよう依頼する表現「（つけたままに）しておいてください」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q12", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "昨日読んだ雑誌に、「忘れることは、必ずしも ( ) 」と書いてあった。",
        "options": ["悪いことなのだ", "悪いことではない", "悪いことのはずだ", "悪いことかもしれない"], "answer": 2, "grammar_points": ["必ずしも〜ない"], "difficulty": 2,
        "explanation": "「必ずしも」は否定表現と呼応して「必ずしも〜ではない（部分否定）」をつくります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q13", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None, "question": "学生「先生は、ふだん何かスポーツを ( ) 。」\n先生「ええ。ゴルフにはときどき行きますよ。」",
        "options": ["いたしますか", "まいりますか", "なさいますか", "いらっしゃいますか"], "answer": 3, "grammar_points": ["尊敬語（なさる）"], "difficulty": 2,
        "explanation": "先生の行為（スポーツをする）を高める尊敬語は「なさいますか」です。"
    },

    # 問題2 (14..18)
    {
        "id": "jlpt_n3_2024_07_g_q14", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "朝、近所のパン屋の前を通ると、パン ______ ______ ★ ______ する。",
        "options": ["が", "焼ける", "の", "いいにおい"], "answer": 4, "grammar_points": ["匂いがする"], "difficulty": 2,
        "explanation": "正しい語順は「パン[の] [焼ける] [★いいにおい] [が] する。」となり、★には4が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q15", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "平日はなかなか運動する時間がないので、日常生活の中で、エレベーターではなくて階段を ______ ______ ★ ______ とかしている。",
        "options": ["とか", "歩く", "使う", "スピードを速くする"], "answer": 4, "grammar_points": ["〜とか〜とかする"], "difficulty": 3,
        "explanation": "「階段を[使う][とか]、[歩く][★スピードを速くする]とかしている。」となり、★には4が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q16", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "森田「西山さん、新しいアルバイトはどうですか。」\n西山「始めた ______ ______ ★ ______ 大変ですが、楽しいです。」",
        "options": ["多くて", "覚えなければいけない", "ことが", "ばかりなので"], "answer": 3, "grammar_points": ["〜たばかりなので"], "difficulty": 2,
        "explanation": "正しい語順は「始めた[ばかりなので] [覚えなければいけない] [★ことが] [多くて] 大変ですが、楽しいです。」となり、★には3が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q17", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "初めて登山をしたとき、山の上からの景色を見て、「 ______ ______ ★ ______ 」と感動した。",
        "options": ["きれいな", "なんて", "なんだろう", "眺め"], "answer": 4, "grammar_points": ["なんて〜なんだろう"], "difficulty": 2,
        "explanation": "正しい語順は「『[なんて] [きれいな] [★眺め] [なんだろう]』と感動した。」となり、★には4が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q18", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 7, "pdf_page": 7, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None, "question": "(会社で)\n田中「ねえ、知ってる？営業課の山下さん、来月「 ______ ______ ★ ______ 。」\n石川「え、そうなんだ。知らなかった。」",
        "options": ["結婚するんだ", "って", "と", "受付の林さん"], "answer": 1, "grammar_points": ["〜んだって"], "difficulty": 2,
        "explanation": "正しい語順は「来月[受付の林さん] [と] [★結婚するんだ] [って]。」となり、★には1が入ります。"
    },

    # 問題3 (19..22)
    {
        "id": "jlpt_n3_2024_07_g_q19", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p08", "question": "私が行くと、林さんはいつも [ 19 ] 。",
        "options": ["話しかけていました", "話しかけてあげました", "話しかけてくれました", "話しかけてもらいました"], "answer": 3, "grammar_points": ["〜てくれる（恩恵表現）"], "difficulty": 2,
        "explanation": "店長の林さんが話し手に対して好意的に会話を始めてくれる動作なので、「話しかけてくれました」が適切です。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q20", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p08", "question": "林さんはいつもいいアドバイスをくれます。 [ 20 ] 私たちは二人とも映画が好きなので、映画の話もよくします。",
        "options": ["確かに", "ところが", "例えば", "それから"], "answer": 4, "grammar_points": ["接続詞（それから）"], "difficulty": 2,
        "explanation": "喫茶店での会話内容（生活相談）に加えて、さらに映画の話題もすることを付け加える接続詞「それから」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q21", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p08", "question": "日本で林さん [ 21 ] 友達ができることは予想していませんでした。",
        "options": ["にも", "のような", "にだけ", "のほかに"], "answer": 2, "grammar_points": ["〜のような（例示）"], "difficulty": 2,
        "explanation": "「林さんのような（50歳も年上の）友達」と例示して修飾する「〜のような」が入ります。"
    },
    {
        "id": "jlpt_n3_2024_07_g_q22", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "文法",
        "page": 9, "pdf_page": 9, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p08", "question": "日本で林さんに [ 22 ] よかったです。",
        "options": ["会えて", "会うから", "会えるのが", "会っても"], "answer": 1, "grammar_points": ["〜てよかった"], "difficulty": 2,
        "explanation": "「〜てよかった」の形で、出会えたことに対する満足や感謝の気持ちを表します。"
    }
]

grammar_data = {
    "book_id": "jlpt_n3_2024_07",
    "book_title": "JLPT N3 2024年7月 過去問",
    "unit": "文法",
    "questions": grammar_questions
}

with open(OUT_DIR / "grammar.json", "w", encoding="utf-8") as f:
    json.dump(grammar_data, f, ensure_ascii=False, indent=2)
print("Saved grammar.json (22 questions)")

# -------------------------------------------------------------
# 4. Reading (16 Questions)
# -------------------------------------------------------------
reading_questions = [
    # 問題4 短文 (23..26)
    {
        "id": "jlpt_n3_2024_07_r_q23", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 10, "pdf_page": 10, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
        "instruction": "つぎの(1)から(4)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p10", "question": "野村さんがこのメールで知らせたいことは何か。",
        "options": [
            "部長会議は、来週に延期する。",
            "部長会議は、明日の15時から行う。",
            "部長会議は天気に関係なく、あさって行う。",
            "部長会議を延期するかどうか、明日の15時に連絡する。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "メール本文に「明日の予報で台風が東京を通ることが確実になった場合は、来週に会議を延期することにします。最終的なご連絡は、明日11日(木)の15時にメールでいたします」とあるため、延期するかどうかを明日15時に連絡することが主旨です。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q24", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 11, "pdf_page": 11, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
        "instruction": "つぎの(1)から(4)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p11", "question": "不思議な気がしたとあるが、どうしてか。",
        "options": [
            "高校生なのに、孫が有名なEスポーツの大会に出ると言っているから。",
            "コンピューターゲームにも大会があると聞いたから。",
            "体を動かさないのに、コンピューターゲームをスポーツと言っているから。",
            "子供のころからずっとなりたいと思い続けていた先生になれたから。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "筆者は「体を動かすことをスポーツだと思っていた」ため、体を動かさないコンピューターゲームをスポーツと呼ぶことに不思議な気がしました。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q25", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 12, "pdf_page": 12, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
        "instruction": "つぎの(1)から(4)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p12", "question": "カラオケ大会に参加したい人で、当日、会場で練習したい人はどうしなければならないか。",
        "options": [
            "5月7日までに留学生課で参加と練習の申し込みをして、29日の10時に会場へ行く。",
            "5月7日までに留学生課で参加と練習の申し込みをして、29日の12時に会場へ行く。",
            "5月7日までに留学生課で参加の申し込みだけして、29日の10時に会場へ行く。",
            "5月29日の10時までに留学生課で参加と練習の申し込みをして、12時に会場へ行く。"
        ],
        "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "お知らせに「5月7日(金)までに留学生課で申し込んでください」「希望者は、参加の申し込みのときに、練習も申し込んでください」「その場合の集合時間は10時になります」とあります。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q26", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 13, "pdf_page": 13, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4",
        "instruction": "つぎの(1)から(4)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p13", "question": "この文章を書いた人が言いたいことは何か。",
        "options": [
            "コーヒーを飲むと眠れなくなるから、昼寝の前には飲まないほうがいい。",
            "集中力が高くなるから、昼寝のあとで30分以内にコーヒーを飲むといい。",
            "昼寝で寝すぎないためには、昼寝をする30分前にコーヒーを飲むといい。",
            "昼寝で、30分ぐらいで自然に起きるためには、昼寝の直前にコーヒーを飲むといい。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "公式正答：3。昼寝の長寝を防ぐため、目覚め効果が約30分後に出るコーヒーを昼寝の前に飲むことを推奨しています。"
    },

    # 問題5 中文 (27..32)
    {
        "id": "jlpt_n3_2024_07_r_q27", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 14, "pdf_page": 14, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p14", "question": "①諦めていたとあるが、何を諦めていたのか。",
        "options": [
            "自分で野菜を育てること。",
            "庭やベランダがある家に住むこと。",
            "友達に野菜の育て方を教えてもらうこと。",
            "部屋の中でホウレンソウを育てること。"
        ],
        "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "「前から自分で野菜を育てたいと思っていました。私のうちには庭もベランダもないので、①諦めていた」とあるため、自分で野菜を育てることです。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q28", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 14, "pdf_page": 14, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p14", "question": "②がっかりしてとあるが、どうしてがっかりしたのか。",
        "options": [
            "ホウレンソウの芽が出なかったから。",
            "ホウレンソウが全部枯れてしまったから。",
            "ホウレンソウについての友達の知識が間違っていたから。",
            "うまく育ったホウレンソウが少なかったから。"
        ],
        "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「だんだん葉が黄色くなって、全部枯れてしまったのです。・・・②がっかりして」とあるため、全部枯れてしまったからです。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q29", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 15, "pdf_page": 15, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p14", "question": "③今度は元気に育ちましたとあるが、どうして元気に育ったのか。",
        "options": [
            "昼、ホウレンソウにもっと光が当たるようにしたから。",
            "昼、ホウレンソウにあまり光が当たらないようにしたから。",
            "夜、ホウレンソウに光が当たるようにしたから。",
            "夜、ホウレンソウに光が当たらないようにしたから。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "友達のアドバイスに従い、段ボール箱でカバーをして夜に光が当たらないようにしたからです。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q30", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 15, "pdf_page": 15, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p15", "question": "驚いてしまったとあるが、文房具店のどんなことに驚いたのか。",
        "options": [
            "シャープペンがあまり売られていなかったこと。",
            "たくさんの種類のシャープペンや芯が売られていたこと。",
            "値段の高いシャープペンばかりが売られていたこと。",
            "シャープペンの芯だけを売る専門の店だったこと。"
        ],
        "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「その店には100円の安い物から5000円以上する高い物まで、すごい数のシャープペンが並んでいたのだ。芯も太さが0.3mmから1.5mmまであって、濃さもいろいろな物が売られていた」とあるためです。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q31", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 15, "pdf_page": 15, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p15", "question": "シャープペンが日本中で使われるようになったのは、いつからか。",
        "options": [
            "日本の会社が、太くて折れにくい芯を作ってから。",
            "日本の会社が、細くて折れにくい芯を作ってから。",
            "日本の会社が、日本でイギリスのシャープペンを売るようになってから。",
            "日本の会社が、世界で初めてシャープペンを作ってから。"
        ],
        "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「ある日本の会社が、複雑な漢字でも美しく書けるよう、世界で初めて0.5mmの折れにくい芯を作ることにチャレンジして、成功したのだそうだ。それからシャープペンが日本中で使われるようになったらしい」とあります。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q32", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 16, "pdf_page": 16, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5",
        "instruction": "つぎの(1)と(2)の文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p15", "question": "「私」が今、シャープペンを使っているのはなぜか。",
        "options": [
            "日本中で使われているから。",
            "小さい字が書きやすいから。",
            "鉛筆より安く買えるから。",
            "高くていい物を買ったから。"
        ],
        "answer": 2, "grammar_points": [], "difficulty": 2,
        "explanation": "「鉛筆のように先が丸くならず、小さい字がきれいに書けるからだ」とあります。"
    },

    # 問題6 長文 (33..36)
    {
        "id": "jlpt_n3_2024_07_r_q33", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 17, "pdf_page": 17, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p16", "question": "①経営者のさまざまな工夫が必要になるとあるが、なぜか。",
        "options": [
            "選手が、客を増やすことに関心を持っていないから。",
            "選手がどんなにいい試合を続けても、客の数には影響しないから。",
            "選手がいい試合をし続けて客を増やすことは、難しいから。",
            "選手が努力することがなく、客が減っているから。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "「どんなに選手が努力しても、そのような試合をずっと続けるのは難しい。そこで、①経営者のさまざまな工夫が必要になる」とあります。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q34", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 17, "pdf_page": 17, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p16", "question": "②試合会場の工夫とあるが、どのような工夫を例として書いているか。",
        "options": [
            "会場内の飲食店の案内をわかりやすくする工夫。",
            "会場で食べ物や飲み物を注文しやすくする工夫。",
            "会場で集中して試合を見てもらうための観客席の工夫。",
            "会場で試合以外に飲食も楽しんでもらうための工夫。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "「1000種類も選べる」「バーベキューをしながら試合が見られる観客席」など、「試合を見ること以外にも会場に来る目的を作る」「飲食も楽しんでもらう」工夫が例示されています。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q35", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 17, "pdf_page": 17, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p16", "question": "③この考え方とあるが、どのような考え方か。",
        "options": [
            "無料のチケットを配って客が増えれば、選手たちのやる気が出るだろう。",
            "無料のチケットを配っても、見に来る客はほとんどいないだろう。",
            "無料のチケットで試合を楽しんだ客は、次はチケットを買って来るだろう。",
            "無料のチケットで試合を楽しんだ客は、次もチケットを買わないだろう。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "直前の段落に「無料のチケットを配るという方法がある。一度会場に来て試合を楽しんでくれたら、次はチケットを買って来てくれる可能性が広がるという考え」とあります。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q36", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 17, "pdf_page": 17, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p16", "question": "この文章全体のテーマは何か。",
        "options": [
            "プロスポーツの経営者が、試合会場に来る客を増やすためにしていること。",
            "プロスポーツの経営者が、選手を強くするためにしていること。",
            "プロスポーツの経営者が、試合会場を客が楽しめる場所にするためにしていること。",
            "プロスポーツの経営者が、客に安く試合を見てもらうためにしていること。"
        ],
        "answer": 1, "grammar_points": [], "difficulty": 2,
        "explanation": "文章冒頭から結びまで一貫して「プロスポーツの経営者が試合会場に来てくれる客を増やすための工夫」について論じています。"
    },

    # 問題7 情報検索 (37..38)
    {
        "id": "jlpt_n3_2024_07_r_q37", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 18, "pdf_page": 18, "section": "読解", "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
        "instruction": "右のページは、ある市の市役所にはってあるお知らせである。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p19", "question": "次の4人は、2月1日から3月31日までの間に「買い物券チャレンジ」の参加店で買い物をした。「買い物券チャレンジ」に応募できるのは誰か。",
        "options": [
            "森田さん。",
            "ヨウさん。",
            "東さん。",
            "クレアさん。"
        ],
        "answer": 3, "grammar_points": [], "difficulty": 2,
        "explanation": "条件：①合計5,000円以上、②5枚以上、③3つ以上の店。東さんは4店・6枚・6100円で3つの条件をすべて満たしています（森田さんは2店で不足、ヨウさんは4枚で不足、クレアさんは4340円で不足）。"
    },
    {
        "id": "jlpt_n3_2024_07_r_q38", "book": "JLPT N3 2024年7月 過去問", "book_code": "jlpt_n3_2024_07", "unit": "読解",
        "page": 18, "pdf_page": 18, "section": "読解", "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7",
        "instruction": "右のページは、ある市の市役所にはってあるお知らせである。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2024_07_p19", "question": "中村さんは、「買い物券チャレンジ」に応募しようと思い、応募用紙の準備をした。今日は4月11日(日)である。応募用紙はどのように出さなければならないか。",
        "options": [
            "今日中に郵送するか、明日の10時から17時までに商業課に持参する。",
            "今日の10時から16時まで、または明日の10時から17時までに商業課に持参する。",
            "明日の10時から16時までに商業課に持参する。",
            "明日の10時から17時までに商業課に持参する。"
        ],
        "answer": 4, "grammar_points": [], "difficulty": 2,
        "explanation": "今日4月11日(日)は市役所窓口は休みで、郵送締切(4月9日)も過ぎています。持参は最終日4月12日(月)まで可能で、最終日の窓口受付時間は「10時〜17時」です。したがって「明日の10時から17時までに商業課に持参する」が正解です。"
    }
]

reading_data = {
    "book_id": "jlpt_n3_2024_07",
    "book_title": "JLPT N3 2024年7月 過去問",
    "unit": "読解",
    "questions": reading_questions
}

with open(OUT_DIR / "reading.json", "w", encoding="utf-8") as f:
    json.dump(reading_data, f, ensure_ascii=False, indent=2)
print("Saved reading.json (16 questions)")
print("ALL DONE for JLPT N3 2024 July!")
