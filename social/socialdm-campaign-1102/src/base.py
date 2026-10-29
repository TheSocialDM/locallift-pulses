"""Shared system for the Nov 2 to 15 SocialDM / LocalLift campaign.
Built on the approved Round 4 generator (gen.py, Oct 28 2026): same tokens, logos, footer, margins.
Social and LinkedIn 1080x1350, Google posts 1200x900, rendered at 2x."""
import pathlib, asyncio, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'out'; OUT.mkdir(exist_ok=True)
HTML = HERE / 'html'; HTML.mkdir(exist_ok=True)
FD = (HERE / 'fonts').as_uri() + '/'
PH = (HERE / 'ph').as_uri() + '/'
LG = (HERE / 'logo').as_uri() + '/'

def ff(fam, file, w=400, st='normal'):
    return f"@font-face{{font-family:'{fam}';src:url('{FD}{file}') format('woff2');font-weight:{w};font-style:{st}}}"

faces = []
for w in (400, 500, 600, 700):
    faces += [ff('Bodoni', f'bodoni-moda-latin-{w}-normal.woff2', w), ff('Bodoni', f'bodoni-moda-latin-{w}-italic.woff2', w, 'italic')]
faces += [ff('Inst', 'instrument-serif-latin-400-normal.woff2'), ff('Inst', 'instrument-serif-latin-400-italic.woff2', 400, 'italic')]
for w in (500, 600, 700): faces.append(ff('Osw', f'oswald-latin-{w}-normal.woff2', w))
for w in (400, 500, 700): faces.append(ff('Sans', f'dm-sans-latin-{w}-normal.woff2', w))
for w in (400, 500): faces.append(ff('Mono', f'dm-mono-latin-{w}-normal.woff2', w))
for w in (300, 400, 600, 800, 900):
    faces += [ff('Fra', f'fraunces-latin-{w}-normal.woff2', w), ff('Fra', f'fraunces-latin-{w}-italic.woff2', w, 'italic')]
faces.append(ff('Anton', 'anton-latin-400-normal.woff2'))
for w in (500, 700, 800): faces.append(ff('Syne', f'syne-latin-{w}-normal.woff2', w))
for w in (300, 400, 500, 600):
    faces += [ff('News', f'newsreader-latin-{w}-normal.woff2', w), ff('News', f'newsreader-latin-{w}-italic.woff2', w, 'italic')]
for w in (300, 500, 800, 900): faces.append(ff('BSD', f'big-shoulders-display-latin-{w}-normal.woff2', w))
faces.append(ff('Ital', 'italiana-latin-400-normal.woff2'))
for w in (500, 700): faces.append(ff('Arch', f'archivo-narrow-latin-{w}-normal.woff2', w))

BASE = ''.join(faces) + """
:root{--ink:#0E0E0E;--paper:#FAFAF8;--red:#D2321E;--warm:#E8E4DC;--mute:#6B665E;--line:#DAD6CE;--dline:rgba(255,255,255,.22);--soft:#3A3631;--dsoft:#CFCAC1}
*{margin:0;padding:0;box-sizing:border-box}
body{position:relative;overflow:hidden;font-family:Sans,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-kerning:normal;font-feature-settings:'kern' 1,'lnum' 1}
.bod{font-family:Bodoni,serif;font-weight:500;letter-spacing:-.01em;font-feature-settings:'lnum' 1}
.ins{font-family:Inst,serif;font-weight:400;letter-spacing:-.01em}
.fra{font-family:Fra,serif;font-feature-settings:'lnum' 1;font-variation-settings:'SOFT' 50,'WONK' 0}
.news{font-family:News,serif;font-feature-settings:'lnum' 1}
.ital{font-family:Ital,serif;letter-spacing:.02em}
.anton{font-family:Anton,sans-serif;text-transform:uppercase;letter-spacing:.005em}
.osw{font-family:Osw,sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:-.005em}
.syne{font-family:Syne,sans-serif}
.bsd{font-family:BSD,sans-serif}
.arch{font-family:Arch,sans-serif}
.mono{font-family:Mono,monospace;font-weight:500;text-transform:uppercase;letter-spacing:.17em}
.it{font-style:italic}
.red{color:var(--red)}
.grad{background:linear-gradient(90deg,#E9531E 0%,#D4145A 60%,#A21F61 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.eye{position:absolute;left:80px;top:80px;font-size:28px}
.eyeR{position:absolute;right:80px;top:80px;font-size:28px}
.photo{position:absolute;background-size:cover;background-repeat:no-repeat}
.foot{position:absolute;left:80px;right:80px;bottom:80px;display:flex;justify-content:space-between;align-items:flex-end}
.url{font-family:Mono,monospace;font-weight:500;font-size:26px;letter-spacing:.17em;text-transform:uppercase}
.tag{display:inline-block;font-family:Mono,monospace;font-weight:500;font-size:24px;letter-spacing:.16em;text-transform:uppercase;padding:9px 14px}
.ex{display:inline-block;font-family:Mono,monospace;font-weight:500;font-size:22px;letter-spacing:.16em;text-transform:uppercase;padding:7px 12px;background:var(--red);color:#FAFAF8}
"""

def foot(brand, dark, right='THESOCIALDM.COM', left=80, rightpx=80, bottom=80, scale=1.0):
    """Approved footer: real SocialDM or LocalLift logo, consistent size and position."""
    c = '#FAFAF8' if dark else '#0E0E0E'
    if brand == 'sdm':
        f = 'socialdm-reversed.png' if dark else 'socialdm-color.png'
        logo = f'<img src="{LG}{f}" style="height:{int(112*scale)}px;display:block">'
    else:
        f = 'locallift-white.png' if dark else 'locallift-dark.png'
        logo = f'<img src="{LG}{f}" style="height:{int(60*scale)}px;display:block">'
    r = f'<span class="url" style="color:{c}">{right}</span>' if right else ''
    return f'<div class="foot" style="left:{left}px;right:{rightpx}px;bottom:{bottom}px">{logo}{r}</div>'

def page(body, w, h, bg, css=''):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}'
            f'body{{width:{w}px;height:{h}px;background:{bg}}}{css}</style></head><body>{body}</body></html>')

def S(body, bg='#FAFAF8', css=''): return page(body, 1080, 1350, bg, css)
def G(body, bg='#FAFAF8', css=''): return page(body, 1200, 900, bg, css)
def ph(name, pos='center', size='cover'): return f"background-image:url('{PH}{name}.jpg');background-position:{pos};background-size:{size}"

T = {}

async def render(only=None):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=2)
        n = 0
        for name, html in T.items():
            if only and not any(o in name for o in only): continue
            w, h = (1200, 900) if name.startswith('g-') else (1080, 1350)
            await pg.set_viewport_size({'width': w, 'height': h})
            f = HTML / f'{name}.html'; f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(120)
            await pg.screenshot(path=str(OUT / f'{name}.png')); n += 1
        await b.close()
    print('rendered', n)
