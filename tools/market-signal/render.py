"""Render a Market Signal edition.
Usage: python3 render.py editions/2026-10-25.json
Writes to out/<slug>/: weekly-half-page.pdf/.png, linkedin.png, web.html, monthly.pdf/.png (if "monthly" present)."""
import asyncio, json, os, sys, re
from jinja2 import Environment, FileSystemLoader
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(HERE, 'templates')), autoescape=True)
CSS = open(os.path.join(HERE, 'templates', 'ms.css')).read()
DASH = re.compile('[–—]')

def check_dashes(obj, path=''):
    """Hard rule: no en or em dashes anywhere in copy."""
    if isinstance(obj, str):
        if DASH.search(obj): raise SystemExit(f'Dash found at {path}: {obj[:80]}')
    elif isinstance(obj, dict):
        for k, v in obj.items(): check_dashes(v, f'{path}.{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj): check_dashes(v, f'{path}[{i}]')

async def main(src):
    data = json.load(open(src)); check_dashes(data)
    e, m = data['edition'], data.get('monthly')
    out = os.path.join(HERE, 'out', data['slug']); os.makedirs(out, exist_ok=True)
    pages = {
        'weekly-half-page': ('weekly.html.j2', dict(e=e), (816, 528), True),
        'linkedin': ('linkedin.html.j2', dict(e=e), (1080, 1350), False),
        'web': ('web.html.j2', dict(e=e), None, False),
    }
    if m: pages['monthly'] = ('monthly.html.j2', dict(m=m), (816, 1056), True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, (tpl, ctx, size, pdf) in pages.items():
            html = env.get_template(tpl).render(css=CSS, webcss=re.sub(r'@font-face\{[^}]*\}\n?', '', CSS), **ctx)
            hp = os.path.join(out, f'{name}.html'); open(hp, 'w').write(html)
            if not size: continue
            pg = await b.new_page(viewport={'width': size[0], 'height': size[1]}, device_scale_factor=2)
            await pg.goto('file://' + hp); await pg.wait_for_timeout(300)
            # overflow guard: fail loudly instead of shipping clipped text
            over = await pg.evaluate('''() => [...document.querySelectorAll('body *')].filter(el => {
                const r = el.getBoundingClientRect(); return r.bottom > innerHeight + 1 || r.right > innerWidth + 1 ||
                el.scrollHeight > el.clientHeight + 2 && getComputedStyle(el).overflow === 'hidden' && el !== document.body }).map(el => el.className || el.tagName)''')
            if over: print(f'WARNING {name}: overflow in {over[:5]}')
            await pg.screenshot(path=os.path.join(out, f'{name}.png'))
            if pdf: await pg.pdf(path=os.path.join(out, f'{name}.pdf'), width=f'{size[0]}px', height=f'{size[1]}px', print_background=True)
            await pg.close()
        await b.close()
    print('rendered', out)

asyncio.run(main(sys.argv[1]))
