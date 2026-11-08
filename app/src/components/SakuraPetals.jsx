// app/src/components/SakuraPetals.jsx
import React from 'react';

export default function SakuraPetals() {
  // 15 floating petals with varying sizes, positions, animations
  const petals = [
    { left: '4%', delay: '0s', duration: '14s', size: 14, opacity: 0.6 },
    { left: '12%', delay: '3.5s', duration: '18s', size: 18, opacity: 0.5 },
    { left: '22%', delay: '7s', duration: '16s', size: 12, opacity: 0.7 },
    { left: '34%', delay: '1s', duration: '20s', size: 16, opacity: 0.4 },
    { left: '45%', delay: '5s', duration: '15s', size: 15, opacity: 0.6 },
    { left: '56%', delay: '2s', duration: '19s', size: 13, opacity: 0.5 },
    { left: '67%', delay: '8s', duration: '17s', size: 17, opacity: 0.6 },
    { left: '78%', delay: '4s', duration: '22s', size: 14, opacity: 0.4 },
    { left: '88%', delay: '6s', duration: '16s', size: 16, opacity: 0.7 },
    { left: '95%', delay: '2.5s', duration: '21s', size: 12, opacity: 0.5 },
  ];

  return (
    <div 
      aria-hidden="true" 
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        pointerEvents: 'none',
        overflow: 'hidden',
        zIndex: 0
      }}
    >
      {petals.map((p, idx) => (
        <span
          key={idx}
          className="sakura-petal"
          style={{
            left: p.left,
            animationDelay: p.delay,
            animationDuration: p.duration,
            width: p.size,
            height: p.size * 1.3,
            opacity: p.opacity,
          }}
        />
      ))}
    </div>
  );
}
