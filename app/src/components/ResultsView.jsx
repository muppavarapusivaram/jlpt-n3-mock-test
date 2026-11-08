// app/src/components/ResultsView.jsx
import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { 
  Award, RotateCcw, Play, CheckCircle2, XCircle, ChevronDown, ChevronUp, 
  BookOpen, ArrowLeft, BarChart3, HelpCircle, AlertTriangle 
} from 'lucide-react';
import { calculateJLPTScore, saveTestResult } from '../services/mockTestAlgorithm';

export default function ResultsView({ exam, userAnswers, onRetake, onNewExam, onGoHome }) {
  const [activeTab, setActiveTab] = useState('overview'); // 'overview' | 'review'
  const [expandedQId, setExpandedQId] = useState(null);
  const [filterMode, setFilterMode] = useState('all'); // 'all' | 'incorrect' | 'correct'

  const scores = calculateJLPTScore(exam, userAnswers);

  // Trigger celebration confetti on pass!
  useEffect(() => {
    if (scores.isPassed) {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 }
      });
    }

    // Save result to local history
    saveTestResult({
      test_id: exam.test_id,
      passed: scores.isPassed,
      total_score: scores.official180Equivalent,
      language_score: scores.languageScore,
      reading_score: scores.readingScore,
      total_correct: scores.totalCorrect,
      total_questions: scores.totalQuestions
    });
  }, []);

  const allExamQuestions = exam.sections.flatMap(s => s.questions);

  const filteredQuestions = allExamQuestions.filter(q => {
    const isCorrect = scores.resultsByQuestion[q.id]?.isCorrect;
    if (filterMode === 'incorrect') return !isCorrect;
    if (filterMode === 'correct') return isCorrect;
    return true;
  });

  return (
    <div style={{ maxWidth: 1040, margin: '0 auto', padding: '36px 20px 80px' }}>
      
      {/* Top Breadcrumb Nav */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
        <button
          onClick={onGoHome}
          style={{
            background: 'var(--bg-surface)',
            border: '1px solid var(--border-light)',
            color: 'var(--text-primary)',
            padding: '7px 16px',
            borderRadius: 8,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            fontSize: '0.85rem',
            fontWeight: 600
          }}
        >
          <ArrowLeft size={16} /> ホームへ戻る (Home)
        </button>

        <div style={{ display: 'flex', gap: 10 }}>
          <button
            onClick={onRetake}
            style={{
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-light)',
              color: 'var(--text-primary)',
              padding: '7px 16px',
              borderRadius: 8,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6,
              fontSize: '0.85rem',
              fontWeight: 600
            }}
          >
            <RotateCcw size={15} /> 同じ問題をもう一度
          </button>

          <button
            onClick={onNewExam}
            style={{
              background: 'linear-gradient(135deg, var(--torii-vermilion), #b91c1c)',
              color: '#ffffff',
              border: 'none',
              padding: '7px 18px',
              borderRadius: 8,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6,
              fontSize: '0.85rem',
              fontWeight: 700,
              boxShadow: '0 2px 8px var(--torii-glow)'
            }}
          >
            <Play size={15} fill="#fff" /> 新しい模試を生成・受験
          </button>
        </div>
      </div>

      {/* Main Score Announcement Banner */}
      <div className="washi-card" style={{
        padding: '36px 30px',
        textAlign: 'center',
        marginBottom: 28,
        position: 'relative',
        overflow: 'hidden'
      }}>
        <div className="torii-header-bar" style={{ position: 'absolute', top: 0, left: 0, right: 0 }} />

        <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: 6, letterSpacing: '0.04em' }}>
          {exam.title}
        </div>

        <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: 16 }}>
          試験結果通知書 (JLPT N3 Score Report)
        </h1>

        {/* Japanese Stamp Badge */}
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: 10,
          padding: '8px 28px',
          borderRadius: 30,
          fontSize: '1.35rem',
          fontWeight: 800,
          letterSpacing: '0.08em',
          background: scores.isPassed ? 'rgba(21, 128, 61, 0.08)' : 'rgba(197, 48, 48, 0.08)',
          border: '2px solid ' + (scores.isPassed ? 'var(--pine-green)' : 'var(--torii-vermilion)'),
          color: scores.isPassed ? 'var(--pine-green)' : 'var(--torii-vermilion)',
          boxShadow: '0 2px 10px ' + (scores.isPassed ? 'rgba(21, 128, 61, 0.15)' : 'var(--torii-glow)'),
          marginBottom: 20
        }}>
          {scores.isPassed ? '💮 合格 (PASS)' : '⚠️ 不合格 (FAIL)'}
        </div>

        <p style={{ color: 'var(--text-secondary)', fontSize: '0.94rem', maxWidth: 540, margin: '0 auto 24px', lineHeight: 1.6 }}>
          {scores.isPassed 
            ? "おめでとうございます！公式合格基準点(95点以上)および各区分の基準点(19点以上)をクリアしました。"
            : "惜しくも基準点に届きませんでした。間違えた設問の解説と文法項目を確認して再挑戦しましょう。"}
        </p>

        {/* 3 Main Score Blocks */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: 14,
          background: 'var(--bg-surface)',
          border: '1px solid var(--border-light)',
          borderRadius: 12,
          padding: '18px'
        }}>
          <div>
            <div style={{ fontSize: '2.2rem', fontWeight: 800, color: 'var(--text-primary)' }}>
              {scores.languageScore} <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>/ 60</span>
            </div>
            <div style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--momiji-amber)', marginTop: 2 }}>
              言語知識 (文字・語彙・文法)
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              正答: {scores.vocabCorrect + scores.grammarCorrect} / {scores.vocabTotal + scores.grammarTotal} 問 (基準点: 19点)
            </div>
          </div>

          <div>
            <div style={{ fontSize: '2.2rem', fontWeight: 800, color: 'var(--text-primary)' }}>
              {scores.readingScore} <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>/ 60</span>
            </div>
            <div style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--torii-vermilion)', marginTop: 2 }}>
              読解 (Reading)
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              正答: {scores.readingCorrect} / {scores.readingTotal} 問 (基準点: 19点)
            </div>
          </div>

          <div>
            <div style={{ fontSize: '2.2rem', fontWeight: 800, color: 'var(--pine-green)' }}>
              {scores.official180Equivalent} <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>/ 180</span>
            </div>
            <div style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--pine-green)', marginTop: 2 }}>
              総合得点 (換算)
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              全体正答率: {Math.round((scores.totalCorrect / scores.totalQuestions) * 100)}% ({scores.totalCorrect} / {scores.totalQuestions} 問)
            </div>
          </div>
        </div>
      </div>

      {/* Tabs: Diagnostic Overview vs Question Review */}
      <div style={{ display: 'flex', gap: 8, marginBottom: 18 }}>
        <button
          onClick={() => setActiveTab('overview')}
          style={{
            background: activeTab === 'overview' ? 'var(--torii-vermilion)' : 'var(--bg-surface)',
            color: activeTab === 'overview' ? '#ffffff' : 'var(--text-primary)',
            border: '1px solid ' + (activeTab === 'overview' ? 'var(--torii-vermilion)' : 'var(--border-light)'),
            padding: '8px 18px',
            borderRadius: 8,
            fontWeight: 600,
            fontSize: '0.86rem',
            cursor: 'pointer'
          }}
        >
          分野別診断 (Diagnostics)
        </button>
        <button
          onClick={() => setActiveTab('review')}
          style={{
            background: activeTab === 'review' ? 'var(--torii-vermilion)' : 'var(--bg-surface)',
            color: activeTab === 'review' ? '#ffffff' : 'var(--text-primary)',
            border: '1px solid ' + (activeTab === 'review' ? 'var(--torii-vermilion)' : 'var(--border-light)'),
            padding: '8px 18px',
            borderRadius: 8,
            fontWeight: 600,
            fontSize: '0.86rem',
            cursor: 'pointer'
          }}
        >
          全問題の解答・解説 (Review 73 Qs)
        </button>
      </div>

      {/* TAB 1: Diagnostics Overview */}
      {activeTab === 'overview' && (
        <div className="washi-card" style={{
          padding: '24px 28px',
          marginBottom: 32
        }}>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: 16 }}>
            📊 大問別 正答率分析
          </h3>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 14 }}>
            {/* Vocab Section */}
            <div style={{ background: 'var(--bg-surface)', padding: '14px 16px', borderRadius: 10, border: '1px solid var(--border-light)' }}>
              <div style={{ fontWeight: 700, color: 'var(--momiji-amber)', marginBottom: 8, fontSize: '0.92rem' }}>
                文字・語彙 ({scores.vocabCorrect} / {scores.vocabTotal})
              </div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: 6 }}>
                <div>漢字読み: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'kanji_reading')}</div>
                <div>表記: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'orthography')}</div>
                <div>文脈規定: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'contextual_defining')}</div>
                <div>類義語: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'paraphrases')}</div>
                <div>用法: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'usage')}</div>
              </div>
            </div>

            {/* Grammar Section */}
            <div style={{ background: 'var(--bg-surface)', padding: '14px 16px', borderRadius: 10, border: '1px solid var(--border-light)' }}>
              <div style={{ fontWeight: 700, color: 'var(--torii-vermilion)', marginBottom: 8, fontSize: '0.92rem' }}>
                文法 ({scores.grammarCorrect} / {scores.grammarTotal})
              </div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: 6 }}>
                <div>文法形式の判断: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bunpou_keishiki')}</div>
                <div>文の組み立て (★): {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bun_kumitate')}</div>
                <div>文章の文法: {calcMondaiStats(allExamQuestions, scores.resultsByQuestion, 'bunshou_bunpou')}</div>
              </div>
            </div>

            {/* Reading Section */}
            <div style={{ background: 'var(--bg-surface)', padding: '14px 16px', borderRadius: 10, border: '1px solid var(--border-light)' }}>
              <div style={{ fontWeight: 700, color: 'var(--pine-green)', marginBottom: 8, fontSize: '0.92rem' }}>
                読解 ({scores.readingCorrect} / {scores.readingTotal})
              </div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: 6 }}>
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
            background: 'var(--bg-card)',
            border: '1px solid var(--border-light)',
            borderRadius: 10,
            padding: '10px 16px',
            marginBottom: 16
          }}>
            <div style={{ display: 'flex', gap: 8 }}>
              <button
                onClick={() => setFilterMode('all')}
                style={{
                  background: filterMode === 'all' ? 'var(--torii-vermilion)' : 'var(--bg-surface)',
                  border: '1px solid ' + (filterMode === 'all' ? 'var(--torii-vermilion)' : 'var(--border-light)'),
                  color: filterMode === 'all' ? '#ffffff' : 'var(--text-primary)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.82rem',
                  fontWeight: 600
                }}
              >
                全問 (73)
              </button>
              <button
                onClick={() => setFilterMode('incorrect')}
                style={{
                  background: filterMode === 'incorrect' ? 'rgba(197, 48, 48, 0.12)' : 'var(--bg-surface)',
                  border: '1px solid ' + (filterMode === 'incorrect' ? 'var(--torii-vermilion)' : 'var(--border-light)'),
                  color: filterMode === 'incorrect' ? 'var(--torii-vermilion)' : 'var(--text-muted)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.82rem',
                  fontWeight: 600
                }}
              >
                不正解のみ ({73 - scores.totalCorrect})
              </button>
              <button
                onClick={() => setFilterMode('correct')}
                style={{
                  background: filterMode === 'correct' ? 'rgba(21, 128, 61, 0.12)' : 'var(--bg-surface)',
                  border: '1px solid ' + (filterMode === 'correct' ? 'var(--pine-green)' : 'var(--border-light)'),
                  color: filterMode === 'correct' ? 'var(--pine-green)' : 'var(--text-muted)',
                  padding: '5px 12px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  fontSize: '0.82rem',
                  fontWeight: 600
                }}
              >
                正解のみ ({scores.totalCorrect})
              </button>
            </div>

            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              表示中: {filteredQuestions.length} 問
            </span>
          </div>

          {/* Question List */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            {filteredQuestions.map((q) => {
              const res = scores.resultsByQuestion[q.id] || {};
              const isCorrect = res.isCorrect;
              const isExpanded = expandedQId === q.id;

              return (
                <div
                  key={q.id}
                  className="washi-card"
                  style={{
                    border: '1px solid ' + (isCorrect ? 'var(--border-light)' : 'rgba(197, 48, 48, 0.35)'),
                    padding: '16px 20px'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                      <span style={{
                        width: 24,
                        height: 24,
                        borderRadius: '50%',
                        background: isCorrect ? 'rgba(21, 128, 61, 0.12)' : 'rgba(197, 48, 48, 0.12)',
                        color: isCorrect ? 'var(--pine-green)' : 'var(--torii-vermilion)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '0.82rem',
                        fontWeight: 800
                      }}>
                        {isCorrect ? '✓' : '✗'}
                      </span>
                      <strong style={{ color: 'var(--text-primary)', fontSize: '0.94rem' }}>
                        第 {q.exam_number} 問 ({q.mondai_label} #{q.mondai_number})
                      </strong>
                      <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)' }}>
                        出所: {q.book}
                      </span>
                    </div>

                    <div style={{ fontSize: '0.82rem', display: 'flex', gap: 12 }}>
                      <span style={{ color: 'var(--text-secondary)' }}>あなたの回答: <strong style={{ color: isCorrect ? 'var(--pine-green)' : 'var(--torii-vermilion)' }}>{res.userAnswer ? `【${res.userAnswer}】` : '未回答'}</strong></span>
                      <span style={{ color: 'var(--text-secondary)' }}>正解: <strong style={{ color: 'var(--pine-green)' }}>【{q.answer}】</strong></span>
                    </div>
                  </div>

                  {/* Question text with high contrast */}
                  <div 
                    style={{ fontSize: '1.02rem', color: 'var(--text-primary)', marginBottom: 12, lineHeight: 1.7, fontWeight: 500 }}
                    dangerouslySetInnerHTML={{
                      __html: (q.question || '')
                        .replace(/\n/g, '<br>')
                        .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:2px solid var(--torii-vermilion); padding:0 2px; font-weight:700;">$1</u>')
                    }}
                  />

                  {/* Options List */}
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 6, marginBottom: 10 }}>
                    {(q.options || []).map((opt, i) => {
                      const optNum = i + 1;
                      const isUserChoice = res.userAnswer === optNum;
                      const isRightChoice = q.answer === optNum;

                      return (
                        <div
                          key={i}
                          style={{
                            padding: '6px 10px',
                            borderRadius: 6,
                            fontSize: '0.84rem',
                            background: isRightChoice ? 'rgba(21, 128, 61, 0.08)' : isUserChoice ? 'rgba(197, 48, 48, 0.08)' : 'var(--bg-surface)',
                            border: '1px solid ' + (isRightChoice ? 'var(--pine-green)' : isUserChoice ? 'var(--torii-vermilion)' : 'var(--border-light)'),
                            color: isRightChoice ? 'var(--pine-green)' : isUserChoice ? 'var(--torii-vermilion)' : 'var(--text-primary)'
                          }}
                        >
                          <span style={{ fontWeight: 700, marginRight: 6 }}>{optNum}.</span>
                          {opt} {isRightChoice && '✓'}
                        </div>
                      );
                    })}
                  </div>

                  {/* Toggle Explanation Button */}
                  <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: 8, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <button
                      onClick={() => setExpandedQId(isExpanded ? null : q.id)}
                      style={{
                        background: 'transparent',
                        border: 'none',
                        color: 'var(--momiji-amber)',
                        cursor: 'pointer',
                        fontSize: '0.8rem',
                        fontWeight: 600,
                        display: 'flex',
                        alignItems: 'center',
                        gap: 4
                      }}
                    >
                      {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                      {isExpanded ? '解説を閉じる' : '公式解説を確認する'}
                    </button>

                    <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                      難易度: レベル {q.difficulty}
                    </span>
                  </div>

                  {/* Expanded Explanation Box */}
                  {isExpanded && (
                    <div style={{
                      marginTop: 10,
                      padding: 12,
                      background: 'var(--bg-surface)',
                      borderRadius: 6,
                      fontSize: '0.85rem',
                      lineHeight: 1.6,
                      color: 'var(--text-secondary)'
                    }}>
                      <div style={{ fontWeight: 700, color: 'var(--text-primary)', marginBottom: 4 }}>
                        💡 <strong>公式解説:</strong> {q.explanation}
                      </div>
                      {q.grammar_points && q.grammar_points.length > 0 && (
                        <div style={{ marginTop: 6, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                          {q.grammar_points.map((gp, i) => (
                            <span key={i} style={{
                              background: 'rgba(217, 119, 6, 0.1)',
                              color: 'var(--momiji-amber)',
                              border: '1px solid rgba(217, 119, 6, 0.25)',
                              fontSize: '0.72rem',
                              padding: '2px 6px',
                              borderRadius: 4
                            }}>
                              {gp}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Floating Bottom Action Bar */}
      <div style={{
        position: 'fixed',
        bottom: 0,
        left: 0,
        right: 0,
        background: 'rgba(255, 255, 255, 0.95)',
        backdropFilter: 'blur(10px)',
        borderTop: '1px solid var(--border-light)',
        padding: '12px 24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        boxShadow: '0 -4px 16px rgba(87, 83, 78, 0.06)',
        zIndex: 40
      }}>
        <div style={{ fontSize: '0.86rem', color: 'var(--text-secondary)' }}>
          総合得点: <strong style={{ color: scores.isPassed ? 'var(--pine-green)' : 'var(--torii-vermilion)' }}>{scores.official180Equivalent}点</strong> / 180点 (正答率 {Math.round((scores.totalCorrect / scores.totalQuestions) * 100)}%)
        </div>

        <div style={{ display: 'flex', gap: 10 }}>
          <button
            onClick={onRetake}
            style={{
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-light)',
              color: 'var(--text-primary)',
              padding: '7px 16px',
              borderRadius: 6,
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.84rem'
            }}
          >
            再挑戦 (Retake)
          </button>
          <button
            onClick={onNewExam}
            style={{
              background: 'linear-gradient(135deg, var(--torii-vermilion), #b91c1c)',
              color: '#ffffff',
              border: 'none',
              padding: '7px 18px',
              borderRadius: 6,
              cursor: 'pointer',
              fontWeight: 700,
              fontSize: '0.84rem',
              boxShadow: '0 2px 8px var(--torii-glow)'
            }}
          >
            次の新しい模試へ (Next Exam)
          </button>
        </div>
      </div>

    </div>
  );
}

function calcMondaiStats(questions, results, mondaiKey) {
  const matching = questions.filter(q => q.mondai === mondaiKey);
  if (matching.length === 0) return '0 / 0問';
  const correct = matching.filter(q => results[q.id]?.isCorrect).length;
  const pct = Math.round((correct / matching.length) * 100);
  return `${correct} / ${matching.length}問 (${pct}%)`;
}
