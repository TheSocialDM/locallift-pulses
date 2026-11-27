import asyncio, base64, os, sys
from playwright.async_api import async_playwright

K = '/home/claude/kit'
V = '/home/claude/vr'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
def font(name, path, w, style='normal'):
    return f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,{b64(path)}) format('woff2');font-weight:{w};font-style:{style}}}"
FONTS = ''.join([
    font('IS', f'{K}/fontsource-instrument-serif/files/instrument-serif-latin-400-normal.woff2', 400),
    font('IS', f'{K}/fontsource-instrument-serif/files/instrument-serif-latin-400-italic.woff2', 400, 'italic'),
    font('MR', f'{K}/fontsource-manrope/files/manrope-latin-600-normal.woff2', 600),
    font('MR', f'{K}/fontsource-manrope/files/manrope-latin-700-normal.woff2', 700),
    font('MR', f'{K}/fontsource-manrope/files/manrope-latin-800-normal.woff2', 800),
    font('IT', f'{K}/fontsource-inter-tight/files/inter-tight-latin-400-normal.woff2', 400),
    font('IT', f'{K}/fontsource-inter-tight/files/inter-tight-latin-500-normal.woff2', 500),
])
LD = 'data:image/png;base64,' + b64(f'{V}/logo_dark.png')
LL = 'data:image/png;base64,' + b64(f'{V}/logo_light.png')
def ph(i): return 'data:image/jpeg;base64,' + b64(f'{V}/big_{i}.jpg')

BASE = """*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:IT}
.eb{font-family:MR;font-weight:800;letter-spacing:.32em;font-size:22px;text-transform:uppercase}
.h{font-family:IS;font-weight:400;line-height:.95;letter-spacing:-.01em}
.h i{font-style:italic}
.p{font-family:IT;font-size:29px;line-height:1.45}
.url{font-family:MR;font-weight:700;letter-spacing:.24em;font-size:20px}
.logo{height:92px}
"""
INK='#121110'; PAPER='#F4EFE6'; GOLD='#B39257'; RED='#B23A2E'

def A(d):  # photo top, paper bottom
    return f"""<div style="height:1350px;background:{PAPER};position:relative">
<div style="height:{d.get('ph',700)}px;background:url({ph(d['img'])}) center {d.get('pos','50%')}/cover"></div>
<div style="padding:62px 72px 0">
<div class=eb style="color:{RED}">{d['eb']}</div>
<div class=h style="font-size:{d.get('fs',112)}px;color:{INK};margin-top:28px">{d['h']}</div>
<div class=p style="color:#2a2725;margin-top:30px;max-width:900px">{d.get('p','')}</div></div>
<img class=logo src={LD} style="position:absolute;left:68px;bottom:48px">
<div class=url style="position:absolute;right:72px;bottom:66px;color:{INK}">LOCALLIFTSIGNATURE.COM</div></div>"""

def B(d):  # full bleed, dark gradient
    return f"""<div style="height:1350px;position:relative;background:url({ph(d['img'])}) {d.get('pos','center')}/cover">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.15) 0%,rgba(18,17,16,.05) 35%,rgba(18,17,16,.86) 60%,rgba(18,17,16,.95) 100%)"></div>
<div style="position:absolute;left:72px;right:72px;bottom:190px">
<div class=eb style="color:#E6D3A8;text-shadow:0 1px 8px rgba(0,0,0,.6)">{d['eb']}</div>
<div class=h style="font-size:{d.get('fs',128)}px;color:{PAPER};margin-top:26px">{d['h']}</div>
<div class=p style="color:#e8e2d8;margin-top:28px;max-width:860px">{d.get('p','')}</div></div>
<img class=logo src={LL} style="position:absolute;left:68px;bottom:48px">
{'' if d.get('nourl') else '<div class=url style="position:absolute;right:72px;bottom:66px;color:'+PAPER+'">LOCALLIFTSIGNATURE.COM</div>'}</div>"""

def C(d):  # ink background, framed photo
    return f"""<div style="height:1350px;background:{INK};position:relative">
<div style="position:absolute;right:0;top:0;width:660px;height:760px;background:url({ph(d['img'])}) {d.get('pos','center')}/cover"></div>
<div style="position:absolute;left:72px;top:96px;width:300px;border-top:3px solid {GOLD}"></div>
<div class=eb style="position:absolute;left:72px;top:126px;width:330px;color:{GOLD};line-height:1.6">{d['eb']}</div>
<div style="position:absolute;left:72px;right:72px;top:{d.get('top',800)}px">
<div class=h style="font-size:{d.get('fs',118)}px;color:{PAPER}">{d['h']}</div>
<div class=p style="color:#cfc8bc;margin-top:30px;max-width:880px">{d.get('p','')}</div></div>
<img class=logo src={LL} style="position:absolute;left:68px;bottom:48px">
<div class=url style="position:absolute;right:72px;bottom:66px;color:{PAPER}">LOCALLIFTSIGNATURE.COM</div></div>"""

def D(d):  # paper, type led, photo strip bottom, optional card
    card = d.get('card', '')
    return f"""<div style="height:1350px;background:{PAPER};position:relative">
<div style="padding:92px 72px 0">
<div class=eb style="color:{RED}">{d['eb']}</div>
<div class=h style="font-size:{d.get('fs',120)}px;color:{INK};margin-top:30px">{d['h']}</div>
{card}</div>
<div style="position:absolute;left:0;right:0;bottom:170px;height:{d.get('ph',380)}px;background:url({ph(d['img'])}) {d.get('pos','center')}/cover"></div>
<img class=logo src={LD} style="position:absolute;left:68px;bottom:48px">
<div class=url style="position:absolute;right:72px;bottom:66px;color:{INK}">LOCALLIFTSIGNATURE.COM</div></div>"""

def E(d):
    return f"""<div style="height:1350px;background:{PAPER};position:relative;text-align:center">
<div style="position:absolute;left:90px;right:90px;top:90px;bottom:200px;border:2px solid {GOLD}"></div>
<div style="position:absolute;left:0;right:0;top:380px">
<div class=eb style="color:{RED}">{d['eb']}</div>
<div class=h style="font-size:190px;color:{INK};margin-top:50px">{d['h']}</div>
<div style="width:120px;border-top:3px solid {GOLD};margin:56px auto 0"></div>
<div class=p style="color:#2a2725;margin:44px auto 0;max-width:720px;font-size:32px">{d['p']}</div></div>
<img class=logo src={LD} style="position:absolute;left:68px;bottom:48px">
<div class=url style="position:absolute;right:72px;bottom:66px;color:{INK}">LOCALLIFTSIGNATURE.COM</div></div>"""

def ex_card(lines, tag='EXAMPLE, NOT A REAL AGENT'):
    rows = ''.join(f"<div style='display:flex;gap:26px;margin-top:22px'><div class=eb style='font-size:18px;color:{GOLD};width:120px;padding-top:8px'>{a}</div><div style='font-family:IT;font-size:30px;line-height:1.35;color:{INK};flex:1'>{b}</div></div>" for a, b in lines)
    return f"<div style='margin-top:48px;border:2px solid {INK};padding:30px 36px 34px;background:#fbf8f2'><div class=eb style='font-size:16px;color:#7b746a'>{tag}</div>{rows}</div>"

def num_list(items):
    rows = ''.join(f"<div style='display:flex;gap:28px;align-items:baseline;margin-top:20px'><div class=h style='font-size:64px;color:{GOLD};width:80px'>{n}</div><div style='font-family:IT;font-size:32px;color:{INK}'>{t}</div></div>" for n, t in items)
    return f"<div style='margin-top:40px'>{rows}</div>"

POSTS = {
 '2026-11-15': (B, dict(img=851555, eb='Sunday', h='One unhurried hour.<br><i>Before the phone.</i>', p='Your week will still be there when you get to it.')),
 '2026-11-16': (D, dict(img=4050315, eb='LinkedIn', fs=104, h='Read your headline<br><i>like a stranger would.</i>', ph=300,
     card=ex_card([('Before', 'Realtor with [Brokerage] | Phoenix'), ('After', 'Helping Central Phoenix homeowners sell and buy in the same move | Realtor with [Brokerage]')]))),
 '2026-11-17': (A, dict(img=4506270, eb='Closing day', pos='40%', h='Ask on closing day.<br><i>While the boxes<br>are still taped.</i>', fs=96, ph=640, p='The details your client remembers today are the ones that help the next person decide to call you.')),
 '2026-11-18': (C, dict(img=5797903, eb='Local expertise', top=770, h='Listings live everywhere.<br><i>Your answers<br>live with you.</i>', fs=100, p='One clear local answer a week shows people how you think before they ever call.')),
 '2026-11-19': (D, dict(img=6347720, eb='The 15 minute habit', fs=118, ph=330, h='Fifteen minutes<br><i>of real conversation.</i>',
     card=num_list([('01', "A real comment on a past client's post"), ('02', "Something useful on a local partner's post"), ('03', 'A note to someone you just met')]))),
 '2026-11-20': (B, dict(img=2774556, eb='Title reps', fs=112, h='The event is the introduction.<br><i>The week after is the relationship.</i>')),
 '2026-11-21': (A, dict(img=1591447, eb='Weekend', pos='60%', h='A weekend walk<br><i>counts as research.</i>', p='Late November light is lovely for photos of the parks and quiet corners you love.')),
 '2026-11-22': (C, dict(img=1395967, eb='The holiday table', h='&ldquo;Is it a good time to buy?&rdquo;<br><i>Have a kind answer ready.</i>', fs=96, p='Then go back to the pie.')),
 '2026-11-23': (D, dict(img=4065876, eb='Google Business Profile', fs=130, ph=420, h='Closed Thursday?<br><i>Tell Google first.</i>',
     card=f"<div class=p style='color:#2a2725;margin-top:34px;max-width:880px'>Holiday hours take a couple of minutes, and they keep a client from driving to a locked door.</div>")),
 '2026-11-24': (B, dict(img=8293778, eb='Past clients', fs=112, h='Your best December list<br><i>is the one you already have.</i>', p='A short note only you could write. No market update, no ask.')),
 '2026-11-25': (C, dict(img=3184465, pos='30% center', eb='LocalLift Signature<br>$199 a month', fs=100, top=790, h='You sell homes.<br><i>We handle the visibility.</i>', p='12 local topics a month, made for Instagram, Facebook, LinkedIn and Google Business Profile.')),
 '2026-11-26': (E, dict(eb='Happy Thanksgiving', h='<i>Thank you.</i>', p='To every agent and title rep who trusted us with their name and their market this year.')),
 '2026-11-27': (C, dict(img=5668471, eb='Quiet Friday<br>homework', fs=110, h='Search yourself<br><i>like a buyer would.</i>', p='Ask Google for the best agent in your neighborhood and read the AI answer at the top, if one shows up.')),
 '2026-11-28': (A, dict(img=19418844, eb='Small Business Saturday', fs=104, h='Shop the places<br><i>you would recommend.</i>', p='The coffee counter, the hardware store, the bookshop with the good window.')),
 '2026-11-29': (B, dict(img=9969158, pos='center 25%', eb='Sunday', h='December can wait<br><i>until tomorrow.</i>', p='One slow afternoon first.')),
 '2026-11-30': (D, dict(img=8850629, eb='Google Business Profile', fs=110, ph=420, pos='center 40%', h='Your description<br><i>is not a bio.</i>',
     card=ex_card([('Before', 'Dedicated Realtor committed to excellence.'), ('After', 'I help families buy and sell in Old Town and the east side, especially first homes and downsizing moves.')]))),
 '2026-12-01': (C, dict(img=6995221, pos='center', eb='Giving Tuesday', fs=130, h='Give where<br><i>you live.</i>', p='Share a local cause you support so others can find it too.')),
 '2026-12-02': (D, dict(img=6787048, eb='Google reviews', fs=112, ph=360, pos='center 45%', h='Reply to every review.<br><i>Strangers are reading.</i>',
     card=ex_card([('Review', '&ldquo;She made my first purchase feel calm.&rdquo;'), ('Reply', '&ldquo;Thank you, Dana. Watching you get the keys to the bungalow on Maple was the best part of my October.&rdquo;')], tag='EXAMPLE, NOT A REAL REVIEW'))),
 '2026-12-03': (A, dict(img=712321, eb='Listing in December', pos='55%', fs=104, ph=680, h='Decorate for the photos,<br><i>not the party.</i>', p='One or two pieces per room, clear counters, and every light on before the photographer arrives.')),
 '2026-12-04': (B, dict(img=6054110, pos='center', nourl=1, eb='Begins tonight at sundown', fs=150, h='Happy<br><i>Hanukkah.</i>', p='Eight nights of light, good food and good company.')),
 '2026-12-05': (C, dict(img=4402584, pos='center', eb='LocalLift Signature<br>$199 a month', fs=112, top=800, h='Your January posts,<br><i>handled.</i>', p='12 local topics a month, made for Instagram, Facebook, LinkedIn and Google Business Profile.')),
 '2026-12-06': (A, dict(img=5618068, pos='60%', ph=700, eb='Sunday', fs=104, h='Flour on the counter.<br><i>Nothing to sign.</i>', p='Bake the one recipe you only make once a year.')),
 '2026-12-07': (D, dict(img=5698415, eb='AI search', fs=116, ph=600, pos='center 55%', h='Ask AI the questions<br><i>your buyers ask.</i>',
     card="<div class=p style='color:#2a2725;margin-top:34px;max-width:880px'>Then notice which sources the answer leans on. Is any of it yours?</div>")),
 '2026-12-08': (B, dict(img=7641868, pos='center', eb='December showings', fs=100, h='Fewer buyers.<br><i>Often more serious ones.</i>', p='Confirm the day before, and ask sellers to leave a few lamps on.')),
 '2026-12-09': (C, dict(img=4692171, pos='15% center', eb='Google Business<br>Profile', fs=124, top=800, h='One photo.<br><i>Three sentences.</i>', p='A weekly post about something new in the neighborhoods you serve.')),
 '2026-12-10': (B, dict(img=30706600, pos='center 40%', eb='Year in review', fs=100, h='Three deals<br><i>that taught you the most.</i>', p='Write them down before December gets any busier.')),
 '2026-12-11': (D, dict(img=6918481, eb='Title reps', fs=112, ph=600, pos='center 55%', h='Remember the closing,<br><i>not just the name.</i>',
     card="<div class=p style='color:#2a2725;margin-top:34px;max-width:880px'>A handwritten note that names one specific moment from a file you closed together.</div>")),
 '2026-12-12': (A, dict(img=9333842, pos='65%', ph=700, eb='Saturday', fs=120, h='Go see<br><i>the lights.</i>', p='Every neighborhood has that one street. Where is yours?')),
}

async def main(only=None):
    os.makedirs(f'{V}/out', exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        for date, (fn, d) in POSTS.items():
            if only and date not in only: continue
            html = f"<html><head><style>{FONTS}{BASE}</style></head><body>{fn(d)}</body></html>"
            await pg.set_content(html); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'{V}/out/signature-vr-{date}.png')
        await b.close()
asyncio.run(main(sys.argv[1:] or None))
