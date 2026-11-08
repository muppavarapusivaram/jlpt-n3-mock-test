// app/src/components/AutumnLeaves.jsx
import React, { useMemo } from 'react';
import leafMomijiRed from '../assets/leaf_momiji_red.png';
import leafMomijiAmber from '../assets/leaf_momiji_amber.png';
import leafGinkgoFan from '../assets/leaf_ginkgo_fan.png';

/**
 * Photorealistic Japanese Autumn Foliage (紅葉 - Momiji & Ginkgo)
 * Uses high-resolution botanical leaf cutouts with organic 3D tumbling physics.
 */
export default function AutumnLeaves() {
  const leaves = useMemo(() => {
    const leafImages = [leafMomijiRed, leafMomijiAmber, leafGinkgoFan];

    return Array.from({ length: 18 }).map((_, i) => {
      const img = leafImages[i % leafImages.length];
      const isForeground = i % 5 === 0;
      const isBackground = i % 3 === 0;
      
      const size = isForeground ? (32 + (i % 3) * 6) : isBackground ? (18 + (i % 4) * 3) : (24 + (i % 4) * 4);
      const opacity = isForeground ? 0.95 : isBackground ? 0.65 : 0.85;
      const duration = 15 + (i % 7) * 2.5; // 15s to 30s gentle fall
      const delay = (i * 1.6) % 18;

      return {
        id: i,
        img,
        left: `${(i * 5.5 + Math.sin(i * 1.8) * 4) % 96}%`,
        delay: `${delay}s`,
        duration: `${duration}s`,
        size,
        opacity,
        isForeground,
        blur: isBackground ? '0.6px' : 'none',
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
        <img
          key={leaf.id}
          src={leaf.img}
          alt=""
          className="real-autumn-leaf"
          style={{
            position: 'absolute',
            left: leaf.left,
            top: -50,
            width: leaf.size,
            height: 'auto',
            opacity: leaf.opacity,
            animationDelay: leaf.delay,
            animationDuration: leaf.duration,
            filter: `drop-shadow(0 4px 10px rgba(180, 83, 9, 0.16)) ${leaf.blur !== 'none' ? `blur(${leaf.blur})` : ''}`,
            userSelect: 'none',
            pointerEvents: 'none',
          }}
        />
      ))}
    </div>
  );
}
