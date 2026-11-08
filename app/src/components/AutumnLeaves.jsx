// app/src/components/AutumnLeaves.jsx
import React, { useMemo } from 'react';
import leafMomijiRed from '../assets/leaf_momiji_red.png';
import leafMomijiAmber from '../assets/leaf_momiji_amber.png';
import leafGinkgoFan from '../assets/leaf_ginkgo_fan.png';

/**
 * Photorealistic Japanese Autumn Foliage (紅葉 - Momiji & Ginkgo)
 * Uses high-resolution botanical leaf cutouts with organic 3D tumbling physics.
 * Floats in foreground (zIndex: 25) with negative delays so leaves are immediately
 * drifting through the air when the page loads.
 */
export default function AutumnLeaves() {
  const leaves = useMemo(() => {
    const leafImages = [leafMomijiRed, leafMomijiAmber, leafGinkgoFan];

    return Array.from({ length: 26 }).map((_, i) => {
      const img = leafImages[i % leafImages.length];
      const isForeground = i % 4 === 0;
      const isBackground = i % 3 === 0;
      
      const size = isForeground ? (34 + (i % 3) * 7) : isBackground ? (18 + (i % 4) * 4) : (26 + (i % 4) * 4);
      const opacity = isForeground ? 0.96 : isBackground ? 0.72 : 0.88;
      const duration = 14 + (i % 7) * 2.5; // 14s to 29s graceful tumbling
      // Negative delay means leaves are already distributed throughout the screen at t=0
      const delay = ((i * 1.8) % duration).toFixed(1);
      const isAlt = i % 2 === 1;

      return {
        id: i,
        img,
        left: `${(i * 4.2 + (i % 5) * 6.5) % 96}%`,
        delay: `-${delay}s`,
        duration: `${duration}s`,
        size,
        opacity,
        isForeground,
        isAlt,
        blur: isBackground ? '0.4px' : 'none',
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
        zIndex: 25
      }}
    >
      {leaves.map((leaf) => (
        <img
          key={leaf.id}
          src={leaf.img}
          alt=""
          className={leaf.isAlt ? "real-autumn-leaf-alt" : "real-autumn-leaf"}
          style={{
            position: 'absolute',
            left: leaf.left,
            top: -60,
            width: leaf.size,
            height: 'auto',
            opacity: leaf.opacity,
            animationDelay: leaf.delay,
            animationDuration: leaf.duration,
            filter: `drop-shadow(0 4px 10px rgba(180, 83, 9, 0.2)) ${leaf.blur !== 'none' ? `blur(${leaf.blur})` : ''}`,
            userSelect: 'none',
            pointerEvents: 'none',
            willChange: 'transform, top'
          }}
        />
      ))}
    </div>
  );
}
