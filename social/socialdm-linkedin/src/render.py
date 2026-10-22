import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for n in range(1,7):
            import os; await pg.goto('file://'+os.path.abspath(f's{n}.html')); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f'../socialdm-li-2026-10-25-sunday-check-{n}.png')
        await b.close()
asyncio.run(main())
