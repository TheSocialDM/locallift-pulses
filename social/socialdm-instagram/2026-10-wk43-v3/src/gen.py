head='<html><head><meta charset=utf-8><link rel=stylesheet href=common.css><style>%s</style></head><body>'
def top(r): return f'<div class=top><span>THE SOCIALDM</span><b>{r}</b></div>'
def foot(k): return f'<div class=foot><span>THE SOCIALDM / LOCALLIFT</span><span>{k}</span></div></body></html>'
P={}
P[1]=(""".bg{background-image:url(p1.jpg);bottom:560px;background-position:center} .sh{position:absolute;left:0;right:0;top:0;height:800px;background:linear-gradient(180deg,rgba(13,27,42,.96) 0%,rgba(13,27,42,.88) 34%,rgba(13,27,42,.45) 60%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:88px}
.grid{position:absolute;left:64px;right:64px;top:600px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.st{padding:40px 34px 44px} .st b{display:block;font-family:'Lora';font-weight:600;font-size:86px;line-height:1;color:#C8F169;margin-bottom:14px} .st span{font-size:24px;line-height:1.35;color:#DDE3EA}
.st.w{background:#fff;border-radius:24px} .st.w b{color:#0D1B2A} .st.w span{color:#33414F}""",
"<div class=bg></div><div class=sh></div>"+top("BEHIND THE SCENES")+"""<div class=head><div class=kick>A WEEK AT THE SOCIALDM</div><h1>By the numbers. <i>The week you don't see.</i></h1></div>
<div class=grid><div class="st w"><b>16</b><span>Google listings checked against their live websites</span></div><div class="st glass"><b>11</b><span>listings with review replies written every day</span></div><div class="st glass"><b>7</b><span>days a week of Google posts and photos</span></div><div class="st w"><b>1:1</b><span>every reply written for its own review</span></div></div>"""+foot("EDITED BEFORE IT SHIPS"))
P[2]=(""".bg{background-image:url(p2.jpg);background-position:center 70%} .sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,27,42,.97) 0%,rgba(13,27,42,.9) 32%,rgba(13,27,42,.2) 58%,rgba(13,27,42,.55) 85%,#0D1B2A 100%)}
.deg{position:absolute;right:64px;bottom:170px;font-family:'Lora';font-weight:600;font-size:170px;line-height:1;color:#C8F169;text-shadow:0 10px 40px rgba(0,0,0,.5)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:82px}
.card{position:absolute;left:64px;width:560px;bottom:150px;background:#fff;color:#1B2635;border-radius:22px;padding:28px 32px;box-shadow:0 30px 80px rgba(0,0,0,.45)}
.card .l{font-size:16px;letter-spacing:.2em;font-weight:700;color:#4C7A12;margin-bottom:10px}
.card .r{display:flex;align-items:center;gap:16px;font-size:26px;padding:12px 0;border-bottom:1.5px solid #E3E8EE} .card .r:last-child{border-bottom:0}
.card .r i{width:14px;height:14px;border-radius:50%;background:#C8F169;border:2px solid #4C7A12;flex:none}""",
"<div class=bg></div><div class=sh></div>"+top("LOCAL BEATS GENERIC")+"""<div class=deg>115°</div><div class=head><div class=kick>PHOENIX, ARIZONA</div><h1>In Phoenix, renters ask <i>“Is the parking covered?”</i></h1></div>
<div class=card><div class=l>OFTEN ASKED BEFORE THE RENT</div><div class=r><i></i>Is the parking covered?</div><div class=r><i></i>Are the walkways shaded?</div><div class=r><i></i>What are the pool hours?</div><div class=r><i></i>Where can the dog walk at noon?</div></div>"""+foot("ASKED BY LOCALS"))
P[3]=(""".bg{background-image:url(p3.jpg);top:700px;background-position:center} .sh{position:absolute;left:0;right:0;top:700px;bottom:0;background:linear-gradient(180deg,#0D1B2A 0%,rgba(13,27,42,.15) 25%,rgba(13,27,42,.2) 70%,#0D1B2A 100%)}
.head{position:absolute;left:64px;right:64px;top:150px} h1{font-size:92px}
.opts{position:absolute;left:64px;right:64px;top:440px;display:flex;flex-direction:column;gap:18px}
.o{display:flex;align-items:center;gap:26px;border-radius:22px;padding:28px 32px;font-size:36px;font-family:'Lora';font-weight:600;line-height:1.2}
.o b{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;font-family:'Inter';font-size:28px;flex:none}
.a{background:#fff;color:#1B2635} .a b{background:#E3E8EE;color:#1B2635}
.bb{background:#132a40;border:2px solid #C8F169;color:#fff} .bb b{background:#C8F169;color:#0D1B2A}
.or{text-align:center;font-size:18px;letter-spacing:.3em;font-weight:700;color:#B9C3D0}""",
"<div class=bg></div><div class=sh></div>"+top("THIS OR THAT")+"""<div class=head><div class=kick>FOR PROPERTY TEAMS AND OWNERS</div><h1>Which would you <i>rather get?</i></h1></div>
<div class=opts><div class="o a"><b>A</b>A 30 page monthly report</div><div class=or>OR</div><div class="o bb"><b>B</b>One page every week, with one thing to do</div></div>"""+foot("VOTE A OR B IN THE COMMENTS"))
P[4]=(""".bg{background-image:url(p4.jpg);left:600px;bottom:0;background-position:center} .tg{position:absolute;left:600px;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(13,27,42,.85),rgba(13,27,42,0))} .edge{position:absolute;left:600px;top:0;bottom:0;width:200px;background:linear-gradient(90deg,#0D1B2A,rgba(13,27,42,0))}
.head{position:absolute;left:64px;width:600px;top:150px} h1{font-size:84px}
.note{position:absolute;left:64px;right:64px;top:1080px;font-family:'Lora';font-weight:600;font-size:44px;color:#fff} .note i{color:#C8F169} .list{position:absolute;left:64px;right:64px;top:560px;padding:16px 36px}
.it{display:flex;align-items:center;gap:22px;padding:22px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:30px}
.it:last-child{border-bottom:0} .bx{width:34px;height:34px;border:2.5px solid #C8F169;border-radius:8px;flex:none}
.it em{margin-left:auto;font-style:normal;font-size:18px;letter-spacing:.16em;font-weight:700;color:#C8F169}""",
"<div class=bg></div><div class=edge></div><div class=tg></div>"+top("THE SUNDAY CHECK")+"""<div class=head><div class=kick>FIVE MINUTES, COFFEE IN HAND</div><h1>Before Monday <i>gets loud.</i></h1></div>
<div class="list glass"><div class=it><span class=bx></span>Read your special on Google<em>1 MIN</em></div><div class=it><span class=bx></span>Check your hours match the site<em>1 MIN</em></div><div class=it><span class=bx></span>Reply to one new review<em>2 MIN</em></div><div class=it><span class=bx></span>Look at your newest photo<em>1 MIN</em></div></div><div class=note>Small checks, <i>big trust.</i></div>"""+foot("SAVE IT FOR NEXT SUNDAY"))
for n,(c,b) in P.items(): open(f'p{n}.html','w').write(head%c+b)
