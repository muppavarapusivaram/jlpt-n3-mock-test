// app/src/components/FujiToriiHero.jsx
import React from 'react';

/**
 * Authentic Japanese Mount Fuji (富士山) & Torii Gate (鳥居) Scenic Illustration
 * Rendered in traditional Nihonga / Ukiyo-e silhouette aesthetic with vermilion & gold.
 */
export default function FujiToriiHero() {
  return (
    <div style={{
      width: '100%',
      maxWidth: 720,
      margin: '0 auto 20px',
      position: 'relative',
      display: 'flex',
      justifyContent: 'center',
      pointerEvents: 'none',
      userSelect: 'none'
    }}>
      <svg
        viewBox="0 0 600 190"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        style={{ width: '100%', height: 'auto', maxHeight: 180, overflow: 'visible' }}
      >
        <defs>
          {/* Rising Sun Radial Gradient */}
          <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#ef4444" stopOpacity="0.85" />
            <stop offset="70%" stopColor="#dc2626" stopOpacity="0.45" />
            <stop offset="100%" stopColor="#dc2626" stopOpacity="0" />
          </radialGradient>

          {/* Mount Fuji Body Gradient */}
          <linearGradient id="fujiGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#475569" />
            <stop offset="45%" stopColor="#334155" />
            <stop offset="100%" stopColor="#1e293b" />
          </linearGradient>

          {/* Snow Cap Gradient */}
          <linearGradient id="fujiSnow" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#ffffff" />
            <stop offset="70%" stopColor="#f8fafc" />
            <stop offset="100%" stopColor="#e2e8f0" />
          </linearGradient>

          {/* Autumn Gold Cloud Gradient */}
          <linearGradient id="cloudGold" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#d97706" stopOpacity="0" />
            <stop offset="50%" stopColor="#f59e0b" stopOpacity="0.25" />
            <stop offset="100%" stopColor="#d97706" stopOpacity="0" />
          </linearGradient>

          {/* Torii Gate Vermilion Lacquer */}
          <linearGradient id="toriiRed" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#ef4444" />
            <stop offset="100%" stopColor="#b91c1c" />
          </linearGradient>
        </defs>

        {/* 1. Crimson Rising Sun (旭日) behind Mount Fuji */}
        <circle cx="300" cy="95" r="70" fill="url(#sunGlow)" />
        <circle cx="300" cy="95" r="48" fill="#dc2626" fillOpacity="0.3" />

        {/* 2. Traditional Kasumi (霞) Mist / Cloud Ribbons */}
        <path d="M 120 110 Q 200 95 320 110 T 500 105" stroke="url(#cloudGold)" strokeWidth="8" strokeLinecap="round" />
        <path d="M 80 135 Q 260 125 440 135 T 540 130" stroke="url(#cloudGold)" strokeWidth="6" strokeLinecap="round" />

        {/* 3. Mount Fuji Mountain Base & Slopes (富士山) */}
        <path
          d="M 170 165 C 230 145 260 85 285 52 L 315 52 C 340 85 370 145 430 165 Z"
          fill="url(#fujiGradient)"
        />

        {/* 4. Mount Fuji Snow-Capped Peak (白雪の冠) with iconic ridges */}
        <path
          d="M 285 52 L 315 52 C 326 67 334 82 342 98 L 332 94 L 322 104 L 314 92 L 302 102 L 295 90 L 285 102 L 278 94 L 268 98 C 275 82 282 67 285 52 Z"
          fill="url(#fujiSnow)"
        />

        {/* 5. Traditional Japanese Torii Gate (鳥居) in Foreground */}
        <g transform="translate(265, 96)">
          {/* Top Curved Beam (笠木 / Kasagi & Shimaki) */}
          <path
            d="M -24 16 C -5 13 75 13 94 16 C 96 11 92 10 70 9 C 35 8 35 8 0 9 C -22 10 -26 11 -24 16 Z"
            fill="url(#toriiRed)"
            filter="drop-shadow(0 2px 4px rgba(0,0,0,0.15))"
          />
          {/* Black Lacquer Top Cap */}
          <path
            d="M -22 10 C -5 8 75 8 92 10 L 91 12 C 73 10 -3 10 -21 12 Z"
            fill="#1e293b"
          />

          {/* Secondary Straight Tie Beam (貫 / Nuki) */}
          <rect x="-8" y="24" width="86" height="5.5" rx="1" fill="url(#toriiRed)" />

          {/* Central Tablet (額束 / Gakuzuka - "奉納 / 合格") */}
          <rect x="31" y="14" width="8" height="11" fill="#1e293b" rx="1" />
          <rect x="32" y="15" width="6" height="9" fill="#f59e0b" rx="0.5" />

          {/* Left Main Pillar (柱 / Hashira) with incline & base rock (亀腹) */}
          <path d="M 6 15 L 2 68 L 10 68 L 12 15 Z" fill="url(#toriiRed)" />
          <rect x="0" y="65" width="14" height="4" rx="1" fill="#1e293b" />

          {/* Right Main Pillar (柱 / Hashira) with incline & base rock */}
          <path d="M 58 15 L 60 68 L 68 68 L 64 15 Z" fill="url(#toriiRed)" />
          <rect x="56" y="65" width="14" height="4" rx="1" fill="#1e293b" />
        </g>

        {/* 6. Distant Pine Tree Silhouettes (松) */}
        <path d="M 155 165 L 160 148 L 165 165 Z M 160 152 L 150 165 L 170 165 Z" fill="#334155" opacity="0.4" />
        <path d="M 440 165 L 445 146 L 450 165 Z M 445 150 L 434 165 L 456 165 Z" fill="#334155" opacity="0.4" />

        {/* 7. Subtle Waterline / Ground Horizon */}
        <line x1="80" y1="165" x2="520" y2="165" stroke="#cbd5e1" strokeWidth="1.5" strokeDasharray="6 4" opacity="0.7" />
      </svg>
    </div>
  );
}
