"""Render only the monthly one page PDF of an edition JSON: python3 render_monthly.py editions/<date>.json"""
import asyncio, json, os, sys, re
from jinja2 import Environment, FileSystemLoader
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(os.path.join(HERE,'templates')),autoescape=True)
CSS=open(os.path.join(HERE,'templates','ms.css')).read()
async def main(src):
    d=json.load(open(src)); m=d['monthly']
    for v in json.dumps(m, ensure_ascii=False).split('"'):
        if re.search('[–—]',v): raise SystemExit('dash: '+v)
    out=os.path.join(HERE,'out',d['slug']); os.makedirs(out,exist_ok=True)
    html=env.get_template('monthly.html.j2').render(css=CSS,m=m,logo=os.path.join(HERE,'templates','michael','sdm-dark.png'))
    hp=os.path.join(out,'monthly.html'); open(hp,'w').write(html)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':816,'height':1056},device_scale_factor=2)
        await pg.goto('file://'+hp); await pg.wait_for_timeout(400)
        over=await pg.evaluate('''()=>[...document.querySelectorAll('body *')].filter(el=>{const r=el.getBoundingClientRect();return r.bottom>innerHeight+1||r.right>innerWidth+1}).map(el=>el.className||el.tagName)''')
        if over: print('WARNING overflow',over[:5])
        await pg.screenshot(path=os.path.join(out,'monthly.png'))
        await pg.pdf(path=os.path.join(out,'monthly.pdf'),width='816px',height='1056px',print_background=True)
        await b.close()
    print('rendered',out)
asyncio.run(main(sys.argv[1]))
