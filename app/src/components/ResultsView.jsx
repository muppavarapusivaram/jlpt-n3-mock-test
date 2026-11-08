// app/src/components/ResultsView.jsx
import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { 
  Award, CheckCircle2, XCircle, RotateCcw, Home, 
  ChevronDown, ChevronUp, Filter, Sparkles, BookOpen, Layers, Check, X 
} from 'lucide-react';
import { calculateJLPTScore, saveTestResult } from '../services/mockTestAlgorithm';

export default function ResultsView({ exam, userAnswers, onRetake, onNewExam, onGoHome }) {
  const [filterMode, setFilterMode] = useState('all'); // 'all' | 'incorrect' | 'correct'
  const [activeTab, setActiveTab] = useState('overview'); // 'overview' | 'review'
  const [expandedQId, setExpandedQId] = useState(null);

  const scores = calculateJLPTScore(exam, userAnswers);

  useEffect(() => {
    // Save to test history
    saveTestResult({
      testId: exam.test_id,
      testTitle: exam.title,
      isPassed: scores.isPassed,
      languageScore: scores.languageScore,
      readingScore: scores.readingScore,
      official180Equivalent: scores.official180Equivalent,
      totalCorrect: scores.totalCorrect,
      totalQuestions: scores.totalQuestions
    });

    // Fire confetti celebration if passed!
    if (scores.isPassed) {
      try {
        confetti({
          particleCount: 120,
          spread: 70,
          origin: { y: 0.6 }
        });
      } catch (e) {
        // ignore
      }
    }
  }, []);

  const allExamQuestions = exam.sections.flatMap(s => s.questions);

  // Filter questions for review
  const filteredQuestions = allExamQuestions.filter(q => {
    const res = scores.resultsByQuestion[q.id];
    if (filterMode === 'incorrect') return !res || !res.isCorrect;
    if (filterMode === 'correct') return res && res.isCorrect;
    return true;
  });

  return (
    <div style={{ maxWidth: 1040, margin: '0 auto', padding: '36px 20px 80px' }}>
      
      {/* Top Banner / Stamp */}
      <div style={{
        background: 'var(--sumi-card)',
        border: '1px solid var(--border-subtle)',
        borderRadius: 16,
        padding: '36px 28px',
        textAlign: 'center',
        position: 'relative',
        boxShadow: '0 12px 36px rgba(0,0,0,0.4)',
        marginBottom: 28,
        overflow: 'hidden'
      }}>
        <div style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 4,
          background: scores.isPassed 
            ? 'linear-gradient(90deg, var(--bamboo-green), #34d399)' 
            : 'linear-gradient(90deg, var(--torii-vermilion), #f87171)'
        }} />

        <div style={{ fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: 8, letterSpacing: '0.08em' }}>
          {exam.title}
        </div>

        <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2rem', fontWeight: 800, color: '#fff', marginBottom: 18 }}>
          試験結果通知書 (JLPT N3 Score Report)
        </h1>

        {/* Japanese Stamp Badge */}
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: 10,
          padding: '10px 32px',
          borderRadius: 30,
          fontSize: '1.5rem',
          fontWeight: 900,
          letterSpacing: '0.12em',
          background: scores.isPassed ? 'rgba(16, 185, 129, 0.15)' : 'rgba(225, 29, 72, 0.15)',
          border: '3px solid ' + (scores.isPassed ? 'var(--bamboo-green)' : 'var(--torii-vermilion)'),
          color: scores.isPassed ? 'var(--bamboo-green)' : 'var(--torii-vermilion)',
          boxShadow: '0 4px 20px ' + (scores.isPassed ? 'var(--bamboo-glow)' : 'var(--torii-glow)'),
          marginBottom: 24
        }}>
          {scores.isPassed ? '💮 合格 (PASS)' : '⚠️ 不合格 (FAIL)'}
        </div>

        <p style={{ color: 'var(--text-secondary)', fontSize: '0.98rem', maxWidth: 540, margin: '0 auto 28px' }}>
          {scores.isPassed 
            ? "おめでとうございます！公式合格基準点(95点以上)および各区分の基準点(19点以上)をクリアしました。"
            : "惜しくも基準点に届きませんでした。間違えた設問の解説と文法項目を確認して再挑戦しましょう。"}
        </p>

        {/* 3 Main Score Blocks */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: 16,
          background: 'var(--sumi-surface)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 12,
          padding: '20px'
        }}>
          <div>
            <div style={{ fontSize: '2.4rem', fontWeight: 900, color: '#fff' }}>
              {scores.languageScore} <span style={{ fontSize: '1rem', color: 'var(--text-muted)' }}>/ 60</span>
            </div>
            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: 'var(--fuji-cyan)', marginTop: 4 }}>
              言語知識 (文字・語彙・文法)
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 2 }}>
              正答: {scores.vocabCorrect + scores.grammarCorrect} / {scores.vocabTotal + scores.grammarTotal} 問 (基準点: 19点)
            </div>
          </div>

          <div>
            <div style={{ fontSize: '2.4rem', fontWeight: 900, color: '#fff' }}>
              {scores.readingScore} <span style={{ fontSize: '1rem', color: 'var(--text-muted)' }}>/ 60</span>
            </div>
            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: 'var(--torii-vermilion)', marginTop: 4 }}>
              読解 (Reading)
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 2 }}>
              正答: {scores.readingCorrect} / {scores.readingTotal} 問 (基準点: 19点)
            </div>
          </div>

          <div>
            <div style={{ fontSize: '2.4rem', fontWeight: 900, color: 'var(--gold-amber)' }}>
              {scores.official180Equivalent} <span style={{ fontSize: '1rem', color: 'var(--text-muted)' }}>/ 180</span>
            </div>
            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: 'var(--gold-amber)', marginTop: 4 }}>
              総合得点 (換算)
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 2 }}>
              全体正答率: {Math.round((scores.totalCorrect / scores.totalQuestions) * 100)}% ({scores.totalCorrect} / {scores.totalQuestions} 問)
            </div>
          </div>
        </div>
      </div>

      {/* Tabs: Diagnostic Overview vs Question Review */}
      <div style={{ display: 'flex', gap: 10, marginBottom: 20 }}>
        <button
          onClick={() => setActiveTab('overview')}
          style={{
            background: activeTab === 'overview' ? 'var(--fuji-cyan)' : 'var(--sumi-surface)',
            color: activeTab === 'overview' ? '#000' : '#fff',
            border: '1px solid ' + (activeTab === 'overview' ? 'var(--fuji-cyan)' : 'var(--border-subtle)'),
            padding: '9px 20px',
            borderRadius: 8,
            fontWeight: 700,
            fontSize: '0.9rem',
            cursor: 'pointer'
          }}
        >
          分野別診断 (Diagnostics)
        </button>
        <button
          onClick={() => setActiveTab('review')}
          style={{
            background: activeTab === 'review' ? 'var(--fuji-cyan)' : 'var(--sumi-surface)',
            color: activeTab === 'review' ? '#000' : '#fff',
            border: '1px solid ' + (activeTab === 'review' ? 'var(--fuji-cyan)' : 'var(--border-subtle)'),
            padding: '9px 20px',
            borderRadius: 8,
            fontWeight: 700,
            fontSize: '0.9rem',
            cursor: 'pointer'
          }}
        >
          全問題の解答・解説 (Review 73 Qs)
        </button>
      </div>

      {/* TAB 1: Diagnostics Overview */}
      {activeTab === 'overview' && (
        <div style={{
          background: 'var(--sumi-card)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 14,
          padding: '24px 28px',
          marginBottom: 32
        }}>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#fff', marginBottom: 18 }}>
            📊 大問別 正答率分析
          </h3>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16 }}>
            {/* Vocab Section */}
            <div style={{ background: 'var(--sumi-surface)', padding: '16px', borderRadius: 8, border: '1px solid var(--border-subtle)' }}>
              <div style={{ fontWeight: 700, color: 'var(--fuji-cyan)', marginBottom: 10, fontSize: '0.95rem' }}>
                文字・語彙 ({scores.vocabCorrect} / {scores.vocabTotal})
              </div>
              <div style={{ fontSize: '0.85rem', display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div>漢字読み: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'kanji_reading')}</div>
                <div>表記: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'orthography')}</div>
                <div>文脈規定: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'contextual_defining')}</div>
                <div>類義語: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'paraphrases')}</div>
                <div>用法: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'usage')}</div>
              </div>
            </div>

            {/* Grammar Section */}
            <div style={{ background: 'var(--sumi-surface)', padding: '16px', borderRadius: 8, border: '1px solid var(--border-subtle)' }}>
              <div style={{ fontWeight: 700, color: 'var(--torii-vermilion)', marginBottom: 10, fontSize: '0.95rem' }}>
                文法 ({scores.grammarCorrect} / {scores.grammarTotal})
              </div>
              <div style={{ fontSize: '0.85rem', display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div>文法形式の判断: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bunpou_keishiki')}</div>
                <div>文の組み立て (★): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bun_kumitate')}</div>
                <div>文章の文法: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bunshou_bunpou')}</div>
              </div>
            </div>

            {/* Reading Section */}
            <div style={{ background: 'var(--sumi-surface)', padding: '16px', borderRadius: 8, border: '1px solid var(--border-subtle)' }}>
              <div style={{ fontWeight: 700, color: 'var(--gold-amber)', marginBottom: 10, fontSize: '0.95rem' }}>
                読解 ({scores.readingCorrect} / {scores.readingTotal})
              </div>
              <div style={{ fontSize: '0.85rem', display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div>短文読解 (4題): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'dokkai_tandun')}</div>
                <div>中文読解 (6題): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'dokkai_chuubun')}</div>
                <div>長文読解 (4題): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'dokkai_choubun')}</div>
                <div>情報検索 (2題): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'dokkai_jouhou_kensaku')}</div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: Question by Question Review */}
      {activeTab === 'review' && (
        <div>
          {/* Review Filter Bar */}
          <div style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            background: 'var(--sumi-surface)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 10,
            padding: '10px 18px',
            marginBottom: 20
          }}>
            <div style={{ display: 'flex', gap: 8 }}>
              <button
                onClick={() => setFilterMode('all')}
                style={{
                  background: filterMode === 'all' ? '#1e293b' : 'transparent',
                  border: '1px solid ' + (filterMode === 'all' ? 'var(--fuji-cyan)' : 'transparent'),
                  color: filterMode === 'all' ? 'var(--fuji-cyan)' : 'var(--text-muted)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.85rem',
                  fontWeight: 600
                }}
              >
                全問 (73)
              </button>
              <button
                onClick={() => setFilterMode('incorrect')}
                style={{
                  background: filterMode === 'incorrect' ? 'rgba(239, 68, 68, 0.2)' : 'transparent',
                  border: '1px solid ' + (filterMode === 'incorrect' ? '#ef4444' : 'transparent'),
                  color: filterMode === 'incorrect' ? '#f87171' : 'var(--text-muted)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.85rem',
                  fontWeight: 600
                }}
              >
                不正解のみ ({73 - scores.totalCorrect})
              </button>
              <button
                onClick={() => setFilterMode('correct')}
                style={{
                  background: filterMode === 'correct' ? 'rgba(16, 185, 129, 0.2)' : 'transparent',
                  border: '1px solid ' + (filterMode === 'correct' ? 'var(--bamboo-green)' : 'transparent'),
                  color: filterMode === 'correct' ? 'var(--bamboo-green)' : 'var(--text-muted)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.85rem',
                  fontWeight: 600
                }}
              >
                正解のみ ({scores.totalCorrect})
              </button>
            </div>

            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              表示中: {filteredQuestions.length} 問
            </span>
          </div>

          {/* Question List */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
            {filteredQuestions.map((q) => {
              const res = scores.resultsByQuestion[q.id] || {};
              const isCorrect = res.isCorrect;
              const isExpanded = expandedQId === q.id;

              return (
                <div
                  key={q.id}
                  style={{
                    background: 'var(--sumi-card)',
                    border: '1px solid ' + (isCorrect ? 'var(--border-subtle)' : 'rgba(239, 68, 68, 0.35)'),
                    borderRadius: 10,
                    padding: '18px 22px'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                      <span style={{
                        width: 24,
                        height: 24,
                        borderRadius: '50%',
                        background: isCorrect ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)',
                        color: isCorrect ? 'var(--bamboo-green)' : '#ef4444',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '0.85rem',
                        fontWeight: 800
                      }}>
                        {isCorrect ? '✓' : '✗'}
                      </span>
                      <strong style={{ color: '#fff', fontSize: '0.98rem' }}>
                        第 {q.exam_number} 問 ({q.mondai_label} #{q.mondai_number})
                      </strong>
                      <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                        出所: {q.book}
                      </span>
                    </div>

                    <div style={{ fontSize: '0.85rem', display: 'flex', gap: 12 }}>
                      <span>あなたの回答: <strong style={{ color: isCorrect ? 'var(--bamboo-green)' : '#f87171' }}>{res.userAnswer ? `【${res.userAnswer}】` : '未回答'}</strong></span>
                      <span>正解: <strong style={{ color: 'var(--bamboo-green)' }}>【{q.answer}】</strong></span>
                    </div>
                  </div>

                  <div 
                    style={{ fontSize: '1.05rem', color: '#e2e8f0', marginBottom: 12, lineHeight: 1.7 }}
                    dangerouslySetInnerHTML={{
                      __html: (q.question || '')
                        .replace(/\n/g, '<br>')
                        .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:2px solid var(--fuji-cyan); padding:0 2px; font-weight:700;">$1</u>')
                    }}
                  />

                  {/* Options List */}
                  <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
                    gap: 8,
                    marginBottom: 12
                  }}>
                    {q.options.map((opt, i) => {
                      const num = i + 1;
                      const isAns = num === q.answer;
                      const isUser = num === res.userAnswer;

                      let border = 'var(--border-subtle)';
                      let bg = '#101826';
                      let color = 'var(--text-secondary)';

                      if (isAns) {
                        border = 'var(--bamboo-green)';
                        bg = 'rgba(16, 185, 129, 0.15)';
                        color = '#6ee7b7';
                      } else if (isUser && !isCorrect) {
                        border = '#ef4444';
                        bg = 'rgba(239, 68, 68, 0.15)';
                        color = '#fca5a5';
                      }

                      return (
                        <div key={i} style={{
                          padding: '8px 12px',
                          borderRadius: 6,
                          background: bg,
                          border: `1px solid ${border}`,
                          color: color,
                          fontSize: '0.9rem',
                          display: 'flex',
                          alignItems: 'center',
                          gap: 8
                        }}>
                          <span style={{ fontWeight: 800 }}>{num}.</span>
                          <span>{opt}</span>
                        </div>
                      );
                    })}
                  </div>

                  {/* Explanation Banner */}
                  <div style={{
                    background: '#0c1322',
                    borderLeft: '3px solid var(--gold-amber)',
                    padding: '8px 14px',
                    borderRadius: '0 6px 6px 0',
                    fontSize: '0.88rem',
                    color: '#cbd5e1'
                  }}>
                    <strong>解説:</strong> {q.explanation}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Action Footer */}
      <div style={{
        marginTop: 36,
        paddingTop: 24,
        borderTop: '1px solid var(--border-subtle)',
        display: 'flex',
        justifyContent: 'center',
        gap: 16,
        flexWrap: 'wrap'
      }}>
        <button
          onClick={onRetake}
          style={{
            background: 'transparent',
            border: '1px solid var(--border-subtle)',
            color: '#fff',
            padding: '10px 24px',
            borderRadius: 8,
            fontWeight: 600,
            fontSize: '0.95rem',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 8
          }}
        >
          <RotateCcw size={16} /> この問題を再挑戦 (Retake)
        </button>

        <button
          onClick={onNewExam}
          style={{
            background: 'var(--fuji-cyan)',
            color: '#000',
            border: 'none',
            padding: '10px 28px',
            borderRadius: 8,
            fontWeight: 700,
            fontSize: '0.95rem',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 8
          }}
        >
          <Sparkles size={16} /> 新しい模試を自動生成 (Shuffle & New)
        </button>

        <button
          onClick={onGoHome}
          style={{
            background: 'var(--sumi-surface)',
            border: '1px solid var(--border-subtle)',
            color: 'var(--text-secondary)',
            padding: '10px 20px',
            borderRadius: 8,
            fontWeight: 600,
            fontSize: '0.95rem',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 8
          }}
        >
          <Home size={16} /> ホームへ戻る
        </button>
      </div>

    </div>
  );
}

function calcMondaiStats(questions, results, mtype) {
  const filtered = questions.filter(q => q.mondai_type === mtype);
  if (!filtered.length) return '0 / 0';
  const correct = filtered.filter(q => results[q.id] && results[q.id].isCorrect).length;
  const pct = Math.round((correct / filtered.length) * 100);
  return `${correct} / ${filtered.length} 問 (${pct}%)`;
}
