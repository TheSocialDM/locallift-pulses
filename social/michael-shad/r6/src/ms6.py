"""Michael Shad personal Facebook, Nov 15 to 21 2026. Approved SocialDM editorial system (base.py). 1080x1350 at 2x."""
import sys, asyncio
from base import *

def mf(brand='sdm', dark=False):
    return foot(brand, dark, right='MICHAEL SHAD')
def tag(t='Illustrative'):
    return f'<div style="position:absolute;right:80px;top:72px"><span class="ex">{t}</span></div>'

# Sun Nov 15, Realtors, whose name comes back (redacted list over black and white aerial)
bars = [560, 430, 640]
T['ms-1115-names'] = S(f"""
<div class="photo" style="inset:0;{ph('aerial','50% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,6,6,.94) 0%,rgba(6,6,6,.9) 44%,rgba(6,6,6,.62) 55%,rgba(6,6,6,.62) 72%,rgba(6,6,6,.92) 84%,#060606 100%)"></div>
<div class="mono eye" style="color:#FAFAF8">For agents</div>{tag()}
<div class="bod" style="position:absolute;left:80px;right:70px;top:150px;font-size:106px;line-height:1;color:#FAFAF8">Someone asked Google’s AI for an agent. <span class="it" style="color:#D2321E">Whose name came back?</span></div>
<div style="position:absolute;left:80px;right:80px;top:740px">
  <div class="mono" style="font-size:23px;color:#FAFAF8;margin-bottom:20px">Names in the answer</div>
  {''.join(f'<div style="height:58px;width:{w}px;background:#FAFAF8;margin-bottom:16px"></div>' for w in bars)}
  <div class="ins it" style="font-size:66px;line-height:1.1;color:#FAFAF8;margin-top:18px;text-shadow:0 2px 14px rgba(0,0,0,.7)">Is yours one of them?</div>
</div>
{mf('ll', True)}
""", bg='#060606')

# Mon Nov 16, MF, the real monthly cost (receipt bleeding off the top)
lines = [('Base rent','$1,650'),('Parking','$50'),('Pet rent','$35'),('Trash and valet','$28'),('Amenity fee','$25')]
T['ms-1116-real-cost'] = S(f"""
<div class="mono red eye">Fees</div>
<div class="anton" style="position:absolute;left:80px;width:440px;top:150px;font-size:120px;line-height:.98;color:#FAFAF8">What will I <span style="color:#D2321E">actually</span> pay?</div>
<div style="position:absolute;left:80px;width:400px;top:730px;font-size:34px;line-height:1.32;color:#FAFAF8">Many renters ask AI this.<br>It tends to repeat<br>what it finds.</div>
<div style="position:absolute;left:550px;right:80px;top:0;height:1090px;background:#FAFAF8;clip-path:polygon(0 0,100% 0,100% 1066px,95% 1090px,90% 1066px,85% 1090px,80% 1066px,75% 1090px,70% 1066px,65% 1090px,60% 1066px,55% 1090px,50% 1066px,45% 1090px,40% 1066px,35% 1090px,30% 1066px,25% 1090px,20% 1066px,15% 1090px,10% 1066px,5% 1090px,0 1066px)">
  <div style="padding:90px 32px 0">
    <span class="ex">Example</span>
    <div class="mono" style="font-size:24px;color:#0E0E0E;margin-top:34px;letter-spacing:.12em">Monthly total</div>
    <div style="border-top:2px dashed #0E0E0E;margin-top:18px"></div>
    {''.join(f'<div style="display:flex;justify-content:space-between;padding:33px 0;font-family:Mono,monospace;font-size:27px;color:#0E0E0E"><span>{a}</span><span>{b}</span></div>' for a,b in lines)}
    <div style="border-top:2px dashed #0E0E0E"></div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:24px"><span class="mono red" style="font-size:26px;letter-spacing:.12em">Total</span><span class="fra red" style="font-size:78px;font-weight:600">$1,788</span></div>
    <div style="font-family:Mono,monospace;font-size:23px;line-height:1.35;color:#3A3631;margin-top:26px">Example only, not a real community or price.</div>
  </div>
</div>
{mf('sdm', True)}
""", bg='#0E0E0E')

# Tue Nov 17, Realtors, sellers ask first (circle crop, Instrument Serif)
qs = ['What should I fix<br>before I sell?','How long are homes<br>near me taking<br>to sell?','Who sells homes<br>like mine?']
T['ms-1117-sellers'] = S(f"""
<div style="position:absolute;left:440px;top:-130px;width:820px;height:820px;border-radius:50%;overflow:hidden"><div class="photo" style="inset:0;{ph('couple','50% 50%')};background-size:1420px auto;background-position:-330px -40px;filter:grayscale(1) contrast(1.08)"></div></div>
<div class="mono red eye">Listing agents</div>
<div style="position:absolute;left:80px;width:350px;top:170px">
  {''.join(f'<div class="news it" style="font-size:38px;line-height:1.16;color:#0E0E0E;border-top:1.5px solid #0E0E0E;padding:16px 0 20px">{q}</div>' for q in qs)}
</div>
<div class="ins" style="position:absolute;left:78px;right:60px;top:745px;font-size:133px;line-height:1;color:#0E0E0E">Some sellers ask AI <span class="it red">before they call you.</span></div>
{mf('ll')}
""")

# Wed Nov 18, MF, new community (letterbox photo, horizontal timeline)
steps = [('Before opening','A real page with the exact name, address and timeline.'),('Preleasing','Floor plans, pets, parking, worded alike.'),('First move ins','Google profile once eligible, reviews and local mentions.')]
T['ms-1118-new-community'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">New communities</div>
<div class="syne" style="position:absolute;left:80px;right:60px;top:150px;font-size:68px;line-height:1.2;font-weight:800;color:#FAFAF8;letter-spacing:-.02em">AI may not know<br>you <span class="bod it" style="color:#D2321E;font-weight:700;font-size:84px;line-height:1;letter-spacing:-.01em">exist yet.</span></div>
<div class="photo" style="left:0;right:0;top:360px;height:460px;{ph('crane','50% 43%')}"></div>
<div style="position:absolute;left:80px;right:80px;top:868px;height:3px;background:var(--red)"></div>
<div style="position:absolute;left:80px;right:80px;top:858px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:34px">
  {''.join(f'<div><div style="width:23px;height:23px;border-radius:50%;background:var(--red)"></div><div class="mono" style="font-size:23px;letter-spacing:.1em;margin-top:18px;color:#FAFAF8">{a}</div><div style="font-size:29px;line-height:1.26;color:#FAFAF8;margin-top:12px">{b}</div></div>' for a,b in steps)}
</div>
{mf('sdm', True)}
""", bg='#0E0E0E')

# Thu Nov 19, Realtors, brokerage move (memo)
rows = [('To','The internet'),('From','You'),('Re','I moved brokerages')]
chk = ['Old brokerage roster','Portal profiles','Google profile','Association directory','License record','Old team pages']
T['ms-1119-brokerage-move'] = S(f"""
<div class="anton" style="position:absolute;left:72px;top:50px;font-size:310px;line-height:1.12;color:#0E0E0E">Memo</div>
<div style="position:absolute;right:80px;top:80px;text-align:right" class="mono red"><span style="font-size:26px">For agents</span></div>
<div style="position:absolute;left:80px;right:80px;top:405px">
  {''.join(f'<div style="display:flex;border-top:1.5px solid #0E0E0E;padding:12px 0;font-family:Mono,monospace;font-size:30px;color:#0E0E0E"><span class="red" style="width:150px">{a}</span><span>{b}</span></div>' for a,b in rows)}
  <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
<div class="bod" style="position:absolute;left:80px;right:60px;top:625px;font-size:82px;line-height:1.03;color:#0E0E0E">You changed brokerages. <span class="it red">Did the internet get the memo?</span></div>
<div style="position:absolute;left:80px;right:80px;top:930px;display:grid;grid-template-columns:1fr 1fr;gap:18px 40px">
  {''.join(f'<div style="display:flex;align-items:center;gap:18px;font-size:32px;color:#0E0E0E"><span style="flex:none;width:30px;height:30px;border:2.5px solid var(--red)"></span>{c}</div>' for c in chk)}
</div>
{mf('ll')}
""")

# Fri Nov 20, MF, AI got it wrong (black over white, proof mark, 2x2 grid)
grid = [('1','Find the source','Click every link it cites.'),('2','Fix it where it lives','Update it or ask the owner to.'),('3','Say it on your site','One clear, readable sentence.'),('4','Test again','Changes can take weeks.')]
T['ms-1120-wrong-answer'] = S(f"""
<div style="position:absolute;left:0;right:0;top:0;height:650px;background:#0E0E0E"></div>
<div class="mono eye" style="color:#FAFAF8">Corrections</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:60px;top:150px;font-size:112px;line-height:1;color:#FAFAF8">AI got it wrong. <span class="it" style="color:#D2321E;font-weight:700">Now what?</span></div>
<div class="news it" style="position:absolute;left:80px;right:80px;top:425px;font-size:50px;line-height:1.3;color:#FAFAF8">“This community does <span style="position:relative;display:inline-block;color:#CFCAC1">not<span style="position:absolute;left:-6px;right:-6px;top:54%;height:5px;background:#D2321E"></span></span> allow dogs.”</div>
<div class="mono" style="position:absolute;left:80px;top:520px;font-size:23px;color:#CFCAC1">Made up answer, for illustration only</div>
<div style="position:absolute;left:80px;right:80px;top:680px;display:grid;grid-template-columns:1fr 1fr;gap:58px 44px">
  {''.join(f'<div style="border-top:2px solid #0E0E0E;padding-top:14px"><div style="display:flex;gap:16px;align-items:baseline"><span class="osw red" style="font-size:54px;line-height:1">{n}</span><span class="fra" style="font-size:42px;line-height:1.06;font-weight:500;color:#0E0E0E">{t}</span></div><div style="font-size:30px;line-height:1.28;color:var(--soft);margin-top:14px">{d}</div></div>' for n,t,d in grid)}
</div>
{mf('sdm')}
""")

# Sat Nov 21, Realtors, relocation (type over, photo bleeding off the bottom with footer on it)
q21 = ['How long is the commute from there?','What does my budget buy in that area?','How far is the airport?']
T['ms-1121-relocation'] = S(f"""
<div class="mono red eye">For agents</div>
<div class="fra" style="position:absolute;left:78px;right:60px;top:140px;font-size:126px;line-height:1;font-weight:300;color:#0E0E0E;letter-spacing:-.025em;white-space:nowrap">Moving to <span style="display:inline-block;width:300px;border-bottom:8px solid var(--red);height:92px;vertical-align:baseline"></span></div>
<div class="fra it red" style="position:absolute;left:80px;right:60px;top:295px;font-size:60px;line-height:1.1;font-weight:400;letter-spacing:-.01em">No agent yet. Plenty of questions.</div>
<div style="position:absolute;left:80px;right:80px;top:405px">
  {''.join(f'<div style="display:flex;gap:24px;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:20px 0 22px"><span class="mono red" style="font-size:24px">0{i+1}</span><span style="font-size:37px;line-height:1.1;color:#0E0E0E">{q}</span></div>' for i,q in enumerate(q21))}
</div>
<div class="photo" style="left:0;right:0;top:700px;bottom:0;{ph('moving','50% 42%')}"></div>
<div style="position:absolute;left:0;right:0;top:1040px;bottom:0;background:linear-gradient(180deg,rgba(8,8,8,0),rgba(8,8,8,.9) 62%)"></div>
{mf('ll', True)}
""")

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
