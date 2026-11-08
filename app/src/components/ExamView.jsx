// app/src/components/ExamView.jsx
import React, { useState, useEffect } from 'react';
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
  }, [currentQIndex, currentSectionId, userAnswers]);

  // Time expired handler
  const handleTimeUp = () => {
    if (currentSectionId === 'sec_vocab') {
      alert("第1部（文字・語彙）の試験時間が終了しました。第2部（文法・読解：70分）に進みます。");
      handleSelectSection('sec_grammar_reading');
    } else {
      alert("全試験時間が終了しました。回答を提出して採点結果を表示します。");
      handleSubmitExam();
    }
  };

  const currentSection = exam.sections.find(s => s.id === currentSectionId) || exam.sections[0];

  const getCurrentQuestions = () => {
    return currentSection ? currentSection.questions : [];
  };

  const handleSelectSection = (secId) => {
    setCurrentSectionId(secId);
    setCurrentQIndex(0);
    setShowPracticeAnswer(false);

    // If switching to section 2 in official mode, reset timer to 70 mins
    if (isTimed) {
      if (secId === 'sec_grammar_reading') {
        setTimeLeft(70 * 60);
      } else {
        setTimeLeft(30 * 60);
      }
    }
  };

  const handleSelectOption = (qId, optionNum) => {
    setUserAnswers(prev => ({ ...prev, [qId]: optionNum }));
  };

  const toggleFlag = (qId) => {
    setFlaggedIds(prev => {
      const next = new Set(prev);
      if (next.has(qId)) next.delete(qId);
      else next.add(qId);
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
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg-main)' }}>
      
      {/* Top Header */}
      <header style={{
        background: 'var(--bg-card)',
        borderBottom: '1px solid var(--border-light)',
        padding: '10px 24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexShrink: 0,
        boxShadow: '0 1px 4px rgba(87, 83, 78, 0.05)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <button
            onClick={onExit}
            style={{
              background: 'transparent',
              border: '1px solid var(--border-light)',
              color: 'var(--text-secondary)',
              padding: '6px 12px',
              borderRadius: 6,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6,
              fontSize: '0.82rem',
              transition: 'all 0.15s'
            }}
            onMouseEnter={e => { e.currentTarget.style.borderColor = 'var(--torii-vermilion)'; e.currentTarget.style.color = 'var(--torii-vermilion)'; }}
            onMouseLeave={e => { e.currentTarget.style.borderColor = 'var(--border-light)'; e.currentTarget.style.color = 'var(--text-secondary)'; }}
          >
            <LogOut size={14} /> 中断して戻る <span style={{ fontSize: '0.7rem', opacity: 0.75 }}>(Exit)</span>
          </button>
          
          <div style={{ fontWeight: 700, fontSize: '0.98rem', color: 'var(--text-primary)' }}>
            {exam.title}
          </div>

          <span style={{
            background: mode === 'official' ? 'rgba(197, 48, 48, 0.08)' : 'rgba(217, 119, 6, 0.08)',
            color: mode === 'official' ? 'var(--torii-vermilion)' : 'var(--momiji-amber)',
            border: '1px solid ' + (mode === 'official' ? 'rgba(197, 48, 48, 0.25)' : 'rgba(217, 119, 6, 0.25)'),
            padding: '2px 8px',
            borderRadius: 4,
            fontSize: '0.74rem',
            fontWeight: 700
          }}>
            {mode === 'official' ? '本番タイムアタック' : '練習モード'}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          {isTimed ? (
            <div style={{
              background: isTimeWarning ? 'rgba(220, 38, 38, 0.1)' : 'var(--bg-surface)',
              border: '1px solid ' + (isTimeWarning ? '#ef4444' : 'var(--border-light)'),
              color: isTimeWarning ? 'var(--torii-vermilion)' : 'var(--text-primary)',
              padding: '5px 14px',
              borderRadius: 20,
              fontFamily: 'monospace',
              fontSize: '1rem',
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
            <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>時間無制限 (Practice)</span>
          )}

          <button
            onClick={handleSubmitExam}
            style={{
              background: 'linear-gradient(135deg, var(--pine-green), #166534)',
              color: '#ffffff',
              border: 'none',
              padding: '7px 18px',
              borderRadius: 6,
              fontWeight: 700,
              fontSize: '0.86rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6,
              boxShadow: '0 2px 8px rgba(21, 128, 61, 0.25)'
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
          background: 'var(--bg-card)',
          borderRight: '1px solid var(--border-light)',
          display: 'flex',
          flexDirection: 'column',
          flexShrink: 0
        }}>
          {/* Section Tabs */}
          <div style={{ display: 'flex', borderBottom: '1px solid var(--border-light)' }}>
            <button
              onClick={() => handleSelectSection('sec_vocab')}
              style={{
                flex: 1,
                padding: '10px 4px',
                fontSize: '0.78rem',
                fontWeight: 700,
                background: currentSectionId === 'sec_vocab' ? 'var(--bg-surface)' : 'transparent',
                color: currentSectionId === 'sec_vocab' ? 'var(--torii-vermilion)' : 'var(--text-muted)',
                border: 'none',
                borderBottom: currentSectionId === 'sec_vocab' ? '2px solid var(--torii-vermilion)' : 'none',
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
                background: currentSectionId === 'sec_grammar_reading' ? 'var(--bg-surface)' : 'transparent',
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
                    background: isCurrent 
                      ? 'rgba(197, 48, 48, 0.12)' 
                      : isSelected 
                      ? 'rgba(21, 128, 61, 0.1)' 
                      : 'var(--bg-surface)',
                    border: '1px solid ' + (
                      isCurrent 
                        ? 'var(--torii-vermilion)' 
                        : isSelected 
                        ? 'rgba(21, 128, 61, 0.4)' 
                        : 'var(--border-light)'
                    ),
                    color: isCurrent 
                      ? 'var(--torii-vermilion)' 
                      : isSelected 
                      ? 'var(--pine-green)' 
                      : 'var(--text-secondary)',
                    fontWeight: isCurrent ? 800 : 600,
                    fontSize: '0.82rem',
                    cursor: 'pointer',
                    position: 'relative',
                    outline: isCurrent ? '2px solid var(--torii-vermilion)' : 'none'
                  }}
                >
                  {q.exam_number || (idx + 1)}
                  {isFlagged && (
                    <span style={{
                      position: 'absolute',
                      top: 1,
                      right: 2,
                      color: 'var(--momiji-amber)',
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
            borderTop: '1px solid var(--border-light)',
            fontSize: '0.78rem',
            color: 'var(--text-muted)',
            display: 'flex',
            justifyContent: 'space-between'
          }}>
            <span>回答済: <strong style={{ color: 'var(--text-primary)' }}>{totalAnswered}</strong> / {allExamQuestions.length}</span>
            <span>目印: <strong style={{ color: 'var(--momiji-amber)' }}>{flaggedIds.size}</strong></span>
          </div>
        </div>

        {/* Middle & Right Content Area */}
        <div style={{ flex: 1, display: 'flex', overflow: 'hidden' }}>
          
          {/* Middle Reading Passage Pane (Conditional) */}
          {currentPassage && (
            <div style={{
              flex: 1.1,
              background: 'var(--bg-surface)',
              borderRight: '1px solid var(--border-light)',
              overflowY: 'auto',
              padding: '24px 28px'
            }}>
              <div className="washi-card" style={{
                padding: '24px 26px',
              }}>
                <div style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginBottom: 16,
                  paddingBottom: 10,
                  borderBottom: '1px solid var(--border-light)'
                }}>
                  <h3 style={{
                    fontFamily: 'var(--font-serif)',
                    fontSize: '1.25rem',
                    fontWeight: 700,
                    color: 'var(--text-primary)'
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
                  letterSpacing: '0.03em',
                  color: 'var(--text-primary)',
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
              background: 'var(--bg-surface)',
              borderLeft: '4px solid var(--momiji-amber)',
              borderTop: '1px solid var(--border-light)',
              borderRight: '1px solid var(--border-light)',
              borderBottom: '1px solid var(--border-light)',
              padding: '10px 16px',
              borderRadius: '0 8px 8px 0',
              fontSize: '0.9rem',
              color: 'var(--text-primary)',
              marginBottom: 18
            }}>
              <strong style={{ color: 'var(--torii-vermilion)' }}>{currentQ.mondai_label}</strong> : {currentQ.instruction}
            </div>

            {/* Question Card */}
            <div className="washi-card" style={{
              padding: '24px 28px',
              marginBottom: 20
            }}>
              {/* Question Header */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
                <span style={{ fontSize: '1.12rem', fontWeight: 700, color: 'var(--torii-vermilion)' }}>
                  第 {currentQ.exam_number} 問 ({currentQ.mondai_label} #{currentQ.mondai_number})
                </span>
                <button
                  onClick={() => toggleFlag(currentQ.id)}
                  style={{
                    background: flaggedIds.has(currentQ.id) ? 'rgba(217, 119, 6, 0.12)' : 'var(--bg-surface)',
                    border: '1px solid ' + (flaggedIds.has(currentQ.id) ? 'var(--momiji-amber)' : 'var(--border-light)'),
                    color: flaggedIds.has(currentQ.id) ? 'var(--momiji-amber)' : 'var(--text-muted)',
                    padding: '5px 12px',
                    borderRadius: 6,
                    fontSize: '0.8rem',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6
                  }}
                >
                  <Flag size={13} fill={flaggedIds.has(currentQ.id) ? 'var(--momiji-amber)' : 'none'} />
                  {flaggedIds.has(currentQ.id) ? '見直し印済' : 'あとで見直す'}
                </button>
              </div>

              {/* Question Prompt - Crisp, Dark, High Contrast Text */}
              <div 
                style={{
                  fontSize: '1.25rem',
                  fontWeight: 600,
                  lineHeight: 1.85,
                  marginBottom: 24,
                  color: 'var(--text-primary)',
                  letterSpacing: '0.02em'
                }}
                dangerouslySetInnerHTML={{
                  __html: (currentQ.question || '')
                    .replace(/\n/g, '<br>')
                    .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:3px solid var(--torii-vermilion); padding:0 3px; font-weight:700; color:var(--text-primary);">$1</u>')
                }}
              />

              {/* Options Group - Clean Light Cards */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {(currentQ.options || []).map((optText, optIdx) => {
                  const optNum = optIdx + 1;
                  const isSelected = userAnswers[currentQ.id] === optNum;

                  return (
                    <div
                      key={optIdx}
                      onClick={() => handleSelectOption(currentQ.id, optNum)}
                      style={{
                        padding: '13px 18px',
                        borderRadius: 10,
                        background: isSelected ? 'rgba(197, 48, 48, 0.08)' : 'var(--bg-surface)',
                        border: '1.5px solid ' + (isSelected ? 'var(--torii-vermilion)' : 'var(--border-light)'),
                        color: isSelected ? 'var(--torii-vermilion)' : 'var(--text-primary)',
                        fontWeight: isSelected ? 600 : 400,
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 14,
                        fontSize: '1.02rem',
                        transition: 'all 0.15s ease',
                        boxShadow: isSelected ? '0 2px 8px var(--torii-glow)' : 'none'
                      }}
                      onMouseEnter={e => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--momiji-amber)';
                          e.currentTarget.style.background = 'var(--bg-hover)';
                        }
                      }}
                      onMouseLeave={e => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--border-light)';
                          e.currentTarget.style.background = 'var(--bg-surface)';
                        }
                      }}
                    >
                      <div style={{
                        width: 28,
                        height: 28,
                        borderRadius: '50%',
                        background: isSelected ? 'var(--torii-vermilion)' : 'var(--border-subtle)',
                        color: isSelected ? '#ffffff' : 'var(--text-primary)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 700,
                        fontSize: '0.88rem',
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
                <div style={{ marginTop: 20, paddingTop: 16, borderTop: '1px solid var(--border-light)' }}>
                  <button
                    onClick={() => setShowPracticeAnswer(!showPracticeAnswer)}
                    style={{
                      background: 'var(--bg-surface)',
                      border: '1px solid var(--border-light)',
                      color: 'var(--momiji-amber)',
                      padding: '6px 14px',
                      borderRadius: 6,
                      fontSize: '0.84rem',
                      fontWeight: 600,
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
                      padding: 16,
                      background: 'var(--bg-surface)',
                      borderLeft: '4px solid var(--pine-green)',
                      borderRadius: '0 8px 8px 0',
                      fontSize: '0.9rem'
                    }}>
                      <div style={{ fontWeight: 700, color: 'var(--pine-green)', marginBottom: 6 }}>
                        ✓ 正解: {currentQ.answer} 番
                      </div>
                      <div style={{ color: 'var(--text-secondary)', lineHeight: 1.6 }}>
                        💡 <strong>公式解説:</strong> {currentQ.explanation}
                      </div>
                      {currentQ.grammar_points && currentQ.grammar_points.length > 0 && (
                        <div style={{ marginTop: 8, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                          {currentQ.grammar_points.map((gp, i) => (
                            <span key={i} style={{
                              background: 'rgba(217, 119, 6, 0.1)',
                              color: 'var(--momiji-amber)',
                              border: '1px solid rgba(217, 119, 6, 0.25)',
                              fontSize: '0.74rem',
                              padding: '2px 8px',
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
              )}
            </div>

            {/* Bottom Nav Buttons */}
            <div style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              paddingTop: 12,
              marginTop: 'auto'
            }}>
              <button
                onClick={handlePrev}
                disabled={currentQIndex === 0}
                style={{
                  background: 'var(--bg-surface)',
                  border: '1px solid var(--border-light)',
                  color: currentQIndex === 0 ? 'var(--text-muted)' : 'var(--text-primary)',
                  padding: '9px 18px',
                  borderRadius: 8,
                  fontSize: '0.86rem',
                  fontWeight: 600,
                  cursor: currentQIndex === 0 ? 'not-allowed' : 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6
                }}
              >
                <ChevronLeft size={16} /> 前の問
              </button>

              <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                キーボード [1] [2] [3] [4] または [←] [→] で操作可能
              </div>

              <button
                onClick={handleNext}
                style={{
                  background: 'linear-gradient(135deg, var(--torii-vermilion), #b91c1c)',
                  color: '#ffffff',
                  border: 'none',
                  padding: '9px 22px',
                  borderRadius: 8,
                  fontSize: '0.86rem',
                  fontWeight: 700,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  boxShadow: '0 2px 8px var(--torii-glow)'
                }}
              >
                次の問 <ChevronRight size={16} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
