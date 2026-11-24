"""Lura print kit (review asks): door hanger, leasing desk card, move in and renewal cards.
QR codes point at moveinlocal.com/review/lura/ with a src tag per piece. Rendered with Chrome via Playwright.
Usage: python3 tools/lura_print.py"""
import os,io,base64,asyncio,segno
from playwright.async_api import async_playwright
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'));L=os.path.join(R,'live/lura-x5r9')
def qr(src):
    b=io.BytesIO();segno.make(f'https://moveinlocal.com/review/lura/?src={src}',error='m').save(b,kind='svg',dark='#0d2233',light='#fff',border=2,xmldecl=False,omitsize=True);return b.getvalue().decode()
def img(p): return 'data:image/'+('png' if p.endswith('png') else 'jpeg')+';base64,'+base64.b64encode(open(os.path.join(L,p),'rb').read()).decode()
CSS="""@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
*{box-sizing:border-box}html,body{margin:0}body{font-family:Poppins,sans-serif;color:#0d2233;background:#edf3f7}
.pg{width:var(--w);height:var(--h);overflow:hidden;position:relative;page-break-after:always;background:#edf3f7;text-align:center}
.top{background:#0d2233;padding:18px 0 10px}.top img{height:var(--lg)}
.ph{height:var(--ph);background:center/cover}.k{font-size:8.5px;letter-spacing:.22em;font-weight:600;color:#00608a;margin:16px 0 4px}
h1{font-size:var(--h1);line-height:1.12;font-weight:600;margin:0 18px 8px;letter-spacing:-.01em}p{font-size:8px;line-height:1.5;margin:0 22px;color:#2c3a45}
.q{width:var(--q);margin:12px auto 6px;background:#fff;border-radius:10px;padding:6px}.q svg{width:100%;height:auto;display:block}
.s{font-size:6.5px;color:#5f6b74}.rule{width:40px;height:1px;background:#8fd0ec;margin:12px auto}
.ln{position:absolute;bottom:26px;left:18px;right:18px;display:flex;gap:16px}.ln div{flex:1;border-top:.6px solid #5f6b74;font-size:6.5px;color:#5f6b74;text-align:left;padding-top:3px}"""
def page(w,h,inner,lg='46px',ph='70px',h1='19px',q='120px'): return f'<div class="pg" style="--w:{w}pt;--h:{h}pt;--lg:{lg};--ph:{ph};--h1:{h1};--q:{q}">{inner}</div>'
W=img('logo-white.png');PH=img('hero.jpg')
hanger=page(229.92,594,f'<div class="top" style="padding:26px 0 18px"><img src="{W}" alt=""></div><div class="ph" style="background-image:url({PH})"></div><div class="k">SERVICE COMPLETE</div><h1>Your work order<br>is done.</h1><p>We stopped by today and took care of your request.<br>Thank you for letting us in.</p><div class="rule"></div><h1 style="font-size:15px">How did we do?</h1><p>Scan to tell Google. It takes under 30 seconds.</p><div class="q" style="width:132px">{qr("hanger")}</div><div class="s">Point your phone camera at the code</div><div class="ln"><div>Completed by</div><div>Date</div></div>',lg='70px',ph='92px',h1='21px')
desk=page(270,378,f'<div class="top"><img src="{W}" alt=""></div><div class="k">LURA ON GOOGLE</div><h1>Tell us how<br>we are doing.</h1><p>Scan and tell Google. It takes under 30 seconds.</p><div class="q" style="width:150px">{qr("desk")}</div><div class="s">Thank you for being part of Lura</div>',lg='58px',h1='22px')
def card(k,h,b,src): return page(270,378,f'<div class="ph" style="height:96px;background-image:url({PH});position:relative"><img src="{W}" alt="" style="height:52px;margin-top:22px;filter:drop-shadow(0 1px 6px rgba(0,0,0,.5))"></div><div class="k">{k}</div><h1>{h}</h1><p>{b}</p><div class="q" style="width:118px">{qr(src)}</div><div class="s">Scan to review Lura on Google</div><div class="s" style="margin-top:8px">With thanks, the Lura team</div>',h1='20px')
mi=card('MOVE IN DAY','Welcome home.','We hope your first days at Lura feel easy. When you have 30 seconds, tell Google how your move in went.','card-movein')+card('RENEWAL','Thank you for staying.','Another lease at Lura means a lot to us. When you have 30 seconds, tell Google how living here has been.','card-renew')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=await b.new_page()
        for name,html,w,h in [('door-hanger-work-order.pdf',hanger,229.92,594),('leasing-desk-card.pdf',desk,270,378),('move-in-and-renewal-cards.pdf',mi,270,378)]:
            await pg.set_content(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}@page{{size:{w}pt {h}pt;margin:0}}</style></head><body>{html}</body></html>');await pg.wait_for_timeout(1200)
            await pg.pdf(path=os.path.join(L,'print',name),width=f'{w/72:.4f}in',height=f'{h/72:.4f}in',print_background=True)
        await b.close()
asyncio.run(main());print('ok')
