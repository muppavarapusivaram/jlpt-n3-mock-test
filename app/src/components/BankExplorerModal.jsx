// app/src/components/BankExplorerModal.jsx
import React, { useState } from 'react';
import { X, Search, Filter, BookOpen, Layers } from 'lucide-react';
import questionBank from '../data/questionBank.json';

export default function BankExplorerModal({ onClose }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedBook, setSelectedBook] = useState('all');
  const [selectedMondai, setSelectedMondai] = useState('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');

  const books = Array.from(new Set(questionBank.questions.map(q => q.book)));
  const mondais = Array.from(new Set(questionBank.questions.map(q => q.mondai_type)));

  const filtered = questionBank.questions.filter(q => {
    if (selectedBook !== 'all' && q.book !== selectedBook) return false;
    if (selectedMondai !== 'all' && q.mondai_type !== selectedMondai) return false;
    if (selectedDifficulty !== 'all' && String(q.difficulty) !== selectedDifficulty) return false;
    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      const matchQ = q.question.toLowerCase().includes(term);
      const matchOpts = q.options.some(o => o.toLowerCase().includes(term));
      const matchExp = (q.explanation || '').toLowerCase().includes(term);
      if (!matchQ && !matchOpts && !matchExp) return false;
    }
    return true;
  });

  return (
    <div style={{
      position: 'fixed',
      top: 0, left: 0, right: 0, bottom: 0,
      background: 'rgba(0,0,0,0.85)',
      backdropFilter: 'blur(6px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000,
      padding: 20
    }}>
      <div style={{
        background: 'var(--bg-surface)',
        border: '1px solid var(--border-subtle)',
        borderRadius: 16,
        width: '100%',
        maxWidth: 1020,
        height: '90vh',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '0 20px 50px rgba(0,0,0,0.6)',
        overflow: 'hidden'
      }}>
        {/* Modal Header */}
        <div style={{
          padding: '16px 24px',
          borderBottom: '1px solid var(--border-subtle)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div>
            <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', fontWeight: 700, color: '#fff' }}>
              📚 JLPT N3 公式問題バンク 探索ブラウザ
            </h2>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              全 {questionBank.total_questions} 問 ・ 42題の長文パッセージ
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text-muted)',
              cursor: 'pointer',
              padding: 6
            }}
          >
            <X size={20} />
          </button>
        </div>

        {/* Filter Controls */}
        <div style={{
          padding: '14px 24px',
          background: 'var(--bg-card)',
          borderBottom: '1px solid var(--border-subtle)',
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
                background: 'var(--bg-surface)',
                border: '1px solid var(--border-subtle)',
                color: '#fff',
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
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-subtle)',
              color: '#fff',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.85rem'
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
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-subtle)',
              color: '#fff',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.85rem'
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
              background: 'var(--bg-surface)',
              border: '1px solid var(--border-subtle)',
              color: '#fff',
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: '0.85rem'
            }}
          >
            <option value="all">すべての難易度</option>
            <option value="1">Level 1 (基礎)</option>
            <option value="2">Level 2 (標準)</option>
            <option value="3">Level 3 (発展)</option>
            <option value="4">Level 4 (難問)</option>
          </select>

          <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)', marginLeft: 'auto' }}>
            該当: <strong>{filtered.length}</strong> 問
          </span>
        </div>

        {/* Question Cards Scroll Area */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '20px 24px', display: 'flex', flexDirection: 'column', gap: 14 }}>
          {filtered.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
              条件に一致する問題が見つかりませんでした。
            </div>
          ) : (
            filtered.map((q, idx) => (
              <div
                key={q.id}
                style={{
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 10,
                  padding: '16px 20px'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{
                      background: 'rgba(56, 189, 248, 0.15)',
                      color: 'var(--fuji-cyan)',
                      padding: '2px 8px',
                      borderRadius: 4,
                      fontSize: '0.75rem',
                      fontWeight: 700
                    }}>
                      {q.mondai_label} #{q.mondai_number}
                    </span>
                    <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                      {q.book}
                    </span>
                  </div>

                  <span style={{
                    fontSize: '0.75rem',
                    background: q.difficulty === 1 ? 'rgba(16, 185, 129, 0.15)' : q.difficulty === 3 ? 'rgba(245, 158, 11, 0.15)' : 'rgba(56, 189, 248, 0.15)',
                    color: q.difficulty === 1 ? 'var(--bamboo-green)' : q.difficulty === 3 ? 'var(--gold-amber)' : 'var(--fuji-cyan)',
                    padding: '2px 8px',
                    borderRadius: 4,
                    fontWeight: 600
                  }}>
                    難易度 Lv.{q.difficulty || 2}
                  </span>
                </div>

                <div 
                  style={{ fontSize: '1.05rem', color: '#fff', marginBottom: 12, lineHeight: 1.7 }}
                  dangerouslySetInnerHTML={{
                    __html: q.question
                      .replace(/\n/g, '<br>')
                      .replace(/__([^_]+)__/g, '<u style="text-decoration:none; border-bottom:2px solid var(--fuji-cyan); font-weight:700;">$1</u>')
                  }}
                />

                {/* 4 Options Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 6, marginBottom: 10 }}>
                  {q.options.map((opt, i) => {
                    const isAns = (i + 1) === q.answer;
                    return (
                      <div key={i} style={{
                        padding: '6px 10px',
                        borderRadius: 6,
                        background: isAns ? 'rgba(16, 185, 129, 0.15)' : 'var(--bg-surface)',
                        border: '1px solid ' + (isAns ? 'var(--bamboo-green)' : 'var(--border-subtle)'),
                        color: isAns ? '#6ee7b7' : 'var(--text-secondary)',
                        fontSize: '0.85rem',
                        fontWeight: isAns ? 700 : 400
                      }}>
                        {i + 1}. {opt} {isAns && '★ 正解'}
                      </div>
                    );
                  })}
                </div>

                {q.explanation && (
                  <div style={{ fontSize: '0.82rem', color: '#cbd5e1', background: '#0c1322', padding: '6px 12px', borderRadius: 4 }}>
                    解説: {q.explanation}
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
