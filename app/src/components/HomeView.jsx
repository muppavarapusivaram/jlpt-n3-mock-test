// app/src/components/HomeView.jsx
import React, { useState, useEffect } from 'react';
import { 
  Sparkles, Play, Shuffle, BookOpen, Clock, Award, 
  RotateCcw, CheckCircle, AlertTriangle, Layers, Compass, BarChart3, ChevronRight,
  ShieldCheck, HelpCircle, BookMarked, Target
} from 'lucide-react';
import { 
  generateBalancedMockTest, getSeenQuestionCounts, resetSeenQuestions, getTestHistory 
} from '../services/mockTestAlgorithm';
import questionBank from '../data/questionBank.json';

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

  const totalBankQuestions = questionBank.total_questions || 441;
  const exploredQuestionsCount = Object.keys(seenCounts).length;
  const exploredPercentage = Math.round((exploredQuestionsCount / totalBankQuestions) * 100);

  return (
    <div style={{ maxWidth: 1140, margin: '0 auto', padding: '36px 20px 80px' }}>
      
      {/* Hero Header */}
      <div style={{ textAlign: 'center', marginBottom: 36, position: 'relative' }}>
        
        {/* Japanese Top Pill with Hanko Stamp */}
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: 10,
          background: 'rgba(220, 38, 38, 0.1)',
          border: '1px solid rgba(220, 38, 38, 0.35)',
          padding: '6px 18px',
          borderRadius: 30,
          color: '#fca5a5',
          fontSize: '0.85rem',
          fontWeight: 700,
          letterSpacing: '0.05em',
          marginBottom: 16
        }}>
          <span style={{ fontSize: '1.05rem' }}>⛩️</span>
          <span>JLPT N3 公式過去問＆実戦模試システム</span>
          <span className="hanko-stamp">公式準拠</span>
        </div>
        <div style={{ fontSize: '0.78rem', color: 'var(--kimpaku-gold)', letterSpacing: '0.08em', marginTop: -8, marginBottom: 12, fontWeight: 600 }}>
          OFFICIAL BLUEPRINT COMPLIANT MOCK EXAM SYSTEM
        </div>

        {/* Big Japanese Headline with English Subtitle */}
        <h1 style={{ 
          fontFamily: 'var(--font-serif)', 
          fontSize: '2.5rem', 
          fontWeight: 800, 
          letterSpacing: '0.06em',
          color: '#fff',
          marginBottom: 6,
          textShadow: '0 2px 10px rgba(0,0,0,0.5)'
        }}>
          日本語能力試験 <span style={{ color: 'var(--torii-vermilion)', borderBottom: '2px solid var(--torii-vermilion)' }}>N3</span> 実戦模擬試験
        </h1>
        <div style={{ 
          fontFamily: 'var(--font-roman)', 
          fontSize: '0.95rem', 
          color: 'var(--text-secondary)', 
          letterSpacing: '0.12em', 
          textTransform: 'uppercase',
          marginBottom: 14 
        }}>
          Japanese Language Proficiency Test (JLPT N3) • Full Authentic Simulator
        </div>

        <p style={{ color: 'var(--text-secondary)', fontSize: '0.96rem', maxWidth: 680, margin: '0 auto', lineHeight: 1.6 }}>
          公式過去問・日本語総まとめから厳選。難易度・問題数を100%公式規格に完全準拠し、
          未出題問題を優先して自動抽出するスマート模試生成エンジンです。
        </p>
        <div style={{ color: 'var(--text-muted)', fontSize: '0.82rem', marginTop: 4 }}>
          Carefully extracted from official JLPT past exam papers and authentic textbooks with balanced difficulty and anti-fatigue question sampling.
        </div>

        {/* Question Bank Coverage Bar */}
        <div style={{
          maxWidth: 660,
          margin: '24px auto 0',
          background: 'var(--sumi-surface)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 14,
          padding: '14px 20px',
          display: 'flex',
          alignItems: 'center',
          gap: 16,
          boxShadow: '0 4px 16px rgba(0,0,0,0.3)'
        }}>
          <div style={{ flex: 1, textAlign: 'left' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 6 }}>
              <div>
                <span style={{ color: '#fff', fontWeight: 700, fontSize: '0.88rem' }}>問題プール出題網羅率</span>
                <span className="en-subtitle" style={{ margin: 0 }}>Question Bank Exploration Rate</span>
              </div>
              <strong style={{ color: 'var(--fuji-cyan)', fontSize: '0.95rem' }}>
                {exploredQuestionsCount} / {totalBankQuestions}問 ({exploredPercentage}%)
              </strong>
            </div>
            <div style={{ height: 7, background: '#1e293b', borderRadius: 4, overflow: 'hidden' }}>
              <div style={{ 
                height: '100%', 
                width: `${Math.min(100, Math.max(4, exploredPercentage))}%`, 
                background: 'linear-gradient(90deg, var(--fuji-cyan), var(--kimpaku-gold), var(--torii-vermilion))',
                borderRadius: 4,
                transition: 'width 0.4s ease'
              }} />
            </div>
          </div>
          <button 
            onClick={handleResetSeen}
            title="出題履歴をリセット (Reset Seen History)"
            style={{
              background: 'transparent',
              border: '1px solid var(--border-subtle)',
              color: 'var(--text-muted)',
              padding: '7px 12px',
              borderRadius: 8,
              cursor: 'pointer',
              fontSize: '0.78rem',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 2,
              transition: 'all 0.2s'
            }}
            onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--torii-vermilion)'; e.currentTarget.style.color = '#fff'; }}
            onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-subtle)'; e.currentTarget.style.color = 'var(--text-muted)'; }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
              <RotateCcw size={12} /> リセット
            </div>
            <span style={{ fontSize: '0.65rem', opacity: 0.7 }}>Reset</span>
          </button>
        </div>
      </div>

      {/* Main Exam Configuration Card */}
      {currentTest && (
        <div style={{
          background: 'var(--sumi-card)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 18,
          padding: '28px 32px',
          boxShadow: '0 16px 40px rgba(0,0,0,0.5)',
          marginBottom: 32,
          position: 'relative',
          overflow: 'hidden'
        }}>
          {/* Traditional Torii Lacquer Top Trim */}
          <div className="torii-header-bar" style={{ position: 'absolute', top: 0, left: 0, right: 0 }} />

          {/* Test Top Meta Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: 16, marginBottom: 22 }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6, flexWrap: 'wrap' }}>
                <span style={{
                  background: 'rgba(56, 189, 248, 0.12)',
                  border: '1px solid var(--fuji-cyan)',
                  color: 'var(--fuji-cyan)',
                  padding: '3px 10px',
                  borderRadius: 6,
                  fontFamily: 'monospace',
                  fontWeight: 700,
                  fontSize: '0.85rem'
                }}>
                  {currentTest.test_id}
                </span>

                <span style={{
                  background: 'rgba(16, 185, 129, 0.12)',
                  color: '#6ee7b7',
                  border: '1px solid rgba(16, 185, 129, 0.4)',
                  padding: '3px 10px',
                  borderRadius: 6,
                  fontSize: '0.8rem',
                  fontWeight: 600
                }}>
                  新鮮度: 未出題 {currentTest.analytics.unseen_percentage}% (Unseen)
                </span>

                <span className="hanko-stamp" style={{ borderColor: 'var(--kimpaku-gold)', color: 'var(--kimpaku-gold)', boxShadow: '0 0 8px rgba(245,158,11,0.2)' }}>
                  厳選問題
                </span>
              </div>

              <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', fontWeight: 700, color: '#fff', margin: '4px 0 2px' }}>
                {currentTest.title}
              </h2>
              <div className="en-subtitle" style={{ fontSize: '0.8rem', color: 'var(--kimpaku-gold)' }}>
                Full-Scale 73-Question Balanced Examination Paper
              </div>
            </div>

            {/* Shuffle Test Button */}
            <button
              onClick={generateNew}
              disabled={isShuffling}
              style={{
                background: 'linear-gradient(135deg, var(--sumi-surface), #1e2d45)',
                border: '1px solid var(--border-gold)',
                color: '#fff',
                padding: '10px 18px',
                borderRadius: 10,
                cursor: 'pointer',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                boxShadow: '0 4px 14px rgba(0,0,0,0.25)',
                transition: 'all 0.2s',
                minWidth: 190
              }}
              onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--kimpaku-gold)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-gold)'; e.currentTarget.style.transform = 'translateY(0)'; }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontWeight: 700, fontSize: '0.92rem' }}>
                <Shuffle size={16} className={isShuffling ? "animate-spin" : ""} style={{ color: 'var(--kimpaku-gold)' }} />
                {isShuffling ? '再抽出中...' : '問題をシャッフル'}
              </div>
              <span className="en-subtitle" style={{ margin: 0, fontSize: '0.68rem', opacity: 0.8 }}>
                Shuffle & Generate New Test
              </span>
            </button>
          </div>

          {/* Test Structure Cards Grid */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))',
            gap: 16,
            marginBottom: 24
          }}>
            {/* Section 1 Specs */}
            <div style={{
              background: 'var(--sumi-surface)',
              border: '1px solid var(--border-subtle)',
              borderTop: '3px solid var(--fuji-cyan)',
              borderRadius: 12,
              padding: '18px 20px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 6 }}>
                <div>
                  <span style={{ fontWeight: 800, color: '#fff', fontSize: '1rem' }}>第1部 言語知識 (文字・語彙)</span>
                  <div className="en-subtitle">Section 1: Language Knowledge (Kanji & Vocabulary)</div>
                </div>
                <span style={{ fontSize: '0.82rem', color: 'var(--fuji-cyan)', fontWeight: 700, background: 'rgba(56, 189, 248, 0.1)', padding: '2px 8px', borderRadius: 4 }}>
                  ⏱️ 30分 (Mins)
                </span>
              </div>

              <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--fuji-cyan)', margin: '10px 0 6px' }}>
                35 <span style={{ fontSize: '0.88rem', fontWeight: 500, color: 'var(--text-secondary)' }}>問 (Questions)</span>
              </div>

              {/* Detailed Breakdown with English */}
              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid rgba(255,255,255,0.06)', paddingTop: 8 }}>
                <div>• <strong>問題1 漢字読み</strong> <span style={{ opacity: 0.7 }}>(Kanji Reading)</span> : 8問</div>
                <div>• <strong>問題2 表記</strong> <span style={{ opacity: 0.7 }}>(Orthography/Spelling)</span> : 6問</div>
                <div>• <strong>問題3 文脈規定</strong> <span style={{ opacity: 0.7 }}>(Contextual Meaning)</span> : 11問</div>
                <div>• <strong>問題4 類義</strong> <span style={{ opacity: 0.7 }}>(Paraphrases / Synonyms)</span> : 5問</div>
                <div>• <strong>問題5 用法</strong> <span style={{ opacity: 0.7 }}>(Word Usage in Sentences)</span> : 5問</div>
              </div>
            </div>

            {/* Section 2 Specs */}
            <div style={{
              background: 'var(--sumi-surface)',
              border: '1px solid var(--border-subtle)',
              borderTop: '3px solid var(--torii-vermilion)',
              borderRadius: 12,
              padding: '18px 20px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 6 }}>
                <div>
                  <span style={{ fontWeight: 800, color: '#fff', fontSize: '1rem' }}>第2部 言語知識 (文法)・読解</span>
                  <div className="en-subtitle">Section 2: Grammar & Reading Comprehension</div>
                </div>
                <span style={{ fontSize: '0.82rem', color: 'var(--torii-vermilion)', fontWeight: 700, background: 'rgba(220, 38, 38, 0.1)', padding: '2px 8px', borderRadius: 4 }}>
                  ⏱️ 70分 (Mins)
                </span>
              </div>

              <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--torii-vermilion)', margin: '10px 0 6px' }}>
                38 <span style={{ fontSize: '0.88rem', fontWeight: 500, color: 'var(--text-secondary)' }}>問 (Questions)</span>
              </div>

              {/* Detailed Breakdown with English */}
              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid rgba(255,255,255,0.06)', paddingTop: 8 }}>
                <div>• <strong>文法</strong>: 形式判断 13問 + 星★文組替 5問 + 文章文法 4問 (計22問)</div>
                <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)', marginBottom: 4 }}>
                  Grammar: Sentential Form (13) + Star Composition (5) + Text Grammar (4)
                </div>
                <div>• <strong>読解</strong>: 短文 4問 + 中文 6問 + 長文 4問 + 情報検索 2問 (計16問)</div>
                <div style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                  Reading: Short (4) + Medium (6) + Long (4) + Info Retrieval (2)
                </div>
              </div>
            </div>

            {/* Balanced Difficulty Spec */}
            <div style={{
              background: 'var(--sumi-surface)',
              border: '1px solid var(--border-subtle)',
              borderTop: '3px solid var(--kimpaku-gold)',
              borderRadius: 12,
              padding: '18px 20px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 6 }}>
                <div>
                  <span style={{ fontWeight: 800, color: '#fff', fontSize: '1rem' }}>難易度バランス設計</span>
                  <div className="en-subtitle">Difficulty Balance Engine</div>
                </div>
                <span style={{ fontSize: '0.82rem', color: 'var(--kimpaku-gold)', fontWeight: 700, background: 'rgba(245, 158, 11, 0.1)', padding: '2px 8px', borderRadius: 4 }}>
                  平均 Lv {currentTest.analytics.average_difficulty}
                </span>
              </div>

              {/* Difficulty Bar */}
              <div style={{ display: 'flex', gap: 4, margin: '14px 0 10px', height: 16, borderRadius: 5, overflow: 'hidden' }}>
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[1] / 73) * 100}%`, background: 'var(--bamboo-green)' }} title={`Lv1 基礎: ${currentTest.analytics.difficulty_distribution[1]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[2] / 73) * 100}%`, background: 'var(--fuji-cyan)' }} title={`Lv2 標準: ${currentTest.analytics.difficulty_distribution[2]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[3] / 73) * 100}%`, background: 'var(--kimpaku-gold)' }} title={`Lv3 発展: ${currentTest.analytics.difficulty_distribution[3]}問`} />
                <div style={{ width: `${(currentTest.analytics.difficulty_distribution[4] / 73) * 100}%`, background: 'var(--torii-vermilion)' }} title={`Lv4 難関: ${currentTest.analytics.difficulty_distribution[4]}問`} />
              </div>

              <div style={{ fontSize: '0.78rem', color: 'var(--text-secondary)', lineHeight: 1.6, borderTop: '1px solid rgba(255,255,255,0.06)', paddingTop: 8 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🟢 <strong>Lv1 基礎</strong> (Foundational):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[1]}問</strong>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🔵 <strong>Lv2 標準</strong> (Standard N3):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[2]}問</strong>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <span>🟡 <strong>Lv3 発展</strong> (Advanced/Nuanced):</span>
                  <strong>{currentTest.analytics.difficulty_distribution[3]}問</strong>
                </div>
                <div style={{ fontSize: '0.72rem', color: 'var(--kimpaku-gold)', marginTop: 4 }}>
                  ★ 極端な全問難問・全問易問を防止し、本番同様に精密調整
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
            gap: 18,
            paddingTop: 20,
            borderTop: '1px solid var(--border-subtle)'
          }}>
            {/* Mode selection with English subtitle */}
            <div>
              <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: 6, fontWeight: 700 }}>
                受験モードの選択 <span className="en-badge-sub">(Select Exam Mode)</span>:
              </div>
              <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
                <button
                  onClick={() => setExamMode('official')}
                  style={{
                    background: examMode === 'official' ? 'var(--torii-vermilion)' : 'var(--sumi-surface)',
                    color: '#fff',
                    border: '1px solid ' + (examMode === 'official' ? 'var(--torii-vermilion)' : 'var(--border-subtle)'),
                    padding: '8px 16px',
                    borderRadius: 8,
                    cursor: 'pointer',
                    textAlign: 'left',
                    boxShadow: examMode === 'official' ? '0 0 14px var(--torii-glow)' : 'none'
                  }}
                >
                  <div style={{ fontWeight: 700, fontSize: '0.85rem' }}>⏱️ 本番タイマー (Timed)</div>
                  <div style={{ fontSize: '0.68rem', opacity: 0.85 }}>30分 + 70分 厳格時間制限</div>
                </button>

                <button
                  onClick={() => setExamMode('practice')}
                  style={{
                    background: examMode === 'practice' ? 'var(--fuji-cyan)' : 'var(--sumi-surface)',
                    color: examMode === 'practice' ? '#0b1120' : '#fff',
                    border: '1px solid ' + (examMode === 'practice' ? 'var(--fuji-cyan)' : 'var(--border-subtle)'),
                    padding: '8px 16px',
                    borderRadius: 8,
                    cursor: 'pointer',
                    textAlign: 'left',
                    boxShadow: examMode === 'practice' ? '0 0 14px rgba(56,189,248,0.3)' : 'none'
                  }}
                >
                  <div style={{ fontWeight: 700, fontSize: '0.85rem' }}>📖 練習モード (Practice)</div>
                  <div style={{ fontSize: '0.68rem', opacity: 0.85 }}>時間無制限・解説即時表示</div>
                </button>
              </div>
            </div>

            {/* Launch CTA Button */}
            <button
              onClick={() => onStartExam(currentTest, examMode)}
              style={{
                background: 'linear-gradient(135deg, var(--torii-vermilion), #b91c1c)',
                color: '#fff',
                border: '1px solid rgba(255,255,255,0.2)',
                padding: '14px 34px',
                borderRadius: 10,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                boxShadow: '0 6px 24px rgba(220, 38, 38, 0.45)',
                transition: 'all 0.15s ease'
              }}
              onMouseEnter={e => { e.currentTarget.style.transform = 'translateY(-2px)'; e.currentTarget.style.boxShadow = '0 8px 28px rgba(220, 38, 38, 0.6)'; }}
              onMouseLeave={e => { e.currentTarget.style.transform = 'translateY(0)'; e.currentTarget.style.boxShadow = '0 6px 24px rgba(220, 38, 38, 0.45)'; }}
            >
              <div style={{
                width: 38,
                height: 38,
                borderRadius: '50%',
                background: 'rgba(255,255,255,0.2)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}>
                <Play size={20} fill="#fff" />
              </div>
              <div style={{ textAlign: 'left' }}>
                <div style={{ fontSize: '1.15rem', fontWeight: 800, letterSpacing: '0.04em' }}>
                  本番試験を開始する
                </div>
                <div style={{ fontSize: '0.74rem', opacity: 0.9, fontWeight: 500, letterSpacing: '0.02em' }}>
                  START OFFICIAL MOCK EXAM (73 QUESTIONS)
                </div>
              </div>
            </button>
          </div>
        </div>
      )}

      {/* Quick Nav Features / Tools with Japanese Motif */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16, marginBottom: 36 }}>
        
        {/* Card 1: Question Bank Explorer */}
        <div 
          onClick={onOpenExplorer}
          style={{
            background: 'var(--sumi-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 14,
            padding: '20px',
            cursor: 'pointer',
            transition: 'all 0.2s',
            display: 'flex',
            alignItems: 'center',
            gap: 16
          }}
          onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--fuji-cyan)'; e.currentTarget.style.background = 'var(--sumi-surface)'; }}
          onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-subtle)'; e.currentTarget.style.background = 'var(--sumi-card)'; }}
        >
          <div style={{
            width: 48,
            height: 48,
            borderRadius: 10,
            background: 'rgba(56, 189, 248, 0.12)',
            border: '1px solid rgba(56, 189, 248, 0.3)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--fuji-cyan)'
          }}>
            <BookMarked size={24} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 700, color: '#fff', fontSize: '1rem', display: 'flex', alignItems: 'center', gap: 6 }}>
              問題バンクを閲覧 <ChevronRight size={16} />
            </div>
            <div className="en-subtitle">
              Question Bank Explorer ({totalBankQuestions} Questions)
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 4 }}>
              過去問・総まとめの全問題を検索・絞り込み閲覧
            </div>
          </div>
        </div>

        {/* Card 2: Passing Rules & Criteria */}
        <div 
          onClick={() => setShowSpecModal(true)}
          style={{
            background: 'var(--sumi-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 14,
            padding: '20px',
            cursor: 'pointer',
            transition: 'all 0.2s',
            display: 'flex',
            alignItems: 'center',
            gap: 16
          }}
          onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--kimpaku-gold)'; e.currentTarget.style.background = 'var(--sumi-surface)'; }}
          onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-subtle)'; e.currentTarget.style.background = 'var(--sumi-card)'; }}
        >
          <div style={{
            width: 48,
            height: 48,
            borderRadius: 10,
            background: 'rgba(245, 158, 11, 0.12)',
            border: '1px solid rgba(245, 158, 11, 0.3)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--kimpaku-gold)'
          }}>
            <Award size={24} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 700, color: '#fff', fontSize: '1rem', display: 'flex', alignItems: 'center', gap: 6 }}>
              合格基準・配点仕様 <ChevronRight size={16} />
            </div>
            <div className="en-subtitle">
              Passing Mark (95/180) & Cutoff Criteria
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 4 }}>
              言語知識 19点・読解 19点の足切りラインを完全再現
            </div>
          </div>
        </div>

        {/* Card 3: Anti-Repeat Frequency Engine */}
        <div 
          style={{
            background: 'var(--sumi-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 14,
            padding: '20px',
            display: 'flex',
            alignItems: 'center',
            gap: 16
          }}
        >
          <div style={{
            width: 48,
            height: 48,
            borderRadius: 10,
            background: 'rgba(16, 185, 129, 0.12)',
            border: '1px solid rgba(16, 185, 129, 0.3)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--bamboo-green)'
          }}>
            <ShieldCheck size={24} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontWeight: 700, color: '#fff', fontSize: '1rem' }}>
              重複防止・記憶定着設計
            </div>
            <div className="en-subtitle">
              Anti-Repeat Sampling Engine (No Login Needed)
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: 4 }}>
              ブラウザに解いた問題を記憶し未出題を優先出題
            </div>
          </div>
        </div>
      </div>

      {/* Test History List (if any) */}
      {history.length > 0 && (
        <div style={{
          background: 'var(--sumi-surface)',
          border: '1px solid var(--border-subtle)',
          borderRadius: 14,
          padding: '22px 26px',
          marginBottom: 36
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14 }}>
            <div>
              <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.15rem', color: '#fff', fontWeight: 700 }}>
                直近の受験履歴
              </h3>
              <div className="en-subtitle">Your Recent Mock Exam Scores</div>
            </div>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              全 {history.length} 回受験
            </span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {history.slice(0, 4).map((h, idx) => (
              <div 
                key={idx}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  background: 'var(--sumi-card)',
                  borderRadius: 8,
                  fontSize: '0.86rem'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span className={h.passed ? "hanko-stamp" : ""} style={{
                    borderColor: h.passed ? 'var(--bamboo-green)' : '#ef4444',
                    color: h.passed ? 'var(--bamboo-green)' : '#ef4444'
                  }}>
                    {h.passed ? '合格' : '不合格'}
                  </span>
                  <div>
                    <span style={{ color: '#fff', fontWeight: 600 }}>{h.test_id}</span>
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.76rem', marginLeft: 8 }}>{h.date}</span>
                  </div>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
                  <span style={{ color: 'var(--text-secondary)' }}>
                    言語: <strong style={{ color: '#fff' }}>{h.language_score}</strong>/60
                  </span>
                  <span style={{ color: 'var(--text-secondary)' }}>
                    読解: <strong style={{ color: '#fff' }}>{h.reading_score}</strong>/60
                  </span>
                  <span style={{ 
                    fontWeight: 800, 
                    color: h.passed ? 'var(--bamboo-green)' : '#ef4444',
                    fontSize: '1rem'
                  }}>
                    総合: {h.total_score}点
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Official Specification Modal */}
      {showSpecModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0,0,0,0.75)',
          backdropFilter: 'blur(5px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 20,
          zIndex: 100
        }}>
          <div style={{
            background: 'var(--sumi-card)',
            border: '1px solid var(--border-gold)',
            borderRadius: 16,
            maxWidth: 640,
            width: '100%',
            padding: '28px 32px',
            position: 'relative',
            maxHeight: '90vh',
            overflowY: 'auto'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 16 }}>
              <div>
                <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.3rem', color: '#fff', fontWeight: 800 }}>
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
                  fontSize: '1.4rem',
                  cursor: 'pointer'
                }}
              >
                ✕
              </button>
            </div>

            <div style={{ fontSize: '0.88rem', color: 'var(--text-secondary)', lineHeight: 1.7 }}>
              <div style={{ marginBottom: 16, padding: '12px 16px', background: 'var(--sumi-surface)', borderRadius: 8, borderLeft: '3px solid var(--kimpaku-gold)' }}>
                <strong style={{ color: '#fff' }}>🎯 合格要件 (Passing Requirement):</strong>
                <ul style={{ paddingLeft: 20, marginTop: 6 }}>
                  <li>総合得点が <strong>95点以上 / 180点満点</strong> であること (Overall score ≥ 95/180)</li>
                  <li>言語知識 (文字・語彙・文法) が <strong>19点以上 / 60点</strong> であること (Language score ≥ 19/60)</li>
                  <li>読解が <strong>19点以上 / 60点</strong> であること (Reading score ≥ 19/60)</li>
                </ul>
                <div style={{ fontSize: '0.78rem', color: 'var(--torii-vermilion)', marginTop: 6 }}>
                  ※ 総合得点が95点以上でも、いずれかの得点区分が19点未満の場合は不合格となります。
                </div>
              </div>

              <h4 style={{ color: '#fff', fontSize: '0.98rem', marginBottom: 8 }}>出題問題と制限時間 (Blueprint):</h4>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.82rem', marginBottom: 16 }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--border-subtle)', textAlign: 'left', color: 'var(--kimpaku-gold)' }}>
                    <th style={{ padding: '6px 8px' }}>セクション (Section)</th>
                    <th style={{ padding: '6px 8px' }}>問題数 (Qs)</th>
                    <th style={{ padding: '6px 8px' }}>制限時間 (Time)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                    <td style={{ padding: '6px 8px' }}>言語知識（文字・語彙）</td>
                    <td style={{ padding: '6px 8px' }}>35問</td>
                    <td style={{ padding: '6px 8px' }}>30分</td>
                  </tr>
                  <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                    <td style={{ padding: '6px 8px' }}>言語知識（文法）・読解</td>
                    <td style={{ padding: '6px 8px' }}>38問 (文法22+読解16)</td>
                    <td style={{ padding: '6px 8px' }}>70分</td>
                  </tr>
                  <tr>
                    <td style={{ padding: '6px 8px', fontWeight: 700, color: '#fff' }}>合計 (Total)</td>
                    <td style={{ padding: '6px 8px', fontWeight: 700, color: 'var(--fuji-cyan)' }}>73問</td>
                    <td style={{ padding: '6px 8px', fontWeight: 700, color: 'var(--torii-vermilion)' }}>100分</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <button
              onClick={() => setShowSpecModal(false)}
              style={{
                width: '100%',
                background: 'var(--sumi-surface)',
                border: '1px solid var(--border-subtle)',
                color: '#fff',
                padding: '10px',
                borderRadius: 8,
                cursor: 'pointer',
                fontWeight: 600,
                fontSize: '0.88rem'
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
