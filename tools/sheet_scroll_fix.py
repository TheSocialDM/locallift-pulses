"""Sheet scroll fix (Nov 24 2026): card back no longer clipped (grows to fit), sheet box fits the real
visible screen (dvh, safe areas) and keeps its own scroll on iPhone. Idempotent. Usage: python3 tools/sheet_scroll_fix.py <html> ..."""
import sys
CSS='<style id="ll-scrollfix">.box{max-height:min(92dvh,calc(100dvh - env(safe-area-inset-top) - 24px))!important;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;touch-action:pan-y}.mcs1[data-side="b"]{height:auto!important;min-height:350px}.mcs1.mcbig[data-side="b"]{min-height:420px}.mcs1[data-side="b"] .mcbk{height:auto;min-height:inherit}</style>'
for p in sys.argv[1:]:
    t=open(p).read()
    if 'id="ll-scrollfix"' in t: print('already',p); continue
    t=t.replace('</head>',CSS+'</head>',1); open(p,'w').write(t); print('fixed',p)
