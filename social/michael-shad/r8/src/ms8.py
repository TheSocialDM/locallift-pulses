"""Michael Shad personal Facebook, Nov 29 to Dec 5 2026. Approved SocialDM editorial system (base.py). 1080x1350 at 2x.
Nov 30 and Dec 2 are Field Notes week 2 (approved copy)."""
import sys, asyncio
from base import *

def mf(brand='sdm', dark=False):
    return foot(brand, dark, right='MICHAEL SHAD')
def tag(t='Example', top=72):
    return f'<div style="position:absolute;right:80px;top:{top}px"><span class="ex">{t}</span></div>'

# Sun Nov 29, MF, same question, different answers (soft white, two ranked columns)
A = ['Community A', 'Community B', 'Community C']
B = ['Community B', 'Community D', 'Community A']
def col(label, items, hi):
    rows = ''.join(f'<div style="display:grid;grid-template-columns:62px 1fr;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:16px 0"><span class="osw" style="font-size:38px;color:{"#D2321E" if it==hi else "#0E0E0E"}">{i+1}</span><span class="fra" style="font-size:40px;line-height:1.1;color:{"#D2321E" if it==hi else "#0E0E0E"};{"font-style:italic;font-weight:600" if it==hi else "font-weight:400"}">{it}</span></div>' for i, it in enumerate(items))
    return f'<div><div class="mono" style="font-size:22px;color:#6B665E;margin-bottom:12px">{label}</div>{rows}</div>'
T['ms-1129-same-question'] = S(f"""
<div class="mono red eye">Renter questions</div>{tag('Illustrative')}
<div class="syne" style="position:absolute;left:78px;right:60px;top:160px;font-size:74px;line-height:.96;font-weight:800;white-space:nowrap;color:#0E0E0E;letter-spacing:-.035em">Same question.</div>
<div class="ins it red" style="position:absolute;left:80px;right:60px;top:262px;font-size:112px;line-height:1;white-space:nowrap">Different answers.</div>
<div style="position:absolute;left:80px;right:80px;top:470px;display:flex;gap:18px;align-items:baseline">
  <span class="mono" style="font-size:22px;color:#6B665E;flex:none">Asked</span>
  <span class="news it" style="font-size:42px;line-height:1.15;color:#0E0E0E">“Best apartments near downtown?”</span>
</div>
<div style="position:absolute;left:80px;right:80px;top:590px;display:grid;grid-template-columns:1fr 1fr;gap:56px">
  {col('Renter one', A, 'Community C')}{col('Renter two', B, 'Community D')}
</div>
<div style="position:absolute;left:80px;right:80px;top:1010px;font-size:31px;line-height:1.32;color:#3A3631">Wording, the tool and the moment can all shift the list. The pattern tells you more than one screenshot.</div>
{mf('sdm')}
""")

# Mon Nov 30, Realtors, Field Notes week 2: say what makes a neighborhood different (photo top, before and after type)
T['ms-1130-neighborhood'] = S(f"""
<div class="photo" style="left:0;right:0;top:0;height:640px;{ph('ranch','62% 70%')}"></div>
<div style="position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,0))"></div>
<div class="mono eye" style="color:#FAFAF8">For agents</div>{tag('Example')}
<div style="position:absolute;left:80px;right:80px;top:690px">
  <div class="mono" style="font-size:22px;color:#6B665E">Could be anywhere</div>
  <div class="news" style="font-size:44px;line-height:1.15;color:#8A857C;margin-top:10px">“Charming homes in a sought after area.”</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:850px;border-top:2px solid #0E0E0E;padding-top:22px;padding-left:6px">
  <div class="mono red" style="font-size:22px">Could only be one place</div>
  <div class="bod" style="font-size:66px;line-height:1.05;color:#0E0E0E;margin-top:14px">Mostly 1960s ranch homes on larger lots, <span class="it red">about a 10 minute drive from downtown.</span></div>
</div>
{mf('ll')}
""")

# Tue Dec 1, Realtors, whose name is on your reviews (black, Anton stack, two review lines)
STARS = ''.join('<span style="width:20px;height:20px;background:#D2321E;display:inline-block"></span>' for _ in range(5))
revs = [('Great experience with the Copper Lane Team.', 'Credits the team', '#CFCAC1'),
        ('Maria found us a condo near the light rail, and she answered every text.', 'Credits the agent', '#FF5A3F')]
T['ms-1201-review-credit'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">For agents</div>{tag('Example reviews')}
<div class="anton" style="position:absolute;left:76px;right:60px;top:150px;font-size:150px;line-height:.92;color:#FAFAF8">Whose name<br>is on <span style="color:#D2321E">the review?</span></div>
<div style="position:absolute;left:80px;right:80px;top:640px">
  {''.join(f'<div style="border-top:1.5px solid rgba(250,250,248,.4);padding:24px 0 26px"><div style="display:flex;gap:8px;margin-bottom:14px">{STARS}</div><div class="news it" style="font-size:42px;line-height:1.16;color:#FAFAF8">“{t}”</div><div class="mono" style="font-size:22px;color:{c};margin-top:14px">{l}</div></div>' for t,l,c in revs)}
</div>
{mf('ll', True)}
""", bg='#0E0E0E')

# Wed Dec 2, MF, Field Notes week 2: "Resort style pool" (full bleed night pool, question annotations)
def q(t, x, y):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;display:flex;align-items:center;gap:12px"><span style="width:18px;height:18px;border-radius:50%;background:#D2321E;box-shadow:0 0 0 6px rgba(210,50,30,.3)"></span><span class="mono" style="font-size:28px;color:#FAFAF8;background:rgba(6,8,12,.62);padding:4px 10px">{t}</span></div>'
T['ms-1202-resort-style'] = S(f"""
<div class="photo" style="inset:0 0 auto 0;height:900px;{ph('pool','30% 50%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,8,12,.78) 0%,rgba(6,8,12,0) 16%,rgba(6,8,12,0) 46%,rgba(6,8,12,.9) 62%,#06080C 70%)"></div>
<div class="mono eye" style="color:#FAFAF8">Apartment amenities</div>{tag('Example only')}
{q('Heated?', 120, 600)}{q('Open until?', 560, 400)}{q('Guests allowed?', 430, 520)}
<div class="bod" style="position:absolute;left:80px;right:60px;top:720px;font-size:84px;line-height:1.02;color:#FAFAF8">“Resort style” <span class="it" style="color:#FF5A3F">answers almost nothing.</span></div>
<div style="position:absolute;left:80px;right:80px;top:960px;display:flex;gap:24px;align-items:baseline;border-top:1.5px solid rgba(250,250,248,.55);padding-top:18px">
  <span class="mono" style="font-size:22px;flex:none;color:#FF5A3F">Try</span>
  <span class="news it" style="font-size:40px;line-height:1.15;color:#FAFAF8">“Heated saltwater pool, open until 10 PM.”</span>
</div>
{mf('sdm', True)}
""", bg='#06080C')

# Thu Dec 3, MF, AI that takes the next step (Swiss stacked type, type only)
T['ms-1203-ask-act'] = S(f"""
<div class="mono red eye">Where AI is heading</div>
<div style="position:absolute;right:0;top:0;width:220px;height:330px;background:#0E0E0E"></div>
<div class="mono" style="position:absolute;right:80px;top:80px;font-size:22px;color:#FAFAF8;text-align:right;line-height:1.5">Where it<br>may go</div>
<div class="bsd" style="position:absolute;left:66px;top:150px;font-size:220px;line-height:.82;font-weight:900;color:#0E0E0E;letter-spacing:-.01em">ASK</div>
<div class="bsd" style="position:absolute;left:66px;top:335px;font-size:220px;line-height:.82;font-weight:300;color:#0E0E0E;letter-spacing:-.01em">ANSWER</div>
<div class="bsd" style="position:absolute;left:66px;top:520px;font-size:220px;line-height:.82;font-weight:900;color:#D2321E;letter-spacing:-.01em">ACT</div>
<div class="ins it" style="position:absolute;left:470px;right:80px;top:580px;font-size:52px;line-height:1.02;color:#0E0E0E">someday, booking a tour?</div>
<div style="position:absolute;left:80px;right:80px;top:820px;border-top:2px solid #0E0E0E;padding-top:24px;display:grid;grid-template-columns:1fr 1fr;gap:48px">
  <div class="fra" style="font-size:44px;line-height:1.1;color:#0E0E0E;font-weight:400">Some AI tools are starting to <span class="it red">take the next step.</span></div>
  <div style="font-size:30px;line-height:1.34;color:#3A3631">The same things help a renter at 11 PM: tour times they can see and a booking page that works.</div>
</div>
{mf('sdm')}
""")

# Fri Dec 4, Realtors, listing description has a new reader (classified page, marked phrases)
mk = lambda t: f'<span style="background:linear-gradient(180deg,transparent 58%,rgba(210,50,30,.35) 58%)">{t}</span>'
T['ms-1204-listing'] = S(f"""
<div class="mono red eye">For agents</div>{tag('Illustrative')}
<div class="news" style="position:absolute;left:78px;right:60px;top:150px;font-size:100px;line-height:1;color:#0E0E0E;letter-spacing:-.01em">Your listing has <span class="it red">a new reader.</span></div>
<div style="position:absolute;left:80px;right:80px;top:400px;border-top:3px solid #0E0E0E;border-bottom:1px solid #0E0E0E;padding:16px 0;display:flex;gap:20px;align-items:baseline">
  <span class="mono" style="font-size:22px;color:#6B665E;flex:none">Typed</span>
  <span class="news it" style="font-size:34px;line-height:1.15;color:#0E0E0E">“3 bedroom home with a fenced yard and a home office”</span>
</div>
<div style="position:absolute;left:80px;right:80px;top:560px;display:grid;grid-template-columns:1fr 1.45fr;gap:48px">
  <div><div class="mono" style="font-size:22px;color:#6B665E">Gives it little</div><div class="news" style="font-size:40px;line-height:1.18;color:#8A857C;margin-top:14px">“Stunning must see gem!”</div></div>
  <div style="border-left:1.5px solid #0E0E0E;padding-left:40px"><div class="mono red" style="font-size:22px">Gives it something to match</div><div class="news" style="font-size:40px;line-height:1.3;color:#0E0E0E;margin-top:14px">3 bedrooms. {mk('Fenced backyard')}, a detached studio {mk('used as a home office')}, roof replaced in 2021.</div></div>
</div>
<div style="position:absolute;left:80px;right:80px;top:900px;font-size:34px;line-height:1.32;color:#3A3631">Describe the home, not who it’s for.</div>
{mf('ll')}
""")

# Sat Dec 5, Realtors, the languages you work in (black, language stack, magazine inset photo)
langs = [('Hablo español.', '#FAFAF8'), ('Falo português.', '#FAFAF8'), ('Je parle français.', '#FAFAF8')]
T['ms-1205-languages'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">For agents</div>
<div class="photo" style="right:80px;top:150px;width:400px;height:560px;{ph('keys','42% 50%')}"></div>
<div style="position:absolute;left:80px;width:480px;top:150px">
  {''.join(f'<div class="ital" style="font-size:66px;line-height:1.24;color:{c};opacity:{1-i*.16}">{t}</div>' for i,(t,c) in enumerate(langs))}
</div>
<div class="mono" style="position:absolute;left:80px;top:520px;font-size:22px;color:#CFCAC1;width:440px;line-height:1.5">Said at the showing.<br>Missing online?</div>
<div class="bod" style="position:absolute;left:80px;right:60px;top:770px;font-size:80px;line-height:1.04;color:#FAFAF8">Can buyers find <span class="it" style="color:#FF5A3F">the languages you work in?</span></div>
<div style="position:absolute;left:80px;right:80px;top:1000px;font-size:30px;line-height:1.32;color:#CFCAC1">Some buyers search by language first.</div>
{mf('ll', True)}
""", bg='#0E0E0E')

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
