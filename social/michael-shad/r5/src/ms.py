"""Michael Shad personal Facebook, Oct 30 to Nov 14 2026, rebuilt in the approved SocialDM editorial system.
Same tokens, fonts, logos and footer as social/socialdm-campaign-1102/src/base.py. 1080x1350 rendered at 2x."""
import sys, asyncio
from base import *

def mf(brand='sdm', dark=False):
    """Personal footer: real logo left, byline right."""
    return foot(brand, dark, right='MICHAEL SHAD')

def tag(t='Illustrative', right=True):
    side = 'right:80px' if right else 'left:80px'
    return f'<div style="position:absolute;{side};top:72px"><span class="ex">{t}</span></div>'

# ---------------------------------------------------------------- Fri Oct 30, Realtors, bio
T['ms-1030-bio'] = S(f"""
<div class="mono red eye">For agents</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:100px;line-height:1;color:#0E0E0E">Would AI pick you<br><span class="it red">from your bio?</span></div>
<div style="position:absolute;left:80px;right:80px;top:430px;border-top:2px solid #0E0E0E;padding-top:22px">
  <div class="mono" style="font-size:22px;color:var(--mute)">The bio most agents have</div>
  <div class="news it" style="margin-top:18px;font-size:44px;line-height:1.3;color:#8E887F;text-decoration:line-through;text-decoration-color:#D2321E;text-decoration-thickness:4px">“Your trusted real estate partner, serving the greater metro area.”</div>
  <div class="mono" style="margin-top:16px;font-size:21px;color:#0E0E0E">Reads fine. Gives AI nothing to match.</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:770px;border-top:2px solid #0E0E0E;padding-top:22px">
  <div class="mono red" style="font-size:22px">Say it in specific terms</div>
  {''.join(f'<div style="display:flex;gap:26px;align-items:baseline;padding:16px 0;border-bottom:1px solid var(--line)"><span class="mono red" style="font-size:24px">{n}</span><span class="fra" style="font-size:42px;line-height:1.1;color:#0E0E0E;font-weight:400">{t}</span></div>' for n,t in [('01','The neighborhoods you actually work in.'),('02','The buyers or sellers you serve best.'),('03','The details only you can claim.')])}
</div>
{mf('sdm')}
""")

# ---------------------------------------------------------------- Sat Oct 31, MF, Halloween
items31 = [('01','A special that ended months ago'),('02','An amenity listed as open after it closed'),('03','A tough review with no reply')]
T['ms-1031-halloween'] = S(f"""
<div class="photo" style="inset:0;{ph('jackolantern','50% 40%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.55) 0%,rgba(8,8,8,.25) 20%,rgba(8,8,8,.88) 38%,#080808 60%)"></div>
<div class="mono eye" style="color:#FAFAF8">Happy Halloween</div>
<div style="position:absolute;left:76px;right:80px;top:560px">
  <div class="bod it red" style="font-size:84px;line-height:1">The scariest things</div>
  <div class="anton" style="font-size:118px;line-height:.95;color:#FAFAF8;margin-top:8px">AI might repeat about you.</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:910px">
  {''.join(f'<div style="display:flex;gap:26px;align-items:baseline;padding:14px 0;border-top:1px solid var(--dline)"><span class="mono red" style="font-size:24px">{n}</span><span style="font-size:36px;line-height:1.2;color:#FAFAF8">{t}</span></div>' for n,t in items31)}
</div>
{mf('ll', True)}
""", bg='#080808')

# ---------------------------------------------------------------- Sun Nov 1, local business, summary and holiday hours
T['ms-1101-summary'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:700px;{ph('latte','50% 55%')}"></div>
<div class="tag" style="position:absolute;left:80px;top:80px;background:#FAFAF8;color:#0E0E0E">Local business</div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:750px;font-size:84px;line-height:1;font-weight:300;color:#0E0E0E;letter-spacing:-.02em">Many customers decide from <span class="it red" style="font-weight:400">the summary.</span></div>
<div style="position:absolute;left:80px;width:760px;top:1030px;font-size:32px;line-height:1.4;color:var(--soft)">Holidays are coming. Summaries pull your hours, so make Google and your website match.</div>
{mf('sdm')}
""")

# ---------------------------------------------------------------- Mon Nov 2, MF, clear specials
T['ms-1102-specials'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">Writing specials</div>{tag('Example')}
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:104px;line-height:1;color:#FAFAF8">Can AI repeat your special <span class="it red">correctly?</span></div>
<div style="position:absolute;left:80px;right:80px;top:480px;border-top:1px solid var(--dline);padding-top:22px">
  <div class="mono" style="font-size:22px;color:var(--dsoft)">Hard to repeat</div>
  <div class="news it" style="margin-top:14px;font-size:42px;line-height:1.25;color:#8E887F">“Huge savings! Weeks free on select homes! Call for details, restrictions apply.”</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:770px;border-top:2px solid var(--red);padding-top:22px">
  <div class="mono red" style="font-size:22px">Easy to repeat</div>
  <div class="fra" style="margin-top:14px;font-size:58px;line-height:1.1;color:#FAFAF8;font-weight:400">6 weeks free on 1 bedroom homes with a 12 month lease. Move in by <span class="it red">November 30.</span></div>
  <div class="mono" style="margin-top:24px;font-size:24px;color:var(--dsoft)">Example special only, not a real offer</div>
</div>
{mf('sdm', True)}
""", bg='#0E0E0E')

# ---------------------------------------------------------------- Tue Nov 3, MF, location is a feature
near = ['the light rail', 'the hospital where they work', 'a good coffee shop', 'a dog park']
T['ms-1103-location'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:560px;{ph('alley','50% 58%')}"></div>
<div class="tag" style="position:absolute;left:80px;top:80px;background:#FAFAF8;color:#0E0E0E">Neighborhood</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:610px;font-size:92px;line-height:1;color:#0E0E0E">Your location is a feature. <span class="it red">Write it down.</span></div>
<div style="position:absolute;left:80px;right:80px;top:840px">
  <div class="mono" style="font-size:22px;color:var(--mute);margin-bottom:6px">Renters search apartments near</div>
  {''.join(f'<div style="display:flex;gap:20px;align-items:baseline;border-top:1.5px solid #0E0E0E;padding:10px 0"><span class="mono red" style="font-size:24px">+</span><span class="ins it" style="font-size:44px;line-height:1;color:#0E0E0E">{p}</span></div>' for p in near)}
  <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
{mf('ll')}
""")

# ---------------------------------------------------------------- Wed Nov 4, Realtors, monthly neighborhood note
T['ms-1104-note'] = S(f"""
<div style="position:absolute;left:80px;right:80px;top:72px;border-top:3px solid #0E0E0E;border-bottom:1px solid #0E0E0E;height:12px"></div>
<div class="ital" style="position:absolute;left:74px;right:80px;top:104px;font-size:108px;line-height:1;color:#0E0E0E;white-space:nowrap">The Neighborhood</div>
<div class="ital red" style="position:absolute;left:76px;top:222px;font-size:108px;line-height:1">Note</div>
<div style="position:absolute;left:80px;right:80px;top:372px;display:flex;justify-content:space-between;border-top:1px solid #0E0E0E;padding-top:12px"><span class="mono" style="font-size:21px;color:#0E0E0E">For agents, once a month</span><span class="mono red" style="font-size:21px">One area at a time</span></div>
<div class="photo" style="left:80px;top:440px;width:440px;height:560px;{ph('street','50% 50%')}"></div>
<div style="position:absolute;left:560px;right:80px;top:440px">
  {''.join(f'<div style="border-top:1.5px solid #0E0E0E;padding:16px 0 22px"><div class="mono red" style="font-size:22px">{n}</div><div class="fra" style="font-size:42px;line-height:1.08;color:#0E0E0E;font-weight:400;margin-top:8px">{t}</div></div>' for n,t in [('01','New listings'),('02','How long homes are taking to sell'),('03','One question buyers keep asking')])}
</div>
<div style="position:absolute;left:80px;right:80px;top:1036px;font-size:28px;line-height:1.4;color:var(--soft)">Short, current, specific to one area and clearly yours. Market facts only, within your MLS rules.</div>
{mf('sdm')}
""")

# ---------------------------------------------------------------- Thu Nov 5, MF, lead response
T['ms-1105-response'] = S(f"""
<div class="photo" style="right:0;top:0;width:520px;height:1350px;{ph('phonewoman','35% 40%')}"></div>
<div style="position:absolute;right:0;top:0;width:520px;height:1350px;background:linear-gradient(90deg,#0E0E0E 0%,rgba(14,14,14,0) 28%)"></div>
<div class="mono red eye">After the shortlist</div>
<div style="position:absolute;left:80px;width:560px;top:170px">
  <div class="anton" style="font-size:112px;line-height:.95;color:#FAFAF8">AI can put you on the list.</div>
  <div class="bod it red" style="font-size:88px;line-height:1.02;margin-top:26px">Your team closes it.</div>
</div>
<div style="position:absolute;left:80px;width:500px;top:760px">
  <div class="mono" style="font-size:22px;color:var(--dsoft);margin-bottom:6px">The response check</div>
  {''.join(f'<div style="border-top:1px solid var(--dline);padding:14px 0;font-size:34px;line-height:1.2;color:#FAFAF8">{t}</div>' for t in ['How fast do weekend tour requests get answered?','Does the reply answer the actual question?','Is there a clear next step?'])}
</div>
{foot('sdm', True, right='')}<div class="url" style="position:absolute;left:80px;bottom:200px;color:#FAFAF8;font-size:22px">Michael Shad</div>
""", bg='#0E0E0E')

# ---------------------------------------------------------------- Fri Nov 6, MF, floor plan as text
plan = """<svg width="420" height="460" viewBox="0 0 420 460" fill="none" stroke="#0E0E0E" stroke-width="5">
<rect x="10" y="10" width="400" height="440"/><line x1="10" y1="230" x2="250" y2="230"/><line x1="250" y1="10" x2="250" y2="320"/>
<line x1="250" y1="320" x2="410" y2="320"/><line x1="140" y1="230" x2="140" y2="450"/>
<path d="M250 150 A60 60 0 0 1 310 210" stroke-width="2"/><path d="M10 330 A55 55 0 0 0 65 385" stroke-width="2"/></svg>"""
fields = ['Plan name','Beds and baths','Square footage','Standout features','Pet policy']
T['ms-1106-floorplan'] = S(f"""
<div class="mono red eye">Websites</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:96px;line-height:1.1;color:#0E0E0E">If it only lives in an image, <span class="it red">AI may not read it.</span></div>
<div style="position:absolute;left:80px;top:500px;width:440px;height:560px;background:var(--warm);display:grid;place-items:center">{plan}
  <div class="mono" style="position:absolute;left:24px;bottom:18px;font-size:20px;color:var(--mute)">Image only</div></div>
<div style="position:absolute;left:570px;right:80px;top:500px">
  <div class="mono red" style="font-size:22px;margin-bottom:6px">Add as real text</div>
  {''.join(f'<div style="border-top:1.5px solid #0E0E0E;padding:16px 0;font-size:36px;line-height:1.1;color:#0E0E0E">{t}</div>' for t in fields)}
  <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
{mf('ll')}
""")

# ---------------------------------------------------------------- Sat Nov 7, MF, AI referrals in analytics
bars = [('Google search',100,False),('Listing sites',62,False),('Direct',48,False),('AI assistants',9,True)]
T['ms-1107-referrals'] = S(f"""
<div class="mono eye" style="color:#FAFAF8">Analytics</div>{tag('Illustrative')}
<div class="fra" style="position:absolute;left:80px;right:80px;top:150px;font-size:94px;line-height:1.02;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">AI may already send renters to your site. <span class="it red" style="font-weight:400">Can you see them?</span></div>
<div style="position:absolute;left:80px;right:80px;top:560px">
  <div class="mono" style="font-size:22px;color:var(--dsoft);margin-bottom:18px">Website visits by source</div>
  {''.join(f'<div style="margin-bottom:22px"><div style="display:flex;justify-content:space-between;font-size:32px;color:{"#FAFAF8" if not r else "#FF6A55"};margin-bottom:10px"><span>{l}</span></div><div style="height:26px;width:{w}%;background:{"#D2321E" if r else "#5A5550"}"></div></div>' for l,w,r in bars)}
</div>
<div style="position:absolute;left:80px;width:800px;top:1060px;font-size:30px;line-height:1.4;color:var(--dsoft)">Small today, so watch it monthly. Some AI visits arrive as direct, so treat the number as a minimum.</div>
{mf('ll', True)}
""", bg='#0E0E0E')

# ---------------------------------------------------------------- Sun Nov 8, MF, follow up questions
steps = [('6','communities named','Best apartments in Tempe'),('3','still on the list','Which allow a large dog?'),('1','left','Which have laundry in the home?')]
T['ms-1108-followups'] = S(f"""
<div class="mono red eye">Renter search</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:98px;line-height:1;color:#0E0E0E">The first answer is <span class="it red">only the start.</span></div>
<div style="position:absolute;left:80px;right:80px;top:410px">
  {''.join(f'<div style="display:flex;align-items:center;gap:30px;border-top:1.5px solid #0E0E0E;padding:14px 0"><span class="bsd" style="font-size:118px;line-height:.9;font-weight:800;color:{"#D2321E" if i==2 else "#0E0E0E"};width:90px">{n}</span><div><div class="ins it" style="font-size:42px;line-height:1.05;color:#0E0E0E">{q}</div><div class="mono" style="font-size:22px;color:var(--mute);margin-top:6px">{l}</div></div></div>' for i,(n,l,q) in enumerate(steps))}
  <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
<div class="photo" style="left:80px;right:80px;top:870px;height:240px;{ph('laptop','50% 62%')}"></div>
<div style="position:absolute;left:80px;right:80px;top:870px;height:240px;background:linear-gradient(90deg,rgba(14,14,14,.92),rgba(14,14,14,.8) 55%,rgba(14,14,14,.3) 85%)"></div>
<div style="position:absolute;left:116px;width:600px;top:925px;font-size:36px;line-height:1.3;color:#FAFAF8">Each follow up narrows the list. State the details as facts.</div>
{mf('sdm')}
""")

# ---------------------------------------------------------------- Mon Nov 9, Realtors, closings as case notes
T['ms-1109-casenotes'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:600px;{ph('porchb','50% 60%')}"></div>
<div style="position:absolute;left:0;top:0;width:1080px;height:600px;background:linear-gradient(180deg,rgba(0,0,0,.62),rgba(0,0,0,0) 32%)"></div>
<div class="mono eye" style="color:#FAFAF8">For agents</div>
<div style="position:absolute;left:80px;right:80px;top:470px;background:#FAFAF8;padding:36px 44px 40px;box-shadow:0 18px 50px rgba(0,0,0,.18)">
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="mono red" style="font-size:22px">Case note 01</span><span class="ex">Example</span></div>
  <div class="news" style="margin-top:20px;font-size:40px;line-height:1.25;color:#0E0E0E">1950s ranch in Arcadia Lite. The pool needed work. We priced for the repair up front.</div>
  <div class="news it red" style="margin-top:12px;font-size:40px;line-height:1.2">Two offers in the first week.</div>
  <div class="mono" style="margin-top:18px;font-size:22px;color:var(--mute)">Example only, not a real sale</div>
</div>
<div class="bod" style="position:absolute;left:80px;right:80px;top:900px;font-size:84px;line-height:1;color:#0E0E0E">Your past sales are proof <span class="it red">only you have.</span></div>
{mf('sdm')}
""")

# ---------------------------------------------------------------- Tue Nov 10, MF, Google profile blanks
blanks = ['Additional categories','Amenity attributes','Holiday hours','A description that names the neighborhood']
T['ms-1110-blanks'] = S(f"""
<div class="photo" style="right:0;top:0;width:380px;height:1350px;{ph('balconies','50% 50%')}"></div>
<div class="mono red eye">Google profile</div>
<div class="bod" style="position:absolute;left:80px;width:580px;top:150px;font-size:94px;line-height:1;color:#0E0E0E">Your Google profile is a <span class="it red">fact sheet.</span></div>
<div style="position:absolute;left:80px;width:580px;top:560px">
  <div class="mono" style="font-size:21px;color:var(--mute);margin-bottom:8px">Fields teams skip most</div>
  {''.join(f'<div style="padding:18px 0 14px"><div style="font-size:31px;line-height:1.2;color:#0E0E0E">{b}</div><div style="margin-top:22px;border-bottom:2px dashed var(--red);height:0"></div></div>' for b in blanks)}
</div>
<div class="ins it red" style="position:absolute;left:80px;width:580px;top:1010px;font-size:50px;line-height:1">How many blanks did you count?</div>
{foot('ll', False, right='', rightpx=400)}<div class="url" style="position:absolute;left:330px;bottom:86px;color:#0E0E0E;font-size:22px">Michael Shad</div>
""")

# ---------------------------------------------------------------- Wed Nov 11, MF, third party mentions (Swiss type)
srcs = ['Local news','Neighborhood guides','Employer relocation pages','City event calendars','Chamber listings']
T['ms-1111-mentions'] = S(f"""
<div class="mono eye" style="color:#0E0E0E">Third party mentions</div>
<div class="anton" style="position:absolute;left:66px;top:150px;font-size:330px;line-height:.82;color:#FAFAF8">They</div>
<div class="anton" style="position:absolute;left:66px;top:420px;font-size:330px;line-height:.82;color:#0E0E0E">said.</div>
<div style="position:absolute;left:80px;width:520px;top:750px;font-size:38px;line-height:1.25;color:#FAFAF8;font-weight:500">AI tools tend to notice what other people say about you.</div>
<div style="position:absolute;left:640px;right:80px;top:750px">
  {''.join(f'<div style="border-top:2px solid #0E0E0E;padding:12px 0;font-size:28px;line-height:1.15;color:#0E0E0E;font-weight:500">{s}</div>' for s in srcs)}
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:250px;background:#0E0E0E"></div>
{mf('sdm', True)}
""", bg='#D2321E')

# ---------------------------------------------------------------- Thu Nov 12, MF, structured data
code = '''<span style="color:#8E887F">{</span>
  <span class="k">"@context"</span>: <span class="v">"https://schema.org"</span>,
  <span class="k">"@type"</span>: <span class="v">"ApartmentComplex"</span>,
  <span class="k">"name"</span>: <span class="v">"Example Community"</span>,
  <span class="k">"petsAllowed"</span>: <span class="v">true</span>,
  <span class="k">"telephone"</span>: <span class="v">"…"</span>
<span style="color:#8E887F">}</span>'''
T['ms-1112-schema'] = S(f"""
<div class="photo" style="inset:0;{ph('greybld','50% 50%')};filter:grayscale(1) brightness(.22)"></div>
<div class="mono eye" style="color:#FAFAF8">Behind the page</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:80px;top:150px;font-size:98px;line-height:1;color:#FAFAF8">There’s a version of your website <span class="it red">only machines read.</span></div>
<pre class="mono" style="position:absolute;left:80px;right:80px;top:560px;background:rgba(14,14,14,.9);border-left:6px solid var(--red);padding:36px 40px;font-size:27px;line-height:1.6;letter-spacing:.02em;text-transform:none;color:#FAFAF8;white-space:pre">{code}</pre>
<div style="position:absolute;left:80px;width:860px;top:1030px;font-size:30px;line-height:1.4;color:var(--dsoft)">Structured data labels the facts. Ask what’s on your site, and when it was last updated.</div>
{mf('sdm', True)}
""", bg='#0E0E0E', css='.k{color:#FF8A78} .v{color:#FAFAF8}')

# ---------------------------------------------------------------- Fri Nov 13, Realtors, video words
T['ms-1113-video'] = S(f"""
<div class="photo" style="left:0;top:0;width:540px;height:1350px;{ph('gimbal','45% 40%')}"></div>
<div class="tag" style="position:absolute;left:80px;top:80px;background:#0E0E0E;color:#FAFAF8">For agents</div>
<div style="position:absolute;left:600px;right:80px;top:80px"><span class="ex">Example</span></div>
<div class="bod" style="position:absolute;left:600px;right:70px;top:170px;font-size:78px;line-height:1.02;color:#FAFAF8">Give your videos <span class="it red">words AI can read.</span></div>
<div style="position:absolute;left:600px;right:70px;top:640px">
  <div class="mono" style="font-size:22px;color:var(--dsoft)">Title before</div>
  <div style="position:relative;display:inline-block;margin-top:10px;font-size:40px;color:#8E887F">Saturday vibes<div style="position:absolute;left:-4px;right:-4px;top:52%;height:4px;background:var(--red)"></div></div>
  <div class="mono red" style="font-size:22px;margin-top:40px">Title after</div>
  <div class="fra" style="margin-top:10px;font-size:44px;line-height:1.12;color:#FAFAF8;font-weight:400">Living in Coronado: bungalows and coffee spots</div>
</div>
{foot('sdm', True, right='', left=600)}<div class="url" style="position:absolute;left:600px;bottom:220px;color:#FAFAF8;font-size:22px">Michael Shad</div>
""", bg='#0A0A0A')

# ---------------------------------------------------------------- Sat Nov 14, MF, comparison A vs B
rows = [('Coworking room','Size and hours listed','“Ask the office”'),('Parking','Covered, stated','Not mentioned'),('Packages','Lockers, stated','Not mentioned'),('Groceries','Walk time named','“Close to everything”')]
T['ms-1114-compare'] = S(f"""
<div class="photo" style="left:0;top:0;width:1080px;height:470px;{ph('facade','50% 45%')}"></div>
<div class="tag" style="position:absolute;left:80px;top:80px;background:#FAFAF8;color:#0E0E0E">Comparison questions</div>{tag('Illustrative')}
<div class="bod" style="position:absolute;left:80px;right:80px;top:510px;font-size:84px;line-height:1;color:#0E0E0E">One question puts you <span class="it red">side by side.</span></div>
<div style="position:absolute;left:80px;right:80px;top:720px">
  <div style="display:grid;grid-template-columns:270px 1fr 1fr;gap:0 24px;padding-bottom:12px"><span></span><span class="mono red" style="font-size:24px">Community A</span><span class="mono" style="font-size:24px;color:var(--mute)">Community B</span></div>
  {''.join(f'<div style="display:grid;grid-template-columns:270px 1fr 1fr;gap:0 24px;border-top:1.5px solid #0E0E0E;padding:14px 0;font-size:29px;line-height:1.2"><span class="mono" style="font-size:20px;color:#0E0E0E;padding-top:6px">{k}</span><span style="color:#0E0E0E">{a}</span><span class="news it" style="color:#8E887F">{b}</span></div>' for k,a,b in rows)}
  <div style="border-top:1.5px solid #0E0E0E"></div>
</div>
{mf('ll')}
""")

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
