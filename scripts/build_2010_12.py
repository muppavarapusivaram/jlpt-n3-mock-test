# -*- coding: utf-8 -*-
"""
build_2010_12.py
Generates the complete, verified JLPT N3 2010 December question bank:
- vocab.json (35 questions)
- grammar.json (23 questions)
- reading.json (16 questions)
- passages.json (9 passages)
All transcribed directly from original exam booklet images with official answer verification.
"""

import json
from pathlib import Path

OUT_DIR = Path("bank/jlpt_n3_2010_12")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. PASSAGES (9 authentic passages)
# -------------------------------------------------------------
passages = {
    "jlpt_n3_2010_12_p26": {
        "passage_id": "jlpt_n3_2010_12_p26",
        "book_id": "jlpt_n3_2010_12",
        "unit": "問題3 文章の文法",
        "page": 26,
        "pdf_page": 26,
        "mondai_number": 3,
        "title": "100円は安い？",
        "author": "イワノワ マリア",
        "content": (
            "わたしはよく100円ショップで買い物をします。100円ショップ [19]、何でも100円で [19]。\n"
            "　100円ショップでは、化粧品、食べ物、食器、衣類、文房具など、何でも100円で買うことができます。それに、100円とは思えないような、便利な物やかわいい物ばかりで、いつもいろいろほしくなってすぐ買ってしまいます。\n"
            "　しかし最近、たった100円で安いからという理由で何でも買ってしまうのは、間違っていたのではないかと思い始めました。部屋の中に、100円ショップで買ったのに、使っていないものがいくつかあることに [20]。\n"
            "　100円で安いと思って買ったものでも、使わなければ100円を捨てたのと同じです。例えば、100円あれば、小学生なら電車で約10km先まで行けます。歩けば何時間もかかる距離です。50円のはがき [21] 2枚買えます。友だち二人に葉書を送ったら、喜んでもらえるかもしれません。 [22]、100円には大きな価値があると言えます。\n"
            "　100円ショップは便利ですから、これからも利用するつもりです。しかし、100円の価値を忘れず、ほしいと思ったらすぐ買うのではなく、必要かどうかをよく考えてから、 [23] と思っています。"
        )
    },
    "jlpt_n3_2010_12_p28": {
        "passage_id": "jlpt_n3_2010_12_p28",
        "book_id": "jlpt_n3_2010_12",
        "unit": "短文 1",
        "page": 28,
        "pdf_page": 28,
        "mondai_number": 4,
        "title": "山中歴史博物館の紹介",
        "author": "山中歴史博物館",
        "content": (
            "これは、ある博物館の紹介文である。\n\n"
            "山中歴史博物館は、山中公園の中にあります。山中町駅から山中公園の入り口までは徒歩10分、そこから山中歴史博物館まで徒歩10分です。\n"
            "山中歴史博物館の建物には、100年以上の歴史があります。今から約20年前、博物館の周りに山中公園が作られました。\n"
            "博物館には、現在日本に残っている鏡の中で最も古いものがあります。この鏡は中国で作られました。鏡は、毎年1月から3月の特別展覧会で見ることができます。"
        )
    },
    "jlpt_n3_2010_12_p29": {
        "passage_id": "jlpt_n3_2010_12_p29",
        "book_id": "jlpt_n3_2010_12",
        "unit": "短文 2",
        "page": 29,
        "pdf_page": 29,
        "mondai_number": 4,
        "title": "お誕生日サービスのご案内",
        "author": "レストラン青木",
        "content": (
            "これは、あるレストランの誕生日サービスについての広告である。\n\n"
            "お誕生日サービス\n"
            "〜 お誕生日を レストラン青木で 〜\n\n"
            "お誕生日のお祝いに、お食事やパーティーでご来店の場合、みなさまにお飲み物をお一人さま1杯ずつサービスいたします。コーヒー、紅茶、オレンジジュースの中から、お好きなものをお選びください。また、人数分のケーキもサービスいたします。\n\n"
            "＊ サービス利用期間：お誕生日の前後1週間\n"
            "＊ ご利用日の1週間前までに、お電話でお申し込みください。\n"
            "＊ ご来店時に、お誕生日を証明するものをお持ちください。\n\n"
            "レストラン青木　電話：01-2345-6789"
        )
    },
    "jlpt_n3_2010_12_p30": {
        "passage_id": "jlpt_n3_2010_12_p30",
        "book_id": "jlpt_n3_2010_12",
        "unit": "短文 3",
        "page": 30,
        "pdf_page": 30,
        "mondai_number": 4,
        "title": "あなたは本を読んでいますか？",
        "author": "読書量調査記事",
        "content": (
            "これは、ある調査についての記事である。\n\n"
            "あなたは本を読んでいますか？\n\n"
            "ある書店が毎年行っている「1か月間の読書量調査」の、今年の結果が報告された。その報告によると、1か月間に本を「読まなかった人」の割合（51%）は、全体では去年より減少した。\n"
            "「読まなかった」と答えた人の割合をそれぞれの年齢で見てみると、去年より増えたのは20歳代と70歳以上であった。特に20歳代では、調査開始以来、毎年増え続けている。\n"
            "これに対して30歳代、40歳代、50歳代、60歳代では、去年より減少した。"
        )
    },
    "jlpt_n3_2010_12_p31": {
        "passage_id": "jlpt_n3_2010_12_p31",
        "book_id": "jlpt_n3_2010_12",
        "unit": "短文 4",
        "page": 31,
        "pdf_page": 31,
        "mondai_number": 4,
        "title": "東京ホテル 料金割引のご案内",
        "author": "東京ホテル お客様サービス係",
        "content": (
            "これは、あるホテルから山田さんに届いたメールである。\n\n"
            "あて先：s.yamada@232mail.com\n"
            "件名：東京ホテル 料金割引のご案内\n"
            "送信日時：2011年2月1日 16:20\n\n"
            "山田真二 様\n\n"
            "いつもご利用ありがとうございます。\n"
            "現在、東京ホテルでは、インターネット予約割引サービスを行っております。\n"
            "インターネットで予約され、2月28日までにお泊まりの方は、1泊の料金を10%割引し、ご朝食を無料にいたします。\n"
            "この割引をご利用になれるお部屋は一日10室だけですので、お早めにご予約ください。\n"
            "なお、このサービスは、電話、ファックスでご予約の場合はご利用できません。\n"
            "ご予約を心よりお待ちしております。\n\n"
            "東京ホテル お客様サービス係"
        )
    },
    "jlpt_n3_2010_12_p32": {
        "passage_id": "jlpt_n3_2010_12_p32",
        "book_id": "jlpt_n3_2010_12",
        "unit": "中文 1",
        "page": 32,
        "pdf_page": 32,
        "mondai_number": 5,
        "title": "小学校のクラス会",
        "author": None,
        "content": (
            "昨日、小学校のクラス会に行きました。50年前に卒業してから初めて開かれたクラス会でした。子どもだったみんなも、もう60歳を過ぎているので、①顔を見てもだれがだれだかわかりません。それで、話をする時は、まず始めに、相手の名前を聞かなければなりませんでした。\n"
            "　一人の女の人がわたしに話しかけてきました。\n"
            "「田中春子さんですよね？」\n"
            "「はい。失礼ですが、お名前は？」\n"
            "その女の人は、昔の小学校のクラス写真を見せて、そこに写っている一人を指して、言いました。\n"
            "「わたしは、これよ。」\n"
            "「あっ。す、すみません。」\n"
            "その女の人は、小学校6年の時のクラス担任の先生でした。わたしは先生に、何度も「②すみません。」と言いました。先生は「うれしいですよ。間違えてくれて。」と笑いました。先生は、何か社会のためになることをしたいと思って、75歳の今でも、近所の子どもたちに無料の絵画教室を開いているそうです。それで、同級生と間違えるほど、お元気で若く見えるのだと思いました。わたしも先生を目標にして、毎日を過ごしていきたいと思います。"
        )
    },
    "jlpt_n3_2010_12_p34": {
        "passage_id": "jlpt_n3_2010_12_p34",
        "book_id": "jlpt_n3_2010_12",
        "unit": "中文 2",
        "page": 34,
        "pdf_page": 34,
        "mondai_number": 5,
        "title": "電気製品と生活の便利さ",
        "author": None,
        "content": (
            "日本では電気製品がどんどん新しくなって、生活はとても便利になったと言われている。パソコンを使えば家にいても買い物ができるし、携帯電話でもメールやインターネットが使えて、お金を支払うことも可能である。製品を作った会社は、新しい製品はいろいろなことができるから、これまでより便利になったと宣伝し、わたしたちも①そう感じさせられている。\n"
            "　しかし、わたしたちは新しい製品を上手に使えているだろうか。携帯電話もテレビも、ボタンの数が増えて、どれを押したらいいのかよくわからないことがある。以前の製品の方が単純で使い方がわかりやすかったかもしれない。\n"
            "　会社は、新しい製品を作るとき、いろいろなことができるようにすることを第一にして、使いやすさのことはあまり考えてこなかったようだ。つまり、製品は進歩してきたが、使い方は複雑になってしまったのだ。\n"
            "　わたしは、これでは本当に生活が便利になったとは言えないと思う。"
        )
    },
    "jlpt_n3_2010_12_p35": {
        "passage_id": "jlpt_n3_2010_12_p35",
        "book_id": "jlpt_n3_2010_12",
        "unit": "長文",
        "page": 35,
        "pdf_page": 35,
        "mondai_number": 6,
        "title": "1000円カットの店",
        "author": None,
        "content": (
            "先日、会社の近くにある①1000円カットの店へ髪を切りに行ってみた。\n"
            "　最近、あちこちにある1000円カットの店は、たった10分で髪を切ってくれるし安いので、男性サラリーマンなどに人気がある。美容院で髪を切ると、普通3000円から4000円はかかる。それに比べると、1000円カットの店は、②どうしてこんなに安くできるのだろうか。\n"
            "　店の人によると、この値段で店を経営していくためには、家賃が安いところを借りることが一番大切なのだそうだ。そして、シャンプーやひげそりをやめて、短い時間で多くの人をカットすれば、1000円でも十分に経営していける。一日に大勢の客を相手にするのでカットの技術もすぐに上がるそうだ。\n"
            "　しかし、平日の昼間は会社員の客が少なくなる。そこで、女性客にも来店してもらうため、壁を明るく優しい色に変えたり、女性だけが使える割引券を配ったり、店に置いておく女性向けの雑誌の種類を増やしたそうだ。特に効果があったのは、店の中に子どもが遊べる場所を作ったことで、子どもを連れた女性客が少しずつ増えていったそうである。\n"
            "　わたしは、店に行く前は、ちょっと心配だった。しかし、カットの技術もかなり満足できるものだったので、忙しいときはこちらの店でもいいと今では思っている。\n\n"
            "（注）シャンプー：髪を洗うこと"
        )
    },
    "jlpt_n3_2010_12_p38": {
        "passage_id": "jlpt_n3_2010_12_p38",
        "book_id": "jlpt_n3_2010_12",
        "unit": "情報検索",
        "page": 38,
        "pdf_page": 38,
        "mondai_number": 7,
        "title": "日本文化教室のご案内",
        "author": "山田市文化会館",
        "content": (
            "日本文化教室のご案内\n\n"
            "【期間（前期）】 4月13日（月）〜 7月31日（金）\n"
            "【場所】 山田市文化会館\n\n"
            "【教室の内容】\n"
            "・柔道　　：月・木　18:30〜20:00（定員20名）\n"
            "・踊り　　：火・土　18:30〜20:00（定員20名）\n"
            "・折り紙　：火　　　18:30〜20:00（定員20名）\n"
            "・お茶　　：金　　　18:30〜20:00（定員15名）\n"
            "・お花　　：土　　　14:30〜16:30（定員15名）\n"
            "・日本料理：第1・第3日曜日　15:00〜18:00（定員20名）\n"
            "※ 週2回ある教室は両方の曜日に参加してください。\n\n"
            "【参加料（前期分）】\n"
            "・週2回の教室：大人 7,000円 / 学生（高校生以上） 5,000円\n"
            "・週1回の教室：大人 4,000円 / 学生（高校生以上） 3,000円\n"
            "・お花・日本料理の教室：8,000円（材料費込み）\n"
            "※ 上の料金は前期分の合計です。\n\n"
            "【申し込み期間・方法】\n"
            "・3月2日（月）〜 4月2日（木）（定員になれば受け付け終了）\n"
            "・文化会館事務室で申し込み用紙に記入して、参加料を支払ってください。\n\n"
            "【その他】\n"
            "・教室で使用する道具は、文化会館に用意してあります。\n"
            "・柔道の教室で着る柔道着は自分で準備してください。会館でも売っています。\n\n"
            "山田市文化会館　〒987-6543 山田市わかば1-2-3　電話：012-345-6789"
        )
    }
}

# -------------------------------------------------------------
# 2. VOCABULARY (35 questions)
# -------------------------------------------------------------
vocab_questions = [
    # 問題1 漢字読み (8問)
    {
        "id": "jlpt_n3_2010_12_v01",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "この飛行機には、もう__空席__がありません。",
        "options": ["そらせき", "そらぜき", "くうせき", "くうぜき"],
        "answer": 3,
        "explanation": "「空席」は「くうせき」と読みます。乗客が座っていない空いている席のことです。",
        "grammar_points": ["漢字読み: 空席 (くうせき)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v02",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "夏休みに__夫婦__で旅行をした。",
        "options": ["ふふ", "ふふう", "ふうふ", "ふうふう"],
        "answer": 3,
        "explanation": "「夫婦」は「ふうふ」と読みます。夫と妻のことです。",
        "grammar_points": ["漢字読み: 夫婦 (ふうふ)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v03",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "30分待って、わたしの__順番__が来ました。",
        "options": ["しゅうばん", "じゅうばん", "しゅんばん", "じゅんばん"],
        "answer": 4,
        "explanation": "「順番」は「じゅんばん」と読みます。順序や番のことです。",
        "grammar_points": ["漢字読み: 順番 (じゅんばん)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v04",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "去年、この会社は海外に工場を__移した__。",
        "options": ["もどした", "うつした", "わたした", "かえした"],
        "answer": 2,
        "explanation": "「移した」は「うつした」と読みます。場所を変えて移動させることです。",
        "grammar_points": ["漢字読み: 移す (うつす)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v05",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "__失業__していた友達が、新しい仕事を見つけた。",
        "options": ["しぎょ", "しぎょう", "しつぎょ", "しつぎょう"],
        "answer": 4,
        "explanation": "「失業」は「しつぎょう」と読みます。職を失うことです。",
        "grammar_points": ["漢字読み: 失業 (しつぎょう)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v06",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "前田さんは足を__組んで__座っていた。",
        "options": ["くんで", "ふんで", "つかんで", "たたんで"],
        "answer": 1,
        "explanation": "「組んで」は「くんで」と読みます。「足を組む（くむ）」という慣用表現です。",
        "grammar_points": ["漢字読み: 組む (くむ)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v07",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "大きく__息__を吸ってください。",
        "options": ["いいぎ", "いぎ", "いいき", "いき"],
        "answer": 4,
        "explanation": "「息」は「いき」と読みます。「息を吸う／吐く」の形で使われます。",
        "grammar_points": ["漢字読み: 息 (いき)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v08",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 2,
        "pdf_page": 2,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "kanji_reading",
        "mondai_label": "問題1",
        "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "おばは__苦労__して三人の子どもを育てた。",
        "options": ["くろう", "くのう", "ぐろう", "ぐのう"],
        "answer": 1,
        "explanation": "「苦労」は「くろう」と読みます。精神的・肉体的な苦痛や困難を乗り越えて努力することです。",
        "grammar_points": ["漢字読み: 苦労 (くろう)"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題2 表記 (6問)
    {
        "id": "jlpt_n3_2010_12_v09",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "試験の__せいせき__がよかったので、うれしい。",
        "options": ["性積", "性績", "成積", "成績"],
        "answer": 4,
        "explanation": "せいせきは「成績」と書きます。仕事や勉強などの結果・成果のことです。",
        "grammar_points": ["漢字表記: 成績 (せいせき)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v10",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "佐藤さんは、いろいろな__がっき__が弾けます。",
        "options": ["楽器", "音器", "楽具", "音具"],
        "answer": 1,
        "explanation": "がっきは「楽器」と書きます。音楽を奏でる器具のことです。",
        "grammar_points": ["漢字表記: 楽器 (がっき)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v11",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "__せんもんか__が指導してくれた。",
        "options": ["専問家", "専門家", "選問家", "選門家"],
        "answer": 2,
        "explanation": "せんもんかは「専門家」と書きます。ある特定の分野を専門に研究・実務する人のことです。",
        "grammar_points": ["漢字表記: 専門家 (せんもんか)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v12",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "この高校の生徒は__せいふく__を着なければなりません。",
        "options": ["製報", "制服", "製服", "制報"],
        "answer": 2,
        "explanation": "せいふくは「制服」と書きます。学校や会社などで定められた衣服のことです。",
        "grammar_points": ["漢字表記: 制服 (せいふく)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v13",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "コートの__うちがわ__にポケットがついています。",
        "options": ["中側", "内測", "内側", "中測"],
        "answer": 3,
        "explanation": "うちがわは「内側」と書きます。内側の面のことです。",
        "grammar_points": ["漢字表記: 内側 (うちがわ)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v14",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 3,
        "pdf_page": 3,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "orthography",
        "mondai_label": "問題2",
        "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "休みの日は家で__すごしました__。",
        "options": ["過ごしました", "速ごしました", "適ごしました", "追ごしました"],
        "answer": 1,
        "explanation": "すごしましたは「過ごしました」（過ごす）と書きます。時間を送ることです。",
        "grammar_points": ["漢字表記: 過ごす (すごす)"],
        "difficulty": 1,
        "needs_review": False
    },

    # 問題3 文脈規定 (11問)
    {
        "id": "jlpt_n3_2010_12_v15",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "かぜをひいたときは（　）薬を飲んだほうがいいですよ。",
        "options": ["急に", "あわてて", "早めに", "さかんに"],
        "answer": 3,
        "explanation": "「早めに（はやめに）」は時期や時刻を通常より早く行うことです。「早めに薬を飲む」が最も自然です。",
        "grammar_points": ["語彙: 早めに"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v16",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "せっけんの（　）が手についているよ。",
        "options": ["どろ", "しみ", "きず", "あわ"],
        "answer": 4,
        "explanation": "せっけんを使うと「泡（あわ）」が立ちます。「せっけんのあわ（泡）」が適切です。",
        "grammar_points": ["語彙: 泡 (あわ)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v17",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "部屋に入るときはドアを（　）してください。",
        "options": ["ノック", "カット", "バック", "セット"],
        "answer": 1,
        "explanation": "ドアをトントンと叩く行為は「ノック（knock）」と言います。",
        "grammar_points": ["外来語: ノック"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v18",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "レポートを書くのに（　）しか、かからなかった。",
        "options": ["半日", "翌週", "月末", "年中"],
        "answer": 1,
        "explanation": "所要時間を表す名詞が入ります。「半日（はんにち）しかかからなかった」が正解です。",
        "grammar_points": ["語彙: 半日 (はんにち)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v19",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "このお皿は割れやすいので、運ぶときはていねいに（　）ください。",
        "options": ["応用して", "愛用して", "扱って", "拾って"],
        "answer": 3,
        "explanation": "壊れやすい物を手で大事に操作・持ち運ぶことは「扱う（あつかう）」と言います。",
        "grammar_points": ["語彙: 扱う (あつかう)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v20",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "この町は（　）人口の約40パーセントが大学生である。",
        "options": ["毎", "両", "各", "全"],
        "answer": 4,
        "explanation": "全体の人口を指す接頭語は「全〜」で、「全人口（ぜんじんこう）」と言います。",
        "grammar_points": ["接頭辞: 全 (ぜん)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v21",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "鈴木さんは海外で働きたいという（　）を持っているそうだ。",
        "options": ["用意", "希望", "決心", "想像"],
        "answer": 2,
        "explanation": "「〜したいという希望（きぼう）を持っている」というコロケーションが自然です。",
        "grammar_points": ["語彙: 希望 (きぼう)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v22",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "どちらのエアコンを買おうか、まだ（　）います。",
        "options": ["まよって", "いのって", "ねがって", "うたがって"],
        "answer": 1,
        "explanation": "どちらにするか決めかねている状態は「迷う（まよう）」です。「迷っています」が適切です。",
        "grammar_points": ["語彙: 迷う (まよう)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v23",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "社長は電話中ですので、こちらで（　）お待ちください。",
        "options": ["いつか", "しばらく", "いつのまにか", "ひさしぶりに"],
        "answer": 2,
        "explanation": "少しのあいだ待つよう丁重に頼む決まり文句は「しばらくお待ちください」です。",
        "grammar_points": ["副詞: しばらく"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v24",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "最近（　）がなくて、とても疲れやすい。",
        "options": ["努力", "体力", "協力", "実力"],
        "answer": 2,
        "explanation": "体の力、スタミナを表す言葉は「体力（たいりょく）」です。「体力がない」と言います。",
        "grammar_points": ["語彙: 体力 (たいりょく)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v25",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 4,
        "pdf_page": 4,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "contextual_defining",
        "mondai_label": "問題3",
        "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "緊張すると胸が（　）する。",
        "options": ["ちかちか", "ぐらぐら", "どきどき", "うろうろ"],
        "answer": 3,
        "explanation": "緊張や興奮で心臓の鼓動が速くなる様子を表すオノマトペは「どきどき」です。",
        "grammar_points": ["オノマトペ: どきどき"],
        "difficulty": 1,
        "needs_review": False
    },

    # 問題4 類義 (5問)
    {
        "id": "jlpt_n3_2010_12_v26",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 5,
        "pdf_page": 5,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "paraphrases",
        "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "わたしの__まご__は銀行につとめている。",
        "options": ["父の弟", "母の姉", "兄の子ども", "娘の息子"],
        "answer": 4,
        "explanation": "「まご（孫）」は子どもの子どもを指します。選択肢の中では「娘の息子」が該当します。",
        "grammar_points": ["親族呼称: 孫 (まご)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v27",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 5,
        "pdf_page": 5,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "paraphrases",
        "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "__たまっている__仕事を、今週中に終わらせたい。",
        "options": ["さっき始めた", "とても急いでいる", "たくさん残っている", "ほかの人に頼まれた"],
        "answer": 3,
        "explanation": "仕事が「たまっている」とは、未処理の仕事が片付かずに「たくさん残っている」状態を指します。",
        "grammar_points": ["語彙: たまる"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v28",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 5,
        "pdf_page": 5,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "paraphrases",
        "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "山田さんは__短気__だ。",
        "options": ["すぐ驚く", "すぐ笑う", "すぐ怒る", "すぐ泣く"],
        "answer": 3,
        "explanation": "「短気（たんき）」とは、忍耐力がなく、すぐにイライラして「すぐ怒る」性格のことです。",
        "grammar_points": ["語彙: 短気 (たんき)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v29",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 5,
        "pdf_page": 5,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "paraphrases",
        "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "単語をたくさん__暗記した__。",
        "options": ["読んだ", "書いた", "忘れた", "覚えた"],
        "answer": 4,
        "explanation": "「暗記する（あんきする）」とは、文字を見ずに言えるように「頭に記憶する（覚える）」ことです。",
        "grammar_points": ["語彙: 暗記 (あんき)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v30",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 5,
        "pdf_page": 5,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "paraphrases",
        "mondai_label": "問題4",
        "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "この会社にはいろいろな__きまり__がある。",
        "options": ["計画", "規則", "連絡", "秘密"],
        "answer": 2,
        "explanation": "「きまり（決まり）」はルールや定めのことで、「規則（きそく）」と同義です。",
        "grammar_points": ["語彙: 決まり／規則"],
        "difficulty": 1,
        "needs_review": False
    },

    # 問題5 用法 (5問)
    {
        "id": "jlpt_n3_2010_12_v31",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5",
        "page": 6,
        "pdf_page": 6,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "usage",
        "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "【回収】",
        "options": [
            "わたしの趣味は、めずらしい切手を回収することです。",
            "アンケート用紙はセミナーが終わったら回収します。",
            "問題を解決するために、多くの人から意見を回収した。",
            "マラソン大会の参加者をインターネットで回収しています。"
        ],
        "answer": 2,
        "explanation": "「回収（かいしゅう）」は配った物や一度出した物を集めて取り戻すことです。アンケート用紙やごみ、テスト用紙などに使います。",
        "grammar_points": ["語彙用法: 回収 (かいしゅう)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v32",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5",
        "page": 6,
        "pdf_page": 6,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "usage",
        "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "【区切る】",
        "options": [
            "先生へのプレゼント代を二人で区切って払った。",
            "大きな部屋を二つに区切って使った。",
            "わたしの家では、みんなで家事を区切っています。",
            "荷物が多いので、二つのかばんに区切って運んだ。"
        ],
        "answer": 2,
        "explanation": "「区切る（くぎる）」は空間や時間を仕切りや境目で分けることです。「部屋を二つに区切る」が正しい用法です。",
        "grammar_points": ["語彙用法: 区切る (くぎる)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v33",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5",
        "page": 6,
        "pdf_page": 6,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "usage",
        "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "【修理】",
        "options": [
            "時計が動かなくなったので修理した。",
            "虫歯を修理するのに2か月かかった。",
            "先生に間違いを修理された。",
            "少し休んで気分を修理しませんか。"
        ],
        "answer": 1,
        "explanation": "「修理（しゅうり）」は壊れた機械や器具・建物などを直すことです。虫歯は「治療」、間違いは「訂正」と言います。",
        "grammar_points": ["語彙用法: 修理 (しゅうり)"],
        "difficulty": 1,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v34",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5",
        "page": 6,
        "pdf_page": 6,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "usage",
        "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "【なだらか】",
        "options": [
            "ここからはなだらかな坂道が続いている。",
            "今日はなだらかな話し合いができてよかったですね。",
            "やせたらズボンがなだらかにはけるようになった。",
            "来週からは天気がなだらかになるそうです。"
        ],
        "answer": 1,
        "explanation": "「なだらか」は傾斜や勾配が緩やかな様子を表します。「なだらかな坂道」「なだらかな山」のように用います。",
        "grammar_points": ["語彙用法: なだらか"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_v35",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5",
        "page": 6,
        "pdf_page": 6,
        "section": "言語知識（文字・語彙）",
        "mondai_type": "usage",
        "mondai_label": "問題5",
        "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "【まずしい】",
        "options": [
            "人数がまずしいので、アルバイトを募集します。",
            "去年は雨がまずしかったので、野菜が育ちませんでした。",
            "学生のころはまずしかったので、毎日アルバイトをしていました。",
            "時間がまずしいので、宿題が終わらないかもしれません。"
        ],
        "answer": 3,
        "explanation": "「まずしい（貧しい）」はお金や物が不足していて経済的に苦しい状態を表します。「貧しい生活」「貧しかった」と使います。",
        "grammar_points": ["語彙用法: 貧しい (まずしい)"],
        "difficulty": 2,
        "needs_review": False
    }
]

# -------------------------------------------------------------
# 3. GRAMMAR (23 questions: 13 form, 5 star, 5 cloze)
# -------------------------------------------------------------
grammar_questions = [
    # 問題1 文法形式 (13問)
    {
        "id": "jlpt_n3_2010_12_g01",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "今夜は風が強くて、庭の木が今にも（　）。",
        "options": ["折れています", "折れそうです", "折れたと思います", "折れたんです"],
        "answer": 2,
        "explanation": "「今にも〜そうだ」は今すぐその事態が起こりそうな直前の様子を表します。「今にも折れそうです」が正解です。",
        "grammar_points": ["今にも〜そうだ"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g02",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "このテレビドラマは人気が出なかった（　）、全20回の放送予定だったものが、10回で終わってしまった。",
        "options": ["たびに", "ために", "なかに", "ように"],
        "answer": 2,
        "explanation": "原因・理由を表す「〜ために」が適切です。「人気が出なかったために（＝出なかったせいで）」放送が打ち切られたという意味になります。",
        "grammar_points": ["〜ために (原因・理由)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g03",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "9月の会社説明会の日程を（　）いたします。",
        "options": ["知らせ", "知らせて", "お知らせ", "お知らせして"],
        "answer": 3,
        "explanation": "謙譲語Ⅰの形は「お＋動詞のマス形＋いたす」です。「お知らせいたします」が正しい敬語表現です。",
        "grammar_points": ["お〜いたす (謙譲表現)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g04",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "子どもだ子どもだと思っていた息子も、明日から（　）大学生になります。",
        "options": ["まだ", "いつか", "しだいに", "とうとう"],
        "answer": 4,
        "explanation": "待ち望んでいたり、長い時間が経過して最終的な結末に至ることを表す副詞は「とうとう（ついに）」です。",
        "grammar_points": ["副詞: とうとう"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g05",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "A「沖縄旅行、どうだった？ こっちはずっと雨だったんだけど。」\nB「あ、そう？ 沖縄は、旅行の（　）ずっと天気がよくて、毎日海で遊べたよ。」",
        "options": ["あいだじゅう", "うちには", "なかで", "ころまでに"],
        "answer": 1,
        "explanation": "「〜の間中（あいだじゅう）」はある期間の初めから終わりまで継続してその状態が続くことを表します。",
        "grammar_points": ["〜間中 (あいだじゅう)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g06",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "弟と妹がいると集中できないから、今日は二人が（　）うちに、宿題をやってしまおう。",
        "options": ["帰ってこない", "帰っていかない", "帰ってこなかった", "帰っていかなかった"],
        "answer": 1,
        "explanation": "「〜ないうちに」はある事態が生じる前に、という意味を表します。現在〜未来の否定形「帰ってこないうちに」が正解です。",
        "grammar_points": ["〜ないうちに"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g07",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 22,
        "pdf_page": 22,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "学生「先生、日本語で作文を書いたのですが、わたしの作文を（　）。」\n先生「ええ、いいですよ。」",
        "options": ["見たいでしょうか", "見てもよろしいでしょうか", "見たらいかがですか", "見ていただけませんか"],
        "answer": 4,
        "explanation": "目上の先生に依頼する適切な表現は「〜ていただけませんか（＝見てくれませんか）」です。",
        "grammar_points": ["〜ていただけませんか (丁寧な依頼)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g08",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "山下「ねえ、わたし、この問題全然わかんないんだけど、田中さん、解けた？」\n田中「わたしに（　）じゃない。わたしが数学苦手なの知ってるでしょ。」",
        "options": ["解けない", "解けないに違いない", "解けるはずがない", "解くことができない"],
        "answer": 3,
        "explanation": "「〜はずがない」は「絶対に〜ない」という強い確信を伴う否定です。「数学が苦手なわたしに解けるはずがない」が文脈上自然です。",
        "grammar_points": ["〜はずがない (強い否定確信)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g09",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "〈ABCこども新聞の宣伝〉\n「私たちが作ったABCこども新聞は、すべての漢字に振り仮名をつけてあるので、小学1年生からでも読める（　）。」",
        "options": ["ことによります", "ことにあります", "ようになっています", "ようになさっています"],
        "answer": 3,
        "explanation": "機械やシステムの構造、仕組みとしてそのように設定・工夫されていることを表す文型は「〜ようになっている」です。",
        "grammar_points": ["〜ようになっている (仕組み・構造)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g10",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "上田「来週、兄の誕生日なんだけど、プレゼントに何を買おうかな。」\n山本「ネクタイでも買って（　）？ 上田さんからのプレゼント、お兄さん、喜ぶと思うよ。」",
        "options": ["もらってもいい", "もらったらどう", "あげてもいい", "あげたらどう"],
        "answer": 4,
        "explanation": "相手に対して「〜してあげたらどうですか（＝〜してあげることを勧める）」と提案する表現「あげたらどう」が正解です。",
        "grammar_points": ["〜てあげたらどう (勧誘・提案)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g11",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "妻「この前の試合、あなたがけがしなかったら、優勝できたかもねえ。」\n夫「うーん。けがをしなかったら、4位くらいには（　）、それでもやっぱり優勝はできなかったと思うよ。」",
        "options": ["なれたらしいし", "なりたかったらしいし", "なれただろうけど", "なりたかったんだろうけど"],
        "answer": 3,
        "explanation": "過去の反実仮想「けがをしなかったら〜なれただろうが、実際は優勝は無理だった」という対比文脈です。「なれただろうけど」が適切です。",
        "grammar_points": ["仮定逆接: 〜ただろうけど"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g12",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "先輩「さっきの会議で話に出た営業の仕事を、たぶん山川部長は、君に（　）？」\n後輩「えっ、そうなんでしょうか。」",
        "options": ["やらせるつもりじゃない", "やられるつもりじゃない", "やらされるんじゃない", "やれるんじゃない"],
        "answer": 1,
        "explanation": "使役形「やらせる（＝させる）」＋「つもりじゃないか」の形です。「山川部長は君に営業の仕事をやらせるつもりではないか」という推測です。",
        "grammar_points": ["使役: やらせるつもり"],
        "difficulty": 3,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g13",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題1",
        "page": 23,
        "pdf_page": 23,
        "section": "言語知識（文法）",
        "mondai_type": "bunpou_keishiki",
        "mondai_label": "問題1",
        "instruction": "つぎの文の ( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": None,
        "question": "わたしの気持ちは、きっとあなたにはわからないだろうし、あなたに（　）。",
        "options": ["わかりたくもない", "わかってほしくもない", "わかりたくはないだろう", "わかってほしくはないだろう"],
        "answer": 2,
        "explanation": "相手に対して「〜してほしくない」という願望の否定を表す表現「〜てほしくもない」が適切です。「あなたにわかってほしくもない」となります。",
        "grammar_points": ["〜てほしくもない (強い否定願望)"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題2 文の組み立て (5問)
    {
        "id": "jlpt_n3_2010_12_g14",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 24,
        "pdf_page": 24,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "（たんすの片付けをしながら）\n娘「お母さん、この着物なぁに？」\n母親「それはね、お母さんが大学生のときにおばあちゃんに買って＿＿ ＿＿ ★ ＿＿大事にしまっておいたのよ。」",
        "options": ["もらった", "ものだ", "から", "大切な"],
        "answer": 2,
        "explanation": "文脈に合わせて語句を並べ替えると、「買って【もらった(1)】 【大切な(4)】 【★ものだ(2)】 【から(3)】大事にしまっておいたのよ」となります。★に入るのは 2（ものだ）です。",
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g15",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 24,
        "pdf_page": 24,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "子どもが生まれた＿＿ ＿＿ ★ ＿＿安全を気にするようになった。",
        "options": ["食べ物", "で", "こと", "の"],
        "answer": 1,
        "explanation": "語句を並べ替えると、「子どもが生まれた【こと(3)】 【で(2)】 【★食べ物(1)】 【の(4)】安全を気にするようになった」となります。★に入るのは 1（食べ物）です。",
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g16",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 24,
        "pdf_page": 24,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "今年の花火大会の観客数は去年＿＿ ＿＿ ★ ＿＿17万人だった。",
        "options": ["10パーセント", "と比べて", "多い", "以上"],
        "answer": 4,
        "explanation": "語句を並べ替えると、「去年【と比べて(2)】 【10パーセント(1)】 【★以上(4)】 【多い(3)】17万人だった」となります。★に入るのは 4（以上）です。",
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g17",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 25,
        "pdf_page": 25,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "もしわからないことがあったら、参考書、インターネット＿＿ ＿＿ ★ ＿＿いいですから、調べておいてください。",
        "options": ["何を", "使って", "など", "も"],
        "answer": 2,
        "explanation": "語句を並べ替えると、「参考書、インターネット【など(3)】 【何を(1)】 【★使って(2)】 【も(4)】いいですから」となります。★に入るのは 2（使って）です。",
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g18",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題2",
        "page": 25,
        "pdf_page": 25,
        "section": "言語知識（文法）",
        "mondai_type": "bun_kumitate",
        "mondai_label": "問題2",
        "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。",
        "passage_id": None,
        "question": "わたしの応援が力＿＿ ＿＿ ★ ＿＿応援します。",
        "options": ["なら", "だって", "いくら", "になる"],
        "answer": 3,
        "explanation": "語句を並べ替えると、「わたしの応援が力【になる(4)】 【なら(1)】 【★いくら(3)】 【だって(2)】応援します」となります。★に入るのは 3（いくら）です。",
        "grammar_points": ["文の組み立て (星並べ)"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題3 文章の文法 (5問)
    {
        "id": "jlpt_n3_2010_12_g19",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 26,
        "pdf_page": 26,
        "section": "言語知識（文法）",
        "mondai_type": "bunshou_bunpou",
        "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p26",
        "question": "[ 19 ] に入る最もよいものはどれか。",
        "options": [
            "a や ／ b 売られているお店です",
            "a のように ／ b 売られています",
            "a なども ／ b 売っています",
            "a というのは ／ b 売っているお店です"
        ],
        "answer": 4,
        "explanation": "定義説明「〜というのは…売っているお店です」という文構造が適切です。「100円ショップというのは、何でも100円で売っているお店です」となります。",
        "grammar_points": ["定義説明: 〜というのは…お店です"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g20",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 26,
        "pdf_page": 26,
        "section": "言語知識（文法）",
        "mondai_type": "bunshou_bunpou",
        "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p26",
        "question": "[ 20 ] に入る最もよいものはどれか。",
        "options": ["気がつくはずです", "気がついたのです", "気がついたことでした", "気がつくところでした"],
        "answer": 2,
        "explanation": "過去に自分が発見・認識した事実を説明する表現「〜に気がついたのです」が文脈に合致しています。",
        "grammar_points": ["説明のノダ: 〜に気がついたのです"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g21",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 26,
        "pdf_page": 26,
        "section": "言語知識（文法）",
        "mondai_type": "bunshou_bunpou",
        "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p26",
        "question": "[ 21 ] に入る最もよいものはどれか。",
        "options": ["なら", "と", "のほかに", "について"],
        "answer": 1,
        "explanation": "「50円のはがきなら2枚買えます」のように、条件・仮定の「なら」を用いて買い物の例を挙げています。",
        "grammar_points": ["仮定助詞: なら"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g22",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 26,
        "pdf_page": 26,
        "section": "言語知識（文法）",
        "mondai_type": "bunshou_bunpou",
        "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p26",
        "question": "[ 22 ] に入る最もよいものはどれか。",
        "options": ["また", "それに", "つまり", "ところで"],
        "answer": 3,
        "explanation": "前述の具体例（電車10km、はがき2枚）を要約・言い換えて結論を導く接続詞は「つまり（＝要するに）」です。",
        "grammar_points": ["接続詞: つまり"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_g23",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題3",
        "page": 26,
        "pdf_page": 26,
        "section": "言語知識（文法）",
        "mondai_type": "bunshou_bunpou",
        "mondai_label": "問題3",
        "instruction": "つぎの文章を読んで、文章全体の内容を考えて、( ) の中に入る最もよいものを、1・2・3・4から一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p26",
        "question": "[ 23 ] に入る最もよいものはどれか。",
        "options": ["買わせたい", "買ってくれる", "買っていい", "買うようにしたい"],
        "answer": 4,
        "explanation": "今後の自分の行動方針や努力目標を表す表現は「〜ようにしたいと思っています」です。「買うようにしたい」が正解です。",
        "grammar_points": ["〜ようにしたい (努力方針)"],
        "difficulty": 2,
        "needs_review": False
    }
]

# -------------------------------------------------------------
# 4. READING (16 questions)
# -------------------------------------------------------------
reading_questions = [
    # 問題4 短文読解 (4問)
    {
        "id": "jlpt_n3_2010_12_r24",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 28,
        "pdf_page": 28,
        "section": "読解",
        "mondai_type": "dokkai_tandun",
        "mondai_label": "問題4",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p28",
        "question": "この紹介文から、山中歴史博物館についてどんなことがわかるか。",
        "options": [
            "山中町駅から歩いて10分のところにある。",
            "建物は100年以上前に建てられたものである。",
            "周りには、博物館の建物より歴史の長い公園がある。",
            "珍しい鏡が置いてあって、いつでも見ることができる。"
        ],
        "answer": 2,
        "explanation": "本文に「山中歴史博物館の建物には、100年以上の歴史があります」と明記されているため、2が正解です。駅から博物館までは公園入口まで10分＋公園内10分で計20分かかります。",
        "grammar_points": ["短文読解: 事実関係の把握"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r25",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 29,
        "pdf_page": 29,
        "section": "読解",
        "mondai_type": "dokkai_tandun",
        "mondai_label": "問題4",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p29",
        "question": "この広告から、誕生日サービスについて、どんなことがわかるか。",
        "options": [
            "3種類の飲み物とケーキの中から、どれか一つが無料でもらえる。",
            "サービスが受けられるのは、誕生日当日だけである。",
            "誕生日の1週間前までに電話で申し込まなければならない。",
            "誕生日を証明するものを店で見せなければならない。"
        ],
        "answer": 4,
        "explanation": "本文の注意書きに「＊ ご来店時に、お誕生日を証明するものをお持ちください」とあるため、4が正解です。期間は前後1週間、申し込みは「ご利用日の1週間前まで」です。",
        "grammar_points": ["短文読解: 条件の正確な読み取り"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r26",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 30,
        "pdf_page": 30,
        "section": "読解",
        "mondai_type": "dokkai_tandun",
        "mondai_label": "問題4",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p30",
        "question": "この記事から、わかることは何か。",
        "options": [
            "1か月間に本を「読まなかった人」の割合は、全体として昨年より増加した。",
            "「読まなかった人」の割合が去年より増えたのは、70歳以上だけである。",
            "20歳代の「読まなかった人」の割合は、調査が始まってから増えていない。",
            "50歳代では1か月間に本を「読まなかった人」の割合は、去年より減った。"
        ],
        "answer": 4,
        "explanation": "本文最後の文に「これに対して30歳代、40歳代、50歳代、60歳代では、去年より減少した」と書かれており、50歳代では減ったとする4が正解です。",
        "grammar_points": ["短文読解: 統計データの読み取り"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r27",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題4",
        "page": 31,
        "pdf_page": 31,
        "section": "読解",
        "mondai_type": "dokkai_tandun",
        "mondai_label": "問題4",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p31",
        "question": "このメールから、東京ホテルのサービスについて、どんなことがわかるか。",
        "options": [
            "インターネットで予約すると、1泊料金と朝食が10%割引になる場合がある。",
            "インターネットで2月中に予約すると、朝食が10%割引になる場合がある。",
            "インターネットで予約し、2月中に泊まると、1泊料金が10%割引され、朝食が無料になる場合がある。",
            "インターネット、電話、ファックスのどれで予約しても、2月中は朝食だけ無料になる場合がある。"
        ],
        "answer": 3,
        "explanation": "本文に「インターネットで予約され、2月28日までにお泊まりの方は、1泊の料金を10%割引し、ご朝食を無料にいたします」「一日10室だけ」とあるため、3が正解です。",
        "grammar_points": ["短文読解: 案内メールの条件把握"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題5 中文読解 (6問)
    {
        "id": "jlpt_n3_2010_12_r28",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (1)",
        "page": 32,
        "pdf_page": 32,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p32",
        "question": "①__だれがだれだかわかりません__とあるが、それはどうしてか。",
        "options": [
            "初めて会った人たちで、名前も知らなかったから",
            "クラスメートにだれがいたか、忘れてしまっていたから",
            "50年の間に、顔や感じが変わってしまっていたから",
            "小学生の時と今とでは、名前が変わってしまっていたから"
        ],
        "answer": 3,
        "explanation": "「50年前に卒業してから初めて開かれたクラス会でした。子どもだったみんなも、もう60歳を過ぎているので」とあり、50年という長い歳月で容姿や雰囲気が変わったことが理由です。",
        "grammar_points": ["中文読解: 理由の把握"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r29",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (1)",
        "page": 33,
        "pdf_page": 33,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p32",
        "question": "どうして何度も②__「すみません。」__と言ったのか。",
        "options": [
            "先生だとわからなくて、名前を聞いてしまったから",
            "先生の名前を、田中春子だと間違えてしまったから",
            "同級生を、クラス担任の先生だと思ってしまったから",
            "田中春子さんを、先生と間違えてしまったから"
        ],
        "answer": 1,
        "explanation": "話しかけてきた女性がクラス担任の恩師だったことに気づかず、「失礼ですが、お名前は？」と同級生のように尋ねてしまったため、恐縮して何度も謝ったのです。",
        "grammar_points": ["中文読解: 心情・発言の背景"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r30",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (1)",
        "page": 33,
        "pdf_page": 33,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p32",
        "question": "この文章を書いた人が、クラス会に出席して感じたことは何か。",
        "options": [
            "同級生がわたしの名前を忘れていて、残念だ。",
            "同級生のように、元気で若く見えるようになりたい。",
            "先生は年をとっているのに、まだ働いていて大変だ。",
            "先生のように、いつまでも元気で頑張りたい。"
        ],
        "answer": 4,
        "explanation": "文末に「わたしも先生を目標にして、毎日を過ごしていきたいと思います」と述べられており、75歳でも元気に活躍する先生を見習って頑張りたいと感じたことがわかります。",
        "grammar_points": ["中文読解: 筆者の心情・主題の把握"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r31",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (2)",
        "page": 34,
        "pdf_page": 34,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p34",
        "question": "①__そう感じさせられている__とあるが、「そう」とはどのようなことか。",
        "options": [
            "新しい電気製品が次々に作られている。",
            "新しい電気製品は以前のものより便利になった。",
            "携帯電話を作る会社がどんどん増えている。",
            "携帯電話でお金が支払えるようになった。"
        ],
        "answer": 2,
        "explanation": "直前に「製品を作った会社は、新しい製品はいろいろなことができるから、これまでより便利になったと宣伝し」とあることから、「新しい電気製品は以前のものより便利になった」を指します。",
        "grammar_points": ["指示語: そうの指す内容"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r32",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (2)",
        "page": 34,
        "pdf_page": 34,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p34",
        "question": "この文章では、新製品を作る場合、会社が一番に考えていることは何だと言っているか。",
        "options": [
            "ボタンの数が少ない製品にすること",
            "使い方がわかりやすい製品にすること",
            "いろいろなことができる製品を作ること",
            "みんなが使いやすい製品を数多く作ること"
        ],
        "answer": 3,
        "explanation": "第3段落冒頭に「会社は、新しい製品を作るとき、いろいろなことができるようにすることを第一にして、使いやすさのことはあまり考えてこなかったようだ」と述べられています。",
        "grammar_points": ["中文読解: 筆者の指摘する事実の把握"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r33",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題5 (2)",
        "page": 34,
        "pdf_page": 34,
        "section": "読解",
        "mondai_type": "dokkai_chuubun",
        "mondai_label": "問題5",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p34",
        "question": "電気製品について、この文章を書いた人が感じていることは何か。",
        "options": [
            "新しい製品が次々とできて、生活が便利になった。",
            "以前の製品の方が、いろいろなことができてよかった。",
            "新しい製品を作るときは、使いやすさを考えることが大切である。",
            "今までできなかったことができる製品を作ることが大切である。"
        ],
        "answer": 3,
        "explanation": "筆者は、機能が増えても使い方が複雑になっては本当に便利とは言えないと主張しており、使いやすさを配慮することが重要だと感じています。",
        "grammar_points": ["中文読解: 筆者の意見・主張の把握"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題6 長文読解 (4問)
    {
        "id": "jlpt_n3_2010_12_r34",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題6",
        "page": 36,
        "pdf_page": 36,
        "section": "読解",
        "mondai_type": "dokkai_choubun",
        "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p35",
        "question": "①__1000円カットの店へ髪を切りに行ってみた__のはなぜか。",
        "options": [
            "男性に人気がある店だったから",
            "忙しくて時間がなかったから",
            "家の近くにある店だったから",
            "いつもの美容院は高いから"
        ],
        "answer": 2,
        "explanation": "第1段落で「たった10分で髪を切ってくれる」点に触れ、最終文でも「忙しいときはこちらの店でもいいと今では思っている」とある通り、短時間で手早く切れる（忙しくて時間がなかった）ことが動機です。",
        "grammar_points": ["長文読解: 行動の動機・理由"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r35",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題6",
        "page": 36,
        "pdf_page": 36,
        "section": "読解",
        "mondai_type": "dokkai_choubun",
        "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p35",
        "question": "②__どうしてこんなに安くできるのだろうか__とあるが、この店の人は、値段を安くするために最も大事なことは何だと言っているか。",
        "options": [
            "安く借りられる場所に店を開くこと",
            "客の髪を洗わないようにすること",
            "短時間で多くの客の髪を切ること",
            "女性のためのサービスを増やすこと"
        ],
        "answer": 1,
        "explanation": "第2段落に「店の人によると、この値段で店を経営していくためには、家賃が安いところを借りることが一番大切なのだそうだ」と明確に書かれています。",
        "grammar_points": ["長文読解: 詳細情報の抽出"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r36",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題6",
        "page": 36,
        "pdf_page": 36,
        "section": "読解",
        "mondai_type": "dokkai_choubun",
        "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p35",
        "question": "この店の人は、1000円カットの店で、女性客を増やすのに一番効果的だったのは何だと言っているか。",
        "options": [
            "壁の色を明るく優しい色に変えたこと",
            "女性だけが使える割引券を配ったこと",
            "女性向けの雑誌の種類を増やしたこと",
            "子どもを遊ばせておく場所を作ったこと"
        ],
        "answer": 4,
        "explanation": "第3段落に「特に効果があったのは、店の中に子どもが遊べる場所を作ったことで、子どもを連れた女性客が少しずつ増えていったそうである」と書かれています。",
        "grammar_points": ["長文読解: 最も効果的だった施策の把握"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r37",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題6",
        "page": 36,
        "pdf_page": 36,
        "section": "読解",
        "mondai_type": "dokkai_choubun",
        "mondai_label": "問題6",
        "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p35",
        "question": "この文章を書いた人は今、どう考えているか。",
        "options": [
            "1000円カットの店は値段が安いので、あまり上手でなくてもしかたない。",
            "1000円カットの店がどんなに工夫をしても、女性はあまり行かないだろう。",
            "時間がない時は、先日行った1000円カットの店を今後も利用してもいい。",
            "十分満足できたので、今後は先日行った1000円カットの店を利用したい。"
        ],
        "answer": 3,
        "explanation": "文末に「カットの技術もかなり満足できるものだったので、忙しいときはこちらの店でもいいと今では思っている」と述べられており、時間がない時は今後も利用したいと考えています。",
        "grammar_points": ["長文読解: 筆者の現状の考え・結論の把握"],
        "difficulty": 2,
        "needs_review": False
    },

    # 問題7 情報検索 (2問)
    {
        "id": "jlpt_n3_2010_12_r38",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題7",
        "page": 37,
        "pdf_page": 37,
        "section": "読解",
        "mondai_type": "dokkai_jouhou_kensaku",
        "mondai_label": "問題7",
        "instruction": "右のページを見て、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p38",
        "question": "田中さんの高校生の娘は、この会館で踊りを習うことにした。田中さんは、毎回車で娘を会館に送って行くので、週に1回だけ、娘と同じ曜日・時間に何か別のものを習いたいと思っている。田中さんはどの教室だったら参加できるか。",
        "options": ["折り紙", "お茶", "お花", "日本料理"],
        "answer": 1,
        "explanation": "娘の「踊り」は火・土の18:30〜20:00です。この同じ時間帯で「週に1回だけ」開講されているのは火曜日の「折り紙」（18:30〜20:00）です。",
        "grammar_points": ["情報検索: スケジュール条件のマッチング"],
        "difficulty": 2,
        "needs_review": False
    },
    {
        "id": "jlpt_n3_2010_12_r39",
        "book": "JLPT N3 2010 December",
        "book_code": "jlpt_n3_2010_12",
        "unit": "問題7",
        "page": 37,
        "pdf_page": 37,
        "section": "読解",
        "mondai_type": "dokkai_jouhou_kensaku",
        "mondai_label": "問題7",
        "instruction": "右のページを見て、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
        "passage_id": "jlpt_n3_2010_12_p38",
        "question": "山田大学の留学生リーさんは、この会館で柔道の教室に参加したいと思っているが、柔道着を持っていない。リーさんは、参加料と柔道着をどうしたらいいか。",
        "options": [
            "参加料7,000円を払い、柔道着は文化会館で借りる。",
            "参加料5,000円を払い、柔道着は文化会館で借りる。",
            "参加料7,000円を払い、柔道着は自分で買う。",
            "参加料5,000円を払い、柔道着は自分で買う。"
        ],
        "answer": 4,
        "explanation": "リーさんは大学生（学生）。柔道は週2回（月・木）なので参加料は学生料金の「5,000円」です。また、その他欄に「柔道着は自分で準備してください。会館でも売っています（貸し出しはなし）」とあるため、「柔道着は自分で買う」が正解です。",
        "grammar_points": ["情報検索: 料金表と注意事項の照合"],
        "difficulty": 2,
        "needs_review": False
    }
]

# -------------------------------------------------------------
# Save to bank/jlpt_n3_2010_12
# -------------------------------------------------------------
(OUT_DIR / "passages.json").write_text(json.dumps(passages, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT_DIR / "vocab.json").write_text(json.dumps({"questions": vocab_questions}, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT_DIR / "grammar.json").write_text(json.dumps({"questions": grammar_questions}, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT_DIR / "reading.json").write_text(json.dumps({"questions": reading_questions}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"JLPT N3 2010 December successfully built:")
print(f"  - Vocab: {len(vocab_questions)} questions")
print(f"  - Grammar: {len(grammar_questions)} questions")
print(f"  - Reading: {len(reading_questions)} questions")
print(f"  - Passages: {len(passages)} passages")
