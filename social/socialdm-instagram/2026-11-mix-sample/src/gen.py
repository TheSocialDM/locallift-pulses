#!/usr/bin/env python3
"""SocialDM new post mix sample (Nov 2026): 3 photo, 3 proof, 3 insight tiles.
Writes t1..t9 html, renders 2x PNGs with Playwright, builds a feed preview."""
import pathlib, asyncio
from playwright.async_api import async_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
F = 'file:///mnt/skills/examples/canvas-design/canvas-fonts/'

BASE = f"""
@font-face{{font-family:LB;src:url('{F}LibreBaskerville-Regular.ttf')}}
@font-face{{font-family:IS;src:url('{F}InstrumentSans-Regular.ttf');font-weight:400}}
@font-face{{font-family:IS;src:url('{F}InstrumentSans-Bold.ttf');font-weight:700}}
@font-face{{font-family:DM;src:url('{F}DMMono-Regular.ttf')}}
:root{{--navy:#0D1B2A;--paper:#F7F5F0;--lime:#C8F169;--mute:#5B6675;--rule:#D9D5CC;--grey:#C9CDD3}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:IS,sans-serif;-webkit-font-smoothing:antialiased}}
.lb{{font-family:LB,serif;font-weight:400;letter-spacing:-.01em;font-feature-settings:'lnum'}}
.mono{{font-family:DM,monospace;font-feature-settings:'lnum'}}
.eyebrow{{font-size:21px;letter-spacing:.2em;font-weight:700;text-transform:uppercase}}
.foot{{position:absolute;left:72px;right:72px;bottom:58px;display:flex;justify-content:space-between;align-items:center;padding-top:24px;font-size:19px}}
.logos{{display:flex;align-items:center;gap:18px}}
.logos img{{height:40px}}
.div{{width:1px;height:34px}}
.ll{{display:inline-flex;align-items:center;gap:9px;font-weight:700;font-size:25px;letter-spacing:-.01em}}
.ll svg{{width:19px;height:25px}}
.photo{{position:absolute;inset:0;background-size:cover;background-position:center}}
"""
PIN = '<svg viewBox="0 0 24 32"><path d="M12 0C5.4 0 0 5.3 0 11.9 0 20.8 12 32 12 32s12-11.2 12-20.1C24 5.3 18.6 0 12 0z" fill="#E0312B"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></svg>'

def foot(dark, left=''):
    logo = 'sdm-white.png' if dark else 'sdm-dark.png'
    col = '#fff' if dark else 'var(--navy)'
    rule = 'rgba(255,255,255,.28)' if dark else 'var(--rule)'
    sub = 'rgba(255,255,255,.75)' if dark else 'var(--mute)'
    return (f'<div class="foot" style="border-top:1px solid {rule};color:{sub}">'
            f'<span>{left}</span><div class="logos"><img src="{logo}">'
            f'<span class="div" style="background:{rule}"></span>'
            f'<span class="ll" style="color:{col}">{PIN}LocalLift</span></div></div>')

def page(body, css=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{css}</style></head><body>{body}</body></html>'

T = {}

# 1 PHOTO: couple at home, short line, photo carries it
T['t1-photo-home'] = page(f"""
<div class="photo" style="background-image:url(p-couple.jpg);background-position:40% center"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,0) 45%,rgba(13,27,42,.82) 100%)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:190px;color:#fff">
 <div style="width:64px;height:4px;background:var(--lime);margin-bottom:30px"></div>
 <h1 class="lb" style="font-size:84px;line-height:1.08">Before the tour,<br>there's a search.</h1>
</div>
{foot(True,'thesocialdm.com')}""")

# 2 PROOF light: direction requests 145 to 573
T['t2-proof-directions'] = page(f"""
<div style="position:absolute;inset:0;background:#fff"></div>
<div style="position:absolute;top:96px;left:72px;right:72px;color:var(--navy)">
 <div class="eyebrow" style="color:var(--mute)">Client result, anonymized</div>
 <h1 class="lb" style="font-size:66px;line-height:1.12;margin-top:30px">Google direction requests at a 183 home lease up.</h1>
</div>
<div style="position:absolute;left:72px;right:72px;top:560px;display:flex;align-items:flex-end;gap:56px;height:470px">
 <div style="flex:1;text-align:center"><div class="mono" style="font-size:54px;color:var(--mute)">145</div>
  <div style="height:84px;background:var(--grey);margin-top:18px"></div>
  <div style="font-size:24px;margin-top:20px;color:var(--mute)">First month</div></div>
 <div style="flex:1;text-align:center"><div class="mono" style="font-size:96px;color:var(--navy)">573</div>
  <div style="height:330px;background:var(--navy);margin-top:18px"></div>
  <div style="font-size:24px;margin-top:20px;color:var(--navy);font-weight:700">September</div></div>
</div>
<div style="position:absolute;left:72px;right:72px;top:1100px;font-size:19px;color:var(--mute)">Outside Portland, OR. Google Business Profile data, March and September 2026.</div>
{foot(False,'Proof, not promises')}""")

# 3 INSIGHT dark: one idea, big type
T['t3-insight-question'] = page(f"""
<div style="position:absolute;inset:0;background:var(--navy)"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:var(--lime)">One idea</span></div>
<div style="position:absolute;left:72px;right:90px;top:330px;color:#fff">
 <h1 class="lb" style="font-size:96px;line-height:1.1">Renters don't read your brochure.</h1>
 <h2 class="lb" style="font-size:96px;line-height:1.1;color:rgba(255,255,255,.55);margin-top:28px">They ask a question.</h2>
</div>
{foot(True,'thesocialdm.com')}""")

# 4 PROOF dark: 38 of 96
dots = ''.join(f'<span style="width:34px;height:34px;border-radius:50%;background:{"var(--lime)" if i<38 else "rgba(255,255,255,.16)"}"></span>' for i in range(96))
T['t4-proof-ai'] = page(f"""
<div style="position:absolute;inset:0;background:var(--navy)"></div>
<div style="position:absolute;top:96px;left:72px;right:72px;color:#fff">
 <div class="eyebrow" style="color:rgba(255,255,255,.7)">Client result, anonymized</div>
 <div style="display:flex;align-items:baseline;gap:22px;margin-top:34px"><span class="mono" style="font-size:150px;line-height:1;color:var(--lime)">38</span><span class="lb" style="font-size:52px">of 96</span></div>
 <p class="lb" style="font-size:44px;line-height:1.25;margin-top:26px">renter questions to AI assistants named one lease up. The next closest: 14.</p>
</div>
<div style="position:absolute;left:72px;right:72px;top:720px;display:grid;grid-template-columns:repeat(16,34px);justify-content:space-between;row-gap:20px">{dots}</div>
<div style="position:absolute;left:72px;right:72px;top:1145px;font-size:19px;color:rgba(255,255,255,.65)">183 home lease up outside Portland, OR. Six communities tested Oct 18, 2026.</div>
{foot(True,'Proof, not promises')}""")

# 5 PHOTO: Sonoran desert, almost no text
T['t5-photo-desert'] = page(f"""
<div class="photo" style="background-image:url(p-desert.jpg);background-position:30% center"></div>
<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(13,27,42,.78) 0%,rgba(13,27,42,0) 40%)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:190px;color:#fff">
 <h1 class="lb" style="font-size:78px;line-height:1.1">Local isn't a keyword.<br>It's the whole game.</h1>
</div>
{foot(True,'Phoenix, AZ')}""")

# 6 INSIGHT light: a single line test
T['t6-insight-ai'] = page(f"""
<div style="position:absolute;inset:0;background:var(--paper)"></div>
<div style="position:absolute;top:96px;left:72px" class="eyebrow"><span style="color:var(--mute)">A simple test</span></div>
<div style="position:absolute;left:72px;right:72px;top:300px;color:var(--navy)">
 <h1 class="lb" style="font-size:92px;line-height:1.12">If AI can't answer it, renters can't find it.</h1>
 <div style="width:96px;height:6px;background:var(--navy);margin:64px 0 40px"></div>
 <p style="font-size:34px;line-height:1.45;color:var(--mute);max-width:820px">Pets. Parking. Commute. Price.<br>Is each answer on your website today?</p>
</div>
{foot(False,'thesocialdm.com')}""")

# 7 INSIGHT dark: one team diagram
nodes = ['Social','Google','Reviews','Website','AI search']
import math
ring = ''
for i,n in enumerate(nodes):
    a = -math.pi/2 + i*2*math.pi/len(nodes)
    x = 540 + 300*math.cos(a); y = 820 + 260*math.sin(a)
    ring += f'<line x1="540" y1="820" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(255,255,255,.3)" stroke-width="2"/>'
    ring += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="#fff"/><text x="{x:.0f}" y="{y+(48 if y>820 else -28):.0f}" fill="#fff" font-family="IS" font-size="32" text-anchor="middle">{n}</text>'
T['t7-insight-oneteam'] = page(f"""
<div style="position:absolute;inset:0;background:var(--navy)"></div>
<div style="position:absolute;top:96px;left:72px;right:72px;color:#fff">
 <div class="eyebrow" style="color:var(--lime)">How we work</div>
 <h1 class="lb" style="font-size:80px;line-height:1.1;margin-top:30px">One team.<br>Not five vendors.</h1>
</div>
<svg style="position:absolute;inset:0" width="1080" height="1350">{ring}<circle cx="540" cy="820" r="58" fill="var(--lime)"/><text x="540" y="830" font-family="IS" font-weight="700" font-size="26" text-anchor="middle" fill="#0D1B2A">One plan</text></svg>
{foot(True,'thesocialdm.com')}""")

# 8 PHOTO: neighborhood market
T['t8-photo-market'] = page(f"""
<div class="photo" style="background-image:url(p-market.jpg);background-position:40% center"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:420px;background:var(--paper)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:190px;color:var(--navy)">
 <h1 class="lb" style="font-size:70px;line-height:1.12">The neighborhood is an amenity. Post it like one.</h1>
</div>
{foot(False,'thesocialdm.com')}""")

# 9 PROOF light: reviews
T['t9-proof-reviews'] = page(f"""
<div style="position:absolute;inset:0;background:#fff"></div>
<div style="position:absolute;top:96px;left:72px;right:72px;color:var(--navy)">
 <div class="eyebrow" style="color:var(--mute)">Client result, anonymized</div>
</div>
<div style="position:absolute;left:72px;right:72px;top:250px;color:var(--navy)">
 <div class="lb" style="font-size:230px;line-height:1">4.8</div>
 <div style="font-size:30px;margin-top:16px;color:var(--mute)">Google rating, 33 reviews</div>
 <div style="height:1px;background:var(--rule);margin:64px 0"></div>
 <h1 class="lb" style="font-size:70px;line-height:1.14">Every review answered. Each one written for that review.</h1>
</div>
<div style="position:absolute;left:72px;right:72px;top:1130px;font-size:19px;color:var(--mute)">183 home lease up outside Portland, OR. As of October 2026.</div>
{foot(False,'Proof, not promises')}""")

ORDER = list(T)

async def main():
    for k,v in T.items(): (HERE/f'{k}.html').write_text(v)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=2)
        for k in ORDER:
            await pg.goto((HERE/f'{k}.html').as_uri()); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT/f'socialdm-{k}.png'))
        await b.close()
    from PIL import Image
    tw, th, gap = 360, 450, 3
    g = Image.new('RGB',(tw*3+gap*2, th*3+gap*2),'white')
    for i,k in enumerate(ORDER):
        im = Image.open(OUT/f'socialdm-{k}.png').convert('RGB').resize((tw,th), Image.LANCZOS)
        g.paste(im,((i%3)*(tw+gap),(i//3)*(th+gap)))
    g.save(OUT/'feed-preview.png')

asyncio.run(main())
