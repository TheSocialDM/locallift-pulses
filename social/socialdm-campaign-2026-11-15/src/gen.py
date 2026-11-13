"""SocialDM week of Nov 15 to 21, 2026 (weekly run Nov 12), round 2 after Editor, fact check and art director.
New layouts on the approved editorial system (base.py). Photo sources: ph/SOURCES.md."""
from base import *
import asyncio, sys

STK = 'font-size:22px;padding:7px 12px'

# ---------- Mon Nov 16 IG/FB: caption makeover as an annotated proof, black ----------
def mark(word, note, y):
    return f'''<div class="mono" style="position:absolute;right:80px;top:{y}px;width:220px;text-align:right;font-size:24px;line-height:1.3;color:#FF8A75">{note}</div>'''
T['s-1116-caption-makeover'] = S(f'''
<div class="mono" style="position:absolute;left:80px;top:80px;font-size:26px;color:#FF8A75">Caption makeover</div>
<div class="ex" style="position:absolute;right:80px;top:74px">Example</div>
<div class="news it" style="position:absolute;left:80px;top:190px;width:900px;font-size:36px;line-height:1.25;color:#9C978F">Instead of &ldquo;Luxury living awaits,&rdquo; try:</div>
<div class="fra" style="position:absolute;left:80px;top:290px;width:650px;font-size:104px;line-height:1.18;font-weight:600;letter-spacing:-.025em;color:#FAFAF8">
<span style="text-decoration:underline;text-decoration-color:#D2321E;text-decoration-thickness:6px;text-underline-offset:12px;text-decoration-skip-ink:none">Coffee</span> on the <span style="text-decoration:underline;text-decoration-color:#D2321E;text-decoration-thickness:6px;text-underline-offset:12px;text-decoration-skip-ink:none">balcony</span> before the <span style="text-decoration:underline;text-decoration-color:#D2321E;text-decoration-thickness:6px;text-underline-offset:12px;text-decoration-skip-ink:none">7:40&nbsp;bus.</span></div>
<div style="position:absolute;left:760px;top:300px;width:1px;height:500px;background:rgba(255,255,255,.25)"></div>
{mark('Coffee','A moment<br>to imagine',310)}
{mark('balcony','A real<br>feature',433)}
{mark('bus','A commute<br>nearby',679)}
<div style="position:absolute;left:80px;right:80px;top:980px;border-top:1px solid rgba(255,255,255,.28)"></div>
<div class="news it" style="position:absolute;left:80px;top:1010px;width:900px;font-size:40px;line-height:1.2;color:#CFCAC1">Write a morning a renter can picture.</div>
{foot('sdm', True, right='', bottom=80)}
''', bg='#0E0E0E')

# ---------- Tue Nov 17 IG/FB: people rent from people ----------
T['s-1117-people'] = S(f'''
<div class="photo" style="left:0;top:0;width:1080px;height:960px;{ph('keys','47% 40%','auto 112%')}"></div>
<div class="mono" style="position:absolute;right:80px;top:80px;font-size:24px;color:#0E0E0E;background:#FAFAF8;padding:8px 12px">Leasing teams</div>
<div class="mono" style="position:absolute;right:80px;top:900px;{STK};color:#FAFAF8;background:rgba(14,14,14,.6)">Stock photo</div>
<div class="bsd" style="position:absolute;left:76px;top:1000px;width:940px;font-size:124px;line-height:.9;font-weight:900;text-transform:uppercase;color:#0E0E0E;letter-spacing:-.005em">People rent<br>from people.</div>
<div class="news" style="position:absolute;left:80px;top:1250px;width:600px;font-size:34px;line-height:1.2;color:#3A3631">Put the team in the feed too.</div>
<div style="position:absolute;right:80px;top:1196px"><img src="{LG}socialdm-color.png" style="height:100px;display:block"></div>
''', bg='#FAFAF8')

# ---------- Wed Nov 18 IG/FB: myth | reality, vertical split red / black ----------
T['s-1118-myth-posts'] = S(f'''
<div style="position:absolute;left:0;top:0;width:580px;height:1350px;background:#D2321E"></div>
<div style="position:absolute;left:580px;top:0;width:500px;height:1350px;background:#0E0E0E"></div>
<div class="mono" style="position:absolute;left:80px;top:80px;font-size:30px;color:#FAFAF8">Myth</div>
<div class="mono" style="position:absolute;left:640px;top:80px;font-size:30px;color:#FF8A75">Reality, often</div>
<div class="anton" style="position:absolute;left:76px;bottom:230px;width:460px;font-size:150px;line-height:.92;color:#0E0E0E">Nobody reads Google posts.</div>
<div class="news" style="position:absolute;left:640px;top:178px;width:400px;font-size:50px;line-height:1.14;color:#FAFAF8;text-wrap:balance">Some renters scroll down to check whether anyone is minding the profile.</div>
<div class="news it" style="position:absolute;left:640px;top:900px;width:380px;font-size:36px;line-height:1.25;color:#CFCAC1">A recent, accurate post answers that at a glance.</div>
<div class="mono" style="position:absolute;left:80px;bottom:92px;width:440px;font-size:26px;line-height:1.4;color:#FAFAF8">Google profile</div>
<div style="position:absolute;left:640px;bottom:84px"><img src="{LG}locallift-white.png" style="height:60px;display:block"></div>
''', bg='#0E0E0E')

# ---------- Thu Nov 19 IG/FB: full bleed photo, soft white card ----------
items = ['The front door, as customers see it.', 'The team, faces included.', 'The space on a busy day.', 'Something from this month.']
T['s-1119-four-photos'] = S(f'''
<div class="photo" style="inset:0;{ph('cafe','56% 0%','auto 100%')}"></div>
<div class="mono" style="position:absolute;left:60px;top:60px;{STK};color:#FAFAF8;background:rgba(14,14,14,.6)">Stock photo</div>
<div style="position:absolute;left:60px;right:60px;bottom:60px;height:640px;background:#FAFAF8"></div>
<div class="mono red" style="position:absolute;left:110px;top:700px;font-size:24px">For agents and local businesses</div>
<div class="fra" style="position:absolute;left:110px;top:744px;width:860px;font-size:58px;line-height:1.02;font-weight:400;letter-spacing:-.02em;color:#0E0E0E">Four photos your Google profile may be missing.</div>
<div style="position:absolute;left:110px;right:110px;top:890px">
{''.join(f'<div style="border-top:{"3px solid #0E0E0E" if i==0 else "1px solid #DAD6CE"};padding:11px 0 12px;display:flex;gap:22px;align-items:baseline"><span class="mono" style="font-size:24px;color:#D2321E">0{i+1}</span><span class="news" style="font-size:34px;color:#0E0E0E">{t}</span></div>' for i,t in enumerate(items))}
</div>
<div style="position:absolute;right:110px;bottom:90px"><img src="{LG}socialdm-color.png" style="height:96px;display:block"></div>
''', bg='#FAFAF8')

# ---------- Fri Nov 20 IG/FB: stacked bands, daylight over golden hour ----------
T['s-1120-light'] = S(f'''
<div class="photo" style="left:0;top:0;width:1080px;height:470px;{ph('daylight','62% 22%','100% auto')}"></div>
<div style="position:absolute;left:0;top:470px;width:1080px;height:4px;background:#FAFAF8"></div>
<div class="photo" style="left:0;top:474px;width:1080px;height:470px;{ph('golden','50% 30%','100% auto')}"></div>
<div class="mono" style="position:absolute;left:60px;top:60px;font-size:24px;color:#0E0E0E;background:#FAFAF8;padding:8px 12px">Daylight</div>
<div class="mono" style="position:absolute;left:60px;top:534px;font-size:24px;color:#0E0E0E;background:#FAFAF8;padding:8px 12px">Golden hour</div>
<div style="position:absolute;left:0;top:944px;width:1080px;height:406px;background:#0E0E0E"></div>
<div class="ex" style="position:absolute;left:80px;top:984px">Example: two different buildings</div>
<div class="syne" style="position:absolute;left:80px;top:1046px;width:700px;font-size:72px;line-height:1.0;font-weight:700;letter-spacing:-.02em;color:#FAFAF8">Let the sun<br>set the schedule.</div>
<div style="position:absolute;right:80px;bottom:80px"><img src="{LG}socialdm-reversed.png" style="height:112px;display:block"></div>
''', bg='#0E0E0E')

# ---------- Sat Nov 21 IG/FB: magazine cover "The DM" ----------
T['s-1121-the-dm'] = S(f'''
<div class="photo" style="left:0;top:300px;width:1080px;height:1050px;{ph('dm','60% 40%','auto 100%')}"></div>
<div style="position:absolute;left:0;top:300px;width:1080px;height:1050px;background:linear-gradient(180deg,rgba(14,14,14,0) 28%,rgba(14,14,14,.88) 66%)"></div>
<div class="ital" style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:210px;line-height:1;color:#0E0E0E;letter-spacing:.06em">THE DM</div>
<div style="position:absolute;left:80px;right:80px;top:262px;display:flex;justify-content:space-between" class="mono"><span style="font-size:22px;color:#0E0E0E">Saturday issue</span><span style="font-size:22px;color:#D2321E">Inbox etiquette</span><span style="font-size:22px;color:#0E0E0E">Nov 2026</span></div>
<div class="bod" style="position:absolute;left:80px;top:910px;width:700px;font-size:96px;line-height:.98;color:#FAFAF8">Answer it<br>like a tour.</div>
<div class="news" style="position:absolute;left:80px;top:1125px;width:560px;font-size:32px;line-height:1.25;color:#E8E4DC">Use your name, answer the question and offer one next step.</div>
<div class="mono" style="position:absolute;right:80px;top:340px;{STK};color:#FAFAF8;background:rgba(14,14,14,.5)">Stock photo</div>
<div style="position:absolute;right:80px;bottom:70px"><img src="{LG}socialdm-reversed.png" style="height:112px;display:block"></div>
''', bg='#FAFAF8')

# ---------- Thu Nov 19 LinkedIn: shortlist, split photo right ----------
T['l-1119-shortlist'] = S(f'''
<div class="photo" style="left:540px;top:0;width:540px;height:1350px;{ph('tour','60% 50%','auto 100%')}"></div>
<div class="mono red" style="position:absolute;left:80px;top:80px;font-size:26px">Leasing</div>
<div class="news" style="position:absolute;left:80px;top:170px;width:440px;font-size:38px;line-height:1.15;color:#6B665E">The shortlist is<br>built online.</div>
<div class="bod" style="position:absolute;left:80px;top:330px;width:460px;font-size:64px;line-height:1.04;color:#0E0E0E">The decision<br>is usually<br>still made<br>in person.</div>
<div style="position:absolute;left:80px;width:380px;top:760px;border-top:3px solid #0E0E0E"></div>
<div class="news" style="position:absolute;left:80px;top:786px;width:400px;font-size:31px;line-height:1.3;color:#0E0E0E">A tour checks whether the place matches what the renter found online.</div>
<div class="mono" style="position:absolute;right:40px;bottom:40px;{STK};color:#FAFAF8;background:rgba(14,14,14,.55)">Stock photo</div>
{foot('sdm', False, right='', bottom=80, rightpx=620)}
''', bg='#FAFAF8')

# ---------- Wed Nov 18 LinkedIn swipe: running checklist system ----------
steps = [
 ('A Google profile<br>that tells the truth.', 'The opening date, where the leasing office is, and renderings labeled as renderings.'),
 ('Floor plans<br>with a next step.', 'Prices once they are set. Until then, a plain line on when they will be posted.'),
 ('A neighborhood page<br>written by a local.', 'What is close today, and what is still being built.'),
 ('A feed that<br>shows progress.', 'Real milestones and the team. Show first residents only with their OK.'),
 ('One easy way<br>to tour.', 'A hard hat tour, a model or a video walkthrough. Pick one and make it easy to find.'),
]
short = ['Google profile', 'Floor plans', 'Neighborhood page', 'Progress feed', 'One way to tour']

T['l-1118-swipe-1'] = S(f'''
<div class="mono" style="position:absolute;left:80px;top:80px;font-size:26px;color:#FF8A75">Lease up</div>
<div class="anton" style="position:absolute;left:74px;top:180px;width:940px;font-size:210px;line-height:.88;color:#FAFAF8">Before<br>the doors<br>open.</div>
<div style="position:absolute;left:80px;width:300px;top:780px;border-top:8px solid #D2321E"></div>
<div class="news it" style="position:absolute;left:80px;top:820px;width:820px;font-size:46px;line-height:1.18;color:#E8E4DC">Five things renters often look for online before a new community opens.</div>
<div class="mono" style="position:absolute;right:80px;top:80px;font-size:26px;color:#FAFAF8">Swipe &rarr;</div>
{foot('sdm', True, right='THESOCIALDM.COM', bottom=80)}
''', bg='#0E0E0E')

for i, (h, s) in enumerate(steps):
    last = (i == 4)
    rail = ''.join(
        f'<div style="display:flex;gap:16px;align-items:baseline;padding:10px 0;border-top:1px solid {"#DAD6CE" if not last else "rgba(255,255,255,.3)"}">'
        f'<span class="mono" style="font-size:26px;font-weight:500;color:{("#D2321E" if not last else "#0E0E0E") if j==i else ("#6B665E" if not last else "#FAFAF8")}">{"&#10003;" if j<i else f"0{j+1}"}</span>'
        f'<span class="arch" style="font-size:28px;font-weight:{700 if j==i else 500};color:{("#0E0E0E" if j==i else "#5F5A54") if not last else ("#0E0E0E" if j==i else "#FAFAF8")}">{t}</span></div>'
        for j, t in enumerate(short))
    bg = '#D2321E' if last else ('#FAFAF8' if i % 2 == 0 else '#E8E4DC')
    ink = '#FAFAF8' if last else '#0E0E0E'
    sub = '#FAFAF8' if last else '#3A3631'
    numc = '#0E0E0E' if last else '#D2321E'
    T[f'l-1118-swipe-{i+2}'] = S(f'''
<div class="mono" style="position:absolute;left:80px;top:80px;font-size:26px;color:{'#0E0E0E' if last else '#D2321E'}">Before the doors open</div>
<div class="bsd" style="position:absolute;right:80px;top:56px;font-size:150px;line-height:1;font-weight:900;color:{numc}">0{i+1}</div>
<div class="fra" style="position:absolute;left:80px;top:250px;width:940px;font-size:88px;line-height:1.02;font-weight:500;letter-spacing:-.02em;color:{ink}">{h}</div>
<div class="news" style="position:absolute;left:80px;top:470px;width:860px;font-size:42px;line-height:1.25;color:{sub}">{s}</div>
<div style="position:absolute;left:80px;width:520px;top:{700 if not last else 680}px">{rail}</div>
{'' if last else foot('sdm', False, right='', bottom=80)}
{'<div style="position:absolute;left:0;top:1080px;width:1080px;height:270px;background:#0E0E0E"></div><div style="position:absolute;left:80px;bottom:80px"><img src="'+LG+'socialdm-reversed.png" style="height:112px;display:block"></div><div class="url" style="position:absolute;right:80px;bottom:84px;color:#FAFAF8">THESOCIALDM.COM</div>' if last else ''}
''', bg=bg)

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
