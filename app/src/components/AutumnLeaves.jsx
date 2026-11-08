// app/src/components/AutumnLeaves.jsx
import React, { useMemo } from 'react';

/**
 * Authentic Japanese Autumn Foliage (紅葉 - Momiji & Ginkgo)
 * Floating gently across the screen with natural swaying & 3D flutter.
 */
export default function AutumnLeaves() {
  const leaves = useMemo(() => {
    const colors = [
      '#dc2626', // Scarlet Red (深紅)
      '#ea580c', // Fiery Orange (柿色)
      '#d97706', // Golden Amber (琥珀)
      '#b91c1c', // Crimson Vermilion (朱色)
      '#eab308', // Ginkgo Gold (銀杏)
      '#c2410c', // Autumn Rust (落葉色)
    ];

    return Array.from({ length: 22 }).map((_, i) => {
      const isMaple = i % 3 !== 0; // 2 out of 3 are maple leaves, 1 is ginkgo
      return {
        id: i,
        left: `${(i * 4.6 + Math.sin(i) * 3) % 96}%`,
        delay: `${(i * 1.3) % 15}s`,
        duration: `${14 + (i % 8) * 2}s`,
        size: 16 + (i % 5) * 4,
        color: colors[i % colors.length],
        opacity: 0.55 + (i % 4) * 0.12,
        isMaple,
      };
    });
  }, []);

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
      {leaves.map((leaf) => (
        <span
          key={leaf.id}
          className="autumn-leaf"
          style={{
            position: 'absolute',
            left: leaf.left,
            animationDelay: leaf.delay,
            animationDuration: leaf.duration,
            width: leaf.size,
            height: leaf.size,
            opacity: leaf.opacity,
            color: leaf.color,
          }}
        >
          {leaf.isMaple ? (
            /* Traditional Japanese Momiji (紅葉) Maple Leaf SVG */
            <svg viewBox="0 0 24 24" fill="currentColor" width="100%" height="100%">
              <path d="M12 2 C12.5 5 14 6 16 5 C15.5 7.5 17 8.5 20 8 C18.5 10.5 19.5 12 21 13 C18.5 13.5 17.5 15 18 17 C15.5 16 14 17 13.5 19.5 C13 17 11 17 10.5 19.5 C10 17 8.5 16 6 17 C6.5 15 5.5 13.5 3 13 C4.5 12 5.5 10.5 4 8 C7 8.5 8.5 7.5 8 5 C10 6 11.5 5 12 2 Z" />
              <path d="M12 14 L12 23" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
            </svg>
          ) : (
            /* Traditional Japanese Ginkgo (銀杏) Fan Leaf SVG */
            <svg viewBox="0 0 24 24" fill="currentColor" width="100%" height="100%">
              <path d="M12 3 C6 3 2 9 5 15 C8 17 11 15 12 14 C13 15 16 17 19 15 C22 9 18 3 12 3 Z" />
              <path d="M12 14 L12 23" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" />
            </svg>
          )}
        </span>
      ))}
    </div>
  );
}
