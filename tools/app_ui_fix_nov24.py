"""Editor fixes Nov 24 2026 for every LocalLift Live app (idempotent):
solid tab bar (97% opaque), room at the bottom of every page for the nav plus the floating Start tour and My card
buttons, readable YOU badge on the card back, one chevron on the page assistant card, no repeated bullet on the Mia sheet.
Usage: python3 tools/app_ui_fix_nov24.py live/<app>/v3/index.html [APPV]"""
import re,sys
p=sys.argv[1];s=open(p).read();n0=s
# 7: tab bar at least 95% opaque, light and dark
s=re.sub(r'(nav\{position:fixed;[^}]*?background:rgba\(\d+,\d+,\d+,)\.8\)',r'\1.97)',s)
s=s.replace('nav{background:rgba(28,28,30,.85);','nav{background:rgba(28,28,30,.97);')
s=s.replace('nav{background:rgba(28,28,30,.96)!important;','nav{background:rgba(28,28,30,.97)!important;')
# 7 and 8: page bottom room = nav + floating buttons
s=s.replace('.app{padding-bottom:calc(150px + env(safe-area-inset-bottom))!important}','.app{padding-bottom:calc(178px + env(safe-area-inset-bottom))!important}')
# 9: YOU badge readable on any card color
s=re.sub(r'\.mcyou\{position:absolute;left:50%;bottom:-8px;transform:translateX\(-50%\);background:#[0-9a-f]{6};color:#fff\}',
 '.mcyou{position:absolute;left:50%;bottom:-8px;transform:translateX(-50%);background:#fff;color:#1c1c1e;box-shadow:0 1px 4px rgba(0,0,0,.25)}',s)
# duplicate chevron on the page assistant card
s=s.replace('See what renters see ›</span></div><em>›</em></section>','See what renters see ›</span></div></section>')
# duplicate bullet on the Mia sheet
s=s.replace('<li><b>She points every lead to you.</b></li>','')
# renters see: hint pill next to Mia, never over the profile card (guide.js hides its own bubble in preview)
s=re.sub(r'\.mchint\{position:absolute;right:96px;bottom:118px;','.mchint{position:static;align-self:center;margin:16px auto calc(16px + env(safe-area-inset-bottom));',s)
# 7: solid backdrop under and around the floating tab bar, so page text never shows below it
if 'id="llnavbg"' not in s:
    s=s.replace('</head>','<style id="llnavbg">body::after{content:"";position:fixed;left:0;right:0;bottom:0;height:calc(92px + env(safe-area-inset-bottom));background:linear-gradient(to bottom,transparent,var(--bg) 26%);pointer-events:none;z-index:4}</style></head>',1)
# renters see: hint sits under the page view, never over it
s=s.replace('.mchint{position:absolute;right:118px;bottom:40px;','.mchint{position:static;align-self:center;margin:16px auto calc(16px + env(safe-area-inset-bottom));')
s=s.replace('.mcifw{flex:1;position:relative;min-height:0;display:flex}','.mcifw{flex:1;position:relative;min-height:0;display:flex;flex-direction:column}')
if len(sys.argv)>2:
    s=re.sub(r"const APPV='[^']*'",f"const APPV='{sys.argv[2]}'",s)
    open(p.replace('index.html','version.txt'),'w').write(sys.argv[2]+'\n')
checks={'nav97':'.97)' in s,'pad178':'178px' in s,'you':'background:#fff;color:#1c1c1e' in s,'chev':'<em>›</em></section>`' not in s,'bullet':'She points every lead to you' not in s,'hint':'.mchint{position:static' in s,'navbg':'id="llnavbg"' in s}
open(p,'w').write(s);print(p,'changed' if s!=n0 else 'unchanged',checks)
