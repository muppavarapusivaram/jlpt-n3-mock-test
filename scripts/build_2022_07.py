# -*- coding: utf-8 -*-
"""
build_2022_07.py
Builds JLPT N3 2022 July question bank:
- vocab.json (34 questions)
- grammar.json (22 questions)
- reading.json (16 questions)
- passages.json (9 passages)
"""

import json
from pathlib import Path

OUT_DIR = Path("bank/jlpt_n3_2022_07")
OUT_DIR.mkdir(parents=True, exist_ok=True)

passages = {
    "jlpt_n3_2022_07_p06": {
        "passage_id": "jlpt_n3_2022_07_p06",
        "book_id": "jlpt_n3_2022_07",
        "unit": "文法",
        "page": 6,
        "pdf_page": 6,
        "mondai_number": 3,
        "title": "工場見学",
        "author": "コルホネン アーロン",
        "content": "日本に来る前に、日本には無料で工場見学ができるところがあると聞いて、面白そうだと思いました。日本に行ったら絶対に行こうと思っていたのですが、先月ついに行くことができました。\n　[ 19 ] のはアイスクリームの会社の工場です。工場では、機械を使って、材料を混ぜたり型に入れたり凍らせたりしていました。工場の人の説明は丁寧で、機械や商品の説明が書かれた資料もくれたので、よくわかりました。できたばかりのアイスも食べさせてくれました。工場見学は本当に楽しかったです。[ 20 ]、どうして無料で見学をさせてくれるのかわかりませんでした。\n　調べてみたら、工場見学は、会社側にもいいことがあるとわかりました。ある新聞の調査によると、工場見学をした人の大部分が、[ 21 ] で作られている商品を好きになり、会社に対するイメージもよくなったそうです。実際に、私も工場見学をした会社の印象が前よりよくなりました。\n　日本には、他にも同じような工場見学ができるところがたくさんあるそうです。今、次に見学に行く工場を探しています。日本にいる間にいろいろな工場に見学に [ 22 ]。"
    },
    "jlpt_n3_2022_07_p07_1": {
        "passage_id": "jlpt_n3_2022_07_p07_1",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 7,
        "pdf_page": 7,
        "mondai_number": 4,
        "title": "学期の目標",
        "author": None,
        "content": "日本語学校の新学期が始まったとき、クラス全員がそれぞれ、学期の目標を紙に書いて教室にはっておくことになった。私は漢字を500字覚えることにしたが、やってみると大変だった。でも、教室に入ると、自分で書いた目標が目に入るし、クラスのみんなも知っているから、簡単にはやめられない。そのおかげで、学期末には目標の500字を覚えることができた。目標を心の中で決めるだけではなく、紙に書いて教室にはったのがよかったのだ。"
    },
    "jlpt_n3_2022_07_p07_2": {
        "passage_id": "jlpt_n3_2022_07_p07_2",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 7,
        "pdf_page": 7,
        "mondai_number": 4,
        "title": "京都の旅 申し込み確認メール",
        "author": "石野旅行 予約課 岩坂",
        "content": "これはある旅行会社が客の水川さんに書いたメールである。\n\n水川真理様\n「京都の旅2泊3日」へのお申し込み、ありがとうございました。下のご予約内容をご確認いただき、ご出発日の1週間前までに旅行代金をお振り込みください。\nなお、ご出発日の20日前以降のお取り消しには、キャンセル料が発生します(20日前〜8日前まで20%、7日前〜前日まで30%、当日100%)。\nご質問などございましたら、ご連絡ください。\n\n＜ご予約内容＞\nツアー名：京都の旅2泊3日\n出発日：2月13日\n代金合計86,000円（税込）\n振り込み先：あおば銀行西島支店 普通 1234567 石野旅行\n石野旅行 予約課 岩坂\n電話：051-960-7451 FAX：051-960-7452"
    },
    "jlpt_n3_2022_07_p08_1": {
        "passage_id": "jlpt_n3_2022_07_p08_1",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 8,
        "pdf_page": 8,
        "mondai_number": 4,
        "title": "郵便局のお年寄り訪問サービス",
        "author": None,
        "content": "郵便局と聞くと、まず思いつくのは手紙や荷物の配達だろう。だが、こんな意外なサービスがあることを知っているだろうか。一人暮らしをしているお年寄りとその家族の安心のため、郵便局員がお年寄りの家を訪問する。そして、そのときのお年寄りの様子をEメールで家族に教えてくれるのだ。親になかなか会いに行けない人には、うれしいサービスだ。"
    },
    "jlpt_n3_2022_07_p08_2": {
        "passage_id": "jlpt_n3_2022_07_p08_2",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 8,
        "pdf_page": 8,
        "mondai_number": 4,
        "title": "研究会の準備メモ",
        "author": None,
        "content": "ナムさん\n来週の「会話の文法研究会」ですが、申し込みが予想より増えています。\n参加者は60名ぐらいになりそうですから、資料をあと20部お願いします。\nそれから、今日、大学の事務所で、教室の予約を304から201に変えてもらいました。研究会の会員にメールでお知らせしておきますが、当日も304のドアに、教室が変わったことを知らせる紙をはったほうがいいと思うので、作っておいてください。"
    },
    "jlpt_n3_2022_07_p09": {
        "passage_id": "jlpt_n3_2022_07_p09",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 9,
        "pdf_page": 9,
        "mondai_number": 5,
        "title": "水筒の使い分け",
        "author": None,
        "content": "今年の夏、初めて水筒を買った。今まで、飲み物はペットボトルを買っていたが、一ヶ月に五千円もかかっていたのだ。\n　買ったのは、コップが付いていない、直接口をつけて飲む水筒で、飲み物の温度が長時間変わらない物だ。コップが付いている水筒もあったが、毎回コップに入れるのはめんどくさいと思ったので、①この水筒にした。\n　夏は一日中冷たいものが飲めたので良かったのだが、冬になって熱い飲み物を入れたら、②困ったことが起きた。熱すぎて、直接は飲めなかったのだ。最初は1本あれば十分だと思っていたが、結局、コップ付きの水筒も買った。コップがあれば冷ますことができる。どちらの水筒もそれほど高くはなかったが、③最初に考えていたよりはお金がかかってしまった。でも、季節によって違う水筒を使うのも楽しいし、ペットボトルも買わなくなったのでこれでよかったと思っている。"
    },
    "jlpt_n3_2022_07_p10": {
        "passage_id": "jlpt_n3_2022_07_p10",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 10,
        "pdf_page": 10,
        "mondai_number": 5,
        "title": "カラス問題と解決の試み",
        "author": None,
        "content": "日本では、町の中でカラスをよく見ます。カラスという鳥は平気で人間に向かって飛んできたり、食べ物を取ったりするので、嫌がる人もいます。\n　私の町では、毎日夕方になると、たくさんのカラスが、公園の木で寝るために集まってきます。声がうるさいし、数が非常に多いので怖さを感じることもあります。それで町の人たちはとても困っています。①この問題の解決方法はあるのでしょうか。\n　ある町では、専門家の協力で一つの②実験に成功しました。安全な状態にいるときと危険を感じたときのカラスの鳴き方の違いを利用して、「いてほしくない場所」から「集まっても問題のない場所」にカラスを移動させることができたそうです。\n　しかし、私の町には大きな森など、カラスが「集まっても問題のない場所」はありません。ですから、同じ方法は使えそうにありません。私の町に合った解決方法が見つかればいいと思います。"
    },
    "jlpt_n3_2022_07_p11": {
        "passage_id": "jlpt_n3_2022_07_p11",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 11,
        "pdf_page": 11,
        "mondai_number": 6,
        "title": "両親への結婚記念日プレゼントと電気ろうそく",
        "author": None,
        "content": "私は両親の結婚記念日に毎年違うプレゼントを送っていて、実家の両親も楽しみにしてくれている。ただ、もう20年以上続けているので、だんだんアイディアがなくなってきた。今年は、前にあげたことがあるものでもしかたないと、①あきらめ始めていた。\n　そんなとき、友達から旅行のお土産に小さい箱に入ったおしゃれなろうそくをもらった。その夜、さっそく火をつけてみた。不規則にやさしく火がゆれて、それを見ていると気持ちが落ちついた。\n　箱には、ろうそくの効果についての②説明の紙も入っていた。ろうそくの火に、嫌なにおいを消す効果があることは知っていたが、料理をおいしく見せる効果があることは初めて知った。それを読んで私は、「両親へのプレゼントにいいかもしれない」と思いついた。ろうそくはあげたことがないし、これを使えば、結婚記念日の夜のごちそうがもっとおいしく感じるだろう。\n　しかし、しばらく火を見つめていると、ちょっと心配になってきた。食事のあとで消し忘れることもあるかもしれない。それに、両親の家では猫を飼っているので、何が起こるかわからない。\n　③ろうそくはやっぱりやめたほうがいいと思ったが、あきらめられずに一緒に入っていたカタログを見ていた。すると、実物の火そっくりにゆれて、同じような効果もある「電気のろうそく」があるのを見つけた。これなら、安全に使えそうだ。\n　結婚記念日まではまだ2週間ある。このタイプには、ほかにも種類があるようなので、もう少し調べてみようと思う。"
    },
    "jlpt_n3_2022_07_p12": {
        "passage_id": "jlpt_n3_2022_07_p12",
        "book_id": "jlpt_n3_2022_07",
        "unit": "読解",
        "page": 12,
        "pdf_page": 12,
        "mondai_number": 7,
        "title": "中村ギター教室 生徒募集",
        "author": "中村カズオ",
        "content": "中村ギター教室 生徒募集\n★初めての方にもわかりやすく教えます。\n★教室に通うかどうか決める前に、60分の「特別割引レッスン」(1000円)を1回受けることができます。\n\n「講師」 中村カズオ (西日本音楽大学卒業)\n「時間」 1回90分(毎日10時〜21時の間) ※日時は、講師と予約を相談して決めます。\n「レッスンのタイプ」\n個人レッスンと、2〜3名で申し込めるグループレッスンがあります。\n「1ヵ月の料金」 （グループレッスンは1名分の料金）\n・月2回：個人 7,000円 ／ グループ 6,000円\n・月3回：個人 10,000円 ／ グループ 8,000円\n・月4回：個人 13,000円 ／ グループ 10,000円\n\n学生割引：学生の方は、上の表の料金から毎月1000円割引します。\n平日昼間割引：平日昼間(月〜金の17時までに終了)にレッスンを受ける方は、上の表の料金から毎月2000円割引します。\n※二つの割引を同時に使うことはできません。\n※毎月の料金は、前の月の最終日までにお支払いください。\n\n「特別割引レッスン」\n・メールに、お名前、連絡先、レッスンのタイプ、希望日時を書いてお申し込みください。\n・グループレッスンを希望する方は、代表の方がお申し込みください。\n・料金(一人1000円)は、当日お支払いください。\n・自分のギターでレッスンを受けたい方は持ってきてください。持ってこられない方には、無料で教室のギターをお貸しします。\n中村ギター教室 〒120-5599 春中市高木町6-2-3（春中駅から徒歩1分）\nホームページ https://nakamuraguitaryuukibui.jp  Eメール k-nakamura@guitar.com"
    }
}

with open(OUT_DIR / "passages.json", "w", encoding="utf-8") as f:
    json.dump(passages, f, ensure_ascii=False, indent=2)
print("Saved passages.json")

# Vocab (34 Questions)
vocab_questions = [
    # 問題1
    {"id": "jlpt_n3_2022_07_v_q01", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "その会社の__情報__は、インターネットで見ました。", "options": ["じょうほう", "ちょうほう", "じょうぼう", "ちょうぼう"], "answer": 1, "grammar_points": [], "difficulty": 1, "explanation": "「情報」の読み方は「じょうほう」です。"},
    {"id": "jlpt_n3_2022_07_v_q02", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "兄は、__現在__は海外で働いています。", "options": ["けんさい", "げんさい", "けんざい", "げんざい"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「現在」の読み方は「げんざい」です。"},
    {"id": "jlpt_n3_2022_07_v_q03", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "小さくて__丸い__いすがほしい。", "options": ["くろい", "まるい", "あおい", "かるい"], "answer": 2, "grammar_points": [], "difficulty": 1, "explanation": "「丸い」の読み方は「まるい」です。"},
    {"id": "jlpt_n3_2022_07_v_q04", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "その歌は日本でも__有名__です。", "options": ["ゆめ", "ゆめい", "ゆうめ", "ゆうめい"], "answer": 4, "grammar_points": [], "difficulty": 1, "explanation": "「有名」の読み方は「ゆうめい」です。"},
    {"id": "jlpt_n3_2022_07_v_q05", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "そこの通りの__角__に、コンビニができるそうです。", "options": ["かど", "そば", "はし", "よこ"], "answer": 1, "grammar_points": [], "difficulty": 1, "explanation": "「角」の読み方は「かど」です。"},
    {"id": "jlpt_n3_2022_07_v_q06", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "大切な物なので、丁寧に__包んで__ください。", "options": ["たたんで", "はこんで", "すすんで", "つつんで"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「包んで」の読み方は「つつんで」です。"},
    {"id": "jlpt_n3_2022_07_v_q07", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 1, "mondai_type": "kanji_reading", "mondai_label": "問題1", "instruction": "______の言葉の読み方として最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "それは、もう__計算__しました。", "options": ["けいけん", "けけん", "けいさん", "けさん"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「計算」の読み方は「けいさん」です。"},

    # 問題2
    {"id": "jlpt_n3_2022_07_v_q08", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私は毎日、どのくらい歩いたか__きろく__している。", "options": ["基緑", "記緑", "基録", "記録"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「きろく」は漢字で「記録」と書きます。"},
    {"id": "jlpt_n3_2022_07_v_q09", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "駅で新しい__こうこく__を見ました。", "options": ["校菅", "校告", "広営", "広告"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「こうこく」は漢字で「広告」と書きます。"},
    {"id": "jlpt_n3_2022_07_v_q10", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "体がすっかり__ひえて__しまいました。", "options": ["冷えて", "寒えて", "氷えて", "低えて"], "answer": 1, "grammar_points": [], "difficulty": 1, "explanation": "「ひえて」は漢字で「冷えて」と書きます。"},
    {"id": "jlpt_n3_2022_07_v_q11", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__けんさ__はしたが何も問題はなかった。", "options": ["健査", "検査", "検察", "健察"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "「けんさ」は漢字で「検査」と書きます。"},
    {"id": "jlpt_n3_2022_07_v_q12", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "その話は__たしか__ですか。", "options": ["定か", "確か", "必か", "常か"], "answer": 2, "grammar_points": [], "difficulty": 1, "explanation": "「たしか」は漢字で「確か」と書きます。"},
    {"id": "jlpt_n3_2022_07_v_q13", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 1, "pdf_page": 1, "section": "言語知識（文字・語彙）", "mondai_number": 2, "mondai_type": "orthography", "mondai_label": "問題2", "instruction": "______のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私の祖父は、日本の__かいが__をたくさん持っている。", "options": ["絵面", "図面", "絵画", "図画"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「かいが」は漢字で「絵画」と書きます。"},

    # 問題3
    {"id": "jlpt_n3_2022_07_v_q14", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "たまねぎとにんじんは皮を ( ) から料理に使ってください。", "options": ["むいて", "ほって", "破って", "離して"], "answer": 1, "grammar_points": [], "difficulty": 1, "explanation": "野菜や果物の皮を取り除くことを「皮をむく」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q15", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "この国には石油やガスなどの ( ) があまりありません。", "options": ["栄養", "資源", "内容", "部品"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "石油や天然ガスなどは天然「資源」と呼ばれます。"},
    {"id": "jlpt_n3_2022_07_v_q16", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "一生懸命頑張ったのに、試合に負けてしまって、とても ( ) です。", "options": ["まずしかった", "あやしかった", "くやしかった", "ずるかった"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "努力したのに失敗や敗北して残念で無念な気持ちを「くやしい」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q17", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "旅行に行けなくなったので、ホテルの予約を ( ) した。", "options": ["ピックアップ", "キャンセル", "ディスカウント", "チェックアウト"], "answer": 2, "grammar_points": [], "difficulty": 1, "explanation": "予約を取り消すことを「キャンセル」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q18", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "コーヒーをこぼして、白いズボンに ( ) ができてしまった。", "options": ["穴", "影", "こぶ", "しみ"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "液体などで布などにできる汚れを「しみ」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q19", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "兄を起こすために、部屋の外からドアを強く ( )。", "options": ["たたいた", "さわった", "つかまえた", "なでた"], "answer": 1, "grammar_points": [], "difficulty": 1, "explanation": "音を立てて気づかせるためにドアを「たたく」動作が適切です。"},
    {"id": "jlpt_n3_2022_07_v_q20", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "交通事故を ( ) ために、ここに横断歩道を作るそうです。", "options": ["直す", "逃す", "防ぐ", "守る"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "事故や被害が起きないように防止することを「防ぐ」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q21", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "のどが ( ) ので、何か飲みたいです。", "options": ["へった", "すいた", "かわいた", "やせた"], "answer": 3, "grammar_points": [], "difficulty": 1, "explanation": "水分を欲する状態を「のどがかわいた」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q22", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "行きは佐藤さんと2人で来たが、帰りは ( ) だった。", "options": ["様々", "半々", "別々", "色々"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "一緒ではなく各自それぞれで行動することを「別々」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q23", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "留学については、両親とよく ( )、決めるつもりだ。", "options": ["取り込んで", "言い返して", "受け取って", "話し合って"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "互いに意見を交わして相談することを「話し合う」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q24", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 3, "mondai_type": "contextual_defining", "mondai_label": "問題3", "instruction": "( ) に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日の夜から歯が痛くて、( ) します。", "options": ["とんとん", "ざあざあ", "ずきずき", "からから"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "脈打つように痛む様子を「ずきずき」と言います。"},

    # 問題4
    {"id": "jlpt_n3_2022_07_v_q25", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__ふだん__と同じようにやってください。", "options": ["みんな", "昔", "いつも", "例"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「ふだん」は日常・平生を指し、「いつも」と同義です。"},
    {"id": "jlpt_n3_2022_07_v_q26", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "あの人は__短気__だ。", "options": ["すぐ怒る", "すぐ謝る", "すぐ驚く", "すぐ喜ぶ"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "「短気」は気が短く「すぐ怒る」性質を指します。"},
    {"id": "jlpt_n3_2022_07_v_q27", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "12時に__グラウンド__に来てください。", "options": ["屋上", "体育館", "公園", "運動場"], "answer": 4, "grammar_points": [], "difficulty": 1, "explanation": "「グラウンド」は「運動場」と同義です。"},
    {"id": "jlpt_n3_2022_07_v_q28", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "私の__おい__は東京に住んでいます。", "options": ["姉の息子", "姉の娘", "父の弟", "父の妹"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "「おい」は兄弟姉妹の男子を指すため、「姉の息子」が同義です。"},
    {"id": "jlpt_n3_2022_07_v_q29", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 2, "pdf_page": 2, "section": "言語知識（文字・語彙）", "mondai_number": 4, "mondai_type": "paraphrases", "mondai_label": "問題4", "instruction": "______に意味が最も近いものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "もっと__くわしく__説明してください。", "options": ["早く", "細かく", "簡単に", "熱心に"], "answer": 2, "grammar_points": [], "difficulty": 1, "explanation": "「くわしく」は詳細に、「細かく」と同義です。"},

    # 問題5
    {"id": "jlpt_n3_2022_07_v_q30", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__諦める__", "options": ["今日は天気がいいから、傘を諦めてよさそうた。", "台風が来そうなので、あしたの登山を諦めることにした。", "家を出てすぐに、鍵をかけるのを諦めたことに気づいた。", "悲しい小説だったので、泣くのを諦められなかった。"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "「登山を諦める」のように、見込みがないとして断念する用法が適切です。"},
    {"id": "jlpt_n3_2022_07_v_q31", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__参加__", "options": ["赤ちゃんが家族に参加したので、生活が変わった。", "山川さんが事故に参加して、足をけがしたそうだ。", "あしたは息子と一緒にパーティーに参加するつもりだ。", "父は貿易会社に参加しているので、出張は海外が多い。"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "集まりや催し物に加わることを「参加する」と言い、「パーティーに参加する」が正解です。"},
    {"id": "jlpt_n3_2022_07_v_q32", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__盛ん__", "options": ["あしたは試合なので、今日は練習時間が盛んだった。", "今日は荷物が盛んなので、大きなかばんが必要だ。", "このレストランは、魚も野菜も盛んでおいしい。", "この町は以前から外国人との交流が盛んだ。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "活動や交流などが活発に行われていることを「盛ん（交流が盛ん）」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q33", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__整理__", "options": ["机の引き出しを整理して、いらない物を捨てました。", "家の廊下が汚れていたので、ぞうきんで整理しました。", "長い間使っていない部屋の窓を開けて、空気を整理した。", "虫歯になると困るので、毎回、食事の後で歯を整理している。"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "乱れたものを片付けて不要なものを処分することを「整理する」と言います。"},
    {"id": "jlpt_n3_2022_07_v_q34", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文字・語彙", "page": 3, "pdf_page": 3, "section": "言語知識（文字・語彙）", "mondai_number": 5, "mondai_type": "usage", "mondai_label": "問題5", "instruction": "つぎのことばの使い方として最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "__通り過ぎる__", "options": ["さっき店の前を自転車で通り過ぎたのは、木村さんだと思う。", "バスが遅れて、待ち合わせの時間を通り過ぎてしまった。", "今日はご飯の量を通り過ぎて、おなかがいっぱいだ。", "締め切りを通り過ぎないように、書類は早めに出したほうがいい。"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "ある場所を通過して先へ進むことを「通り過ぎる」と言います。"}
]

vocab_data = {"book_id": "jlpt_n3_2022_07", "book_title": "JLPT N3 2022年7月 過去問", "unit": "文字・語彙", "questions": vocab_questions}
with open(OUT_DIR / "vocab.json", "w", encoding="utf-8") as f:
    json.dump(vocab_data, f, ensure_ascii=False, indent=2)
print("Saved vocab.json (34 questions)")

# Grammar (22 Questions)
grammar_questions = [
    # 問題1
    {"id": "jlpt_n3_2022_07_g_q01", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "友達がおいしいカレー屋があると言って連れていってくれた。友達と同じものを頼んだが、私（ ）辛すぎた。", "options": ["で", "へ", "には", "より"], "answer": 3, "grammar_points": ["〜には（評価の対象）"], "difficulty": 2, "explanation": "評価や判断の基準・主体を表す「私には（辛すぎた）」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q02", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "A「（ ）絵本、知ってる？」\nB「うん、知ってるよ。子供のとき、大好きだった。」", "options": ["「大きな家」と", "「大きな家」って", "「大きな家」でも", "「大きな家」なんか"], "answer": 2, "grammar_points": ["〜って（話題提示）"], "difficulty": 1, "explanation": "名称や題目を取り立てる会話表現「〜って」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q03", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "昨日見た映画は、面白いと聞いていたのに（ ）面白くなかった。", "options": ["やっと", "すっかり", "せっかく", "ちっとも"], "answer": 4, "grammar_points": ["ちっとも〜ない"], "difficulty": 2, "explanation": "否定と呼応して「少しも〜ない」を表す「ちっとも（面白くなかった）」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q04", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "近所のパン屋は、パンの種類が多い。一年中売っているパン（ ）季節ごとに発売されるパンもある。", "options": ["のほかに", "のことで", "に比べて", "について"], "answer": 1, "grammar_points": ["〜のほかに"], "difficulty": 2, "explanation": "「〜に加えて、別に」を表す「のほかに」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q05", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "夫は、プロのサッカー選手として活動する（ ）大学院でスポーツ科学を学んでいる。", "options": ["点で", "一方で", "としたら", "のだから"], "answer": 2, "grammar_points": ["〜一方で"], "difficulty": 2, "explanation": "二つの活動を並行して行うことを表す「一方で」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q06", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "もうすぐ夏だ。（ ）エアコンが問題なく動くかどうか、確認しておこうと思う。", "options": ["暑くなるまで", "暑くなる前に", "暑くするまで", "暑くする前に"], "answer": 2, "grammar_points": ["〜前に"], "difficulty": 1, "explanation": "夏が来て「暑くなる前に」準備をする文脈です。"},
    {"id": "jlpt_n3_2022_07_g_q07", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "新しいパソコンを買って1か月（ ）使っていないのに、壊れてしまった。", "options": ["ごろしか", "ごろだけ", "ぐらいしか", "ぐらいだけ"], "answer": 3, "grammar_points": ["数量詞＋しか〜ない"], "difficulty": 2, "explanation": "期間「1か月ぐらい」に限定と不満を表す「しか（使っていない）」が続きます。"},
    {"id": "jlpt_n3_2022_07_g_q08", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "(薬局で)\n店員「この薬を1日3回、食事の後に飲んでください。飲むと眠く（ ）、飲んだ後、車の運転などはしないでください。」", "options": ["なればいいので", "なったばかりなので", "なることがあるので", "なってはいけないので"], "answer": 3, "grammar_points": ["〜ことがある"], "difficulty": 2, "explanation": "副作用として眠くなる可能性があることを表す「なることがあるので」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q09", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "(インタビューで)\n選手「優勝できたのは皆さんの応援の（ ）。ありがとうございました。」", "options": ["はずです", "ようです", "ことです", "おかげです"], "answer": 4, "grammar_points": ["〜のおかげです"], "difficulty": 1, "explanation": "好ましい結果への恩恵や感謝を表す「おかげです」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q10", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 4, "pdf_page": 4, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "(電話で)\n田中「はい、営業課の田中です。」\n石山「会計課の石山ですが、今ちょっとよろしいですか。」\n田中「すみません。これから会議なんです。」\n石山「わかりました。では、またあとで（ ）。」", "options": ["かけ直します", "かけ出します", "かけています", "かけておきます"], "answer": 1, "grammar_points": ["〜直す（やり直す）"], "difficulty": 1, "explanation": "電話を再度かけるビジネス表現「かけ直します」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q11", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "(玄関で)\n妻「あれ、出かけるの？散歩？」\n夫「うん」\n妻「じゃあ、帰りにスーパーで卵を（ ）？」\n夫「わかった。」", "options": ["買っていってもらわない", "買っていってくれない", "買ってきてもらわない", "買ってきてくれない"], "answer": 4, "grammar_points": ["〜てきてくれない？（依頼）"], "difficulty": 2, "explanation": "出先から戻るときに買ってきてほしいと依頼する表現「買ってきてくれない？」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q12", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "村山「中野さん、3月で会社を辞めるって本当ですか。」\n中野「はい、私、4月から（ ）。」", "options": ["留学することにしたんです", "留学することにしそうです", "留学したことがあるんです", "留学したことがありそうです"], "answer": 1, "grammar_points": ["〜ことにした（意志・決定）"], "difficulty": 2, "explanation": "自分自身で決断した進路を説明する「留学することにしたんです」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q13", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 1, "mondai_type": "bunpou_keishiki", "mondai_label": "問題1", "instruction": "つぎの文の（ ）に入れるのに最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": None, "question": "(銀行のホームページで)\nキャッシュカードの暗証番号は決して他人に（ ）。", "options": ["知ってはいけません", "知らせにくいです", "知られないようにしてください", "知らないほうがいいでしょう"], "answer": 3, "grammar_points": ["受身＋〜ようにしてください"], "difficulty": 2, "explanation": "他人に知られる事態を防ぐための注意・指示表現「知られないようにしてください」が入ります。"},

    # 問題2
    {"id": "jlpt_n3_2022_07_g_q14", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "私は、森先生の授業を受けてから数学が好きになった。 ______ ______ ★ ______ いないと思う。", "options": ["先生は", "先生ほど", "あの", "わかりやすく教えてくれる"], "answer": 4, "grammar_points": ["〜ほど〜はいない"], "difficulty": 2, "explanation": "語順は「あの(3) 先生ほど(2) ★わかりやすく教えてくれる(4) 先生は(1) いないと思う。」となり、★には4が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q15", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "「今日は、コーラを使った鶏肉の煮物を紹介します。鶏肉は ______ ______ ★ ______ 知っていますか。」", "options": ["煮ることで", "柔らかく", "コーラで", "なるのを"], "answer": 2, "grammar_points": ["〜ことで〜になるのを"], "difficulty": 2, "explanation": "語順は「鶏肉は コーラで(3) 煮ることで(1) ★柔らかく(2) なるのを(4) 知っていますか。」となり、★には2が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q16", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "山下「今度、北森町に行くんだけど、北森町のレストランでどこかいいところ、知ってる？」\n南「私はあまり知らないんだけど、田中さん ______ ______ ★ ______ どう？」", "options": ["が", "聞いてみたら", "から", "北森町に住んでいる"], "answer": 3, "grammar_points": ["〜から聞いてみたらどう？"], "difficulty": 2, "explanation": "語順は「田中さん が(1) 北森町に住んでいる(4) ★から(3) 聞いてみたら(2) どう？」となり、★には3が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q17", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "林「タンさんは、夏休みに国へ帰りますか。」\nタン「いいえ、今年は帰りません。日本で ______ ______ ★ ______ なので楽しみです。」", "options": ["今年が", "過ごすのは", "初めて", "夏休みを"], "answer": 1, "grammar_points": ["〜のは〜が初めて"], "difficulty": 2, "explanation": "語順は「日本で 夏休みを(4) 過ごすのは(2) ★今年が(1) 初めて(3) なので楽しみです。」となり、★には1が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q18", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 5, "pdf_page": 5, "section": "言語知識（文法）", "mondai_number": 2, "mondai_type": "bun_kumitate", "mondai_label": "問題2", "instruction": "次の文の ★ に入る最もよいものを、1・2・3・4から一つ選びなさい。", "passage_id": None, "question": "さくら大学の周りには、レストランや喫茶店などの ______ ______ ★ ______ ある。", "options": ["中心に", "飲食店を", "いろいろな店が", "本屋や美容院など"], "answer": 4, "grammar_points": ["〜を中心に〜など"], "difficulty": 3, "explanation": "語順は「飲食店を(2) 中心に(1) ★本屋や美容院など(4) いろいろな店が(3) ある。」となり、★には4が入ります。"},

    # 問題3
    {"id": "jlpt_n3_2022_07_g_q19", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p06", "question": "[ 19 ] のはアイスクリームの会社の工場です。", "options": ["見学する", "見学した", "見学している", "見学してある"], "answer": 2, "grammar_points": ["〜たのは（過去の特定）"], "difficulty": 1, "explanation": "先月実際に行った過去の経験を述べているため、「見学したのは」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q20", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p06", "question": "工場見学は本当に楽しかったです。[ 20 ]、どうして無料で見学をさせてくれるのかわかりませんでした。", "options": ["でも", "また", "すると", "たとえば"], "answer": 1, "grammar_points": ["接続詞（でも）"], "difficulty": 1, "explanation": "楽しかったというプラスの感想に対して、疑問を抱いたという逆接の接続詞「でも」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q21", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p06", "question": "工場見学をした人の大部分が、[ 21 ] で作られている商品を好きになり、会社に対するイメージもよくなったそうです。", "options": ["これ", "それ", "ここ", "そこ"], "answer": 4, "grammar_points": ["指示詞（そこ）"], "difficulty": 2, "explanation": "見学した工場という話題の場所を指す指示詞「そこ」が入ります。"},
    {"id": "jlpt_n3_2022_07_g_q22", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "文法", "page": 6, "pdf_page": 6, "section": "言語知識（文法）", "mondai_number": 3, "mondai_type": "bunshou_bunpou", "mondai_label": "問題3", "instruction": "つぎの文章を読んで、文章全体の内容を考えて、(19)から(22)の中に入る最もよいものを、1・2・3・4から一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p06", "question": "日本にいる間にいろいろな工場に見学に [ 22 ]。", "options": ["行ってみてほしいです", "行ってみたがっています", "行ってみるつもりです", "行ってみるといいです"], "answer": 3, "grammar_points": ["〜つもりです（意志）"], "difficulty": 2, "explanation": "話し手自身のこれからの意図・希望を表す「行ってみるつもりです」が入ります。"}
]

grammar_data = {"book_id": "jlpt_n3_2022_07", "book_title": "JLPT N3 2022年7月 過去問", "unit": "文法", "questions": grammar_questions}
with open(OUT_DIR / "grammar.json", "w", encoding="utf-8") as f:
    json.dump(grammar_data, f, ensure_ascii=False, indent=2)
print("Saved grammar.json (22 questions)")

# Reading (16 Questions)
reading_questions = [
    # 問題4 短文
    {"id": "jlpt_n3_2022_07_r_q23", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 7, "pdf_page": 7, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（１）から（４）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p07_1", "question": "「私」はどうして目標の500字を覚えることができたと考えているか。", "options": ["「私」にとって簡単な目標だったから。", "クラス全員で話し合って、同じ目標に決めたから。", "簡単にあきらめないようにしようと、心の中で決めていたから。", "決めた目標が、自分にもほかの人にも見えるようにしてあったから。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "本文に「教室に入ると、自分で書いた目標が目に入るし、クラスのみんなも知っているから、簡単にはやめられない」「紙に書いて教室にはったのがよかったのだ」とあるためです。"},
    {"id": "jlpt_n3_2022_07_r_q24", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（１）から（４）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p07_2", "question": "旅行会社がこのメールで最も言いたい事は何か。", "options": ["旅行の予約内容を確認したら、連絡してください。", "旅行代金を出発日の1週間前までに振り込んでください。", "旅行のキャンセル料を1週間以内に支払ってください。", "旅行について何かわからないことがあれば質問をしてください。"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "メール本文に「ご出発日の1週間前までに旅行代金をお振り込みください」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q25", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（１）から（４）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p08_1", "question": "意外なサービスとあるが一人暮らしのお年寄りとその家族に対するどのようなサービスか。", "options": ["家族の指定した時間に、お年寄りに荷物を配達する。", "お年寄りを訪問し、その様子を家族にEメールで連絡する。", "家族からのEメールを郵便局員が受け取り、印刷してお年寄りに渡す。", "ふだんなかなか会えない家族のところに、お年寄りを連れて行く。"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "本文に「郵便局員がお年寄りの家を訪問する。そして、そのときのお年寄りの様子をEメールで家族に教えてくれるのだ」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q26", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 8, "pdf_page": 8, "section": "読解", "mondai_number": 4, "mondai_type": "dokkai_tandun", "mondai_label": "問題4", "instruction": "つぎの（１）から（４）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p08_2", "question": "ナムさんがこのメモで頼まれていることは何か。", "options": ["資料を60部準備することと、教室が変わったことを全員にメールで知らせること。", "準備する資料を20部増やすことと、304のドアにはる紙を作っておくこと。", "教室の予約を304から201を変えることと、304のドアに紙をはること。", "教室の予約を304から201に変えることと、全員にメールを送ること。"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "メモに「資料をあと20部お願いします」「304のドアに、教室が変わったことを知らせる紙をはったほうがいいと思うので、作っておいてください」とあります。"},

    # 問題5 中文
    {"id": "jlpt_n3_2022_07_r_q27", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p09", "question": "①この水筒とあるが、どのような水筒か。", "options": ["飲み物の温度が変わりにくい、直接口をつけて飲む水筒。", "飲み物の温度が変わりにくい、コップが付いている水筒。", "熱い飲み物を冷ましやすい、直接口をつけて飲む水筒。", "熱い飲み物を冷ましやすい、コップがついている水筒。"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "「買ったのは、コップが付いていない、直接口をつけて飲む水筒で、飲み物の温度が長時間変わらない物だ・・・①この水筒にした」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q28", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p09", "question": "②困ったこととあるが、どのようなことか。", "options": ["熱い飲み物を外で飲む機会が少なくなったこと。", "熱い飲み物を入れたら、水筒が壊れてしまったこと。", "熱い飲み物が水筒から直接飲めなかったこと。", "熱い飲み物がすぐに冷めてしまったこと。"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「熱すぎて、直接は飲めなかったのだ」と書かれています。"},
    {"id": "jlpt_n3_2022_07_r_q29", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 9, "pdf_page": 9, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p09", "question": "③最初に考えていたよりはお金がかかってしまったとあるが、それはなぜか。", "options": ["ペットボトルを買うことが増えたから。", "とても高い水筒を買うことになったから。", "水筒とは別にコップも買うことになったから。", "水筒を2本も買うことになったから。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「最初は1本あれば十分だと思っていたが、結局、コップ付きの水筒も買った」ため、水筒を2本買ったからです。"},
    {"id": "jlpt_n3_2022_07_r_q30", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p10", "question": "①この問題とあるが、何か。", "options": ["日本にカラスが多すぎること。", "日本にカラスを嫌がる人が多いこと。", "カラスが人に向かって飛んできたり、食べ物を取ったりして、危険で困ること。", "「私」の町の公園に、カラスが夕方たくさん集まってきて、うるさくて怖いこと。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "直前の段落に「私の町では、毎日夕方になると、たくさんのカラスが、公園の木で寝るために集まってきます。声がうるさいし、数が非常に多いので怖さを感じることもあります」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q31", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p10", "question": "どのような②実験か。", "options": ["カラスを「集まっても問題のない場所」でよく眠らせて、静かにさせる実験。", "カラスが「いてほしくない場所」にいても、鳴き声は周りに聞こえないようにする実験。", "カラスの苦手な食べ物を利用して、「いてほしくない場所」に来ないようにする実験。", "カラスの鳴き方の違いを利用して、「集まっても問題のない場所」に行かせる実験。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「安全な状態にいるときと危険を感じたときのカラスの鳴き方の違いを利用して、『いてほしくない場所』から『集まっても問題のない場所』にカラスを移動させることができた」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q32", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 10, "pdf_page": 10, "section": "読解", "mondai_number": 5, "mondai_type": "dokkai_chuubun", "mondai_label": "問題5", "instruction": "つぎの（１）と（２）の文章を読んで、質問に答えなさい。答えは、１・２・３・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p10", "question": "「私」の町のカラスの問題について、「私」はどう考えているか。", "options": ["「私」の町で成功した方法を、これからも続けていきたい。", "「私」の町でも、別の町で成功した方法を使って解決してほしい。", "別の町で成功した方法とは違う、「私」の町に合った新しい方法が必要だ。", "別の町で成功した方法は「私」の町では使えないから、解決はあきらめよう。"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「同じ方法は使えそうにありません。私の町に合った解決方法が見つかればいいと思います」とあります。"},

    # 問題6 長文
    {"id": "jlpt_n3_2022_07_r_q33", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p11", "question": "①「あきらめ始めていた」とあるが、何をあきらめ始めていたのか。", "options": ["両親に今までと違うプレゼントを送ること。", "両親にいつもと同じプレゼントを送ること。", "両親に結婚記念日までにプレゼントを送ること。", "両親に欲しいものを決めてもらうこと。"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "「毎年違うプレゼントを送っていて・・・今年は、前にあげたことがあるものでもしかたないと、あきらめ始めていた」とあるためです。"},
    {"id": "jlpt_n3_2022_07_r_q34", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p11", "question": "「私」が②説明の紙を読んで知ったことは、どんなことか。", "options": ["ろうそくの火が、不規則なゆれ方をすること。", "ろうそくの火が、人の気持ちを落ち着かせること。", "ろうそくの火が、嫌なにおいを消すこと。", "ろうそくの火が、料理をおいしく見せること。"], "answer": 4, "grammar_points": [], "difficulty": 2, "explanation": "「料理をおいしく見せる効果があることは初めて知った」とあります。"},
    {"id": "jlpt_n3_2022_07_r_q35", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 11, "pdf_page": 11, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p11", "question": "③ろうそくはやっぱりやめたほうがいいと思ったとあるが、なぜか。", "options": ["前に両親にろうそくをあげたことを思い出したから。", "結婚記念日にろうそくあげるのは変だと思ったから。", "ろうそくの火は危険かもしれないと心配になったから。", "ろうそくより新しいペットをあげた方が喜ばれると思ったから。"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「食事のあとで消し忘れることもあるかもしれない。それに、両親の家では猫を飼っているので、何が起こるかわからない」と危険を心配したからです。"},
    {"id": "jlpt_n3_2022_07_r_q36", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 12, "pdf_page": 12, "section": "読解", "mondai_number": 6, "mondai_type": "dokkai_choubun", "mondai_label": "問題6", "instruction": "つぎの文章を読んで、質問に答えなさい。答えは、１・２・３・４から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p11", "question": "両親へのプレゼントについて、「私」は今、どのように考えているか。", "options": ["友達にもらったろうそくがよかったから、同じろうそくが売られているか調べよう。", "安全に使える「電気ろうそく」を見つけたから、さっそく両親に送ろう。", "「電気ろうそく」にしようと思うが、もう少し調べてからどれにするか決めよう。", "「電気ろうそく」をあげるのはやめて、ろうそくについてもう一度調べてみよう。"], "answer": 3, "grammar_points": [], "difficulty": 2, "explanation": "「このタイプには、ほかにも種類があるようなので、もう少し調べてみようと思う」とあります。"},

    # 問題7 情報検索
    {"id": "jlpt_n3_2022_07_r_q37", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解", "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、中村ギター教室の生徒募集のお知らせである。これを読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p12", "question": "トムさんは、同じ大学に通う友達と一緒に月に3回グループレッスンを受けたいと考えている。2人の予定が合うのは、平日の18時以降である。トムさんと友達がこの教室に通う場合、トムさんは毎月いくら支払わなければならないか。", "options": ["8000円から、1000円引いたものを支払う。", "8000円から、2000円引いたものを支払う。", "10,000円から1000円引いたものを支払う。", "10,000円から2000円引いたものを支払う。"], "answer": 1, "grammar_points": [], "difficulty": 2, "explanation": "グループレッスン月3回は1名あたり8,000円。18時以降なので平日昼間割引(17時終了)は対象外、学生割引(1000円引)のみ適用されるため、「8000円から、1000円引いたものを支払う」となります。"},
    {"id": "jlpt_n3_2022_07_r_q38", "book": "JLPT N3 2022年7月 過去問", "book_code": "jlpt_n3_2022_07", "unit": "読解", "page": 13, "pdf_page": 13, "section": "読解", "mondai_number": 7, "mondai_type": "dokkai_jouhou_kensaku", "mondai_label": "問題7", "instruction": "右のページは、中村ギター教室の生徒募集のお知らせである。これを読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。", "passage_id": "jlpt_n3_2022_07_p12", "question": "特別割引レッスンを申し込んだ人が、当日必ず持っていかなければならないものは何か。", "options": ["特別割引レッスンの料金と、自分のギター。", "特別割引レッスンの料金。", "自分のギター。", "特にない。"], "answer": 2, "grammar_points": [], "difficulty": 2, "explanation": "「料金(一人1000円)は、当日お支払いください」「持ってこられない方には、無料で教室のギターをお貸しします」とあるため、ギターは必須ではなく、必ず持っていくのは料金です。"}
]

reading_data = {"book_id": "jlpt_n3_2022_07", "book_title": "JLPT N3 2022年7月 過去問", "unit": "読解", "questions": reading_questions}
with open(OUT_DIR / "reading.json", "w", encoding="utf-8") as f:
    json.dump(reading_data, f, ensure_ascii=False, indent=2)
print("Saved reading.json (16 questions)")
print("JLPT N3 2022 July generated successfully!")
