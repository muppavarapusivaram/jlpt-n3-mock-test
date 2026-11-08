// app/src/components/FujiToriiHero.jsx
import React from 'react';
import fujiToriiImage from '../assets/fuji_torii_real.jpg';

/**
 * Ultra-realistic Mount Fuji & Grand Vermilion Torii Gate Scenic Banner
 * Features authentic photographic depth, sunrise lighting, and seamless parchment fade.
 */
export default function FujiToriiHero() {
  return (
    <div style={{
      width: '100%',
      maxWidth: 1040,
      margin: '0 auto 16px',
      position: 'relative',
      borderRadius: 18,
      overflow: 'hidden',
      boxShadow: '0 8px 30px rgba(87, 83, 78, 0.08)',
    }}>
      {/* Real Photographic Fuji & Torii Hero */}
      <div style={{
        position: 'relative',
        width: '100%',
        height: 290,
        backgroundImage: `url(${fujiToriiImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center 40%',
      }}>
        {/* Soft bottom parchment gradient fade for seamless integration */}
        <div style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 120,
          background: 'linear-gradient(to bottom, rgba(250, 249, 246, 0) 0%, rgba(250, 249, 246, 0.8) 60%, var(--bg-main) 100%)',
          pointerEvents: 'none'
        }} />

        {/* Subtle top vignette */}
        <div style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 60,
          background: 'linear-gradient(to bottom, rgba(0,0,0,0.12) 0%, transparent 100%)',
          pointerEvents: 'none'
        }} />

        {/* Floating Japanese Seal Stamp in top right corner */}
        <div style={{
          position: 'absolute',
          top: 16,
          right: 20,
          background: 'rgba(255, 255, 255, 0.85)',
          backdropFilter: 'blur(8px)',
          border: '1px solid rgba(197, 48, 48, 0.3)',
          borderRadius: 24,
          padding: '5px 14px',
          display: 'flex',
          alignItems: 'center',
          gap: 6,
          boxShadow: '0 4px 12px rgba(0,0,0,0.08)'
        }}>
          <span style={{ color: 'var(--torii-vermilion)', fontSize: '0.82rem', fontWeight: 700 }}>⛩️ 富士山麓・鳥居</span>
          <span className="hanko-stamp" style={{ fontSize: '0.68rem', padding: '1px 5px' }}>合掌</span>
        </div>
      </div>
    </div>
  );
}
