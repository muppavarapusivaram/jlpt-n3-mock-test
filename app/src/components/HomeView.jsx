// app/src/components/HomeView.jsx
import React, { useState, useEffect } from 'react';
import { 
  Sparkles, Play, Shuffle, BookOpen, Clock, Award, 
  RotateCcw, CheckCircle, ChevronRight, ShieldCheck, 
  BookMarked, Compass, Calendar
} from 'lucide-react';
import { 
  generateBalancedMockTest, getSeenQuestionCounts, resetSeenQuestions, getTestHistory 
} from '../services/mockTestAlgorithm';
import questionBank from '../data/questionBank.json';
import FujiToriiHero from './FujiToriiHero';

export default function HomeView({ onStartExam, onOpenExplorer }) {
  const [currentTest, setCurrentTest] = useState(null);
  const [examMode, setExamMode] = useState('official'); // 'official' | 'practice'
  const [isShuffling, setIsShuffling] = useState(false);
  const [seenCounts, setSeenCounts] = useState({});
  const [history, setHistory] = useState([]);
  const [showSpecModal, setShowSpecModal] = useState(false);

  useEffect(() => {
    refreshStats();
    generateNew();
  }, []);

  const refreshStats = () => {
    const sc = getSeenQuestionCounts();
    setSeenCounts(sc);
    setHistory(getTestHistory());
  };

  const generateNew = () => {
    setIsShuffling(true);
    setTimeout(() => {
      const newTest = generateBalancedMockTest();
      setCurrentTest(newTest);
      setIsShuffling(false);
      refreshStats();
    }, 280);
  };

  const handleResetSeen = () => {
    if (window.confirm("問題の出題履歴をリセットしますか？次回から全問が未出題として扱われます。\n(Reset question history? All questions will be treated as unseen.)")) {
      resetSeenQuestions();
      refreshStats();
      generateNew();
    }
  };

  const totalBankQuestions = questionBank.total_questions || 963;
  const exploredQuestionsCount = Object.keys(seenCounts).length;
  const exploredPercentage = Math.round((exploredQuestionsCount / totalBankQuestions) * 100);

  return (
    <div style={{ maxWidth: 1040, margin: '0 auto', padding: '24px 20px 80px' }}>
      
      {/* 1. Mount Fuji & Torii Gate Scenic Hero Header */}
      <div style={{ textAlign: 'center', marginBottom: 28, position: 'relative' }}>
        <FujiToriiHero />

        {/* Traditional Vermilion Tag */}
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: 8,
          background: 'rgba(197, 48, 48, 0.06)',
          border: '1px solid rgba(197, 48, 48, 0.25)',
          padding: '5px 16px',
          borderRadius: 30,
          color: 'var(--torii-vermilion)',
          fontSize: '0.84rem',
          fontWeight: 600,
          letterSpacing: '0.04em',
          marginBottom: 12
        }}>
          <span>⛩️</span>
          <span>日本語能力試験 N3 公式模擬試験</span>
          <span className="hanko-stamp">公式準拠</span>
        </div>

        {/* Light & Refined Typography for Title */}
        <h1 style={{ 
          fontFamily: 'var(--font-serif)', 
          fontSize: '2.4rem', 
          fontWeight: 700, 
          letterSpacing: '0.04em',
          color: 'var(--text-primary)',
          marginBottom: 4,
        }}>
          実戦模擬試験 <span style={{ color: 'var(--torii-vermilion)', borderBottom: '2px solid var(--torii-vermilion)' }}>N3</span>
        </h1>
        
        <div style={{ 
          fontFamily: 'var(--font-roman)', 
          fontSize: '0.9rem', 
          color: 'var(--text-english)', 
          letterSpacing: '0.14em', 
          textTransform: 'uppercase',
          marginBottom: 10,
          fontWeight: 500
        }}>
          Official JLPT N3 Examination Simulator
        </div>

        <p style={{ color: 'var(--text-secondary)', fontSize: '0.94rem', maxWidth: 620, margin: '0 auto', lineHeight: 1.6, fontWeight: 400 }}>
          過去問および厳選問題から、本番規格（73問・100分）に沿って毎回ランダムに生成。
          難易度バランスと未出題優先サンプリングで偏りのない学習を提供します。
        </p>

        {/* Question Bank Coverage Bar - Clean & Light */}
        <div style={{
          maxWidth: 580,
          margin: '20px auto 0',
          background: 'var(--bg-card)',
          border: '1px solid var(--border-light)',
          borderRadius: 14,
          padding: '12px 18px',
          display: 'flex',
          alignItems: 'center',
          gap: 14,
          boxShadow: '0 2px 12px rgba(87, 83, 78, 0.05)'
        }}>
          <div style={{ flex: 1, textAlign: 'left' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                <span style={{ color: 'var(--text-primary)', fontWeight: 600, fontSize: '0.84rem' }}>
                  問題プール網羅率
                </span>
                <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)' }}>
                  (Bank Progress)
                </span>
              </div>
              <span style={{ color: 'var(--momiji-amber)', fontSize: '0.86rem', fontWeight: 700 }}>
                {exploredQuestionsCount} / {totalBankQuestions}問 ({exploredPercentage}%)
              </span>
            </div>
            <div style={{ height: 6, background: 'var(--bg-surface)', borderRadius: 3, overflow: 'hidden' }}>
              <div style={{ 
                height: '100%', 
                width: `${Math.min(100, Math.max(3, exploredPercentage))}%`, 
                background: 'linear-gradient(90deg, var(--momiji-amber), var(--torii-vermilion))',
                borderRadius: 3,
                transition: 'width 0.4s ease'
              }} />
            </div>
          </div>
          
          <button 
            onClick={handleResetSeen}
            title="出題履歴をリセット (Reset Seen History)"
            style={{
              background: 'transparent',
              border: '1px solid var(--border-light)',
              color: 'var(--text-muted)',
              padding: '6px 10px',
              borderRadius: 6,
              cursor: 'pointer',
              fontSize: '0.74rem',
              display: 'flex',
              alignItems: 'center',
              gap: 4,
              transition: 'all 0.15s'
            }}
            onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--torii-vermilion)'; e.currentTarget.style.color = 'var(--torii-vermilion)'; }}
            onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-light)'; e.currentTarget.style.color = 'var(--text-muted)'; }}
          >
            <RotateCcw size={12} />
            <span>リセット</span>
          </button>
        </div>
      </div>

      {/* 2. Main Exam Configuration Card - Elegant White & Vermilion */}
      {currentTest && (
        <div className="washi-card" style={{
          padding: '28px 32px',
          marginBottom: 28,
          position: 'relative',
          overflow: 'hidden'
        }}>
          {/* Traditional Vermilion Lacquer Top Accent */}
          <div className="torii-header-bar" style={{ position: 'absolute', top: 0, left: 0, right: 0 }} />

          {/* Test Top Meta Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 14, marginBottom: 20 }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6, flexWrap: 'wrap' }}>
                <span style={{
                  background: 'var(--bg-surface)',
                  border: '1px solid var(--border-light)',
                  color: 'var(--text-secondary)',
                  padding: '2px 8px',
                  borderRadius: 6,
                  fontFamily: 'monospace',
                  fontWeight: 600,
                  fontSize: '0.8rem'
                }}>
                  {currentTest.test_id}
                </span>

                <span style={{
                  background: 'rgba(21, 128, 61, 0.08)',
                  color: 'var(--pine-green)',
                  border: '1px solid rgba(21, 128, 61, 0.25)',
                  padding: '2px 8px',
                  borderRadius: 6,
                  fontSize: '0.76rem',
                  fontWeight: 600
                }}>
                  新鮮度: 未出題 {currentTest.analytics.unseen_percentage}%
                </span>

                <span className="hanko-stamp">
                  厳選 73問
                </span>
              </div>

              <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.45rem', fontWeight: 700, color: 'var(--text-primary)', margin: '2px 0 2px' }}>
                {currentTest.title}
              </h2>
              <div className="en-subtitle" style={{ color: 'var(--text-muted)' }}>
                73-Question Balanced Examination Paper • 100 Minutes Total
              </div>
            </div>

            {/* Shuffle Test Button */}
            <button
              onClick={generateNew}
              disabled={isShuffling}
              style={{
                background: 'var(--bg-surface)',
                border: '1px solid var(--border-subtle)',
                color: 'var(--text-primary)',
                padding: '9px 16px',
                borderRadius: 10,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                boxShadow: '0 1px 4px rgba(87, 83, 78, 0.06)',
                transition: 'all 0.15s',
              }}
              onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--momiji-amber)'; e.currentTarget.style.color = 'var(--momiji-amber)'; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-subtle)'; e.currentTarget.style.color = 'var(--text-primary)'; }}
            >
              <Shuffle size={16} className={isShuffling ? "animate-spin" : ""} style={{ color: 'var(--momiji-amber)' }} />
              <div style={{ textAlign: 'left' }}>
                <div style={{ fontWeight: 600, fontSize: '0.84rem' }}>
                  {isShuffling ? '再抽出中...' : '問題をシャッフル'}
                </div>
                <div style={{ fontSize: '0.66rem', color: 'var(--text-muted)' }}>
                  Shuffle & Re-roll
                </div>
              </div>
            </button>
          </div>

          {/* Test Structure Cards Grid - Clean, Spacious, Not Cluttered */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
            gap: 14,
            marginBottom: 22
          }}>
            {/* Section 1 Specs */}
            <div style={{
              background: 'var(--bg-card-subtle)',
              border: '1px solid var(--border-light)',
              borderTop: '3px solid var(--momiji-amber)',
              borderRadius: 12,
              padding: '16px 18px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <span style={{ fontWeight: 700, color: 'var(--text-primary)', fontSize: '0.94rem' }}>
                  第1部 言語知識 (文字・語彙)
                </span>
                <span style={{ fontSize: '0.76rem', color: 'var(--momiji-amber)', fontWeight: 600, background: 'rgba(217, 119, 6, 0.08)', padding: '2px 7px', borderRadius: 4 }}>
                  ⏱️ 30分
                </span>
              </div>
              <div className="en-subtitle" style={{ marginBottom: 8 }}>
                Section 1: Vocabulary & Kanji
              </div>

              <div style={{ fontSize: '1.45rem', fontWeight: 700, color: 'var(--momiji-amber)', marginBottom: 8 }}>
                35 <span style={{ fontSize: '0.84rem', fontWeight: 400, color: 'var(--text-secondary)' }}>問 (Questions)</span>
              </div>

              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid var(--border-light)', paddingTop: 8 }}>
                <div>• <strong>問題1 漢字読み</strong> (Kanji Reading) : 8問</div>
                <div>• <strong>問題2 表記</strong> (Orthography) : 6問</div>
                <div>• <strong>問題3 文脈規定</strong> (Context Meaning) : 11問</div>
                <div>• <strong>問題4 類義</strong> (Paraphrases) : 5問</div>
                <div>• <strong>問題5 用法</strong> (Usage) : 5問</div>
              </div>
            </div>

            {/* Section 2 Specs */}
            <div style={{
              background: 'var(--bg-card-subtle)',
              border: '1px solid var(--border-light)',
              borderTop: '3px solid var(--torii-vermilion)',
              borderRadius: 12,
              padding: '16px 18px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <span style={{ fontWeight: 700, color: 'var(--text-primary)', fontSize: '0.94rem' }}>
                  第2部 言語知識 (文法)・読解
                </span>
                <span style={{ fontSize: '0.76rem', color: 'var(--torii-vermilion)', fontWeight: 600, background: 'rgba(197, 48, 48, 0.08)', padding: '2px 7px', borderRadius: 4 }}>
                  ⏱️ 70分
                </span>
              </div>
              <div className="en-subtitle" style={{ marginBottom: 8 }}>
                Section 2: Grammar & Reading
              </div>

              <div style={{ fontSize: '1.45rem', fontWeight: 700, color: 'var(--torii-vermilion)', marginBottom: 8 }}>
                38 <span style={{ fontSize: '0.84rem', fontWeight: 400, color: 'var(--text-secondary)' }}>問 (Questions)</span>
              </div>

              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid var(--border-light)', paddingTop: 8 }}>
                <div>• <strong>文法</strong>: 形式 13問 + 星★文組替 5問 + 文章文法 4問 (計22問)</div>
                <div>• <strong>読解</strong>: 短文 4問 + 中文 6問 + 長文 4問 + 情報検索 2問 (計16問)</div>
                <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginTop: 4 }}>
                  ※ 聴解 (Listening) は含まれません
                </div>
              </div>
            </div>

            {/* Balanced Difficulty Spec */}
            <div style={{
              background: 'var(--bg-card-subtle)',
              border: '1px solid var(--border-light)',
              borderTop: '3px solid var(--pine-green)',
              borderRadius: 12,
              padding: '16px 18px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <span style={{ fontWeight: 700, color: 'var(--text-primary)', fontSize: '0.94rem' }}>
                  難易度バランス設計
                </span>
                <span style={{ fontSize: '0.76rem', color: 'var(--pine-green)', fontWeight: 600, background: 'rgba(21, 128, 61, 0.08)', padding: '2px 7px', borderRadius: 4 }}>
                  平均 Lv {currentTest.analytics.average_difficulty}
                </span>
              </div>
              <div className="en-subtitle" style={{ marginBottom: 8 }}>
                Difficulty Distribution Curve
              </div>

              {/* Clean Difficulty Bar */}
              <div style={{ display: 'flex', gap: 3, margin: '8px 0 10px', height: 10, borderRadius: 5, overflow: 'hidden' }}>
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[1] / 73) * 100}%`, background: '#86efac' }} title={`Lv1 基礎: ${currentTest.analytics.difficulty_distribution[1]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[2] / 73) * 100}%`, background: '#93c5fd' }} title={`Lv2 標準: ${currentTest.analytics.difficulty_distribution[2]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[3] / 73) * 100}%`, background: '#fde047' }} title={`Lv3 発展: ${currentTest.analytics.difficulty_distribution[3]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[4] / 73) * 100}%`, background: '#fca5a5' }} title={`Lv4 難関: ${currentTest.analytics.difficulty_distribution[4]}問`} />
              </div>

              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid var(--border-light)', paddingTop: 8 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🟢 Lv1 基礎 (Foundational):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[1]}問</strong>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🔵 Lv2 標準 (Standard N3):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[2]}問</strong>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🟡 Lv3 発展 (Advanced):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[3]}問</strong>
                </div>
              </div>
            </div>
          </div>

          {/* Mode Switcher & Launch CTA */}
          <div style={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-between',
            alignItems: 'center',
            gap: 16,
            paddingTop: 18,
            borderTop: '1px solid var(--border-light)'
          }}>
            {/* Mode selection with English subtitle */}
            <div>
              <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', marginBottom: 6, fontWeight: 600 }}>
                受験モード <span className="en-badge-sub">(Mode)</span>:
              </div>
              <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                <button
                  onClick={() => setExamMode('official')}
                  style={{
                    background: examMode === 'official' ? 'var(--torii-vermilion)' : 'var(--bg-surface)',
                    color: examMode === 'official' ? '#fff' : 'var(--text-primary)',
                    border: '1px solid ' + (examMode === 'official' ? 'var(--torii-vermilion)' : 'var(--border-light)'),
                    padding: '7px 14px',
                    borderRadius: 8,
                    cursor: 'pointer',
                    textAlign: 'left',
                    boxShadow: examMode === 'official' ? '0 2px 8px var(--torii-glow)' : 'none'
                  }}
                >
                  <div style={{ fontWeight: 600, fontSize: '0.82rem' }}>⏱️ 本番タイマー (Timed)</div>
                  <div style={{ fontSize: '0.66rem', opacity: 0.85 }}>30分 + 70分 厳格制限</div>
                </button>

                <button
                  onClick={() => setExamMode('practice')}
                  style={{
                    background: examMode === 'practice' ? 'var(--text-primary)' : 'var(--bg-surface)',
                    color: examMode === 'practice' ? '#fff' : 'var(--text-primary)',
                    border: '1px solid ' + (examMode === 'practice' ? 'var(--text-primary)' : 'var(--border-light)'),
                    padding: '7px 14px',
                    borderRadius: 8,
                    cursor: 'pointer',
                    textAlign: 'left',
                    boxShadow: examMode === 'practice' ? '0 2px 8px rgba(0,0,0,0.1)' : 'none'
                  }}
                >
                  <div style={{ fontWeight: 600, fontSize: '0.82rem' }}>📖 練習モード (Practice)</div>
                  <div style={{ fontSize: '0.66rem', opacity: 0.85 }}>時間無制限・即時解説</div>
                </button>
              </div>
            </div>

            {/* Launch CTA Button */}
            <button
              onClick={() => onStartExam(currentTest, examMode)}
              style={{
                background: 'linear-gradient(135deg, var(--torii-vermilion), #b91c1c)',
                color: '#fff',
                border: 'none',
                padding: '12px 28px',
                borderRadius: 10,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                boxShadow: '0 4px 16px var(--torii-glow)',
                transition: 'all 0.15s ease'
              }}
              onMouseEnter={e => { e.currentTarget.style.transform = 'translateY(-1px)'; e.currentTarget.style.boxShadow = '0 6px 20px rgba(197, 48, 48, 0.35)'; }}
              onMouseLeave={e => { e.currentTarget.style.transform = 'translateY(0)'; e.currentTarget.style.boxShadow = '0 4px 16px var(--torii-glow)'; }}
            >
              <Play size={18} fill="#fff" />
              <div style={{ textAlign: 'left' }}>
                <div style={{ fontSize: '1.05rem', fontWeight: 700, letterSpacing: '0.02em' }}>
                  試験を開始する
                </div>
                <div style={{ fontSize: '0.7rem', opacity: 0.9, fontWeight: 400 }}>
                  START MOCK EXAM (73 QUESTIONS)
                </div>
              </div>
            </button>
          </div>
        </div>
      )}

      {/* 3. Quick Nav Tools - Clean Washi Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 14, marginBottom: 32 }}>
        
        {/* Card 1: Question Bank Explorer */}
        <div 
          onClick={onOpenExplorer}
          className="washi-card"
          style={{
            padding: '18px 20px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 14
          }}
        >
          <div style={{
            width: 44,
            height: 44,
            borderRadius: 10,
            background: 'rgba(217, 119, 6, 0.08)',
            border: '1px solid rgba(217, 119, 6, 0.25)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--momiji-amber)'
          }}>
            <BookMarked size={22} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.94rem', display: 'flex', alignItems: 'center', gap: 4 }}>
              問題バンクを閲覧 <ChevronRight size={15} />
            </div>
            <div className="en-subtitle">
              Question Bank Explorer ({totalBankQuestions} Qs)
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              過去問・総まとめの全問題を検索・絞り込み
            </div>
          </div>
        </div>

        {/* Card 2: Passing Rules & Criteria */}
        <div 
          onClick={() => setShowSpecModal(true)}
          className="washi-card"
          style={{
            padding: '18px 20px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: 14
          }}
        >
          <div style={{
            width: 44,
            height: 44,
            borderRadius: 10,
            background: 'rgba(197, 48, 48, 0.08)',
            border: '1px solid rgba(197, 48, 48, 0.25)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--torii-vermilion)'
          }}>
            <Award size={22} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.94rem', display: 'flex', alignItems: 'center', gap: 4 }}>
              合格基準・配点仕様 <ChevronRight size={15} />
            </div>
            <div className="en-subtitle">
              Passing Mark (95/180) & Cutoff Criteria
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              言語知識 19点・読解 19点の足切りラインを再現
            </div>
          </div>
        </div>

        {/* Card 3: Anti-Repeat Frequency Engine */}
        <div 
          className="washi-card"
          style={{
            padding: '18px 20px',
            display: 'flex',
            alignItems: 'center',
            gap: 14
          }}
        >
          <div style={{
            width: 44,
            height: 44,
            borderRadius: 10,
            background: 'rgba(21, 128, 61, 0.08)',
            border: '1px solid rgba(21, 128, 61, 0.25)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--pine-green)'
          }}>
            <ShieldCheck size={22} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.94rem' }}>
              出題重複防止システム
            </div>
            <div className="en-subtitle">
              Anti-Repeat Sampling Engine (No Login Needed)
            </div>
            <div style={{ fontSize: '0.74rem', color: 'var(--text-muted)', marginTop: 2 }}>
              未出題問題を優先し、偏りのない出題を実現
            </div>
          </div>
        </div>
      </div>

      {/* 4. Test History List (if any) */}
      {history.length > 0 && (
        <div className="washi-card" style={{
          padding: '20px 24px',
          marginBottom: 28
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
            <div>
              <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.05rem', color: 'var(--text-primary)', fontWeight: 600 }}>
                直近の受験履歴
              </h3>
              <div className="en-subtitle">Recent Mock Exam Records</div>
            </div>
            <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)' }}>
              全 {history.length} 回受験
            </span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {history.slice(0, 4).map((h, idx) => (
              <div 
                key={idx}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '9px 12px',
                  background: 'var(--bg-surface)',
                  borderRadius: 8,
                  fontSize: '0.84rem'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span className={h.passed ? "hanko-stamp" : ""} style={{
                    borderColor: h.passed ? 'var(--pine-green)' : '#ef4444',
                    color: h.passed ? 'var(--pine-green)' : '#ef4444'
                  }}>
                    {h.passed ? '合格' : '不合格'}
                  </span>
                  <div>
                    <span style={{ color: 'var(--text-primary)', fontWeight: 600 }}>{h.test_id}</span>
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.72rem', marginLeft: 8 }}>{h.date}</span>
                  </div>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <span style={{ color: 'var(--text-secondary)', fontSize: '0.8rem' }}>
                    言語: <strong style={{ color: 'var(--text-primary)' }}>{h.language_score}</strong>/60
                  </span>
                  <span style={{ color: 'var(--text-secondary)', fontSize: '0.8rem' }}>
                    読解: <strong style={{ color: 'var(--text-primary)' }}>{h.reading_score}</strong>/60
                  </span>
                  <span style={{ 
                    fontWeight: 700, 
                    color: h.passed ? 'var(--pine-green)' : '#ef4444',
                    fontSize: '0.94rem'
                  }}>
                    総合: {h.total_score}点
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 5. Official Specification Modal */}
      {showSpecModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(30, 41, 59, 0.45)',
          backdropFilter: 'blur(4px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 20,
          zIndex: 100
        }}>
          <div className="washi-card" style={{
            maxWidth: 580,
            width: '100%',
            padding: '26px 30px',
            position: 'relative',
            maxHeight: '90vh',
            overflowY: 'auto'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 14 }}>
              <div>
                <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.2rem', color: 'var(--text-primary)', fontWeight: 700 }}>
                  日本語能力試験 N3 公式合格基準
                </h3>
                <div className="en-subtitle">Official JLPT N3 Scoring & Passing Criteria</div>
              </div>
              <button 
                onClick={() => setShowSpecModal(false)}
                style={{
                  background: 'transparent',
                  border: 'none',
                  color: 'var(--text-muted)',
                  fontSize: '1.3rem',
                  cursor: 'pointer'
                }}
              >
                ✕
              </button>
            </div>

            <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', lineHeight: 1.65 }}>
              <div style={{ marginBottom: 14, padding: '10px 14px', background: 'var(--bg-surface)', borderRadius: 8, borderLeft: '3px solid var(--momiji-amber)' }}>
                <strong style={{ color: 'var(--text-primary)' }}>🎯 合格要件 (Passing Requirements):</strong>
                <ul style={{ paddingLeft: 18, marginTop: 4 }}>
                  <li>総合得点が <strong>95点以上 / 180点満点</strong> (Overall score ≥ 95/180)</li>
                  <li>言語知識 (文字・語彙・文法) が <strong>19点以上 / 60点</strong> (Language score ≥ 19/60)</li>
                  <li>読解が <strong>19点以上 / 60点</strong> (Reading score ≥ 19/60)</li>
                </ul>
                <div style={{ fontSize: '0.74rem', color: 'var(--torii-vermilion)', marginTop: 4 }}>
                  ※ いずれかの得点区分が19点未満の場合は不合格となります。
                </div>
              </div>

              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.8rem', marginBottom: 14 }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--border-light)', textAlign: 'left', color: 'var(--momiji-amber)' }}>
                    <th style={{ padding: '6px 8px' }}>セクション</th>
                    <th style={{ padding: '6px 8px' }}>問題数</th>
                    <th style={{ padding: '6px 8px' }}>制限時間</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '6px 8px' }}>言語知識（文字・語彙）</td>
                    <td style={{ padding: '6px 8px' }}>35問</td>
                    <td style={{ padding: '6px 8px' }}>30分</td>
                  </tr>
                  <tr style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '6px 8px' }}>言語知識（文法）・読解</td>
                    <td style={{ padding: '6px 8px' }}>38問 (文法22+読解16)</td>
                    <td style={{ padding: '6px 8px' }}>70分</td>
                  </tr>
                  <tr>
                    <td style={{ padding: '6px 8px', fontWeight: 600, color: 'var(--text-primary)' }}>合計</td>
                    <td style={{ padding: '6px 8px', fontWeight: 600, color: 'var(--momiji-amber)' }}>73問</td>
                    <td style={{ padding: '6px 8px', fontWeight: 600, color: 'var(--torii-vermilion)' }}>100分</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <button
              onClick={() => setShowSpecModal(false)}
              style={{
                width: '100%',
                background: 'var(--bg-surface)',
                border: '1px solid var(--border-light)',
                color: 'var(--text-primary)',
                padding: '9px',
                borderRadius: 8,
                cursor: 'pointer',
                fontWeight: 600,
                fontSize: '0.84rem'
              }}
            >
              閉じる (Close)
            </button>
          </div>
        </div>
      )}

    </div>
  );
}
