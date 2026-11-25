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
# Meet Mia hero mockup: speech bubble under the mini card, never over its buttons; same words as the card
s=re.sub(r'(\.mcah\{position:relative;)height:210px;',r'\1height:240px;',s)
s=re.sub(r'\.mcsay\{position:absolute;right:100px;bottom:62px;max-width:52%;','.mcsay{position:absolute;left:16px;right:auto;bottom:16px;max-width:calc(100% - 136px);',s)
s=s.replace("<div class=\"mcsay\">Hi, I'm Mia! Want to book a tour with ${esc(me||'us')}?</div>","<div class=\"mcsay\">Hi, I'm Mia! I'll get you to ${esc(me||'your leasing team')}.</div>")
# Today hero: a little room between the logo row and the date line
if 'id="lltopgap"' not in s:
    s=s.replace('</head>','<style id="lltopgap">.top .trow{margin-bottom:8px}</style></head>',1)
# no gate flash: when the link carries a code or this phone is already signed in, start with the gate hidden.
# shut() still shows it (inline display:flex) if the code turns out to be wrong or removed.
if 'id="llnoflash"' not in s:
    s=s.replace('</head>','<script id="llnoflash">try{var q=new URLSearchParams(location.search),on=q.get("p")||q.get("invite");for(var i=0;!on&&i<localStorage.length;i++){var k=localStorage.key(i);if(/-invited$/.test(k)&&localStorage.getItem(k))on=1}if(on)document.write("<style id=llnoflashcss>#gate{display:none}</style>")}catch(e){}</script></head>',1)
# name from a personal link always wins (so Michael's n=Greyson link renames his phone); and a visible
# "Not <name>? Change name" link on My card, not only at the bottom of Reviews
s=re.sub(r"if\(nm&&!get\('([a-z]+)-me'\)\)",r"if(nm)",s)
if 'id="bMe" data-where="card"' not in s:
    mcol=re.search(r'<button class="gl" id="bMe" style="[^"]*color:(#[0-9a-fA-F]{3,6})',s)
    col=mcol.group(1) if mcol else '#0b4a6b'
    s=s.replace("${me?'':'<div class=\"mcnm\">","${me?'<button class=\"gl\" id=\"bMe\" data-where=\"card\" style=\"display:block;margin:4px auto 6px;border:0;background:none;padding:6px 10px;font:inherit;font-size:14px;font-weight:700;color:"+col+";cursor:pointer\">Not '+esc(me)+'? Change name</button>':'<div class=\"mcnm\">",1)

# Editor Nov 24 (Fora and COYA): plural aware review ask label, hide stat tiles that read 0, scroll padding above the floating buttons
s=s.replace('<div class="cen">practice review asks</div>',"<div class=\"cen\">practice review ask${asks===1?'':'s'}</div>")
_ms=re.search(r"const mcStats=\(\)=>`<div class=\"mcst\"><div><b>\$\{mcN\(/\^Card opened/\)\}</b><span>Card opens</span></div><div><b>\$\{mcN\(/\^QR shown\|\^Card opened/\)\}</b><span>QR shown</span></div><div><b>\$\{mcN\(/\^Sent/\)\}</b><span>Cards sent</span></div></div>`;",s)
if _ms:
    s=s.replace(_ms.group(0),"const mcStats=()=>{const a=[[mcN(/^Card opened/),'Card opens'],[mcN(/^QR shown|^Card opened/),'QR shown'],[mcN(/^Sent/),'Cards sent']].filter(x=>x[0]>0);return a.length?`<div class=\"mcst\" style=\"grid-template-columns:repeat(${a.length},1fr)\">${a.map(x=>`<div><b>${x[0]}</b><span>${x[1]}</span></div>`).join('')}</div>`:''};")
if "${mcStats()?'<p class=\"mcd\">" not in s: s=s.replace('<p class="mcd">Counts from this phone for the last 7 days.</p>',"${mcStats()?'<p class=\"mcd\">Counts from this phone for the last 7 days.</p>':''}")
s=s.replace('<div class="mine" style="grid-template-columns:1fr"><div><b>${row?row[1]:0}</b><span>residents opened Google from your code this month</span></div></div>',"${row&&+row[1]>0?`<div class=\"mine\" style=\"grid-template-columns:1fr\"><div><b>${row[1]}</b><span>residents opened Google from your code this month</span></div></div>`:''}")
if 'id="llscrollpad"' not in s:
    s=s.replace('</head>','<style id="llscrollpad">html{scroll-padding-bottom:140px}</style></head>',1)

# Editor Nov 24 final pass: star row drawn from the rating (half star for .3 to .7), and text-wrap:pretty on body text so phones avoid one word last lines
s=re.sub(r'(<div class="stars" aria-label="\$\{esc\(\(D&&D\.rv&&D\.rv\.rating\)\|\|\'\'\)\} stars">)★★★★★(</div>)',r"\1${llStars((D&&D.rv&&D.rv.rating)||'')}\2",s)
if 'id="llstars"' not in s:
    s=s.replace('</head>','<style id="llstars">.llst{display:inline-block;position:relative}.llst .e{opacity:.28}.llst .f{position:absolute;left:0;top:0;width:50%;overflow:hidden;white-space:nowrap}</style><script id="llstarsjs">window.llStars=function(r){r=parseFloat(r);if(!(r>=0))return"★★★★★";var n=Math.floor(r),d=r-n,h=0;if(d>=.3&&d<=.7)h=1;else if(d>.7)n+=1;n=Math.min(n,5);var o="";for(var i=0;i<n;i++)o+="★";if(h&&n<5)o+=\'<span class="llst"><span class="e">★</span><span class="f">★</span></span>\';for(var j=n+(h&&n<5?1:0);j<5;j++)o+=\'<span class="llst"><span class="e">★</span></span>\';return o}</script></head>',1)
if 'id="llpretty"' not in s:
    s=s.replace('</head>','<style id="llpretty">p,li,small,.mcd,.vs,.cen,.sub,.hint,.body,figcaption{text-wrap:pretty}</style></head>',1)
if len(sys.argv)>2:
    s=re.sub(r"const APPV='[^']*'",f"const APPV='{sys.argv[2]}'",s)
    open(p.replace('index.html','version.txt'),'w').write(sys.argv[2]+'\n')
checks={'nav97':'.97)' in s,'pad178':'178px' in s,'you':'background:#fff;color:#1c1c1e' in s,'chev':'<em>›</em></section>`' not in s,'bullet':'She points every lead to you' not in s,'hint':'.mchint{position:static' in s,'navbg':'id="llnavbg"' in s,'mcsay':'left:16px;right:auto;bottom:16px' in s and "I'll get you to ${esc(me" in s,'topgap':'lltopgap' in s,'plural':'practice review asks</div>' not in s,'zerotiles':'${mcN(/^Sent/)}</b>' not in s,'scrollpad':'llscrollpad' in s,'stars':'★★★★★</div>' not in s and 'llStars' in s,'pretty':'llpretty' in s}
open(p,'w').write(s);print(p,'changed' if s!=n0 else 'unchanged',checks)
