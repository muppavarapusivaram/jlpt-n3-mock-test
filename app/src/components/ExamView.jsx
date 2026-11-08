// app/src/components/ExamView.jsx
import React, { useState, useEffect, useRef } from 'react';
import { 
  Clock, Flag, CheckCircle, ChevronLeft, ChevronRight, 
  HelpCircle, AlertCircle, Eye, EyeOff, Pause, Play, LogOut, ArrowRight 
} from 'lucide-react';
import { recordSeenQuestions } from '../services/mockTestAlgorithm';

export default function ExamView({ exam, mode, onFinishExam, onExit }) {
  const [currentSectionId, setCurrentSectionId] = useState('sec_vocab');
  const [currentQIndex, setCurrentQIndex] = useState(0); // Index within current section questions
  const [userAnswers, setUserAnswers] = useState({}); // q.id -> option (1..4)
  const [flaggedIds, setFlaggedIds] = useState(new Set());
  const [showPracticeAnswer, setShowPracticeAnswer] = useState(false);

  // Timers
  const isTimed = mode === 'official';
  const [timeLeft, setTimeLeft] = useState(30 * 60); // 30 mins for sec 1
  const [isPaused, setIsPaused] = useState(false);

  // Track timer interval
  useEffect(() => {
    if (!isTimed) return;

    const timer = setInterval(() => {
      if (!isPaused) {
        setTimeLeft(prev => {
          if (prev <= 1) {
            clearInterval(timer);
            handleTimeUp();
            return 0;
          }
          return prev - 1;
        });
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [isTimed, isPaused, currentSectionId]);

  // Handle keyboard shortcuts (1, 2, 3, 4 for options, arrows for nav)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (['1', '2', '3', '4'].includes(e.key)) {
        const q = getCurrentQuestions()[currentQIndex];
        if (q) handleSelectOption(q.id, parseInt(e.key, 10));
      } else if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrev();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [currentSectionId, currentQIndex, userAnswers]);

  const handleTimeUp = () => {
    alert("試験時間が終了しました。採点画面に移行します。");
    handleSubmitExam();
  };

  const getCurrentQuestions = () => {
    const sec = exam.sections.find(s => s.section_id === currentSectionId);
    return sec ? sec.questions : [];
  };

  const handleSelectSection = (secId) => {
    if (secId === currentSectionId) return;
    setCurrentSectionId(secId);
    setCurrentQIndex(0);
    setShowPracticeAnswer(false);
    if (isTimed) {
      const sec = exam.sections.find(s => s.section_id === secId);
      setTimeLeft(sec.time_limit_minutes * 60);
    }
  };

  const handleSelectOption = (qid, optNum) => {
    setUserAnswers(prev => ({
      ...prev,
      [qid]: optNum
    }));
  };

  const toggleFlag = (qid) => {
    setFlaggedIds(prev => {
      const next = new Set(prev);
      if (next.has(qid)) next.delete(qid);
      else next.add(qid);
      return next;
    });
  };

  const handlePrev = () => {
    if (currentQIndex > 0) {
      setCurrentQIndex(prev => prev - 1);
      setShowPracticeAnswer(false);
    }
  };

  const handleNext = () => {
    const questions = getCurrentQuestions();
    if (currentQIndex < questions.length - 1) {
      setCurrentQIndex(prev => prev + 1);
      setShowPracticeAnswer(false);
    } else if (currentSectionId === 'sec_vocab') {
      if (window.confirm("第1部（文字・語彙）の全問に到達しました。第2部（文法・読解）へ進みますか？")) {
        handleSelectSection('sec_grammar_reading');
      }
    }
  };

  const handleSubmitExam = () => {
    const answeredCount = Object.keys(userAnswers).length;
    const totalQ = exam.scoring.total_questions;
    
    if (answeredCount < totalQ) {
      const confirmSubmit = window.confirm(`未回答の問題が ${totalQ - answeredCount} 問あります。試験を終了して採点しますか？`);
      if (!confirmSubmit) return;
    }

    // Record seen questions in algorithm tracker
    const allIds = exam.sections.flatMap(s => s.questions.map(q => q.id));
    recordSeenQuestions(allIds);

    onFinishExam(exam, userAnswers);
  };

  const questions = getCurrentQuestions();
  const currentQ = questions[currentQIndex] || {};
  const currentPassage = currentQ.passage_id ? exam.passages[currentQ.passage_id] : null;

  // Format timer string
  const mins = Math.floor(timeLeft / 60);
  const secs = timeLeft % 60;
  const timeFormatted = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  const isTimeWarning = timeLeft <= 300;

  // Question counts
  const allExamQuestions = exam.sections.flatMap(s => s.questions);
  const totalAnswered = Object.keys(userAnswers).length;

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--sumi-deep)' }}>
      
      {/* Top Header */}
      <header style={{
        background: 'var(--sumi-surface)',
        borderBottom: '1px solid var(--border-subtle)',
        padding: '10px 20px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexShrink: 0
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <button
            onClick={onExit}
            style={{
              background: 'transparent',
              border: '1px solid var(--border-subtle)',
              color: 'var(--text-secondary)',
              padding: '6px 12px',
              borderRadius: 6,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6,
              fontSize: '0.82rem'
            }}
          >
            <LogOut size={14} /> 中断して戻る <span style={{ fontSize: '0.7rem', opacity: 0.75 }}>(Exit)</span>
          </button>
          <div style={{ fontWeight: 700, fontSize: '1rem', color: '#fff' }}>
            {exam.title}
          </div>
          <span style={{
            background: mode === 'official' ? 'rgba(225, 29, 72, 0.15)' : 'rgba(56, 189, 248, 0.15)',
            color: mode === 'official' ? 'var(--torii-vermilion)' : 'var(--fuji-cyan)',
            border: '1px solid ' + (mode === 'official' ? 'var(--torii-vermilion)' : 'var(--fuji-cyan)'),
            padding: '2px 8px',
            borderRadius: 4,
            fontSize: '0.75rem',
            fontWeight: 700
          }}>
            {mode === 'official' ? '本番タイムアタック' : '練習モード'}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          {isTimed ? (
            <div style={{
              background: isTimeWarning ? 'rgba(239, 68, 68, 0.2)' : '#1e293b',
              border: '1px solid ' + (isTimeWarning ? '#ef4444' : '#334155'),
              color: isTimeWarning ? '#fca5a5' : '#fff',
              padding: '5px 14px',
              borderRadius: 20,
              fontFamily: 'monospace',
              fontSize: '1.05rem',
              fontWeight: 700,
              display: 'flex',
              alignItems: 'center',
              gap: 8
            }}>
              <Clock size={16} />
              <span>{timeFormatted}</span>
              <button 
                onClick={() => setIsPaused(!isPaused)}
                style={{ background: 'transparent', border: 'none', color: 'inherit', cursor: 'pointer', display: 'flex' }}
                title={isPaused ? "再開" : "一時停止"}
              >
                {isPaused ? <Play size={14} /> : <Pause size={14} />}
              </button>
            </div>
          ) : (
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>時間無制限 (Practice)</span>
          )}

          <button
            onClick={handleSubmitExam}
            style={{
              background: 'var(--bamboo-green)',
              color: '#000',
              border: 'none',
              padding: '7px 18px',
              borderRadius: 6,
              fontWeight: 700,
              fontSize: '0.88rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6
            }}
          >
            <CheckCircle size={15} />
            試験終了・採点 (Submit Exam)
          </button>
        </div>
      </header>

      {/* Main Body */}
      <div style={{ flex: 1, display: 'flex', overflow: 'hidden' }}>
        
        {/* Left Sidebar Palette */}
        <div style={{
          width: 250,
          background: 'var(--sumi-surface)',
          borderRight: '1px solid var(--border-subtle)',
          display: 'flex',
          flexDirection: 'column',
          flexShrink: 0
        }}>
          {/* Section Tabs */}
          <div style={{ display: 'flex', borderBottom: '1px solid var(--border-subtle)' }}>
            <button
              onClick={() => handleSelectSection('sec_vocab')}
              style={{
                flex: 1,
                padding: '10px 4px',
                fontSize: '0.78rem',
                fontWeight: 700,
                background: currentSectionId === 'sec_vocab' ? 'var(--sumi-card)' : 'transparent',
                color: currentSectionId === 'sec_vocab' ? 'var(--fuji-cyan)' : 'var(--text-muted)',
                border: 'none',
                borderBottom: currentSectionId === 'sec_vocab' ? '2px solid var(--fuji-cyan)' : 'none',
                cursor: 'pointer'
              }}
            >
              文字・語彙 (35問)
            </button>
            <button
              onClick={() => handleSelectSection('sec_grammar_reading')}
              style={{
                flex: 1,
                padding: '10px 4px',
                fontSize: '0.78rem',
                fontWeight: 700,
                background: currentSectionId === 'sec_grammar_reading' ? 'var(--sumi-card)' : 'transparent',
                color: currentSectionId === 'sec_grammar_reading' ? 'var(--torii-vermilion)' : 'var(--text-muted)',
                border: 'none',
                borderBottom: currentSectionId === 'sec_grammar_reading' ? '2px solid var(--torii-vermilion)' : 'none',
                cursor: 'pointer'
              }}
            >
              文法・読解 (38問)
            </button>
          </div>

          {/* Question Number Grid */}
          <div style={{
            flex: 1,
            overflowY: 'auto',
            padding: 12,
            display: 'grid',
            gridTemplateColumns: 'repeat(4, 1fr)',
            gap: 6,
            alignContent: 'start'
          }}>
            {questions.map((q, idx) => {
              const isSelected = userAnswers[q.id] !== undefined;
              const isCurrent = idx === currentQIndex;
              const isFlagged = flaggedIds.has(q.id);

              return (
                <button
                  key={q.id}
                  onClick={() => {
                    setCurrentQIndex(idx);
                    setShowPracticeAnswer(false);
                  }}
                  style={{
                    height: 36,
                    borderRadius: 6,
                    background: isSelected ? 'rgba(56, 189, 248, 0.22)' : 'var(--sumi-card)',
                    border: '1px solid ' + (isCurrent ? 'var(--fuji-cyan)' : isSelected ? 'var(--fuji-cyan)' : 'var(--border-subtle)'),
                    color: isCurrent ? '#fff' : isSelected ? 'var(--fuji-cyan)' : 'var(--text-secondary)',
                    fontWeight: isCurrent ? 800 : 600,
                    fontSize: '0.82rem',
                    cursor: 'pointer',
                    position: 'relative',
                    outline: isCurrent ? '2px solid var(--fuji-cyan)' : 'none'
                  }}
                >
                  {q.exam_number || (idx + 1)}
                  {isFlagged && (
                    <span style={{
                      position: 'absolute',
                      top: 1,
                      right: 2,
                      color: 'var(--gold-amber)',
                      fontSize: '0.65rem'
                    }}>
                      ★
                    </span>
                  )}
                </button>
              );
            })}
          </div>

          {/* Palette Footer Stats */}
          <div style={{
            padding: '10px 14px',
            borderTop: '1px solid var(--border-subtle)',
            fontSize: '0.78rem',
            color: 'var(--text-muted)',
            display: 'flex',
            justifyContent: 'space-between'
          }}>
            <span>回答済: <strong style={{ color: '#fff' }}>{totalAnswered}</strong> / {allExamQuestions.length}</span>
            <span>目印: <strong style={{ color: 'var(--gold-amber)' }}>{flaggedIds.size}</strong></span>
          </div>
        </div>

        {/* Middle & Right Content Area */}
        <div style={{ flex: 1, display: 'flex', overflow: 'hidden' }}>
          
          {/* Middle Reading Passage Pane (Conditional) */}
          {currentPassage && (
            <div style={{
              flex: 1.1,
              background: '#0c1322',
              borderRight: '1px solid var(--border-subtle)',
              overflowY: 'auto',
              padding: '24px 28px'
            }}>
              <div style={{
                background: 'var(--sumi-card)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 12,
                padding: '24px 26px',
                boxShadow: '0 4px 16px rgba(0,0,0,0.3)'
              }}>
                <div style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginBottom: 16,
                  paddingBottom: 10,
                  borderBottom: '1px solid var(--border-subtle)'
                }}>
                  <h3 style={{
                    fontFamily: 'var(--font-serif)',
                    fontSize: '1.25rem',
                    fontWeight: 700,
                    color: '#fff'
                  }}>
                    {currentPassage.title || '本文'}
                  </h3>
                  {currentPassage.author && (
                    <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                      作者: {currentPassage.author}
                    </span>
                  )}
                </div>

                <div style={{
                  fontFamily: 'var(--font-serif)',
                  fontSize: '1.08rem',
                  lineHeight: 2.1,
                  letterSpacing: '0.04em',
                  color: '#e2e8f0',
                  whiteSpace: 'pre-line'
                }}>
                  {currentPassage.content}
                </div>
              </div>
            </div>
          )}

          {/* Right Question Area */}
          <div style={{
            flex: 1.2,
            overflowY: 'auto',
            padding: '24px 36px',
            display: 'flex',
            flexDirection: 'column'
          }}>
            {/* Mondai Instruction Banner */}
            <div style={{
              background: 'rgba(30, 41, 59, 0.65)',
              borderLeft: '4px solid var(--fuji-cyan)',
              padding: '10px 16px',
              borderRadius: '0 8px 8px 0',
              fontSize: '0.92rem',
              color: '#cbd5e1',
              marginBottom: 20
            }}>
              <strong>{currentQ.mondai_label}</strong> : {currentQ.instruction}
            </div>

            {/* Question Card */}
            <div style={{
              background: 'var(--sumi-card)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 12,
              padding: '24px',
              marginBottom: 20
            }}>
              {/* Question Header */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
                <span style={{ fontSize: '1.15rem', fontWeight: 800, color: 'var(--fuji-cyan)' }}>
                  第 {currentQ.exam_number} 問 ({currentQ.mondai_label} #{currentQ.mondai_number})
                </span>
                <button
                  onClick={() => toggleFlag(currentQ.id)}
                  style={{
                    background: flaggedIds.has(currentQ.id) ? 'var(--gold-glow)' : 'transparent',
                    border: '1px solid ' + (flaggedIds.has(currentQ.id) ? 'var(--gold-amber)' : 'var(--border-subtle)'),
                    color: flaggedIds.has(currentQ.id) ? 'var(--gold-amber)' : 'var(--text-muted)',
                    padding: '5px 12px',
                    borderRadius: 6,
                    cursor: 'pointer',
                    fontSize: '0.82rem',
                    fontWeight: 600,
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6
                  }}
                >
                  <Flag size={13} fill={flaggedIds.has(currentQ.id) ? 'var(--gold-amber)' : 'none'} />
                  {flaggedIds.has(currentQ.id) ? '見直し印済' : 'あとで見直す'}
                </button>
              </div>

              {/* Question Prompt */}
              <div 
                style={{
                  fontSize: '1.25rem',
                  fontWeight: 500,
                  lineHeight: 1.8,
                  marginBottom: 24,
                  color: '#fff',
                  letterSpacing: '0.02em'
                }}
                dangerouslySetInnerHTML={{
                  __html: (currentQ.question || '')
                    .replace(/\n/g, '<br>')
                    .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:3px solid var(--fuji-cyan); padding:0 3px; font-weight:700;">$1</u>')
                }}
              />

              {/* Options Group */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                {(currentQ.options || []).map((optText, optIdx) => {
                  const optNum = optIdx + 1;
                  const isSelected = userAnswers[currentQ.id] === optNum;

                  return (
                    <div
                      key={optIdx}
                      onClick={() => handleSelectOption(currentQ.id, optNum)}
                      style={{
                        padding: '14px 18px',
                        borderRadius: 8,
                        background: isSelected ? 'rgba(56, 189, 248, 0.18)' : '#111b2b',
                        border: '1px solid ' + (isSelected ? 'var(--fuji-cyan)' : 'var(--border-subtle)'),
                        color: isSelected ? '#fff' : 'var(--text-primary)',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 14,
                        fontSize: '1.05rem',
                        transition: 'all 0.15s ease'
                      }}
                      onMouseEnter={e => {
                        if (!isSelected) e.currentTarget.style.borderColor = '#475569';
                      }}
                      onMouseLeave={e => {
                        if (!isSelected) e.currentTarget.style.borderColor = 'var(--border-subtle)';
                      }}
                    >
                      <div style={{
                        width: 28,
                        height: 28,
                        borderRadius: '50%',
                        background: isSelected ? 'var(--fuji-cyan)' : '#1e293b',
                        color: isSelected ? '#000' : 'var(--text-muted)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 800,
                        fontSize: '0.9rem',
                        flexShrink: 0
                      }}>
                        {optNum}
                      </div>
                      <div style={{ flex: 1, letterSpacing: '0.02em' }}>
                        {optText}
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Practice Mode Instant Check Button */}
              {mode === 'practice' && (
                <div style={{ marginTop: 20, paddingTop: 16, borderTop: '1px solid var(--border-subtle)' }}>
                  <button
                    onClick={() => setShowPracticeAnswer(!showPracticeAnswer)}
                    style={{
                      background: 'transparent',
                      border: '1px solid var(--border-subtle)',
                      color: 'var(--fuji-cyan)',
                      padding: '6px 12px',
                      borderRadius: 6,
                      fontSize: '0.85rem',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6
                    }}
                  >
                    {showPracticeAnswer ? <EyeOff size={14} /> : <Eye size={14} />}
                    {showPracticeAnswer ? '正解と解説を隠す' : '正解と解説を確認する'}
                  </button>

                  {showPracticeAnswer && (
                    <div style={{
                      marginTop: 12,
                      background: '#0d1524',
                      border: '1px solid var(--border-subtle)',
                      borderRadius: 8,
                      padding: '14px 16px',
                      fontSize: '0.92rem',
                      lineHeight: 1.7
                    }}>
                      <div style={{ color: 'var(--bamboo-green)', fontWeight: 700, marginBottom: 4 }}>
                        正解: 【 {currentQ.answer} 】 {currentQ.options[currentQ.answer - 1]}
                      </div>
                      <div style={{ color: '#cbd5e1' }}>{currentQ.explanation}</div>
                      {currentQ.grammar_points && currentQ.grammar_points.length > 0 && (
                        <div style={{ marginTop: 8, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                          {currentQ.grammar_points.map((gp, i) => (
                            <span key={i} style={{
                              background: 'rgba(129, 140, 248, 0.15)',
                              color: 'var(--accent)',
                              border: '1px solid rgba(129, 140, 248, 0.3)',
                              padding: '2px 8px',
                              borderRadius: 4,
                              fontSize: '0.78rem'
                            }}>
                              {gp}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Bottom Nav Buttons */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 'auto' }}>
              <button
                onClick={handlePrev}
                disabled={currentQIndex === 0}
                style={{
                  background: 'transparent',
                  border: '1px solid var(--border-subtle)',
                  color: currentQIndex === 0 ? 'var(--text-muted)' : '#fff',
                  padding: '9px 18px',
                  borderRadius: 6,
                  cursor: currentQIndex === 0 ? 'not-allowed' : 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  fontWeight: 600,
                  fontSize: '0.9rem'
                }}
              >
                <ChevronLeft size={16} /> 前の問
              </button>

              <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                キーボード [1] [2] [3] [4] または [←] [→] で操作可能
              </span>

              <button
                onClick={handleNext}
                style={{
                  background: 'var(--fuji-cyan)',
                  color: '#000',
                  border: 'none',
                  padding: '9px 22px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  fontWeight: 700,
                  fontSize: '0.9rem'
                }}
              >
                {currentQIndex === questions.length - 1 && currentSectionId === 'sec_vocab' ? (
                  <>第2部へ進む <ArrowRight size={16} /></>
                ) : (
                  <>次の問 <ChevronRight size={16} /></>
                )}
              </button>
            </div>

          </div>
        </div>

      </div>

    </div>
  );
}
