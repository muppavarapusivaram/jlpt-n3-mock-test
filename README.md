# ⛩️ JLPT N3 Authentic Mock Exam & Practice Platform (日本語能力試験 N3 模試システム)

[![JLPT Level](https://img.shields.io/badge/JLPT-N3-E11D48.svg?style=for-the-badge&logo=target)](https://www.jlpt.jp/e/)
[![React](https://img.shields.io/badge/React-19.3-61DAFB.svg?style=for-the-badge&logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-8.3-646CFF.svg?style=for-the-badge&logo=vite)](https://vitejs.dev/)
[![Question Bank](https://img.shields.io/badge/Questions-963%20Verified-10B981.svg?style=for-the-badge&logo=checkmarx)](bank/progress.md)
[![Reading Passages](https://img.shields.io/badge/Passages-95%20Authentic-8B5CF6.svg?style=for-the-badge)](bank/progress.md)
[![Deploy with Vercel](https://img.shields.io/badge/Vercel-Deployment%20Ready-black.svg?style=for-the-badge&logo=vercel)](https://vercel.com/)

An authentic, responsive Japanese Language Proficiency Test (JLPT) N3 mock exam simulator and learning platform. Built with React 19, Vite, and Lucide icons, styled in an elegant traditional Japanese aesthetic (*Seigaiha* ocean wave patterns, falling *sakura* cherry blossoms, and bilingual English subtitles).

Powered by a verified bank of **963 questions** and **95 passages** drawn from real past exam papers (2018–2025) and authoritative prep textbooks.

---

## ✨ Features

- **🎯 Official JLPT N3 Structure (73 Questions / 140 Minutes)**:
  - **言語知識（文字・語彙）(Language Knowledge - Vocab)**: 35 Questions (Mondai 1 to 5) — 30 min
  - **言語知識（文法）・読解 (Grammar & Reading)**: 38 Questions (Grammar Mondai 1 to 3: 22 Qs, Reading Mondai 4 to 7: 16 Qs) — 70 min
  - *(Note: Listening section is excluded by design for focused written & reading practice)*.

- **🎲 Smart Anti-Fatigue & Shuffle Engine**:
  - Unseen-priority reservoir sampling: guarantees questions won't feel repetitious across consecutive mock attempts.
  - Multi-level randomization with persistent test history tracking.

- **⚖️ Balanced Difficulty Curve**:
  - Questions are strictly stratified (~15% Level 1 easy, ~70% Level 2 standard N3, ~15% Level 3 challenging).
  - Every mock exam maintains a genuine exam difficulty curve.

- **🌸 Authentic Japanese Aesthetic**:
  - High-performance animated CSS *sakura* petal physics.
  - Traditional Indigo & Washi parchment card layout.
  - Bilingual Japanese-English subtitles beneath section headers to assist learners.

- **📊 Comprehensive Scoring & Instant Explanations**:
  - Implements official scaled score logic (0–180 total: 0–60 Language Knowledge, 0–60 Reading).
  - Enforces official passing marks: **Total $\ge$ 95/180** AND **Sectional cutoff $\ge$ 19/60**.
  - Detailed Japanese explanations (公式解説) and grammar points for every item.

---

## 📚 Question Bank Composition

All 963 questions and 95 passages are 100% verified with 4 distinct options, valid answer keys, and authentic Japanese texts:

| Source Booklet | Questions | Passages | Sections Included |
| :--- | :---: | :---: | :--- |
| **日本語総まとめ N3 文法** | 150 | 6 | Weeks 1 to 6 Complete (Grammar, Star sentence, Text grammar) |
| **JLPT N3 2018年12月 過去問** | 74 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2019年12月 過去問** | 72 | 8 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2020年12月 過去問** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2021年07月 過去問** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2022年07月 過去問** | 72 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2023年07月 過去問** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2023年12月 過去問** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2024年07月 過去問** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2025年07月 実戦問題** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 2025年12月 実戦問題** | 73 | 9 | Kanji reading, Orthography, Vocab, Grammar, Full Reading |
| **JLPT N3 文の組み立て 公式問題集** | 84 | - | 2010–2019 Sentence arrangement star (★) questions |
| **TOTAL** | **963** | **95** | **0 Errors, 100% Passed Validation** |

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- [Node.js](https://nodejs.org/) (version 18 or newer recommended)
- [Python 3](https://www.python.org/) (for running validation scripts)

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/muppavarapusivaram/jlpt-n3-mock-test.git
   cd jlpt-n3-mock-test
   ```

2. **Install dependencies & start the dev server:**
   ```bash
   cd app
   npm install
   npm run dev
   ```
   Open your browser at `http://localhost:5173`.

3. **Build for production:**
   ```bash
   cd app
   npm run build
   ```

---

## 🧪 Testing & Validation

The project includes automated validation suites:

- **Validate Question Bank Integrity**:
  ```bash
  python scripts/validate_bank.py
  ```
  *Verifies JSON schemas, 4-option constraints, non-empty explanations, valid passage bindings, and difficulty distribution.*

- **Run Generator & Anti-Fatigue Test Suite**:
  ```bash
  node scripts/run_all_tests.js
  ```
  *Executes 14 test suites verifying blueprint quota adherence, unseen-rate shuffling, scoring math, and sectional pass/fail boundaries.*

---

## 🌐 Deploy to Vercel

This repository is pre-configured with `vercel.json` for seamless deployment.

### Option A: Import via GitHub (Recommended)
1. Push this repository to your GitHub account:
   ```bash
   git remote add origin https://github.com/muppavarapusivaram/jlpt-n3-mock-test.git
   git push -u origin main
   ```
2. Go to [Vercel Dashboard](https://vercel.com/new).
3. Click **Import** next to your `jlpt-n3-mock-test` repository.
4. Leave all build settings at their defaults:
   - **Framework Preset**: Vite
   - **Build Command**: `npm --prefix app install && npm --prefix app run build`
   - **Output Directory**: `app/dist`
5. Click **Deploy**. Your site will be live within seconds!

### Option B: Deploy via Vercel CLI
```bash
npm install -g vercel
vercel
```

---

## 📁 Project Architecture

```
jlpt-mock-test/
├── app/                      # Frontend Application (React 19 + Vite)
│   ├── src/
│   │   ├── App.jsx           # Main Application Component & State Machine
│   │   ├── engine.js         # Generator, Shuffler & Scoring Algorithm
│   │   ├── questionsData.js  # Compiled Question Bank Bundle
│   │   └── index.css         # Traditional Japanese Design & Sakura CSS
│   ├── package.json
│   └── vite.config.js
├── bank/                     # Canonical Verified Question Bank (JSON)
│   ├── passages/             # Reading passages with authentic formatting
│   ├── 2018_12_*.json
│   ├── ...
│   ├── 2025_12_*.json
│   ├── sou_matome_grammar_*.json
│   └── progress.md           # Granular audit log of all questions
├── scripts/                  # Automated verification and build tools
│   ├── validate_bank.py      # Strict schema & integrity validator
│   ├── run_all_tests.js      # 14-suite automated test engine
│   └── export_app_data.py    # Bundler from bank JSONs to React data
├── vercel.json               # Vercel deployment configuration
├── package.json              # Root package configuration
├── .gitignore                # Excludes large PDF files (>100MB) & node_modules
└── README.md
```

---

## 📜 License
This software and exam generator engine are released under the [MIT License](LICENSE).
Exam questions are transcribed and organized for educational review and self-study purposes.
