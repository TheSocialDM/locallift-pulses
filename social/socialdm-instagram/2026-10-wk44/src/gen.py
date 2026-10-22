import os, asyncio
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
LI=os.path.abspath(os.path.join(HERE,'../../../socialdm-linkedin/2026-10-wk44/src'))
head='<html><head><meta charset=utf-8><link rel=stylesheet href=common.css><style>.ex{display:inline-block;font-size:18px;letter-spacing:.22em;font-weight:700;color:#B9C3D0;border:1.5px solid rgba(185,195,208,.5);padding:6px 12px;border-radius:6px}%s</style></head><body>'
def top(r): return f'<div class=top><span>THE SOCIALDM</span><b>{r}</b></div>'
def foot(k): return f'<div class=foot><span>THE SOCIALDM / LOCALLIFT</span><span>{k}</span></div></body></html>'
G={}
# ---------- Instagram / Facebook ----------
G[(HERE,'ig-2026-10-26-vendor-questions')]=(""".bg{background-image:url(i1.jpg);bottom:760px;background-position:center 40%} .sh{position:absolute;left:0;right:0;top:0;height:600px;background:linear-gradient(180deg,rgba(13,27,42,.85) 0%,rgba(13,27,42,.2) 40%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:380px} h1{font-size:84px}
.list{position:absolute;left:64px;right:64px;top:640px}
.r{display:flex;gap:26px;align-items:baseline;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.14);font-size:31px;line-height:1.3}
.r:last-child{border-bottom:0} .r b{font-family:'Lora';font-weight:600;color:#C8F169;font-size:34px;width:40px;flex:none}""",
"<div class=bg></div><div class=sh></div>"+top("SAVE THIS")+"""<div class=head><div class=kick>BEFORE YOUR NEXT VENDOR CALL</div><h1>Ask these <i>before you sign.</i></h1></div>
<div class=list><div class=r><b>1</b>Who writes the posts?</div><div class=r><b>2</b>Who checks them before they go live?</div><div class=r><b>3</b>What happens when our special changes?</div><div class=r><b>4</b>How often do you check our Google listing against our website?</div><div class=r><b>5</b>What will you tell us that we won't want to hear?</div></div>"""+foot("SAVE IT FOR YOUR NEXT CALL"))
G[(HERE,'ig-2026-10-27-myth-fact')]=(""".bg{background-image:url(i2.jpg);background-position:center} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.95) 0%,rgba(13,27,42,.75) 30%,rgba(13,27,42,.35) 55%,rgba(13,27,42,.9) 85%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:96px}
.card{position:absolute;left:64px;right:64px;border-radius:24px;padding:34px 40px}
.card .k{font-size:18px;letter-spacing:.24em;font-weight:700;margin-bottom:12px}
.card p{font-family:'Lora';font-weight:600;font-size:46px;line-height:1.2}
.myth{top:470px;background:rgba(255,255,255,.92);color:#1B2635} .myth .k{color:#A3372A} .myth p{text-decoration:line-through;text-decoration-color:#A3372A;text-decoration-thickness:4px}
.fact{top:760px;background:#0D1B2A;border:2px solid #C8F169;color:#fff} .fact .k{color:#C8F169} .fact p i{color:#C8F169}""",
"<div class=bg></div><div class=sh></div>"+top("MYTH VS FACT")+"""<div class=head><div class=kick>SOCIAL MEDIA FOR APARTMENTS</div><h1>Busy isn't <i>the goal.</i></h1></div>
<div class="card myth"><div class=k>MYTH</div><p>More posts mean more leases.</p></div>
<div class="card fact"><div class=k>FACT</div><p>Posts that answer renter questions <i>tend to do more.</i></p></div>"""+foot("FREQUENCY GETS YOU SEEN"))
G[(HERE,'ig-2026-10-28-editor')]=(""".bg{background-image:url(i3.jpg);background-position:center} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.96) 0%,rgba(13,27,42,.85) 35%,rgba(13,27,42,.6) 60%,#0D1B2A 92%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:84px}
.panel{position:absolute;left:64px;right:64px;top:470px;padding:14px 38px}
.r{display:flex;align-items:center;gap:22px;padding:24px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:29px;line-height:1.3}
.r:last-child{border-bottom:0} .r span{flex:1} .r em{font-style:normal;font-size:16px;letter-spacing:.2em;font-weight:700;color:#0D1B2A;background:#C8F169;padding:8px 12px;border-radius:6px;flex:none}
.big{position:absolute;left:64px;right:64px;top:1020px;font-family:'Lora';font-weight:600;font-size:46px;line-height:1.2} .big i{color:#C8F169}""",
"<div class=bg></div><div class=sh></div>"+top("BEHIND THE SCENES")+"""<div class=head><div class=kick>THE SECOND READ</div><h1>What our editor caught <i>before it went live.</i></h1></div>
<div class="panel glass"><div class=r><span>An offer worded differently from the property's own website</span><em>FIXED</em></div><div class=r><span>A floor plan graphic printing an old price</span><em>FIXED</em></div><div class=r><span>A stranger's phone number in the corner of a stock photo</span><em>FIXED</em></div></div>
<div class=big>Hundreds of fixes <i>in a single posting run.</i></div>"""+foot("READ TWICE, POSTED ONCE"))
G[(HERE,'ig-2026-10-29-reviews-poll')]=(""".bg{background-image:url(i4.jpg);top:640px;background-position:center 40%} .sh{position:absolute;left:0;right:0;top:640px;bottom:0;background:linear-gradient(180deg,#0D1B2A 0%,rgba(13,27,42,.1) 30%,rgba(13,27,42,.2) 70%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:86px}
.ab{position:absolute;left:64px;right:64px;top:470px;display:flex;gap:22px}
.o{flex:1;border-radius:22px;padding:28px 30px;font-family:'Lora';font-weight:600;font-size:34px;line-height:1.2}
.o b{display:grid;place-items:center;width:58px;height:58px;border-radius:50%;font-family:'Inter';font-size:26px;margin-bottom:16px}
.a{background:#fff;color:#1B2635} .a b{background:#E3E8EE} .bb{background:#0D1B2A;border:2px solid #C8F169;color:#fff} .bb b{background:#C8F169;color:#0D1B2A}""",
"<div class=bg></div><div class=sh></div>"+top("THIS OR THAT")+"""<div class=head><div class=kick>REVIEW REPLIES</div><h1>Every review, or <i>only the tough ones?</i></h1></div>
<div class=ab><div class="o a"><b>A</b>Reply to every review, five stars included</div><div class="o bb"><b>B</b>Only reply to the tough ones</div></div>"""+foot("VOTE A OR B BELOW"))
G[(HERE,'ig-2026-10-30-five-states')]=(""".bg{background-image:url(i5.jpg);background-position:center 30%} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.95) 0%,rgba(13,27,42,.6) 28%,rgba(13,27,42,.25) 50%,rgba(13,27,42,.85) 72%,#0D1B2A 90%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:100px}
.chips{position:absolute;left:64px;right:64px;top:820px;display:flex;flex-wrap:wrap;gap:12px}
.chips span{font-size:22px;font-weight:600;letter-spacing:.08em;padding:12px 20px;border-radius:30px;background:rgba(13,27,42,.7);border:1.5px solid rgba(200,241,105,.7);color:#C8F169}
.q{position:absolute;left:64px;right:64px;top:960px;background:#fff;color:#1B2635;border-radius:22px;padding:30px 38px;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.q .k{font-size:16px;letter-spacing:.22em;font-weight:700;color:#4C7A12;margin-bottom:8px} .q p{font-family:'Lora';font-weight:600;font-size:48px}""",
"<div class=bg></div><div class=sh></div>"+top("LOCAL BEATS GENERIC")+"""<div class=head><div class=kick>WHERE WE WORK</div><h1>Five states. <i>One rule.</i></h1></div>
<div class=chips><span>Arizona</span><span>Nevada</span><span>Florida</span><span>Oregon</span><span>Washington</span></div>
<div class=q><div class=k>THE RULE</div><p>Write like you live there.</p></div>"""+foot("LOCAL, WHEREVER YOU ARE"))
G[(HERE,'ig-2026-10-31-trick-treat')]=(""".bg{background-image:url(i6.jpg);bottom:640px;background-position:center 55%} .sh{position:absolute;left:0;right:0;top:0;height:720px;background:linear-gradient(180deg,rgba(13,27,42,.9) 0%,rgba(13,27,42,.3) 35%,rgba(13,27,42,.2) 60%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:92px}
.cols{position:absolute;left:64px;right:64px;top:650px;display:flex;gap:22px}
.c{flex:1;border-radius:22px;padding:28px 30px}
.c .k{font-size:20px;letter-spacing:.24em;font-weight:700;margin-bottom:14px}
.c div.i{font-size:26px;line-height:1.3;padding:14px 0;border-bottom:1px solid rgba(127,143,162,.3)} .c div.i:last-child{border-bottom:0}
.trick{background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.18)} .trick .k{color:#E58A7A}
.treat{background:#fff;color:#1B2635} .treat .k{color:#4C7A12}""",
"<div class=bg></div><div class=sh></div>"+top("HAPPY HALLOWEEN")+"""<div class=head><div class=kick>APARTMENT EDITION</div><h1>Trick <i>or treat?</i></h1></div>
<div class=cols><div class="c trick"><div class=k>TRICK</div><div class=i>A special that ended weeks ago</div><div class=i>Photos from three summers ago</div><div class=i>A review nobody answered</div></div>
<div class="c treat"><div class=k>TREAT</div><div class=i>Today's special, everywhere</div><div class=i>Photos from this season</div><div class=i>A reply that says something</div></div></div>"""+foot("TREATS ONLY"))
# ---------- LinkedIn single graphics ----------
G[(LI,'li-2026-10-27-say-something')]=(""".bg{background-image:url(l2.jpg);left:0;right:0;bottom:700px;background-position:center 45%} .sh{position:absolute;left:0;right:0;top:0;height:720px;background:linear-gradient(180deg,rgba(13,27,42,.96) 0%,rgba(13,27,42,.85) 40%,rgba(13,27,42,.4) 65%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:84px}
.pair{position:absolute;left:64px;right:64px;top:640px;display:flex;flex-direction:column;gap:20px}
.p{border-radius:20px;padding:26px 30px;display:flex;gap:22px;align-items:flex-start}
.p .av{width:56px;height:56px;border-radius:50%;flex:none;background:#E3E8EE}
.p .k{font-size:16px;letter-spacing:.22em;font-weight:700;margin-bottom:8px} .p .t{font-size:28px;line-height:1.35}
.gen{background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.18);color:#B9C3D0} .gen .k{color:#B9C3D0}
.spec{background:#fff;color:#1B2635} .spec .k{color:#4C7A12} .spec .av{background:#C8F169}
.exw{position:absolute;right:64px;top:590px}""",
"<div class=bg></div><div class=sh></div>"+top("GENERIC VS SPECIFIC")+"""<div class=head><div class=kick>DAILY POSTING</div><h1>A post every day can <i>still say nothing.</i></h1></div>
<div class=exw><span class=ex>EXAMPLE</span></div>
<div class=pair><div class="p gen"><div class=av></div><div><div class=k>GENERIC</div><div class=t>Happy Monday from our community!</div></div></div>
<div class="p spec"><div class=av></div><div><div class=k>SPECIFIC</div><div class=t>The pool is closed for resurfacing through Friday. The spa stays open.</div></div></div></div>"""+foot("SAY SOMETHING"))
G[(LI,'li-2026-10-31-scary-phrases')]=(""".bg{background-image:url(l6.jpg);background-position:center 40%} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.96) 0%,rgba(13,27,42,.8) 30%,rgba(13,27,42,.45) 55%,rgba(13,27,42,.88) 78%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:86px}
.grid{position:absolute;left:64px;right:64px;top:640px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.g{padding:30px 30px 34px} .g p{font-family:'Lora';font-weight:600;font-size:38px;line-height:1.2;margin-bottom:12px} .g span{font-size:21px;color:#B9C3D0;line-height:1.35}""",
"<div class=bg></div><div class=sh></div>"+top("HAPPY HALLOWEEN")+"""<div class=head><div class=kick>FOR OWNERS AND OPERATORS</div><h1>The scariest words in a <i>marketing report.</i></h1></div>
<div class=grid><div class="g glass"><p>“Engagement is up.”</p><span>Up from what, and did it lead anywhere?</span></div><div class="g glass"><p>“We're optimizing.”</p><span>What changed, and when?</span></div><div class="g glass"><p>“It's the algorithm.”</p><span>Sometimes. What did you try next?</span></div><div class="g glass"><p>“Results may vary.”</p><span>Varied how, compared to what?</span></div></div>"""+foot("ASK THE FOLLOW-UP"))
# ---------- LinkedIn swipe slides ----------
def sfoot(n): return foot(f'{n:02d} / 06')
G[(LI,'li-2026-10-29-report-1')]=(""".bg{background-image:url(c1.jpg);background-position:center} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.8) 0%,rgba(13,27,42,.2) 25%,rgba(13,27,42,.35) 45%,rgba(13,27,42,.92) 65%,#0D1B2A 82%)}
.head{position:absolute;left:64px;right:64px;top:720px} h1{font-size:96px} .sw{position:absolute;right:64px;top:1180px;font-size:20px;font-weight:700;letter-spacing:.2em}""",
"<div class=bg></div><div class=sh></div>"+top("THE WEEKLY REPORT")+"""<div class=head><div class=kick>FOR OWNERS AND OPERATORS</div><h1>Four questions a weekly report <i>should answer.</i></h1></div><div class=sw>SWIPE →</div>"""+sfoot(1))
def qslide(n,img,num,topic,q,note,layout):
    if layout=='top':
        css=f""".bg{{background-image:url({img});bottom:640px;background-position:center}} .sh{{position:absolute;left:0;right:0;top:0;height:720px;background:linear-gradient(180deg,rgba(13,27,42,.85) 0%,rgba(13,27,42,.2) 35%,#0D1B2A 100%)}}
.head{{position:absolute;left:64px;right:64px;top:720px}} h1{{font-size:92px}} .note{{position:absolute;left:64px;right:64px;top:1080px;font-size:30px;line-height:1.4;color:#DDE3EA}}"""
        body="<div class=bg></div><div class=sh></div>"
    elif layout=='split':
        css=f""".bg{{background-image:url({img});left:540px;background-position:center}} .edge{{position:absolute;left:540px;top:0;bottom:0;width:320px;background:linear-gradient(90deg,#0D1B2A 20%,rgba(13,27,42,0))}} .tg{{position:absolute;left:540px;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(13,27,42,.85),rgba(13,27,42,0))}} .bt{{position:absolute;left:540px;right:0;bottom:0;height:260px;background:linear-gradient(0deg,#0D1B2A 30%,rgba(13,27,42,0))}}
.head{{position:absolute;left:64px;width:600px;top:330px}} h1{{font-size:84px}} .note{{position:absolute;left:64px;width:560px;top:900px;font-size:30px;line-height:1.4;color:#DDE3EA}}"""
        body="<div class=bg></div><div class=edge></div><div class=tg></div><div class=bt></div>"
    else:
        css=f""".bg{{background-image:url({img});background-position:center}} .sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.96) 0%,rgba(13,27,42,.85) 40%,rgba(13,27,42,.5) 65%,#0D1B2A 92%)}}
.head{{position:absolute;left:64px;right:64px;top:170px}} h1{{font-size:96px}} .note{{position:absolute;left:64px;right:64px;top:620px;font-size:32px;line-height:1.4;color:#DDE3EA;padding:30px 36px}}"""
        body="<div class=bg></div><div class=sh></div>"
    gl=' glass' if layout=='full' else ''
    return (css, body+top("THE WEEKLY REPORT")+f"<div class=head><div class=kick>{num} · {topic}</div><h1>{q}</h1></div><div class='note{gl}'>{note}</div>"+sfoot(n))
G[(LI,'li-2026-10-29-report-2')]=qslide(2,'c2.jpg','01','WHAT CHANGED','What changed <i>since last week?</i>','Not a snapshot. The difference between this week and last is where the story is.','top')
G[(LI,'li-2026-10-29-report-3')]=qslide(3,'c3.jpg','02','THE MARKET','Who moved on <i>price or specials?</i>','New concessions nearby can change a week faster than any monthly report can catch.','split')
G[(LI,'li-2026-10-29-report-4')]=qslide(4,'c4.jpg','03','YOUR LISTING','Is our listing <i>still right?</i>','Special, hours, price and photos, checked against your own website, not assumed.','full')
G[(LI,'li-2026-10-29-report-5')]=qslide(5,'c5.jpg','04','THE ACTION','What is the <i>one thing to do?</i>','A report that ends without a next step is just a longer way of saying nothing changed.','top')
G[(LI,'li-2026-10-29-report-6')]=(""".bg{background-image:url(c6.jpg);background-position:center} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.95) 0%,rgba(13,27,42,.85) 35%,rgba(13,27,42,.6) 55%,rgba(13,27,42,.94) 75%,#0D1B2A 90%)}
.head{position:absolute;left:64px;right:64px;top:170px} h1{font-size:82px}
.list{position:absolute;left:64px;right:64px;top:640px;padding:16px 38px}
.it{display:flex;align-items:center;gap:22px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:29px} .it:last-child{border-bottom:0}
.ck{width:42px;height:42px;border-radius:50%;background:#C8F169;color:#0D1B2A;display:grid;place-items:center;font-weight:800;font-size:22px;flex:none}
.sig{position:absolute;left:64px;right:64px;top:1150px;display:flex;justify-content:space-between;align-items:baseline} .sig b{font-family:'Lora';font-size:38px;font-weight:600} .sig span{font-size:24px;color:#C8F169;font-weight:600}""",
"<div class=bg></div><div class=sh></div>"+top("THE WEEKLY REPORT")+"""<div class=head><div class=kick>EVERY WEEK</div><h1>What our weekly reports <i>are built to answer.</i></h1></div>
<div class="list glass"><div class=it><span class=ck>✓</span>What changed since last week</div><div class=it><span class=ck>✓</span>Who moved on price or specials</div><div class=it><span class=ck>✓</span>Whether your listing is still right</div><div class=it><span class=ck>✓</span>The one thing to do next</div></div>
<div class=sig><b>Michael Shad</b><span>thesocialdm.com</span></div>"""+sfoot(6))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for (d,name),(css,body) in G.items():
            src=os.path.join(d,name+'.html'); open(src,'w').write(head%css+body)
            await pg.goto('file://'+src); await pg.wait_for_timeout(350)
            await pg.screenshot(path=os.path.join(os.path.dirname(d),'socialdm-'+name+'.png'))
        await b.close()
asyncio.run(main())
