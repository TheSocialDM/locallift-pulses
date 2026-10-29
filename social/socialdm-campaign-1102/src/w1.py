from base import *

SEA = 'sea-pexels-josh-hild-1270765-'

# ============================================================ Mon Nov 2
# G02 SDM. Approved copy: SEO traction, early traction often 60 to 90 days. Cinematic road + timeline.
ticks = [('Week 1', 0), ('Day 30', 33.3), ('Day 60', 66.6), ('Day 90', 100)]
T['g-1102-traction'] = G(f"""
<div class="photo" style="inset:0;{ph(SEA+'34685136','50% 60%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,10,.86) 0%,rgba(10,10,10,.55) 48%,rgba(10,10,10,.05) 80%)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,0) 55%,rgba(10,10,10,.85) 100%)"></div>
<div class="mono" style="position:absolute;left:64px;top:64px;font-size:24px;color:#FAFAF8">Apartment SEO</div>
<div class="fra" style="position:absolute;left:64px;width:640px;top:128px;font-size:76px;line-height:1.02;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">Real traction is measured in <span class="it red" style="font-weight:400">seasons,</span> not weeks.</div>
<div style="position:absolute;left:64px;right:64px;top:640px">
  <div style="position:relative;height:2px;background:rgba(255,255,255,.45)">
    <div style="position:absolute;left:66.6%;right:0;top:-3px;height:8px;background:var(--red)"></div>
    {''.join(f'<div style="position:absolute;left:{x}%;top:-9px;width:2px;height:20px;background:#FAFAF8;transform:translateX(-1px)"></div>' for _,x in ticks)}
  </div>
  {''.join(f'<div class="mono" style="position:absolute;left:{x}%;top:26px;font-size:21px;color:#FAFAF8;white-space:nowrap;transform:translateX({"0" if x==0 else "-100%" if x==100 else "-50%"})">{t}</div>' for t,x in ticks)}
  <div class="ins it" style="position:absolute;left:66.6%;top:-58px;font-size:30px;color:#FAFAF8;white-space:nowrap">early traction often shows up here</div>
</div>
{foot('sdm', True, right='', left=64, rightpx=64, bottom=48, scale=.82)}
""", bg='#0E0E0E')

# S02 SDM. Slow season. Cinematic gold balconies, condensed poster type.
T['s-1102-slow-season'] = S(f"""
<div class="photo" style="inset:0;{ph('34135423','50% 35%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.1) 0%,rgba(10,10,10,.15) 30%,rgba(10,10,10,.88) 62%,#0A0A0A 100%)"></div>
<div style="position:absolute;left:0;top:0;width:1080px;height:200px;background:linear-gradient(180deg,rgba(10,10,10,.55),rgba(10,10,10,0))"></div><div class="mono eye" style="color:#FAFAF8">Leasing in November</div>
<div style="position:absolute;left:76px;right:80px;top:560px">
  <div class="anton" style="font-size:150px;line-height:.92;color:#FAFAF8">Slow season</div>
  <div class="bod it red" style="font-size:96px;line-height:1.05;margin:4px 0 6px 6px">isn’t</div>
  <div class="anton" style="font-size:150px;line-height:.92;color:#FAFAF8">quiet season.</div>
</div>
<div style="position:absolute;left:80px;width:620px;top:1010px;font-size:30px;line-height:1.4;color:var(--dsoft)">Fewer renters are searching. The ones who are tend to be ready.</div>
{foot('sdm', True, right='')}
""", bg='#0A0A0A')

# ============================================================ Tue Nov 3
# G03 LL. Approved copy: renters search the neighborhood. Search phrases + leafy path.
phr = ['near my office', 'walkable to coffee', 'near a dog park', 'with a short commute']
T['g-1103-neighborhood-search'] = G(f"""
<div class="photo" style="right:0;top:0;width:470px;height:900px;{ph('19071671','50% 55%')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">How renters search</div>
<div class="bod" style="position:absolute;left:64px;top:118px;font-size:96px;line-height:1;color:#0E0E0E">apartments</div>
<div style="position:absolute;left:64px;width:590px;top:250px">
 {''.join(f'<div style="display:flex;align-items:baseline;gap:18px;border-top:1.5px solid #0E0E0E;padding:14px 0"><span class="mono red" style="font-size:24px">+</span><span class="ins it" style="font-size:46px;line-height:1;color:#0E0E0E">{p}</span></div>' for p in phr)}
 <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
<div class="news" style="position:absolute;left:64px;width:620px;top:606px;font-size:34px;line-height:1.15;color:#0E0E0E;font-weight:500">The neighborhood is part<br>of the search.</div>
{foot('ll', False, right='', left=64, rightpx=534, bottom=56)}
""")

# LI03 SDM. One renter, five doors. Editorial diagram.
doors = [('01','Google Search'),('02','Google Maps'),('03','Instagram'),('04','AI assistant'),('05','Listing site')]
cx, cy = 540, 650
import math
pts = []
for i,(n,l) in enumerate(doors):
    a = math.radians(-90 + i*72)
    pts.append((cx + 340*math.cos(a), cy + 300*math.sin(a), n, l))
svg_lines = ''.join(f'<line x1="{cx}" y1="{cy}" x2="{cx+(x-cx)*.8:.0f}" y2="{cy+(y-cy)*.8:.0f}" stroke="#0E0E0E" stroke-width="1.5" stroke-dasharray="6 8"/>' for i,(x,y,_,_) in enumerate(pts))
lab = ''
for i,(x,y,n,l) in enumerate(pts):
    anchor = 'center'
    lab += f'<div style="position:absolute;left:{x-170:.0f}px;top:{y-52:.0f}px;width:340px;text-align:center;background:#FAFAF8;padding:6px 0"><div class="mono red" style="font-size:28px">{n}</div><div class="news" style="font-size:46px;line-height:1.02;color:#0E0E0E;font-weight:500">{l}</div></div>'
T['li-1103-five-doors'] = S(f"""
<div class="mono red eye">How renters arrive</div><div class="eyeR"><span class="ex">Illustrative</span></div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:88px;line-height:1;color:#0E0E0E">One renter. <span class="it red">Five doors.</span></div>
<svg style="position:absolute;left:0;top:0" width="1080" height="1350">{svg_lines}<circle cx="{cx}" cy="{cy}" r="96" fill="#0E0E0E"/></svg>
<div class="mono" style="position:absolute;left:{cx-96}px;top:{cy-34}px;width:192px;text-align:center;font-size:28px;line-height:1.2;color:#FAFAF8">One<br>renter</div>
{lab}
<div class="fra" style="position:absolute;left:80px;right:80px;top:1000px;font-size:44px;line-height:1.15;font-weight:400;color:#0E0E0E">One story, told the same way <span class="it">at every door.</span></div>
{foot('sdm', False, right='')}
""")

# S03 SDM. Contact sheet, one frame circled.
frames = ['9368696','36486485','16058436','12187764','36486482','10161222']
cells = ''
for i,f in enumerate(frames):
    col, row = i % 3, i // 3
    x = 80 + col*312; y = 470 + row*330
    cells += f'<div class="photo" style="left:{x}px;top:{y}px;width:296px;height:296px;{ph(f)}"></div>'
    cells += f'<div class="mono" style="position:absolute;left:{x}px;top:{y+302}px;font-size:18px;color:#8E887F">{14+i}A</div>'
T['s-1103-first-tour'] = S(f"""
<div class="mono eye" style="color:#0E0E0E">Contact sheet</div><div class="mono red eyeR">Social</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:98px;line-height:1;color:#0E0E0E">Your feed is the <span class="red">first tour.</span></div>
<div style="position:absolute;left:66px;top:456px;width:948px;height:684px;background:#1A1918"></div>
{cells}
<svg style="position:absolute;left:0;top:0" width="1080" height="1350"><ellipse cx="540" cy="947" rx="190" ry="186" fill="none" stroke="#D2321E" stroke-width="7" transform="rotate(-6 540 947)"/></svg>
<div class="ins it red" style="position:absolute;left:690px;top:1146px;font-size:58px;transform:rotate(-4deg)">keep.</div>
{foot('sdm', False, right='')}
""")

# ============================================================ Wed Nov 4
# G04 SDM. Approved copy: research and insights, pour a coffee. Magazine masthead.
T['g-1104-insights'] = G(f"""
<div class="photo" style="left:0;top:330px;width:1200px;height:570px;{ph('3747070','50% 62%')}"></div>
<div style="position:absolute;left:0;top:330px;width:1200px;height:570px;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.72) 100%)"></div>
<div style="position:absolute;left:64px;right:64px;top:48px;border-top:2px solid #0E0E0E;border-bottom:1px solid #0E0E0E;height:10px"></div>
<div class="ital" style="position:absolute;left:58px;top:70px;font-size:168px;line-height:1;color:#0E0E0E;letter-spacing:-.01em">Insights</div>
<div style="position:absolute;right:64px;top:92px;text-align:right"><img src="{LG}socialdm-color.png" style="height:96px"></div>
<div style="position:absolute;left:64px;right:64px;top:268px;display:flex;justify-content:space-between;border-top:1px solid #0E0E0E;padding-top:12px">
 <span class="mono" style="font-size:20px;color:#0E0E0E">Research for multifamily</span><span class="mono red" style="font-size:20px">November 2026</span></div>
<div class="bod it" style="position:absolute;left:64px;width:1000px;bottom:56px;font-size:52px;line-height:1.05;color:#FAFAF8">How apartment communities get found.</div>
""")

# LI04 SDM. Swipe: before you set the 2027 budget.
Q4 = [
 ('01','Which channel brought tours, not just clicks?','Clicks are easy to count. Tours tell you what actually worked.'),
 ('02','Is your Google profile as current as your website?','Hours, specials, photos and prices. When they disagree, renters notice.'),
 ('03','What do AI assistants say about you today?','Ask them the questions your renters ask. Write down what comes back.'),
 ('04','What will you stop paying for?','A new year is a good moment to cut what can’t show its work.'),
]
T['li-1104-budget-1'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:760px;{ph('28534124','40% 50%')}"></div>
<div class="tag" style="position:absolute;left:80px;top:80px;background:#FAFAF8;color:#0E0E0E">Q4 planning</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:810px;font-size:96px;line-height:1;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">Before you set the <span class="it red" style="font-weight:400;margin-right:.12em">2027</span> budget.</div>
<div class="mono" style="position:absolute;left:80px;top:1060px;font-size:26px;color:#FAFAF8">Four questions</div><div class="mono red" style="position:absolute;right:80px;top:1060px;font-size:26px">Swipe</div>
{foot('sdm', True, right='')}
""", bg='#0E0E0E')
# four slides, four different placements of the numeral
n,q,b = Q4[0]
T['li-1104-budget-2'] = S(f"""
<div class="mono red eye">The 2027 budget</div>
<div class="bsd red" style="position:absolute;left:66px;top:180px;font-size:420px;line-height:.85;font-weight:900">{n}</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:560px;font-size:84px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">{q}</div>
<div style="position:absolute;left:80px;right:220px;top:930px;font-size:34px;line-height:1.42;color:var(--soft)">{b}</div>
{foot('sdm', False, right='')}
""")
n,q,b = Q4[1]
T['li-1104-budget-3'] = S(f"""
<div class="mono red eye">The 2027 budget</div>
<div class="bsd" style="position:absolute;right:40px;top:150px;font-size:520px;line-height:.85;font-weight:900;color:transparent;-webkit-text-stroke:3px #D2321E">{n}</div>
<div class="fra" style="position:absolute;left:80px;width:820px;top:640px;font-size:84px;line-height:1.02;font-weight:400;color:#FAFAF8;letter-spacing:-.015em">{q}</div>
<div style="position:absolute;left:80px;right:220px;top:1000px;font-size:34px;line-height:1.42;color:var(--dsoft)">{b}</div>
{foot('sdm', True, right='')}
""", bg='#0E0E0E')
n,q,b = Q4[2]
T['li-1104-budget-4'] = S(f"""
<div class="mono red eye">The 2027 budget</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:170px;font-size:84px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">{q}</div>
<div style="position:absolute;left:80px;right:240px;top:520px;font-size:34px;line-height:1.42;color:var(--soft)">{b}</div>
<div style="position:absolute;left:80px;width:500px;top:700px;border-top:2px solid #0E0E0E"></div>
<div class="bsd red" style="position:absolute;right:66px;top:690px;font-size:420px;line-height:.85;font-weight:900">{n}</div>
{foot('sdm', False, right='')}
""")
n,q,b = Q4[3]
T['li-1104-budget-5'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">The 2027 budget</div>
<div class="bsd" style="position:absolute;left:0;right:0;top:250px;text-align:center;font-size:700px;line-height:.8;font-weight:900;color:#BE2D1B">{n}</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:560px;font-size:96px;line-height:1;font-weight:600;color:#FAFAF8;letter-spacing:-.02em">{q}</div>
<div style="position:absolute;left:80px;right:220px;top:960px;font-size:34px;line-height:1.42;color:#FAFAF8">{b}</div>
<div style="position:absolute;left:0;bottom:0;width:1080px;height:240px;background:#0E0E0E"></div>
{foot('sdm', True, right='')}
""", bg='#D2321E')
T['li-1104-budget-6'] = S(f"""
<div class="mono red eye">The 2027 budget</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:150px;font-size:78px;line-height:1.04;font-weight:300;color:#0E0E0E;letter-spacing:-.02em">Four questions to ask <span class="it red" style="font-weight:400">before</span> you sign anything.</div>
<div style="position:absolute;left:80px;right:80px;top:500px">
""" + ''.join(f'<div style="display:flex;gap:30px;align-items:baseline;border-top:2px solid #0E0E0E;padding:24px 0"><span class="bsd red" style="font-size:44px;font-weight:800;width:58px">{n}</span><span style="font-size:35px;line-height:1.25;color:#0E0E0E;font-weight:500">{q}</span></div>' for n,q,b in Q4) + f"""
<div style="border-top:2px solid #0E0E0E"></div></div>
<div class="ins" style="position:absolute;left:80px;top:1070px;font-size:40px;color:#0E0E0E">Michael Shad</div>
{foot('sdm', False)}
""")

# S04 SDM. Poll: photos or video.
T['s-1104-poll'] = S(f"""
<div style="position:absolute;left:0;top:0;width:1080px;height:330px;background:#FAFAF8"></div>
<div class="mono red eye">Quick poll</div>
<div class="syne" style="position:absolute;left:80px;right:80px;top:140px;font-size:76px;line-height:1;font-weight:800;color:#0E0E0E;letter-spacing:-.03em">What gets you to book a tour?</div>
<div class="photo" style="left:0;top:330px;width:540px;height:860px;{ph('29696169','50% 50%')}"></div>
<div class="photo" style="left:540px;top:330px;width:540px;height:860px;{ph('10421300','30% 40%')}"></div>
<div style="position:absolute;left:538px;top:330px;width:4px;height:860px;background:#FAFAF8"></div>
<div class="anton" style="position:absolute;left:80px;top:400px;width:120px;height:120px;background:#FAFAF8;color:#0E0E0E;font-size:96px;line-height:120px;text-align:center">A</div>
<div class="anton" style="position:absolute;left:620px;top:400px;width:120px;height:120px;background:var(--red);color:#FAFAF8;font-size:96px;line-height:120px;text-align:center">B</div>
<div style="position:absolute;left:80px;top:1000px;width:380px;height:128px;background:#FAFAF8;padding:18px 22px"><div class="news" style="font-size:40px;line-height:1.05;font-weight:500;color:#0E0E0E">Ten great<br>photos</div></div>
<div style="position:absolute;left:620px;top:1000px;width:380px;height:128px;background:#0E0E0E;padding:18px 22px"><div class="news" style="font-size:40px;line-height:1.05;font-weight:500;color:#FAFAF8">One 20 second<br>video</div></div>
<div style="position:absolute;left:0;top:1190px;width:1080px;height:160px;background:#0E0E0E"></div>
{foot('sdm', True, right='VOTE A OR B', bottom=36, scale=.72)}
""", bg='#0E0E0E')

# ============================================================ Thu Nov 5
# G05 SDM. Pitch vs proof. Evaluate an agency on its live work.
pitch = ['More reach','More engagement','More leads']
proof = ['The Google special matches the website','Recent reviews have a thoughtful reply','Posts answer what renters ask']
T['g-1105-pitch-proof'] = G(f"""
<div class="photo" style="right:0;top:0;width:420px;height:900px;{ph('26629544','40% 50%')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:60px;font-size:24px">Choosing an agency</div>
<div class="bod" style="position:absolute;left:64px;width:660px;top:104px;font-size:64px;line-height:1.02;color:#FAFAF8">Ask to see the work, not the deck.</div>
<div style="position:absolute;left:64px;width:280px;top:330px">
 <div class="mono" style="font-size:20px;color:#8E887F;border-bottom:1px solid #3A3836;padding-bottom:12px">The pitch</div>
 {''.join(f'<div class="news" style="font-size:32px;line-height:1.1;color:#B5AFA6;padding:16px 0;text-decoration:line-through;text-decoration-color:#D2321E;text-decoration-thickness:2px">{p}</div>' for p in pitch)}
</div>
<div style="position:absolute;left:376px;width:364px;top:330px">
 <div class="mono red" style="font-size:20px;border-bottom:1px solid #D2321E;padding-bottom:12px">The proof</div>
 {''.join(f'<div style="font-size:25px;line-height:1.25;color:#FAFAF8;padding:14px 0;border-bottom:1px solid var(--dline)">{p}</div>' for p in proof)}
</div>
{foot('sdm', True, right='', left=64, rightpx=484, bottom=48, scale=.8)}
""", bg='#0E0E0E')

# S05 LL. Renters don't search like marketers.
T['s-1105-search-like'] = S(f"""
<div class="mono red eye">Search, as typed</div><div class="eyeR"><span class="ex">Example</span></div>
<div class="mono" style="position:absolute;left:80px;top:220px;font-size:24px;color:#8E887F">What the website says</div>
<div class="bod it" style="position:absolute;left:80px;top:268px;font-size:70px;color:#A39D93;text-decoration:line-through;text-decoration-color:#D2321E;text-decoration-thickness:4px">Luxury apartment homes</div>
<div class="mono" style="position:absolute;left:80px;top:470px;font-size:24px;color:#FAFAF8">What the renter types</div>
<div style="position:absolute;left:80px;right:80px;top:520px;background:#FAFAF8;border-radius:22px;padding:34px 40px 36px 104px">
 <svg style="position:absolute;left:38px;top:42px" width="40" height="40" viewBox="0 0 40 40"><circle cx="16" cy="16" r="12" fill="none" stroke="#0E0E0E" stroke-width="4"/><line x1="25" y1="25" x2="37" y2="37" stroke="#0E0E0E" stroke-width="4" stroke-linecap="round"/></svg>
 <div style="font-family:Mono,monospace;font-weight:500;font-size:40px;line-height:1.32;color:#0E0E0E">2 bed near light rail with covered parking under $1,900<span style="display:inline-block;width:4px;height:44px;background:#D2321E;vertical-align:-8px;margin-left:6px"></span></div>
</div>
<div class="syne" style="position:absolute;left:80px;right:80px;top:830px;font-size:82px;line-height:.98;font-weight:800;color:#FAFAF8;letter-spacing:-.035em">Renters don’t<br>search like <span style="color:#D2321E">marketers.</span></div>
{foot('ll', True, right='')}
""", bg='#0E0E0E')

# ============================================================ Fri Nov 6
# G06 LL. Approved copy: what LocalLift does.
layers = [('01','Search'),('02','Maps'),('03','Google profile'),('04','AI discovery')]
T['g-1106-locallift'] = G(f"""
<div class="photo" style="right:0;top:0;width:380px;height:900px;{ph('37476786','50% 50%')}"></div>
<div style="position:absolute;left:64px;top:64px"><img src="{LG}locallift-white.png" style="height:64px;display:block"></div>
<div class="bod" style="position:absolute;left:64px;width:700px;top:170px;font-size:68px;line-height:1.04;color:#FAFAF8">Be found where renters <span class="red">actually look.</span></div>
<div style="position:absolute;left:64px;width:690px;top:470px">
 {''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--dline);padding:18px 0"><span class="news" style="font-size:40px;color:#FAFAF8">{l}</span><span class="mono red" style="font-size:22px">{n}</span></div>' for n,l in layers)}
 <div style="border-top:1px solid var(--dline)"></div>
</div>
<div class="url" style="position:absolute;left:64px;bottom:56px;color:#FAFAF8;font-size:22px">By The SocialDM</div>
""", bg='#0E0E0E')

# LI06 LL. AI summarizes what's out there.
srcs = ['Your website','Your Google profile','Your reviews','Listing sites']
T['li-1106-ai-summarizes'] = S(f"""
<div class="mono red eye">AI search</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:150px;font-size:104px;line-height:.98;font-weight:300;color:#FAFAF8;letter-spacing:-.025em">AI doesn’t start from scratch.</div>
<div class="fra it red" style="position:absolute;left:80px;right:80px;top:420px;font-size:58px;line-height:1.08;font-weight:400">It summarizes what’s already out there about you.</div>
<div style="position:absolute;left:80px;width:440px;top:760px">
 {''.join(f'<div style="border:1px solid rgba(255,255,255,.4);padding:16px 20px;margin-bottom:14px;margin-left:{i*14}px"><span class="mono" style="font-size:22px;color:#FAFAF8">{s}</span></div>' for i,s in enumerate(srcs))}
</div>
<svg style="position:absolute;left:0;top:0" width="1080" height="1350"><path d="M580 910 C640 910 660 910 710 910" stroke="#D2321E" stroke-width="3" fill="none"/><path d="M702 900 L716 910 L702 920" stroke="#D2321E" stroke-width="3" fill="none"/></svg>
<div style="position:absolute;left:720px;right:40px;top:840px;background:#FAFAF8;padding:24px 22px 26px"><div class="mono red" style="font-size:20px">The answer</div><div class="news it" style="font-size:31px;line-height:1.2;margin-top:10px;color:#0E0E0E">built from what<br>it finds</div></div>
{foot('ll', True, right='')}
""", bg='#0E0E0E')

# S06 SDM. The reply is for the next renter.
T['s-1106-next-renter'] = S(f"""
<div class="photo" style="left:430px;top:0;width:650px;height:1350px;{ph('6589018','42% 40%')}"></div>
<div style="position:absolute;left:0;top:0;width:430px;height:1350px;background:#FAFAF8"></div>
<div class="mono red eye">Reviews</div>
<div class="bod" style="position:absolute;left:80px;width:340px;top:150px;font-size:74px;line-height:1.04;color:#0E0E0E">The reply is for the <span class="red">next</span> renter.</div>
<div style="position:absolute;left:80px;width:640px;top:760px;background:#FAFAF8;box-shadow:0 24px 60px rgba(0,0,0,.28);padding:30px 32px">
 <div style="display:flex;justify-content:space-between;align-items:center"><span class="red" style="font-size:34px;letter-spacing:3px">★★★★<span style="color:#CFCAC1">★</span></span><span class="ex">Example</span></div>
 <div class="news" style="font-size:30px;line-height:1.3;margin-top:14px;color:#0E0E0E">“Quiet building, quick maintenance. Parking gets tight on weekends.”</div>
 <div style="border-left:3px solid #D2321E;padding-left:18px;margin-top:20px"><div class="mono" style="font-size:19px;color:#6B665E">Reply from the leasing team</div><div class="news it" style="font-size:28px;line-height:1.3;margin-top:8px;color:#0E0E0E">Thank you, Jordan. We hear you on weekend parking. Stop by and we’ll walk you through guest options.</div></div>
</div>
{foot('sdm', False, right='', rightpx=670)}
""")

# ============================================================ Sat Nov 7
# G07 SDM. Your Google profile never closes. Night skyline.
T['g-1107-never-closes'] = G(f"""
<div class="photo" style="inset:0;{ph('9314007','50% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,8,12,.75) 0%,rgba(6,8,12,.45) 45%,rgba(6,8,12,.1) 62%,rgba(6,8,12,.85) 100%)"></div>
<div class="mono" style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:24px;color:#FAFAF8">After hours</div>
<div class="bod" style="position:absolute;left:100px;right:100px;top:118px;text-align:center;font-size:86px;line-height:1.02;color:#FAFAF8">Open late. <span class="it" style="color:#F0907F">Every night.</span></div>
<div class="news it" style="position:absolute;left:0;right:0;top:300px;text-align:center;font-size:38px;color:#FAFAF8;text-shadow:0 2px 18px rgba(0,0,0,.9)">Your Google profile never closes.</div>
<div style="position:absolute;left:0;right:0;bottom:52px;display:flex;justify-content:center"><img src="{LG}socialdm-reversed.png" style="height:92px"></div>
""", bg='#0E0E0E')

# LI07 SDM. Who answers at 7 PM on a Saturday.
T['li-1107-seven-pm'] = S(f"""
<div class="photo" style="left:0;top:0;width:600px;height:1350px;{ph('6611921','52% 50%')}"></div>
<div class="mono red" style="position:absolute;left:660px;top:80px;font-size:26px">After hours</div>
<div class="bsd red" style="position:absolute;left:650px;top:140px;font-size:222px;line-height:.86;font-weight:900;letter-spacing:-.01em">7:00</div>
<div class="bsd" style="position:absolute;left:656px;top:350px;font-size:96px;line-height:1;font-weight:500;color:#0E0E0E">PM · SAT</div>
<div class="bod" style="position:absolute;left:660px;right:60px;top:560px;font-size:56px;line-height:1.05;color:#0E0E0E">Who answers when renters <span class="it red">are</span> looking?</div>
<div style="position:absolute;left:660px;right:70px;top:920px;font-size:28px;line-height:1.42;color:var(--soft)">Plenty of apartment searches happen after work and on weekends.</div>
{foot('sdm', False, right='', left=660, rightpx=70)}
""")

# S07 SDM. Same month, different renter. Diptych.
T['s-1107-same-month'] = S(f"""
<div class="photo" style="left:0;top:0;width:540px;height:1350px;{ph('31418279','55% 50%')}"></div>
<div class="photo" style="left:540px;top:0;width:540px;height:1350px;{ph(SEA+'34685145','50% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 62%,rgba(0,0,0,.78) 100%)"></div>
<div style="position:absolute;left:538px;top:0;width:4px;height:1350px;background:#FAFAF8"></div>
<div class="mono" style="position:absolute;left:80px;top:80px;font-size:24px;color:#FAFAF8">Warm and dry · November</div>
<div class="mono" style="position:absolute;left:600px;top:80px;font-size:24px;color:#FAFAF8">Cool and wet · November</div>
<div style="position:absolute;left:150px;right:150px;top:470px;background:#FAFAF8;padding:42px 40px 46px;text-align:center">
 <div class="bod" style="font-size:78px;line-height:1.02;color:#0E0E0E">Same month.<br><span class="it red">Different renter.</span></div>
</div>
<div class="ins it" style="position:absolute;left:80px;top:960px;font-size:56px;color:#FAFAF8">Patio season.</div>
<div class="ins it" style="position:absolute;left:600px;top:960px;font-size:56px;color:#FAFAF8">Rain jacket season.</div>
{foot('sdm', True, right='')}
""", bg='#0E0E0E')

# ============================================================ Sun Nov 8
# G08 LL. Does your website say what your Google profile says?
T['g-1108-say-the-same'] = G(f"""
<div class="photo" style="left:0;top:0;width:500px;height:900px;{ph('7583444','50% 60%')}"></div>
<div class="mono red" style="position:absolute;left:564px;top:64px;font-size:24px">Consistency check</div>
<div class="fra" style="position:absolute;left:564px;right:64px;top:116px;font-size:62px;line-height:1.04;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">Does your website say what your <span class="red">Google profile</span> says?</div>
<div style="position:absolute;left:564px;right:64px;top:420px;display:grid;grid-template-columns:1fr 80px 1fr;align-items:center;border-top:2px solid #0E0E0E;border-bottom:2px solid #0E0E0E;padding:26px 0">
 <div class="news" style="font-size:36px;color:#0E0E0E;font-weight:500">Website</div>
 <div class="bod red" style="font-size:64px;text-align:center;line-height:1">=</div>
 <div class="news" style="font-size:36px;color:#0E0E0E;font-weight:500;text-align:right">Google profile</div>
</div>
<div class="mono" style="position:absolute;left:564px;right:64px;top:570px;font-size:21px;color:#6B665E;line-height:1.6">Hours · Specials · Prices · Pets</div>
{foot('ll', False, right='', left=564, rightpx=64, bottom=56)}
""")

# S08 SDM. Magazine cover manifesto. Fresh Sunday concept.
T['s-1108-playful-curious'] = S(f"""
<div style="position:absolute;left:80px;right:80px;top:66px;display:flex;justify-content:space-between;border-bottom:1.5px solid #0E0E0E;padding-bottom:12px"><span class="mono" style="font-size:22px;color:#0E0E0E">Vol. Sunday</span><span class="mono red" style="font-size:22px">November 2026</span></div>
<div class="ital" style="position:absolute;left:68px;top:96px;font-size:226px;line-height:1;color:#0E0E0E;letter-spacing:-.015em">Curious</div>
<div class="photo" style="left:520px;top:380px;width:480px;height:640px;{ph('36486477','50% 50%')}"></div>
<div style="position:absolute;left:80px;width:410px;top:390px">
 {''.join(f'<div style="border-top:1.5px solid #0E0E0E;padding:16px 0 18px"><div class="mono red" style="font-size:20px">{a}</div><div class="news" style="font-size:31px;line-height:1.15;margin-top:6px;color:#0E0E0E">{b}</div></div>' for a,b in [('Creative','Ideas that earn a second look'),('Search','Being found, then being chosen'),('Local','Writing like you live there')])}
</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:1030px;font-size:52px;line-height:1.06;color:#0E0E0E">The future is going to reward the <span class="it red">playful</span> and <span class="it red">curious.</span></div>
{foot('sdm', False, right='', bottom=60, scale=.9)}
""")

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
