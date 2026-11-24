"""Michael Shad personal Facebook, Dec 6 to 12 2026. Approved SocialDM editorial system (base.py). 1080x1350 at 2x.
Dec 7 and Dec 9 are Field Notes week 3 (approved copy)."""
import sys, asyncio
from base import *

def mf(brand='sdm', dark=False):
    return foot(brand, dark, right='MICHAEL SHAD')
def tag(t='Example', top=72):
    return f'<div style="position:absolute;right:80px;top:{top}px"><span class="ex">{t}</span></div>'

# Sun Dec 6, MF, query fan-out (soft white, one question branching into many searches)
subs = ['pet policy, large dogs', 'one bedroom floor plans', 'drive to the hospital', 'covered parking', 'apartments in the area']
ys = [520, 610, 700, 790, 880]
lines = ''.join(f'<path d="M 420 700 C 520 700, 520 {y}, 600 {y}" stroke="#D2321E" stroke-width="3" fill="none"/>' for y in ys)
T['ms-1206-fan-out'] = S(f"""
<div class="mono red eye">Renter questions</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:78px;right:80px;top:160px;font-size:104px;line-height:1;color:#0E0E0E">One question,<br><span class="it red">many searches.</span></div>
<svg width="1080" height="1350" style="position:absolute;left:0;top:0">{lines}<circle cx="420" cy="700" r="9" fill="#D2321E"/></svg>
<div style="position:absolute;left:80px;width:320px;top:560px;border-top:2px solid #0E0E0E;padding-top:18px">
  <div class="mono" style="font-size:22px;color:#6B665E">Asked once</div>
  <div class="news it" style="font-size:38px;line-height:1.16;color:#0E0E0E;margin-top:12px">“Pet friendly one bedroom near the hospital, with parking?”</div>
</div>
{''.join(f'<div class="mono" style="position:absolute;left:620px;top:{y-16}px;font-size:23px;letter-spacing:.08em;color:#0E0E0E;text-transform:none;font-family:Mono">{s}</div>' for s,y in zip(subs,ys))}
<div style="position:absolute;left:80px;right:80px;top:1000px;font-size:31px;line-height:1.32;color:#3A3631">Google calls it query fan out. Each smaller search may need its own clear answer on your site.</div>
{mf('sdm')}
""")

# Mon Dec 7, Realtors, Field Notes week 3 (black, photo framed like a rear view mirror)
T['ms-1207-this-fall'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">For agents</div>
<div class="photo" style="left:80px;right:80px;top:150px;height:470px;border-radius:235px;{ph('car','0% 0%','165%')}"></div>
<div style="position:absolute;left:80px;right:80px;top:690px">
  <div class="mono" style="font-size:30px;color:#B5B0A6;text-decoration:line-through;text-decoration-color:#D2321E;text-decoration-thickness:4px">Staging tips any agent could post</div>
  <div class="ins" style="font-size:96px;line-height:1;color:#FAFAF8;margin-top:28px">Only you know what buyers <span class="it red">kept asking this fall.</span></div>
</div>
<div style="position:absolute;left:80px;right:80px;top:1000px;font-size:30px;line-height:1.32;color:#CFCAC1">A lot of it never leaves your car.</div>
{mf('ll', True)}
""", bg='#0E0E0E')

# Tue Dec 8, Realtors, answer first (inverted pyramid, newspaper)
tri = [('The answer', 920, '#D2321E', '#FAFAF8'), ('The detail', 700, '#0E0E0E', '#FAFAF8'), ('Your experience', 480, '#E8E4DC', '#0E0E0E')]
T['ms-1208-answer-first'] = S(f"""
<div style="position:absolute;left:80px;right:80px;top:80px;border-bottom:3px double #0E0E0E;padding-bottom:16px;display:flex;justify-content:space-between">
  <span class="mono" style="font-size:22px">For agents</span><span class="mono" style="font-size:22px;color:#6B665E">Writing for AI search</span></div>
<div class="news" style="position:absolute;left:78px;right:80px;top:170px;font-size:110px;line-height:.98;color:#0E0E0E;letter-spacing:-.015em">Don’t bury<br><span class="it red">the answer.</span></div>
<div style="position:absolute;left:80px;right:80px;top:470px;display:flex;flex-direction:column;align-items:center;gap:12px">
  {''.join(f'<div style="width:{w}px;height:132px;background:{bg};display:flex;align-items:center;justify-content:center"><span class="osw" style="font-size:44px;color:{c};letter-spacing:.04em">{t}</span></div>' for t,w,bg,c in tri)}
</div>
<div style="position:absolute;left:80px;right:80px;top:960px;display:grid;grid-template-columns:1fr 1fr;gap:48px;border-top:1.5px solid #0E0E0E;padding-top:24px">
  <div style="font-size:30px;line-height:1.32;color:#3A3631">AI tools tend to lift a single passage from a post.</div>
  <div style="font-size:30px;line-height:1.32;color:#3A3631">Put the direct answer in the first sentence or two.</div>
</div>
{mf('ll')}
""")

# Wed Dec 9, MF, Field Notes week 3 (left photo, right tally sheet)
def tally(n):
    out = ''
    for g in range(n // 5):
        out += '<span style="display:inline-block;position:relative;width:74px;height:56px;margin-right:22px">' + ''.join(f'<span style="position:absolute;left:{i*16}px;top:0;width:5px;height:56px;background:#0E0E0E"></span>' for i in range(4)) + '<span style="position:absolute;left:-8px;top:28px;width:84px;height:5px;background:#D2321E;transform:rotate(-28deg)"></span></span>'
    out += ''.join('<span style="display:inline-block;width:5px;height:56px;background:#0E0E0E;margin-right:11px"></span>' for _ in range(n % 5))
    return out
rows = [('Package delivery', 12), ('Parking', 7), ('Pet rules', 4)]
T['ms-1209-tally'] = S(f"""
<div class="photo" style="left:0;top:0;width:440px;height:1350px;{ph('notes','46% 58%')}"></div>
<div class="mono red" style="position:absolute;left:500px;top:80px;font-size:28px">Leasing teams</div>
<div class="fra" style="position:absolute;left:500px;right:80px;top:150px;font-size:66px;line-height:1.04;color:#0E0E0E;font-weight:400">Your leasing office hears things <span class="it red" style="font-weight:600">no website knows.</span></div>
<div style="position:absolute;left:500px;right:80px;top:560px">
  <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #0E0E0E;padding-bottom:12px"><span class="mono" style="font-size:22px">Tour questions</span><span class="ex">Example</span></div>
  {''.join(f'<div style="border-bottom:1px solid #DAD6CE;padding:18px 0 20px"><div class="news it" style="font-size:36px;color:#0E0E0E;margin-bottom:12px">{t}</div><div>{tally(n)}</div></div>' for t,n in rows)}
</div>
<div style="position:absolute;left:500px;right:80px;top:1098px;font-size:27px;line-height:1.3;color:#3A3631">True, dated and seen by your team.</div>
{foot('sdm', False, right='', left=500)}
<div class="url" style="position:absolute;right:80px;bottom:80px;color:#0E0E0E;font-size:22px">MICHAEL SHAD</div>
""")

# Thu Dec 10, MF, review replies are public writing (soft white, giant red quote mark, reply as pull quote)
T['ms-1210-replies'] = S(f"""
<div class="mono red eye">Online reviews</div>{tag('Example replies')}
<div class="bod red" style="position:absolute;left:62px;top:110px;font-size:420px;line-height:1">“</div>
<div class="bod" style="position:absolute;left:300px;right:80px;top:190px;font-size:100px;line-height:1;color:#0E0E0E">The reply is<br><span class="it red">public too.</span></div>
<div style="position:absolute;left:80px;right:80px;top:500px;display:grid;grid-template-columns:200px 1fr;gap:32px;border-top:1.5px solid #DAD6CE;padding-top:24px">
  <div class="mono" style="font-size:22px;color:#6B665E;line-height:1.5">Says nothing</div>
  <div class="news it" style="font-size:38px;line-height:1.2;color:#8A857C">“Thank you for your feedback! We take all concerns seriously.”</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:700px;display:grid;grid-template-columns:200px 1fr;gap:32px;border-top:3px solid #D2321E;padding-top:24px">
  <div class="mono red" style="font-size:22px;line-height:1.5">Adds a fact</div>
  <div class="news it" style="font-size:44px;line-height:1.2;color:#0E0E0E">“Thanks for flagging this. The north gate was repaired in October, and maintenance requests can be submitted 24/7 in the resident app.”</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:1060px;font-size:30px;line-height:1.3;color:#3A3631">Renters read replies. Some AI tools may too.</div>
{mf('sdm')}
""")

# Fri Dec 11, Realtors, service areas (type top, map photo fading in at the bottom)
T['ms-1211-service-area'] = S(f"""
<div class="photo" style="left:0;right:0;bottom:0;height:820px;{ph('pin','40% 60%')}"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(180deg,#FAFAF8 0%,rgba(250,250,248,0) 34%,rgba(250,250,248,0) 52%,rgba(250,250,248,.94) 82%,#FAFAF8 100%)"></div>
<div class="mono red eye">For agents</div>
<div class="arch" style="position:absolute;left:78px;right:80px;top:150px;font-size:118px;line-height:.94;font-weight:700;color:#0E0E0E;text-transform:uppercase;letter-spacing:-.01em">Where do you<br><span style="color:#D2321E">actually sell?</span></div>
<div style="position:absolute;left:80px;width:700px;top:420px;font-size:30px;line-height:1.32;color:#3A3631">Your Google profile’s service areas answer that for you. Make sure they match where you work.</div>
{mf('ll')}
""")

# Sat Dec 12, MF, Google isn't the only map (dark board, listing status rows)
maps = [('Google Maps', 'Claimed', '#FAFAF8'), ('Apple Maps', 'Not checked', '#D2321E'), ('Your car’s map', 'Not checked', '#D2321E')]
T['ms-1212-other-maps'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">Map listings</div>{tag('Illustrative')}
<div class="fra" style="position:absolute;left:78px;right:80px;top:160px;font-size:100px;line-height:1;color:#FAFAF8;font-weight:300">Google isn’t<br><span class="it red" style="font-weight:600">the only map.</span></div>
<div style="position:absolute;left:80px;right:80px;top:500px">
  <div style="display:flex;justify-content:space-between;padding-bottom:14px;border-bottom:2px solid #FAFAF8"><span class="mono" style="font-size:27px;color:#E8E4DC">Where renters look</span><span class="mono" style="font-size:27px;color:#E8E4DC">Listing</span></div>
  {''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:30px 0;border-bottom:1px solid rgba(250,250,248,.25)"><span class="arch" style="font-size:58px;font-weight:500;color:#FAFAF8">{m}</span><span class="mono" style="font-size:26px;color:{c}">{s}</span></div>' for m,s,c in maps)}
</div>
<div style="position:absolute;left:80px;right:80px;top:1000px;font-size:30px;line-height:1.32;color:#CFCAC1">Each map can carry its own hours, phone number and pin.</div>
{mf('sdm', True)}
""", bg='#141414')

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
