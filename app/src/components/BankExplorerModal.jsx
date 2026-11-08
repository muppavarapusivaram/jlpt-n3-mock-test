// app/src/components/BankExplorerModal.jsx
import React, { useState, useMemo } from 'react';
import { X, Search, Filter, BookOpen, Layers, Star, ExternalLink, HelpCircle } from 'lucide-react';
import questionBank from '../data/questionBank.json';

export default function BankExplorerModal({ onClose }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedBook, setSelectedBook] = useState('all');
  const [selectedMondai, setSelectedMondai] = useState('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');

  const allQuestions = questionBank.questions || [];

  // Extract unique books & mondai types
  const books = useMemo(() => {
    return Array.from(new Set(allQuestions.map(q => q.book))).filter(Boolean);
  }, [allQuestions]);

  const mondais = useMemo(() => {
    return Array.from(new Set(allQuestions.map(q => q.mondai_label))).filter(Boolean);
  }, [allQuestions]);

  // Filtering
  const filtered = useMemo(() => {
    return allQuestions.filter(q => {
      if (selectedBook !== 'all' && q.book !== selectedBook) return false;
      if (selectedMondai !== 'all' && q.mondai_label !== selectedMondai) return false;
      if (selectedDifficulty !== 'all' && q.difficulty !== parseInt(selectedDifficulty, 10)) return false;

      if (searchTerm.trim()) {
        const term = searchTerm.toLowerCase();
        const matchQ = (q.question || '').toLowerCase().includes(term);
        const matchExpl = (q.explanation || '').toLowerCase().includes(term);
        const matchOpts = (q.options || []).some(o => o.toLowerCase().includes(term));
        const matchGp = (q.grammar_points || []).some(g => g.toLowerCase().includes(term));
        if (!matchQ && !matchExpl && !matchOpts && !matchGp) return false;
      }

      return true;
    });
  }, [allQuestions, searchTerm, selectedBook, selectedMondai, selectedDifficulty]);

  return (
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
        maxWidth: 1000,
        width: '100%',
        height: '90vh',
        display: 'flex',
        flexDirection: 'column',
        overflow: 'hidden',
        position: 'relative'
      }}>
        {/* Header */}
        <div style={{
          padding: '18px 24px',
          background: 'var(--bg-card)',
          borderBottom: '1px solid var(--border-light)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div>
            <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', fontWeight: 700, color: 'var(--text-primary)' }}>
              📚 JLPT N3 公式問題バンク 探索ブラウザ
            </h2>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              全 {questionBank.total_questions} 問 ・ 95題の長文パッセージ収録
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text-muted)',
              cursor: 'pointer',
              padding: 6,
              fontSize: '1.2rem'
            }}
          >
            ✕
          </button>
        </div>

        {/* Filter Controls */}
        <div style={{
          padding: '14px 24px',
          background: 'var(--bg-surface)',
          borderBottom: '1px solid var(--border-light)',
          display: 'flex',
          flexWrap: 'wrap',
          gap: 12,
          alignItems: 'center'
        }}>
          {/* Search Box */}
          <div style={{
            flex: '1 1 240px',
            position: 'relative',
            display: 'flex',
            alignItems: 'center'
          }}>
            <Search size={16} style={{ position: 'absolute', left: 12, color: 'var(--text-muted)' }} />
            <input
              type="text"
              placeholder="漢字、単語、文法、解説で検索..."
              value={searchTerm}
              onChange={e => setSearchTerm(e.target.value)}
              style={{
                width: '100%',
                background: 'var(--bg-card)',
                border: '1px solid var(--border-light)',
                color: 'var(--text-primary)',
                padding: '8px 12px 8px 36px',
                borderRadius: 8,
                fontSize: '0.88rem',
                outline: 'none'
              }}
            />
          </div>

          {/* Book Filter */}
          <select
            value={selectedBook}
            onChange={e => setSelectedBook(e.target.value)}
            style={{
              background: 'var(--bg-card)',
              border: '1px solid var(--border-light)',
              color: 'var(--text-primary)',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.84rem'
            }}
          >
            <option value="all">すべての出所 (全冊)</option>
            {books.map(b => <option key={b} value={b}>{b}</option>)}
          </select>

          {/* Mondai Filter */}
          <select
            value={selectedMondai}
            onChange={e => setSelectedMondai(e.target.value)}
            style={{
              background: 'var(--bg-card)',
              border: '1px solid var(--border-light)',
              color: 'var(--text-primary)',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.84rem'
            }}
          >
            <option value="all">すべての大問</option>
            {mondais.map(m => <option key={m} value={m}>{m}</option>)}
          </select>

          {/* Difficulty Filter */}
          <select
            value={selectedDifficulty}
            onChange={e => setSelectedDifficulty(e.target.value)}
            style={{
              background: 'var(--bg-card)',
              border: '1px solid var(--border-light)',
              color: 'var(--text-primary)',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.84rem'
            }}
          >
            <option value="all">すべての難易度</option>
            <option value="1">レベル 1 (基礎)</option>
            <option value="2">レベル 2 (標準)</option>
            <option value="3">レベル 3 (発展)</option>
            <option value="4">レベル 4 (難関)</option>
          </select>

          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginLeft: 'auto' }}>
            該当: <strong style={{ color: 'var(--torii-vermilion)' }}>{filtered.length}</strong> 問
          </span>
        </div>

        {/* Question Cards List */}
        <div style={{
          flex: 1,
          overflowY: 'auto',
          padding: 24,
          display: 'flex',
          flexDirection: 'column',
          gap: 14,
          background: 'var(--bg-main)'
        }}>
          {filtered.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
              条件に一致する問題が見つかりませんでした。
            </div>
          ) : (
            filtered.map((q) => (
              <div
                key={q.id}
                className="washi-card"
                style={{
                  padding: '18px 22px',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                    <span style={{
                      background: 'rgba(197, 48, 48, 0.08)',
                      color: 'var(--torii-vermilion)',
                      padding: '2px 8px',
                      borderRadius: 4,
                      fontSize: '0.74rem',
                      fontWeight: 700
                    }}>
                      {q.mondai_label} #{q.mondai_number}
                    </span>
                    <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                      [{q.id}]
                    </span>
                    <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                      • {q.book} (p.{q.page})
                    </span>
                  </div>

                  <span style={{
                    fontSize: '0.74rem',
                    padding: '2px 8px',
                    borderRadius: 4,
                    background: q.difficulty === 1 ? 'rgba(21, 128, 61, 0.08)' : q.difficulty === 2 ? 'rgba(217, 119, 6, 0.08)' : 'rgba(197, 48, 48, 0.08)',
                    color: q.difficulty === 1 ? 'var(--pine-green)' : q.difficulty === 2 ? 'var(--momiji-amber)' : 'var(--torii-vermilion)',
                    fontWeight: 600
                  }}>
                    難易度: Lv{q.difficulty}
                  </span>
                </div>

                <div 
                  style={{ fontSize: '1.02rem', color: 'var(--text-primary)', marginBottom: 12, lineHeight: 1.7, fontWeight: 500 }}
                  dangerouslySetInnerHTML={{
                    __html: (q.question || '')
                      .replace(/\n/g, '<br>')
                      .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:2px solid var(--torii-vermilion); padding:0 2px; font-weight:700;">$1</u>')
                  }}
                />

                {/* Options Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 6, marginBottom: 10 }}>
                  {(q.options || []).map((opt, i) => {
                    const optNum = i + 1;
                    const isAnswer = q.answer === optNum;

                    return (
                      <div
                        key={i}
                        style={{
                          padding: '6px 10px',
                          borderRadius: 6,
                          fontSize: '0.84rem',
                          background: isAnswer ? 'rgba(21, 128, 61, 0.08)' : 'var(--bg-surface)',
                          border: '1px solid ' + (isAnswer ? 'var(--pine-green)' : 'var(--border-light)'),
                          color: isAnswer ? 'var(--pine-green)' : 'var(--text-primary)',
                          fontWeight: isAnswer ? 700 : 400
                        }}
                      >
                        <span style={{ marginRight: 6 }}>{optNum}.</span>
                        {opt} {isAnswer && '✓ (正解)'}
                      </div>
                    );
                  })}
                </div>

                {/* Explanation */}
                {q.explanation && (
                  <div style={{ fontSize: '0.82rem', color: 'var(--text-secondary)', background: 'var(--bg-surface)', padding: '8px 12px', borderRadius: 6, borderLeft: '3px solid var(--momiji-amber)' }}>
                    💡 <strong>公式解説:</strong> {q.explanation}
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
