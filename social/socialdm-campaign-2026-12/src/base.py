"""SocialDM Dec 2026 fill: shared tokens, fonts, logos, footer. 1080x1350 social, rendered at 2x."""
import pathlib, asyncio, sys
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'out'; OUT.mkdir(exist_ok=True)
HTML = HERE / 'html'; HTML.mkdir(exist_ok=True)
FD = (HERE.parent / 'fonts' / 'w').as_uri() + '/'
PH = (HERE.parent / 'ph').as_uri() + '/'
LG = HERE.as_uri() + '/'

def ff(fam, file, w=400, st='normal'):
    return f"@font-face{{font-family:'{fam}';src:url('{FD}{file}') format('woff2');font-weight:{w};font-style:{st}}}"
faces = []
for w in (300, 400, 500, 600, 700, 900):
    faces += [ff('Fra', f'fraunces-latin-{w}-normal.woff2', w), ff('Fra', f'fraunces-latin-{w}-italic.woff2', w, 'italic')]
for w in (300, 400, 500, 600):
    faces += [ff('News', f'newsreader-latin-{w}-normal.woff2', w), ff('News', f'newsreader-latin-{w}-italic.woff2', w, 'italic')]
for w in (300, 500, 700, 800, 900): faces.append(ff('BSD', f'big-shoulders-display-latin-{w}-normal.woff2', w))
faces += [ff('Inst', 'instrument-serif-latin-400-normal.woff2'), ff('Inst', 'instrument-serif-latin-400-italic.woff2', 400, 'italic')]
for w in (400, 500): faces.append(ff('Mono', f'dm-mono-latin-{w}-normal.woff2', w))

BASE = ''.join(faces) + """
:root{--ink:#0E0E0E;--paper:#FAFAF8;--red:#D2321E;--warm:#E8E4DC;--mute:#5E5952;--line:#DAD6CE}
*{margin:0;padding:0;box-sizing:border-box}
body{position:relative;overflow:hidden;font-family:'IBM Plex Sans',sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
.fra{font-family:Fra,serif;font-variation-settings:'SOFT' 50,'WONK' 0}
.news{font-family:News,serif}
.pf{font-family:'Playfair Display',serif}
.ins{font-family:Inst,serif}
.anton{font-family:Anton,sans-serif;text-transform:uppercase}
.osw{font-family:Oswald,sans-serif;text-transform:uppercase}
.bsd{font-family:BSD,sans-serif;text-transform:uppercase}
.plex{font-family:'IBM Plex Sans',sans-serif}
.mono{font-family:Mono,monospace;font-weight:500;text-transform:uppercase;letter-spacing:.16em}
.it{font-style:italic}.red{color:var(--red)}
.abs{position:absolute}
.photo{position:absolute;background-size:cover;background-repeat:no-repeat}
.ex{display:inline-block;font-family:Mono,monospace;font-weight:500;font-size:22px;letter-spacing:.16em;text-transform:uppercase;padding:7px 12px;background:var(--red);color:#FAFAF8}
"""

def logo(brand, dark, h=None):
    if brand == 'sdm':
        f = 'socialdm-reversed.png' if dark else 'socialdm-color.png'; h = h or 104
    else:
        f = 'locallift-white.png' if dark else 'locallift-dark.png'; h = h or 56
    return f'<img src="{LG}{f}" style="height:{h}px;display:block">'

def foot(brand, dark, left=80, right=None, bottom=72, h=None):
    pos = f'left:{left}px' if right is None else f'right:{right}px'
    return f'<div class="abs" style="{pos};bottom:{bottom}px">{logo(brand, dark, h)}</div>'

def S(body, bg='#FAFAF8', css=''):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}'
            f'body{{width:1080px;height:1350px;background:{bg}}}{css}</style></head><body>{body}</body></html>')

def ph(name, pos='center', size='cover'):
    return f"background-image:url('{PH}{name}.jpg');background-position:{pos};background-size:{size}"

T = {}

async def render(only=None):
    from playwright.async_api import async_playwright
    from PIL import Image
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=2, viewport={'width': 1080, 'height': 1350})
        for name, html in T.items():
            if only and not any(o in name for o in only): continue
            f = HTML / f'{name}.html'; f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            png = OUT / f'{name}.png'
            await pg.screenshot(path=str(png))
            Image.open(png).convert('RGB').resize((1440, 1800), Image.LANCZOS).save(OUT / f'{name}.jpg', quality=92)
            png.unlink()
        await b.close()
