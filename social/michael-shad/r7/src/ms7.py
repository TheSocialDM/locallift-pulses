"""Michael Shad personal Facebook, Nov 22 to 28 2026. Approved SocialDM editorial system (base.py). 1080x1350 at 2x."""
import sys, asyncio
from base import *

def mf(brand='sdm', dark=False):
    return foot(brand, dark, right='MICHAEL SHAD')
def tag(t='Example', top=72):
    return f'<div style="position:absolute;right:80px;top:{top}px"><span class="ex">{t}</span></div>'

# Sun Nov 22, MF, communities that share a name (type led, stacked repeats)
rows = [('Community 1', '#0E0E0E', 1), ('Community 2', '#0E0E0E', .55), ('Community 3', '#D2321E', 1), ('Community 4', '#0E0E0E', .32), ('Community 5', '#0E0E0E', .18)]
T['ms-1122-same-name'] = S(f"""
<div class="mono red eye">Apartment names</div>{tag('Example names')}
<div class="fra" style="position:absolute;left:80px;right:70px;top:150px;font-size:92px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.02em">Five communities.<br><span class="it red">One name.</span></div>
<div style="position:absolute;left:80px;right:80px;top:395px">
  {''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:6px 0 4px"><span class="bod it" style="font-size:96px;line-height:1.1;color:{c};opacity:{o}">The Juniper</span><span class="mono" style="font-size:22px;color:{'#D2321E' if c=='#D2321E' else '#6B665E'}">{n}</span></div>' for n,c,o in rows)}
</div>
<div style="position:absolute;left:80px;right:80px;top:1105px;font-size:31px;line-height:1.3;color:#3A3631">AI tools tend to tell them apart by the details around the name.</div>
{mf('ll')}
""")

# Mon Nov 23, Realtors, guide behind a form (Field Notes week 1), padlock full bleed
T['ms-1123-locked-guide'] = S(f"""
<div class="photo" style="inset:0;{ph('padlock','58% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.55) 0%,rgba(8,8,8,0) 22%,rgba(8,8,8,0) 38%,rgba(8,8,8,.82) 58%,#080808 100%)"></div>
<div class="mono eye" style="color:#FAFAF8;text-shadow:0 1px 8px rgba(0,0,0,.6)">For agents</div>
<div class="bod" style="position:absolute;left:80px;right:70px;top:760px;font-size:96px;line-height:1.02;color:#FAFAF8">Your best guide may be <span class="it" style="color:#FF5A3F">invisible to AI.</span></div>
<div style="position:absolute;left:80px;right:80px;top:1010px;display:flex;align-items:stretch;border:2px solid rgba(250,250,248,.75)">
  <div style="flex:1;padding:18px 22px;font-size:28px;color:#CFCAC1">Enter your email to read the guide</div>
  <div class="mono" style="background:#D2321E;color:#FAFAF8;font-size:22px;padding:0 24px;display:flex;align-items:center">Unlock</div>
</div>
<div class="mono" style="position:absolute;left:80px;top:1090px;font-size:22px;color:#CFCAC1">Example form, for illustration</div>
{mf('ll', True)}
""", bg='#080808')

# Tue Nov 24, Realtors, how buying works here (soft white, B&W photo band, three question columns)
qs = ['How long is the inspection period here?', 'Who usually pays for the title policy?', 'When does earnest money go hard?']
T['ms-1124-how-it-works'] = S(f"""
<div class="mono red eye">Buyer questions</div>
<div class="news" style="position:absolute;left:78px;right:60px;top:140px;font-size:104px;line-height:1;color:#0E0E0E;font-weight:400;letter-spacing:-.01em">How does buying <span class="it red">work here?</span></div>
<div class="photo" style="left:0;right:0;top:390px;height:400px;{ph('reader','40% 45%')};filter:grayscale(1) contrast(1.05)"></div>
<div style="position:absolute;left:80px;right:80px;top:835px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:36px">
  {''.join(f'<div style="border-top:2px solid #0E0E0E;padding-top:16px"><div class="osw red" style="font-size:44px;line-height:1">Q{i+1}</div><div style="font-size:30px;line-height:1.24;color:#0E0E0E;margin-top:12px">{q}</div></div>' for i,q in enumerate(qs))}
</div>
<div class="ins it" style="position:absolute;left:80px;right:80px;top:1105px;font-size:40px;line-height:1.1;color:#3A3631">Answers vary by state, even by county.</div>
{mf('ll')}
""")

# Wed Nov 25, MF, "Contact us for more information" (Field Notes week 1), full red, type led
T['ms-1125-contact-us'] = S(f"""
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#D2321E 0%,#D2321E 70%,#5A140C 92%,#1A0604 100%)"></div>
<div class="mono eye" style="color:#FAFAF8">Apartment websites</div>
<div class="ins" style="position:absolute;left:72px;right:60px;top:150px;font-size:150px;line-height:.98;color:#FAFAF8">“Contact us<br>for more<br><span class="it">information.”</span></div>
<div style="position:absolute;left:80px;right:80px;top:680px;border-top:2px solid #FAFAF8"></div>
<div style="position:absolute;left:80px;right:80px;top:710px;display:grid;grid-template-columns:1fr 1fr;gap:40px">
  <div><div class="mono" style="font-size:22px;color:#FAFAF8">To a renter</div><div class="fra" style="font-size:40px;line-height:1.1;color:#FAFAF8;margin-top:12px">A phone number.</div></div>
  <div><div class="mono" style="font-size:22px;color:#FAFAF8">To an AI tool</div><div class="fra it" style="font-size:40px;line-height:1.1;color:#0E0E0E;margin-top:12px;font-weight:600;white-space:nowrap">Can be a locked door.</div></div>
</div>
{mf('sdm', True)}
""", bg='#1A0604')

# Thu Nov 26, Thanksgiving, grateful for your questions (full bleed photo, dark lower gradient)
T['ms-1126-thanksgiving'] = S(f"""
<div class="photo" style="inset:0;{ph('harvest','50% 40%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,8,6,0) 0%,rgba(10,8,6,0) 38%,rgba(10,8,6,.9) 55%,#0A0806 76%)"></div>
<div class="mono" style="position:absolute;left:80px;top:745px;font-size:26px;color:#FAFAF8;text-shadow:0 1px 10px rgba(0,0,0,.9)">Happy Thanksgiving</div>
<div class="bod" style="position:absolute;left:80px;right:60px;top:800px;font-size:100px;line-height:1;color:#FAFAF8">Grateful for <span class="it" style="color:#FF5A3F">your questions.</span></div>
<div style="position:absolute;left:80px;right:80px;top:1030px;display:flex;gap:24px;align-items:baseline;border-top:1.5px solid rgba(250,250,248,.6);padding-top:18px">
  <span class="mono" style="font-size:22px;flex:none;color:#FF5A3F">Asked most</span>
  <span class="news it" style="font-size:38px;line-height:1.15;color:#FAFAF8">Is AI going to replace Google?</span>
</div>
{mf('sdm', True)}
""", bg='#0A0806')

# Fri Nov 27, MF, is there an elevator (charcoal, illustrated elevator button panel)
facts = ['Which buildings have elevators', 'Where the ground floor homes are', 'A step free route from parking']
btn = lambda n, on: f'<div style="width:118px;height:118px;border-radius:50%;border:3px solid {"#D2321E" if on else "#8A857C"};display:flex;align-items:center;justify-content:center;font-family:Fra,serif;font-size:52px;color:{"#FAFAF8" if on else "#CFCAC1"};background:{"#D2321E" if on else "transparent"};box-shadow:{"0 0 40px rgba(210,50,30,.55)" if on else "none"}">{n}</div>'
T['ms-1127-elevator'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">Renter questions</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:420px;top:160px;font-size:104px;line-height:1;color:#FAFAF8">Is there an <span class="it" style="color:#FF5A3F">elevator<span style="margin-left:-.12em">?</span></span></div>
<div style="position:absolute;right:80px;top:170px;width:270px;height:560px;border:2px solid #4A4640;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;background:linear-gradient(180deg,#24221F,#1A1916)">
  {btn('3',False)}{btn('2',False)}{btn('1',True)}
</div>
<div style="position:absolute;left:80px;width:540px;top:430px;font-size:31px;line-height:1.32;color:#CFCAC1">Many apartment websites never say. For some renters it decides everything.</div>
<div style="position:absolute;left:80px;right:80px;top:790px">
  <div class="mono" style="font-size:22px;color:#FAFAF8;margin-bottom:6px">Say it plainly</div>
  {''.join(f'<div style="display:grid;grid-template-columns:70px 1fr;align-items:baseline;border-top:1.5px solid rgba(250,250,248,.35);padding:18px 0"><span class="osw" style="font-size:40px;line-height:1;color:#FF5A3F">0{i+1}</span><span style="font-size:32px;line-height:1.2;color:#FAFAF8">{f}</span></div>' for i,f in enumerate(facts))}
</div>
{mf('sdm', True)}
""", bg='#161513')

# Sat Nov 28, Realtors, fewer clicks (black, data bars)
bars = [('No AI summary', 15, '#FAFAF8'), ('With an AI summary', 8, '#D2321E'), ('Clicked a link inside the summary (visits with a summary)', 1, '#CFCAC1')]
T['ms-1128-fewer-clicks'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">For agents</div>
<div class="fra" style="position:absolute;left:80px;right:60px;top:150px;font-size:84px;line-height:1.02;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">Fewer clicks<br><span class="it" style="color:#FF5A3F;font-weight:400">may not mean fewer clients.</span></div>
<div class="mono" style="position:absolute;left:80px;top:470px;font-size:22px;color:#CFCAC1">Share of Google search visits with a click</div>
<div style="position:absolute;left:80px;right:80px;top:525px">
  {''.join(f'<div style="margin-bottom:34px"><div style="display:flex;align-items:flex-end;gap:24px"><div style="height:74px;width:{max(int(v/15*640),14)}px;background:{c}"></div><span class="anton" style="font-size:88px;line-height:.85;color:{c}">{v}%</span></div><div style="font-size:29px;color:#FAFAF8;margin-top:12px">{t}</div></div>' for t,v,c in bars)}
</div>
<div style="position:absolute;left:80px;right:80px;top:1060px;font-size:22px;line-height:1.4;color:#CFCAC1">Source: Pew Research Center, browsing data from 900 U.S. adults, March 2025. Share of visits to Google search pages.</div>
{mf('ll', True)}
""", bg='#0E0E0E')

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
