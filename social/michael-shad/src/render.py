import sys,asyncio
from playwright.sync_api import sync_playwright
import pathlib
names=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    for n in names:
        src,out=n.split('=')
        pg.goto('file://'+str(pathlib.Path(src).resolve())); pg.wait_for_timeout(600)
        pg.screenshot(path=out)
    b.close()
