from base import *

SEA = 'sea-pexels-josh-hild-1270765-'

# ============================================================ Mon Nov 9 (specials)
rows = [('Website','6 weeks free',True),('Google profile','6 weeks free',True),('Listing site','2 weeks free',False),('Instagram bio','6 weeks free',True)]
T['g-1109-one-special'] = G(f"""
<div style="position:absolute;left:0;top:0;width:1200px;height:12px;background:var(--red)"></div>
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Specials</div><div style="position:absolute;right:64px;top:58px"><span class="ex">Example</span></div>
<div class="bod" style="position:absolute;left:64px;width:520px;top:116px;font-size:72px;line-height:1.02;color:#0E0E0E">One special. <span class="it red">The same everywhere.</span></div>
<div style="position:absolute;left:640px;right:64px;top:250px">
 <div style="display:flex;justify-content:space-between;padding-bottom:12px"><span class="mono" style="font-size:19px;color:#6B665E">Where</span><span class="mono" style="font-size:19px;color:#6B665E">What it says</span></div>
 {''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:20px 0;{"background:#F6E3DF;padding:20px 12px" if not ok else ""}"><span class="arch" style="font-size:34px;font-weight:500;color:#0E0E0E">{w}</span><span class="arch" style="font-size:34px;font-weight:700;color:{"#0E0E0E" if ok else "#D2321E"}">{s}{"" if ok else " ✕"}</span></div>' for w,s,ok in rows)}
 <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
<div class="news it" style="position:absolute;left:64px;width:520px;top:470px;font-size:34px;line-height:1.25;color:#3A3631">One out of date line is enough to make a renter wonder which one is true.</div>
{foot('ll', False, right='', left=64, rightpx=64, bottom=56)}
""")

lu = ['Get found by people who have never heard of you','Show progress as homes open','Say what is open, and when']
st = ['Keep review replies current','Show resident life over finishes','Keep every listing accurate']
T['li-1109-two-jobs'] = S(f"""
<div style="position:absolute;left:0;top:0;width:540px;height:1350px;background:#0E0E0E"></div>
<div style="position:absolute;left:0;top:0;width:1080px;height:430px;background:#FAFAF8;border-bottom:2px solid #0E0E0E"></div>
<div class="mono red" style="position:absolute;left:80px;top:80px;font-size:26px">Multifamily marketing</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:80px;line-height:1.02;color:#0E0E0E">Lease up and stabilized are <span class="red">different jobs.</span></div>
<div class="anton" style="position:absolute;left:80px;top:500px;font-size:84px;line-height:1;color:#FAFAF8">Lease up</div>
<div class="anton" style="position:absolute;left:620px;top:500px;font-size:84px;line-height:1;color:#0E0E0E">Stabilized</div>
<div style="position:absolute;left:80px;width:400px;top:640px">{''.join(f'<div style="border-top:1px solid var(--dline);padding:20px 0;font-size:30px;line-height:1.3;color:#FAFAF8">{t}</div>' for t in lu)}</div>
<div style="position:absolute;left:620px;width:380px;top:640px">{''.join(f'<div style="border-top:1.5px solid #0E0E0E;padding:20px 0;font-size:30px;line-height:1.3;color:#0E0E0E">{t}</div>' for t in st)}</div>
<div class="ins it red" style="position:absolute;left:620px;top:1100px;font-size:40px">Same feed. New brief.</div>
<div class="foot" style="left:80px;right:620px;bottom:80px"><img src="{LG}socialdm-reversed.png" style="height:112px;display:block"></div>
""")

T['s-1109-special-nobody'] = S(f"""
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#D2321E 0%,#D2321E 60%,#4A0E08 84%,#160403 100%)"></div>
<div class="mono eye" style="color:#FAFAF8;font-size:30px">Specials</div>
<div class="anton" style="position:absolute;left:72px;right:72px;top:190px;font-size:150px;line-height:.93;color:#FAFAF8">A special nobody can find</div>
<div class="bod it" style="position:absolute;left:80px;top:830px;font-size:110px;line-height:1;color:#0E0E0E">isn’t a special.</div>
<div class="mono" style="position:absolute;left:80px;top:1004px;font-size:30px;color:#FAFAF8">Same offer · every place renters look</div>
{foot('ll', True, right='', scale=1.15)}
""", bg='#D2321E')

# ============================================================ Tue Nov 10 (metrics)
lad = [('Tours',100),('Calls',84),('Direction requests',70),('Website clicks',56),('Profile views',38),('Impressions',22)]
T['g-1110-value-ladder'] = G(f"""
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Reporting</div><div style="position:absolute;right:64px;top:56px"><span class="ex">Illustrative</span></div>
<div class="fra" style="position:absolute;left:64px;width:470px;top:116px;font-size:76px;line-height:1;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">Not all numbers are <span class="it red" style="font-weight:400">equal.</span></div>
<div class="news it" style="position:absolute;left:64px;width:440px;top:470px;font-size:30px;line-height:1.3;color:#CFCAC1">How much each one tells a property team. Our view, not a formula.</div>
<div style="position:absolute;left:580px;right:64px;top:130px">
 <div style="display:flex;justify-content:space-between;margin-bottom:14px"><span class="mono" style="font-size:22px;color:#CFCAC1">Tells you more</span><span class="mono" style="font-size:22px;color:#CFCAC1">↓ less</span></div>
 {''.join(f'<div style="margin-bottom:16px"><div class="arch" style="font-size:28px;font-weight:500;color:#FAFAF8;margin-bottom:8px">{n}</div><div style="height:22px;width:{w}%;background:{"#D2321E" if i<3 else "#5A5650"}"></div></div>' for i,(n,w) in enumerate(lad))}
</div>
{foot('sdm', True, right='', left=64, rightpx=64, bottom=48, scale=.82)}
""", bg='#0E0E0E')

BK = [('Impressions','What did people do next?'),('Follower count','Who here could actually rent from you?'),('Engagement rate','What were people responding to?'),('Reach','What is the next step?')]
T['li-1110-back-1'] = S(f"""
<div class="mono red eye">The report</div>
<div class="anton" style="position:absolute;left:66px;top:150px;font-size:300px;line-height:.86;color:transparent;-webkit-text-stroke:3px #0E0E0E">Back</div>
<div class="anton" style="position:absolute;left:66px;top:410px;font-size:300px;line-height:.86;color:#0E0E0E">page.</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:740px;font-size:72px;line-height:1.04;color:#0E0E0E">Four numbers to move to the <span class="it red">back</span> of the report.</div>
<div class="mono" style="position:absolute;left:80px;top:1040px;font-size:26px;color:#0E0E0E">Not deleted. Just moved.</div><div class="mono red" style="position:absolute;right:80px;top:1040px;font-size:26px">Swipe</div>
{foot('sdm', False, right='')}
""")
for i,(m,a) in enumerate(BK):
    dark = i % 2 == 0
    fg = '#FAFAF8' if dark else '#0E0E0E'; bg = '#0E0E0E' if dark else '#FAFAF8'
    T[f'li-1110-back-{i+2}'] = S(f"""
<div class="mono red eye">Move to the back · 0{i+1}</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:420px;font-size:{120 if len(m)<12 else 104}px;line-height:1;color:{fg};text-decoration:line-through;text-decoration-color:#D2321E;text-decoration-thickness:7px">{m}</div>
<div class="mono" style="position:absolute;left:80px;top:760px;font-size:26px;color:{'#CFCAC1' if dark else '#6B665E'}">Ask instead</div>
<div class="fra it" style="position:absolute;left:80px;right:120px;top:820px;font-size:76px;line-height:1.04;font-weight:400;color:{fg}">{a}</div>
{foot('sdm', dark, right='')}
""", bg=bg)
T['li-1110-back-6'] = S(f"""
<div class="mono red eye">Lead with</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:150px;font-size:88px;line-height:1;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">What goes on the <span class="red" style="font-weight:400">front</span> page.</div>
<div style="position:absolute;left:80px;right:80px;top:520px">
""" + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--dline);padding:24px 0"><span style="font-size:38px;color:#FAFAF8">{t}</span><span class="mono red" style="font-size:24px">0{k+1}</span></div>' for k,t in enumerate(['Tours','Calls','Direction requests','The one thing to fix this week'])) + f"""
<div style="border-top:1px solid var(--dline)"></div></div>
{foot('sdm', True)}
""", bg='#0E0E0E')

vb = [('Likes','Tours'),('Followers','Calls'),('Views','Leases')]
T['s-1110-likes-leases'] = S(f"""
<div class="mono red eye">Scoreboard</div><div class="eyeR"><span class="ex">Illustrative</span></div>
<div class="anton" style="position:absolute;left:76px;right:76px;top:150px;font-size:136px;line-height:.92;color:#FAFAF8">Likes don’t sign leases.</div>
<div style="position:absolute;left:80px;right:80px;top:520px;display:grid;grid-template-columns:1fr 1fr;gap:14px">
 <div class="mono" style="font-size:24px;color:#8E887F;padding:0 0 6px">Feels good</div><div class="mono red" style="font-size:24px;padding:0 0 6px">Pays rent</div>
 {''.join(f'<div class="bsd" style="background:#1C1B1A;border:1px solid #2E2C2A;color:#8E887F;font-size:76px;font-weight:800;text-transform:uppercase;padding:22px 26px;line-height:1">{a}</div><div class="bsd" style="background:#1C1B1A;border:1px solid #D2321E;color:#FAFAF8;font-size:76px;font-weight:800;text-transform:uppercase;padding:22px 26px;line-height:1">{b}</div>' for a,b in vb)}
</div>
<div class="news it" style="position:absolute;left:80px;right:80px;top:1060px;font-size:36px;color:#CFCAC1">Renters do.</div>
<div style="position:absolute;left:0;right:0;bottom:80px;display:flex;justify-content:center"><img src="{LG}socialdm-reversed.png" style="height:112px"></div>
""", bg='#0E0E0E')

# ============================================================ Wed Nov 11 (discoverability)
def phone(x, n, title, img, hi):
    r = ''.join(f'<div style="height:{12 if k!=hi else 26}px;margin:12px 0;background:{"#D2321E" if k==hi else "#3A3836"};width:{[90,70,82,60][k%4]}%;border-radius:3px"></div>' for k in range(4))
    return f'''<div style="position:absolute;left:{x}px;top:236px;width:300px;height:470px;border:10px solid #2A2826;border-radius:44px;background:#181716;overflow:hidden">
<div class="photo" style="left:0;top:0;width:280px;height:230px;{ph(img)}"></div>
<div style="position:absolute;left:22px;right:22px;top:248px"><div class="mono" style="font-size:20px;color:#FAFAF8;letter-spacing:.12em">{title}</div>{r}</div></div>
<div class="bsd red" style="position:absolute;left:{x}px;top:730px;font-size:44px;font-weight:800">Tap {n}</div>'''
T['g-1111-three-taps'] = G(f"""
<div class="mono red" style="position:absolute;left:64px;top:56px;font-size:24px">Discoverability</div><div style="position:absolute;right:64px;top:782px"><span class="ex">Example</span></div>
<div class="fra" style="position:absolute;left:64px;right:280px;top:106px;font-size:56px;line-height:1.05;font-weight:400;color:#FAFAF8;letter-spacing:-.015em">Can a renter find your floor plans in <span class="it red">three taps?</span></div>
{phone(64,1,'Google profile','34135423',2)}{phone(450,2,'Your website','6908500',1)}{phone(836,3,'Floor plans','12187764',0)}
<svg style="position:absolute;left:0;top:0" width="1200" height="900"><path d="M372 496 L440 496 M428 486 L442 496 L428 506 M758 496 L826 496 M814 486 L828 496 L814 506" stroke="#FAFAF8" stroke-width="3" fill="none"/></svg>
<div style="position:absolute;right:64px;top:62px"><img src="{LG}locallift-white.png" style="height:44px;display:block"></div>
""", bg='#0E0E0E')

T['s-1111-found-fancy'] = S(f"""
<div class="photo" style="inset:0;{ph('26902734','50% 40%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.35) 0%,rgba(10,10,10,0) 25%,rgba(10,10,10,0) 45%,rgba(10,10,10,.9) 80%)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,10,.78) 0%,rgba(10,10,10,.55) 50%,rgba(10,10,10,0) 85%)"></div>
<div class="mono eye" style="color:#FAFAF8">Discoverability</div>
<div class="fra" style="position:absolute;left:76px;right:80px;top:770px;font-size:150px;line-height:.92;font-weight:300;color:#FAFAF8;letter-spacing:-.035em">Found beats <span class="it red" style="font-weight:400">fancy.</span></div>
<div style="position:absolute;left:80px;width:600px;top:1100px;font-size:28px;line-height:1.4;color:#E6E1D8">A beautiful page still has to be found.</div>
{foot('ll', True, right='', left=760)}
""", bg='#0A0A0A')

# ============================================================ Thu Nov 12 (creative)
rules = ['Real light','Real space, shown honestly','A season that matches today','Nothing that isn’t there']
T['g-1112-photo-work'] = G(f"""
<div class="photo" style="left:0;top:0;width:560px;height:900px;{ph('6908360','50% 50%')}"></div>
<div class="mono red" style="position:absolute;left:624px;top:64px;font-size:24px">Creative</div>
<div class="fra" style="position:absolute;left:624px;right:64px;top:112px;font-size:62px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">What makes a listing photo <span class="red">work.</span></div>
<div style="position:absolute;left:624px;right:64px;top:380px">
 {''.join(f'<div style="display:flex;gap:22px;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:17px 0"><span class="bsd red" style="font-size:34px;font-weight:800;width:22px;flex:none">{i+1}</span><span class="news" style="font-size:33px;line-height:1.15;color:#0E0E0E">{r}</span></div>' for i,r in enumerate(rules))}
 <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
{foot('sdm', False, right='', left=624, rightpx=64, bottom=48, scale=.78)}
""")

T['li-1112-better-crop'] = S(f"""
<div class="mono red eye">Creative, up close</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:92px;line-height:1;color:#0E0E0E">Same photo. <span class="red">Better crop.</span></div>
<div class="photo" style="left:80px;top:420px;width:445px;height:556px;{ph('7031880','0% 50%')}"></div>
<div class="photo" style="left:555px;top:420px;width:445px;height:556px;{ph('7031880','70% 62%','auto 150%')}"></div>
<div class="mono" style="position:absolute;left:80px;top:996px;font-size:24px;color:#6B665E">Before · as shot</div>
<div class="mono red" style="position:absolute;left:555px;top:996px;font-size:24px">After · cropped for 4:5</div>
{foot('sdm', False, right='')}
""")

grid = ['33022919','24838641','2497637','4876018','5473880','35123428','12187764','16058436','29696169']
cells = ''.join(f'<div class="photo" style="left:{16+(k%3)*328}px;top:{16+(k//3)*328}px;width:312px;height:312px;{ph(g)};{"" if k==4 else "filter:blur(9px) grayscale(.85) brightness(.55)"}"></div>' for k,g in enumerate(grid))
T['s-1112-thumb'] = S(f"""
<div style="position:absolute;left:44px;top:64px;width:992px;height:1000px;overflow:hidden">{cells}</div>
<div style="position:absolute;left:44px;top:64px;width:992px;height:1000px;background:linear-gradient(180deg,rgba(10,10,10,0) 60%,#0A0A0A 100%)"></div>
<div class="syne" style="position:absolute;left:80px;right:80px;top:830px;font-size:66px;line-height:1.02;font-weight:800;color:#FAFAF8;letter-spacing:-.03em">A thumb moves fast. Give it a reason to <span style="color:#D2321E">stop.</span></div>
{foot('sdm', True, right='', bottom=64)}
""", bg='#0A0A0A')

# ============================================================ Fri Nov 13 (renter questions)
qs = ['Is parking included?','What’s the pet policy?','When can I move in?']
T['g-1113-before-they-ask'] = G(f"""
<div class="photo" style="right:0;top:0;width:520px;height:900px;{ph('5332214','50% 35%')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Renter questions</div>
<div class="bod" style="position:absolute;left:64px;width:560px;top:112px;font-size:64px;line-height:1.04;color:#FAFAF8">Answer the question <span class="it red">before</span> they ask.</div>
<div style="position:absolute;left:64px;width:560px;top:400px">
 {''.join(f'<div style="display:flex;gap:20px;align-items:baseline;border-top:1px solid var(--dline);padding:16px 0"><span class="mono red" style="font-size:22px">Q{i+1}</span><span class="ins it" style="font-size:44px;line-height:1.05;color:#FAFAF8">{q}</span></div>' for i,q in enumerate(qs))}
 <div style="border-top:1px solid var(--dline)"></div>
</div>
<div style="position:absolute;left:64px;bottom:52px"><img src="{LG}locallift-white.png" style="height:52px;display:block"></div>
""", bg='#0E0E0E')

q5 = [('Is parking included?','Amenities'),('What’s the pet policy?','FAQ'),('What will I pay each month, all in?','Floor plans'),('How long is the commute?','Neighborhood'),('Can I tour tonight or this weekend?','Tour booking')]
T['s-1113-five-questions'] = S(f"""
<div style="position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;border-bottom:1.5px solid #0E0E0E;padding-bottom:14px"><span class="mono" style="font-size:24px;color:#0E0E0E">Site map</span><span class="mono red" style="font-size:24px">Before the tour</span></div>
<div class="news" style="position:absolute;left:80px;right:80px;top:150px;font-size:76px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">Five questions. <span class="red">Where does each answer live?</span></div>
<div style="position:absolute;left:80px;right:80px;top:420px;display:flex;justify-content:space-between;padding-bottom:10px"><span class="mono" style="font-size:20px;color:#6B665E">The question</span><span class="mono" style="font-size:20px;color:#6B665E">Page it belongs on</span></div>
<div style="position:absolute;left:80px;right:80px;top:460px">
 {''.join(f'<div style="display:flex;align-items:baseline;gap:22px;padding:20px 0;border-top:1.5px solid #0E0E0E"><span class="bod red" style="font-size:56px;line-height:.9;width:44px">{i+1}</span><span class="news" style="font-size:34px;line-height:1.2;color:#0E0E0E;flex:1">{q}</span><span class="mono" style="font-size:26px;color:#FAFAF8;background:#0E0E0E;padding:8px 12px;white-space:nowrap">{p}</span></div>' for i,(q,p) in enumerate(q5))}
 <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
<div class="news it" style="position:absolute;left:80px;right:80px;top:1080px;font-size:32px;color:#6B665E">If an answer lives nowhere, renters go looking somewhere else.</div>
{foot('ll', False, right='')}
""")

# ============================================================ Sat Nov 14 (local)
T['g-1114-neighborhood-home'] = G(f"""
<div class="photo" style="inset:0;{ph('34580768','20% 70%','160% auto')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,10,.82) 0%,rgba(10,10,10,.6) 45%,rgba(10,10,10,0) 75%)"></div>
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Local</div>
<div class="bod" style="position:absolute;left:64px;width:620px;top:120px;font-size:76px;line-height:1.02;color:#FAFAF8">The neighborhood is part of the home.</div>
{foot('sdm', True, right='', left=64, rightpx=64, bottom=52, scale=.85)}
""", bg='#0E0E0E')

T['li-1114-local-beats'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:760px;{ph('33327057','18% 62%','190% auto')}"></div>
<div style="position:absolute;left:0;top:560px;width:1080px;height:200px;background:linear-gradient(180deg,rgba(14,14,14,0),#0E0E0E)"></div>
<div class="mono eye" style="color:#FAFAF8">Local search</div>
<div class="anton" style="position:absolute;left:72px;top:790px;font-size:200px;line-height:.86;color:#FAFAF8">Local</div>
<div class="bod it red" style="position:absolute;left:80px;top:978px;font-size:92px;line-height:1">beats generic.</div>
{foot('sdm', True, right='')}
""", bg='#0E0E0E')

tags = [('Coffee','3 min walk',640,470),('Farmers market','Saturdays',640,600),('Dog park','6 min walk',640,730)]
T['s-1114-errands'] = S(f"""
<div class="photo" style="inset:0;{ph('6264038','85% 70%','140% auto')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(250,250,248,1) 0%,rgba(250,250,248,.96) 26%,rgba(250,250,248,0) 38%)"></div>
<div class="mono red eye">Saturday</div><div class="eyeR"><span class="ex">Example</span></div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:80px;line-height:1.02;color:#0E0E0E">Saturday errands are a <span class="it red">neighborhood tour.</span></div>
{''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;background:#0E0E0E;padding:14px 18px 16px"><div class="news" style="font-size:32px;color:#FAFAF8;line-height:1">{a}</div><div class="mono red" style="font-size:19px;margin-top:8px">{b}</div></div>' for a,b,x,y in tags)}
<div style="position:absolute;left:0;bottom:0;width:1080px;height:300px;background:linear-gradient(180deg,rgba(10,10,10,0),rgba(10,10,10,.75))"></div>
<div style="position:absolute;right:80px;bottom:80px"><img src="{LG}socialdm-reversed.png" style="height:112px;display:block"></div>
""", bg='#0E0E0E')

# ============================================================ Sun Nov 15 (weekly reporting)
rep = [('What changed','A nearby community added a special'),('Listing check','Hours and photos match the website'),('Reviews','Three new, all answered'),('One next step','Refresh the pet policy on the FAQ')]
T['g-1115-one-page'] = G(f"""
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Weekly reporting</div>
<div class="fra" style="position:absolute;left:64px;width:440px;top:112px;font-size:66px;line-height:1.02;font-weight:300;color:#0E0E0E;letter-spacing:-.02em">What changed this week, <span class="red" style="font-weight:400">on one page.</span></div>
<div style="position:absolute;left:560px;right:64px;top:110px;background:#FFFFFF;box-shadow:0 20px 60px rgba(0,0,0,.14);padding:36px 40px">
 <div style="display:flex;justify-content:space-between;align-items:center"><span class="mono" style="font-size:19px;color:#6B665E">This week</span><span class="ex">Illustrative sample</span></div>
 {''.join(f'<div style="border-top:1.5px solid #0E0E0E;padding:16px 0;margin-top:{18 if k==0 else 0}px"><div class="mono {"red" if k==3 else ""}" style="font-size:17px;color:{"#D2321E" if k==3 else "#6B665E"}">{a}</div><div class="news" style="font-size:30px;line-height:1.2;margin-top:6px;color:#0E0E0E;{"font-weight:600" if k==3 else ""}">{b}</div></div>' for k,(a,b) in enumerate(rep))}
</div>
<div class="news it" style="position:absolute;left:64px;width:440px;top:420px;font-size:30px;line-height:1.3;color:#6B665E">A sample layout, not a real client report.</div>
{foot('ll', False, right='', left=64, rightpx=700, bottom=64)}
""", bg='#F1EEE8')

T['s-1115-monday'] = S(f"""
<div class="photo" style="inset:0;{ph('28584802','50% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(250,250,248,.0) 40%,rgba(250,250,248,.0) 100%)"></div>
<div class="mono eye" style="color:#0E0E0E">Monday, 8 AM</div><div class="eyeR"><span class="ex">Illustrative</span></div>
<div class="ital" style="position:absolute;left:72px;top:140px;font-size:150px;line-height:.95;color:#0E0E0E;word-spacing:-.18em">Your Monday,</div>
<div class="bod it red" style="position:absolute;left:80px;top:300px;font-size:100px;line-height:1">previewed.</div>
<div style="position:absolute;left:80px;width:700px;top:560px;background:#0E0E0E;padding:36px 44px">
 {''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:14px 0;{"border-top:1px solid rgba(255,255,255,.22)" if k else ""}"><span class="bsd" style="font-size:112px;font-weight:900;line-height:.85;color:{"#D2321E" if k==1 else "#FAFAF8"};width:70px">{n}</span><span class="news" style="font-size:50px;line-height:1.05;color:#FAFAF8">{t}</span></div>' for k,(n,t) in enumerate([('1','change'),('1','fix'),('0','surprises')]))}
 <div class="mono" style="font-size:28px;color:#FAFAF8;border-top:1px solid rgba(255,255,255,.22);padding-top:18px;margin-top:8px;letter-spacing:.12em">Illustrative sample</div>
</div>

<div style="position:absolute;left:0;bottom:0;width:1080px;height:300px;background:linear-gradient(180deg,rgba(10,10,10,0),rgba(10,10,10,.7))"></div>
{foot('sdm', True, right='')}
""")

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
