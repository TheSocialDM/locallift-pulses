#!/usr/bin/env python3
"""SocialDM Oct 29 to Nov 11 2026 rebuild in the new feed mix.
Social tiles 1080x1350 (2x export), LinkedIn carousel slides 1080x1350,
Google post images 1200x900 (2x export), Google photo uploads (plain crops)."""
import pathlib, asyncio, math
from playwright.async_api import async_playwright
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / 'out'
OUT.mkdir(exist_ok=True)
F = 'file:///mnt/skills/examples/canvas-design/canvas-fonts/'

BASE = f"""
@font-face{{font-family:LB;src:url('{F}LibreBaskerville-Regular.ttf')}}
@font-face{{font-family:IS;src:url('{F}InstrumentSans-Regular.ttf');font-weight:400}}
@font-face{{font-family:IS;src:url('{F}InstrumentSans-Bold.ttf');font-weight:700}}
@font-face{{font-family:DM;src:url('{F}DMMono-Regular.ttf')}}
:root{{--navy:#0D1B2A;--paper:#F7F5F0;--lime:#C8F169;--mute:#5B6675;--rule:#D9D5CC;--grey:#C9CDD3}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{overflow:hidden;position:relative;font-family:IS,sans-serif;-webkit-font-smoothing:antialiased}}
.lb{{font-family:LB,serif;font-weight:400;letter-spacing:-.01em;font-feature-settings:'lnum'}}
.mono{{font-family:DM,monospace;font-feature-settings:'lnum'}}
.eyebrow{{font-size:21px;letter-spacing:.2em;font-weight:700;text-transform:uppercase}}
.foot{{position:absolute;left:72px;right:72px;bottom:58px;display:flex;justify-content:space-between;align-items:center;padding-top:24px;font-size:19px}}
.logos{{display:flex;align-items:center;gap:18px}}
.logos img{{height:40px}}
.div{{width:1px;height:34px}}
.ll{{display:inline-flex;align-items:center;gap:9px;font-weight:700;font-size:25px;letter-spacing:-.01em}}
.ll svg{{width:19px;height:25px}}
.photo{{position:absolute;background-size:cover;background-position:center}}
"""
PIN = '<svg viewBox="0 0 24 32"><path d="M12 0C5.4 0 0 5.3 0 11.9 0 20.8 12 32 12 32s12-11.2 12-20.1C24 5.3 18.6 0 12 0z" fill="#E0312B"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></svg>'

def foot(dark, left='thesocialdm.com', l=72, r=72, b=58):
    logo = 'sdm-white.png' if dark else 'sdm-dark.png'
    col = '#fff' if dark else 'var(--navy)'
    rule = 'rgba(255,255,255,.28)' if dark else 'var(--rule)'
    sub = 'rgba(255,255,255,.75)' if dark else 'var(--mute)'
    return (f'<div class="foot" style="left:{l}px;right:{r}px;bottom:{b}px;border-top:1px solid {rule};color:{sub}">'
            f'<span>{left}</span><div class="logos"><img src="{logo}">'
            f'<span class="div" style="background:{rule}"></span>'
            f'<span class="ll" style="color:{col}">{PIN}LocalLift</span></div></div>')

def page(body, w, h, css=''):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}'
            f'body{{width:{w}px;height:{h}px}}{css}</style></head><body>{body}</body></html>')

def S(body): return page(body, 1080, 1350)
def G(body): return page(body, 1200, 900)

T = {}   # name -> (html, w, h)

# ---------------- Social 4:5 tiles ----------------
# Oct 29 review poll, light insight
T['s-1029-review-poll'] = (S(f"""
<div style="position:absolute;inset:0;background:var(--paper)"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:var(--mute)">Settle this one</span></div>
<h1 class="lb" style="position:absolute;left:72px;right:72px;top:190px;font-size:76px;line-height:1.12;color:var(--navy)">Reply to every review, or only the tough ones?</h1>
<div style="position:absolute;left:72px;right:72px;top:640px;display:flex;flex-direction:column;gap:28px">
 <div style="display:flex;gap:30px;align-items:center;background:#fff;border:1px solid var(--rule);padding:34px 40px">
  <span class="lb" style="font-size:64px;color:var(--navy)">A</span><span style="font-size:34px;color:var(--navy)">Every review, five stars included</span></div>
 <div style="display:flex;gap:30px;align-items:center;background:#fff;border:1px solid var(--rule);padding:34px 40px">
  <span class="lb" style="font-size:64px;color:var(--navy)">B</span><span style="font-size:34px;color:var(--navy)">Only the tough ones</span></div>
</div>
<div style="position:absolute;left:72px;top:1080px;font-size:26px;color:var(--mute)">Vote in the comments.</div>
{foot(False)}"""), 1080, 1350)

# Oct 30 five states, photo
T['s-1030-five-states'] = (S(f"""
<div class="photo" style="inset:0;background-image:url(ph/19544002.jpg);background-position:center 45%"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(13,27,42,.92) 0%,rgba(13,27,42,.55) 32%,rgba(13,27,42,0) 58%)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:190px;color:#fff">
 <div style="width:64px;height:4px;background:var(--lime);margin-bottom:30px"></div>
 <div class="eyebrow" style="color:rgba(255,255,255,.8);margin-bottom:22px">Five states. One rule.</div>
 <h1 class="lb" style="font-size:84px;line-height:1.08">Write like<br>you live there.</h1>
</div>
{foot(True)}"""), 1080, 1350)

# Oct 31 Halloween, photo top + paper
T['s-1031-trick-treat'] = (S(f"""
<div class="photo" style="left:0;right:0;top:0;height:690px;background-image:url(ph/5845545.jpg);background-position:center 62%"></div>
<div style="position:absolute;left:0;right:0;top:690px;bottom:0;background:var(--paper)"></div>
<div style="position:absolute;left:72px;right:72px;top:750px;color:var(--navy)">
 <div class="eyebrow" style="color:var(--mute)">Trick or treat, apartment edition</div>
 <div style="display:flex;gap:48px;margin-top:34px">
  <div style="flex:1"><div class="lb" style="font-size:44px">Tricks</div>
   <p style="font-size:27px;line-height:1.5;color:var(--mute);margin-top:14px">A special that ended weeks ago. Photos from three summers ago.</p></div>
  <div style="width:1px;background:var(--rule)"></div>
  <div style="flex:1"><div class="lb" style="font-size:44px">Treats</div>
   <p style="font-size:27px;line-height:1.5;color:var(--mute);margin-top:14px">Today's special everywhere. A reply that actually says something.</p></div>
 </div>
</div>
{foot(False,'Happy Halloween')}"""), 1080, 1350)

# Nov 1 FAQ before and after, light insight
T['s-1101-faq'] = (S(f"""
<div style="position:absolute;inset:0;background:#fff"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:var(--mute)">Same question, two answers</span></div>
<h1 class="lb" style="position:absolute;left:72px;right:72px;top:180px;font-size:70px;line-height:1.12;color:var(--navy)">“Which utilities are included?”</h1>
<div style="position:absolute;left:72px;right:72px;top:470px">
 <div class="eyebrow" style="font-size:19px;color:var(--mute)">Before</div>
 <p class="lb" style="font-size:40px;line-height:1.3;color:#8A93A0;margin-top:16px;text-decoration:line-through;text-decoration-thickness:2px">Please contact the leasing office for details.</p>
 <div style="height:1px;background:var(--rule);margin:52px 0"></div>
 <div class="eyebrow" style="font-size:19px;color:var(--navy)">After</div>
 <p class="lb" style="font-size:40px;line-height:1.3;color:var(--navy);margin-top:16px">Water, sewer and trash are one flat monthly fee. Electric and internet go in your name.</p>
</div>
{foot(False)}"""), 1080, 1350)

# Nov 11 proof, dark
T['s-1111-proof-search'] = (S(f"""
<div style="position:absolute;inset:0;background:var(--navy)"></div>
<div style="position:absolute;top:96px;left:72px;right:72px;color:#fff">
 <div class="eyebrow" style="color:rgba(255,255,255,.7)">Client result, anonymized</div>
 <h1 class="lb" style="font-size:60px;line-height:1.15;margin-top:30px">How often a new lease up appeared in Google search and maps.</h1>
</div>
<div style="position:absolute;left:72px;right:72px;top:560px;display:flex;align-items:flex-end;gap:56px;height:470px">
 <div style="flex:1;text-align:center"><div style="font-size:22px;color:rgba(255,255,255,.6);letter-spacing:.14em">ABOUT</div><div class="lb" style="font-size:72px;color:rgba(255,255,255,.75)">970</div>
  <div style="height:105px;background:rgba(255,255,255,.22);margin-top:18px"></div>
  <div style="font-size:24px;margin-top:20px;color:rgba(255,255,255,.7)">March</div></div>
 <div style="flex:1;text-align:center"><div style="font-size:22px;color:rgba(255,255,255,.6);letter-spacing:.14em">ABOUT</div><div class="lb" style="font-size:104px;color:var(--lime)">2,900</div>
  <div style="height:315px;background:var(--lime);margin-top:18px"></div>
  <div style="font-size:24px;margin-top:20px;color:#fff;font-weight:700">September</div></div>
</div>
<div style="position:absolute;left:72px;right:72px;top:1120px;font-size:19px;color:rgba(255,255,255,.65)">183 home lease up outside Portland, OR. Opened March 2026.</div>
{foot(True,'Proof, not promises')}"""), 1080, 1350)

# LinkedIn Oct 31 Halloween, dark
T['li-1031-scary-phrases'] = (S(f"""
<div style="position:absolute;inset:0;background:var(--navy)"></div>
<div class="photo" style="left:0;right:0;top:0;height:420px;background-image:url(ph/5859427.jpg);background-position:center 55%"></div>
<div style="position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(0deg,var(--navy) 0%,rgba(13,27,42,0) 60%)"></div>
<div style="position:absolute;left:72px;right:72px;top:440px;color:#fff">
 <h1 class="lb" style="font-size:62px;line-height:1.12">Forget ghosts. These phrases should make an owner nervous.</h1>
 <div style="margin-top:44px;display:flex;flex-direction:column;gap:22px;font-size:31px">
  <div style="border-left:3px solid var(--lime);padding-left:24px">“Engagement is up.”</div>
  <div style="border-left:3px solid var(--lime);padding-left:24px">“We're optimizing.”</div>
  <div style="border-left:3px solid var(--lime);padding-left:24px">“It's the algorithm.”</div>
  <div style="border-left:3px solid var(--lime);padding-left:24px">“Results may vary.”</div>
 </div>
</div>
{foot(True,'Happy Halloween')}"""), 1080, 1350)

# LinkedIn Oct 29 carousel, 6 slides
car = [
 ('li-1029-report-1', 'cover', None),
 ('li-1029-report-2', 'q', ('01', 'What changed since last week?', 'Not a snapshot. The difference between this week and last is where the story is.', False)),
 ('li-1029-report-3', 'q', ('02', 'Who moved on price or specials?', 'New concessions nearby can change a week faster than a monthly report can catch.', True)),
 ('li-1029-report-4', 'q', ('03', 'Is our listing still right?', 'Special, hours, price and photos, checked against your own website, not assumed.', False)),
 ('li-1029-report-5', 'q', ('04', 'What is the one thing to do?', 'A report that ends without a next step is just a longer way of saying nothing changed.', True)),
 ('li-1029-report-6', 'end', None),
]
for i,(name,kind,d) in enumerate(car):
    num = f'{i+1:02d} / 06'
    if kind=='cover':
        body = f"""
<div class="photo" style="inset:0;background-image:url(ph/17724744.jpg);background-position:38% center"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(13,27,42,.95) 0%,rgba(13,27,42,.6) 38%,rgba(13,27,42,.1) 70%)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:200px;color:#fff">
 <div class="eyebrow" style="color:var(--lime);margin-bottom:26px">The weekly report</div>
 <h1 class="lb" style="font-size:86px;line-height:1.08">Four questions a weekly report should answer.</h1>
 <div style="margin-top:34px;font-size:26px;color:rgba(255,255,255,.8)">Swipe</div>
</div>
{foot(True,num)}"""
    elif kind=='q':
        n,q,sub,dark = d
        bg = 'var(--navy)' if dark else 'var(--paper)'; fg = '#fff' if dark else 'var(--navy)'; mu = 'rgba(255,255,255,.7)' if dark else 'var(--mute)'
        body = f"""
<div style="position:absolute;inset:0;background:{bg}"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:{mu}">The weekly report</span></div>
<div class="lb" style="position:absolute;left:66px;top:200px;font-size:200px;line-height:1;color:{'var(--lime)' if dark else 'var(--navy)'}">{n}</div>
<div style="position:absolute;left:72px;right:72px;top:520px;color:{fg}">
 <h1 class="lb" style="font-size:80px;line-height:1.1">{q}</h1>
 <p style="font-size:32px;line-height:1.5;color:{mu};margin-top:44px">{sub}</p>
</div>
{foot(dark,num)}"""
    else:
        items = ['What changed since last week','Who moved on price or specials','Whether your listing is still right','The one thing to do next']
        rows = ''.join(f'<div style="display:flex;gap:24px;align-items:baseline;padding:26px 0;border-top:1px solid var(--rule)"><span class="lb" style="font-size:28px;color:var(--mute)">0{j+1}</span><span style="font-size:34px">{t}</span></div>' for j,t in enumerate(items))
        body = f"""
<div style="position:absolute;inset:0;background:#fff"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:var(--mute)">Every week</span></div>
<div style="position:absolute;left:72px;right:72px;top:200px;color:var(--navy)">
 <h1 class="lb" style="font-size:70px;line-height:1.12">What our weekly reports are built to answer.</h1>
 <div style="margin-top:64px">{rows}</div>
</div>
{foot(False,num)}"""
    T[name] = (S(body), 1080, 1350)

# ---------------- Google post images 4:3 ----------------
def g_panel(photo, pos, eyebrow, head, dark=False):
    bg = 'var(--navy)' if dark else 'var(--paper)'; fg = '#fff' if dark else 'var(--navy)'; mu = 'rgba(255,255,255,.72)' if dark else 'var(--mute)'
    return G(f"""
<div class="photo" style="left:0;top:0;bottom:0;width:690px;background-image:url(ph/{photo}.jpg);background-position:{pos}"></div>
<div style="position:absolute;left:690px;right:0;top:0;bottom:0;background:{bg}"></div>
<div style="position:absolute;left:740px;right:96px;top:84px;color:{fg}">
 <div class="eyebrow" style="font-size:16px;color:{mu}">{eyebrow}</div>
 <h1 class="lb" style="font-size:44px;line-height:1.16;margin-top:26px">{head}</h1>
</div>
{foot(dark,'',l=740,r=96,b=76)}""")

def g_full(photo, pos, eyebrow, head):
    return G(f"""
<div class="photo" style="inset:0;background-image:url(ph/{photo}.jpg);background-position:{pos}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(13,27,42,.92) 0%,rgba(13,27,42,.55) 34%,rgba(13,27,42,0) 62%)"></div>
<div style="position:absolute;left:96px;right:96px;bottom:176px;color:#fff">
 <div style="width:56px;height:4px;background:var(--lime);margin-bottom:22px"></div>
 <div class="eyebrow" style="font-size:16px;color:rgba(255,255,255,.8);margin-bottom:16px">{eyebrow}</div>
 <h1 class="lb" style="font-size:54px;line-height:1.1">{head}</h1>
</div>
{foot(True,'thesocialdm.com',l=96,r=96,b=76)}""")

GP = [
 ('g-1029', 'panel', '4049870', 'center 30%', 'AI search', 'AI reads your website before many renters do.', False),
 ('g-1030', 'full', '31528818', 'center 55%', 'Google Maps', 'Your listing should look as fresh as the street.', None),
 ('g-1031', 'panel', '3142467', 'center 60%', 'Happy Halloween', 'The front step is now a search result.', True),
 ('g-1101', 'full', '31418279', 'center 60%', 'The 2026 report', 'Being online is not the same as being found.', None),
 ('g-1102', 'panel', '34490278', 'center 60%', 'Apartment SEO', 'Good SEO is a steady drive, not a teleport.', False),
 ('g-1103', 'full', '5748631', '60% 40%', 'Local search', 'Renters search neighborhoods, not apartments.', None),
 ('g-1104', 'panel', '5332214', 'center 35%', 'Research', 'The short list gets made online.', True),
 ('g-1105', 'full', '32189195', 'center 45%', 'Choosing an agency', 'See the fruit before you pay for it.', None),
 ('g-1106', 'panel', '4339952', '60% center', 'LocalLift', 'Visibility a community owns, not rents.', False),
 ('g-1107', 'full', '3764173', '62% 35%', 'Reviews', 'The next renter reads your reply.', None),
 ('g-1108', 'panel', '28584802', 'center 50%', 'The weekly check', 'Special, hours, price, reviews. Every week.', True),
 ('g-1109', 'full', '7647206', 'center 30%', 'Lease ups', 'A new community starts with no search history.', None),
 ('g-1110', 'panel', '7710077', '100% 30%', 'One team', 'One plan across every channel.', False),
 ('g-1111', 'full', '27307398', 'center 40%', 'Apartment SEO', 'Write the page a renter wishes existed.', None),
]
for name, kind, ph, pos, eb, head, dark in GP:
    T[name] = ((g_panel(ph,pos,eb,head,dark) if kind=='panel' else g_full(ph,pos,eb,head)), 1200, 900)

# Google photo uploads (no text): 4:3 crops, 2400x1800
GPHOTO = {'gp-1107':('17411447',0.5), 'gp-1108':('27302669',0.2), 'gp-1109':('28586739',0.35), 'gp-1110':('14617456',0.5), 'gp-1111':('18072674',0.5)}

def crop43(src, dst, cy, xfrac=None, bright=None):
    im = Image.open(src).convert('RGB'); w,h = im.size
    if xfrac is not None:
        nw=int(w*xfrac); im=im.crop((0,0,nw,h)); w=nw
    if bright:
        from PIL import ImageEnhance
        im=ImageEnhance.Brightness(im).enhance(bright)
    if w/h > 4/3:
        nw = int(h*4/3); x = (w-nw)//2; im = im.crop((x,0,x+nw,h))
    else:
        nh = int(w*3/4); y = int((h-nh)*cy); im = im.crop((0,y,w,y+nh))
    im = im.resize((2400,1800), Image.LANCZOS); im.save(dst, quality=90)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name,(html,w,h) in T.items():
            f = HERE/f'{name}.html'; f.write_text(html)
            pg = await b.new_page(viewport={'width':w,'height':h}, device_scale_factor=2)
            await pg.goto(f.as_uri()); await pg.wait_for_timeout(350)
            await pg.screenshot(path=str(OUT/f'socialdm-{name}.png')); await pg.close()
        await b.close()
    EXTRA={'gp-1107':dict(xfrac=0.82),'gp-1108':dict(bright=1.35)}
    for k,(ph,cy) in GPHOTO.items():
        crop43(HERE/'ph'/f'{ph}.jpg', OUT/f'socialdm-{k}.jpg', cy, **EXTRA.get(k,{}))
    # contact sheets
    def sheet(names, tw, th, cols, out):
        rows = (len(names)+cols-1)//cols
        g = Image.new('RGB',(cols*tw+(cols-1)*6, rows*th+(rows-1)*6),'white')
        for i,n in enumerate(names):
            im = Image.open(n).convert('RGB').resize((tw,th), Image.LANCZOS)
            g.paste(im,((i%cols)*(tw+6),(i//cols)*(th+6)))
        g.save(out)
    soc = [OUT/f'socialdm-{n}.png' for n in T if n.startswith(('s-','li-'))]
    goo = [OUT/f'socialdm-{n}.png' for n in T if n.startswith('g-')] + [OUT/f'socialdm-{k}.jpg' for k in GPHOTO]
    sheet(soc, 360, 450, 4, HERE.parent/'sheet-social.png')
    sheet(goo, 400, 300, 4, HERE.parent/'sheet-google.png')

asyncio.run(main())
