# JLPT N3 Question Bank Extraction Progress

## Overall Progress Summary

| Source Book | Total Target Pages | Mapped Pages | Extracted Questions | Status |
|---|---|---|---|---|
| **日本語総まとめ N3 文法** | 118 | 118 | 150 / 150 | **全6週完了 (150問・長文6題) 100% 達成** ✅ |
| **JLPT N3 2018年12月 過去問** | 12 (非聴解) | 12 | 74 / 74 | **本試験全問完了 (74問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2019年12月 過去問** | 13 (非聴解) | 13 | 72 / 72 | **本試験全問完了 (72問・長文8題) 100% 達成** ✅ |
| **JLPT N3 2020年12月 過去問** | 16 (非聴解) | 16 | 73 / 73 | **本試験全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2021年7月 過去問** | 14 (非聴解) | 14 | 73 / 73 | **本試験全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2022年7月 過去問** | 13 (非聴解) | 13 | 72 / 72 | **本試験全問完了 (72問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2023年7月 過去問** | 20 (非聴解) | 20 | 73 / 73 | **本試験全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2023年12月 過去問** | 31 (非聴解) | 31 | 73 / 73 | **本試験全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2024年7月 過去問** | 19 (非聴解) | 19 | 73 / 73 | **本試験全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2025年7月 実戦問題** | 18 (非聴解) | 18 | 73 / 73 | **実戦問題全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 2025年12月 実戦問題** | 18 (非聴解) | 18 | 73 / 73 | **実戦問題全問完了 (73問・長文9題) 100% 達成** ✅ |
| **JLPT N3 文の組み立て 公式過去問集 (2010-2019)** | 10 | 10 | 84 / 84 | **公式星並べ84問完了 (重複除外済) 100% 達成** ✅ |
| 日本語総まとめ N3 読解 | 130 MB | Pending | 0 | Pending |
| 日本語総まとめ N3 語彙 | 63 MB | Pending | 0 | Pending |
| 日本語総まとめ N3 漢字 | 53 MB | Pending | 0 | Pending |
| 新完全マスター N3 シリーズ | 4冊 | Pending | 0 | Pending |

**現在蓄積された総問題数**: **963問** (検証合格率: 100%・エラー0件・要確認フラグ0件)  
**収録長文・情報検索パッセージ総数**: **95題**

---

## Mock Test Generator & React Application Status
- **Bank Integration**: Both `bank/bank_data.js` and `app/src/data/questionBank.json` updated with 963 questions and 95 passages.
- **React.js Mock Exam Application**: Complete with Japanese theme (Seigaiha ocean waves pattern, falling Sakura petals, Torii red / Sumi indigo palette), bilingual subtitles, stratified difficulty sampling (18.4% Lv1, 70.5% Lv2, 10.7% Lv3, 0.4% Lv4), and collision-proof cryptographic Fisher-Yates shuffling.
- **Test Suite**: 14/14 automated tests passing (`node scripts/run_all_tests.js`). Overlap between consecutive tests is just 1 question (99% unseen rate).
- **Reviewer**: `review.html` split-screen auditor updated with tabs and scan image bindings for all units (including 2025.7, 2025.12, 2020.12, and Star Reordering Collection).
