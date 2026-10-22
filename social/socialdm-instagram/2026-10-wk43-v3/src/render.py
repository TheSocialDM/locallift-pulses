import asyncio,os
from playwright.async_api import async_playwright
names={1:'2026-10-22-numbers',2:'2026-10-23-phoenix',3:'2026-10-24-this-or-that',4:'2026-10-25-sunday-check'}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for n,nm in names.items():
            await pg.goto('file://'+os.path.abspath(f'p{n}.html')); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f'../socialdm-ig-{nm}.png')
        await b.close()
asyncio.run(main())
