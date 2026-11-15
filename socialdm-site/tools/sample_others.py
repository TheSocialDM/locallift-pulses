"""Med spa, medical and hospitality demo sites (all fictional, Larkspur Vale)."""
from samples_kit import page, esc


def faq_html(qs):
    return ''.join(f'<details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(qs))


def faq_schema(qs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}


def footer(brand, blurb, cols, legal):
    c = ''.join(f'<div><h4>{h}</h4>' + ''.join(f'<a href="{u}">{t}</a>' for t, u in links) + '</div>' for h, links in cols)
    return f"""<footer><div class="cols"><div><div class="brand" style="color:#fff">{brand}</div><p style="margin-top:16px;max-width:340px;opacity:.8">{blurb}</p></div>{c}</div>
<div class="legal"><span>{legal}</span><span>Sample site concept by LocalLift, a SocialDM company. Not a real business.</span></div></footer>"""


EXTRA = """
.svc{display:block;background:#fff;border:1px solid var(--line);transition:transform .3s,box-shadow .3s}
.svc:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(0,0,0,.08)}
.svc .ph{aspect-ratio:4/3}.svc div.t{padding:22px 22px 26px}.svc h3{margin-bottom:6px}.svc p{font-size:14.5px;opacity:.8}
.svc .more{display:block;margin-top:14px;font:500 11.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--acc2)}
.menu-t{width:100%;border-collapse:collapse}.menu-t td{padding:16px 0;border-bottom:1px solid var(--line);vertical-align:top}.menu-t td:last-child{text-align:right;font-family:var(--serif);font-size:19px;white-space:nowrap;padding-left:20px}
.menu-t small{display:block;font-size:13px;opacity:.7}
.bookbar{display:grid;grid-template-columns:repeat(4,1fr) auto;background:#fff;max-width:900px;box-shadow:0 20px 50px rgba(0,0,0,.25);color:#222}
.bookbar label{display:block;padding:12px 18px;border-right:1px solid #eee;font:500 10.5px var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#777}
.bookbar input,.bookbar select{display:block;border:0;font:400 15px var(--sans);color:#222;padding:4px 0 0;width:100%;background:none}
.prov{display:grid;grid-template-columns:160px 1fr;gap:26px;align-items:center}.prov .ph{aspect-ratio:1;border-radius:50%}
.badges{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}.badges span{border:1px solid var(--line);padding:8px 12px;font-size:12.5px;letter-spacing:.06em}
.alert{background:var(--soft);border:1px solid var(--line);padding:16px 20px;font-size:14.5px}
@media(max-width:900px){.bookbar{grid-template-columns:1fr 1fr}.bookbar .btn{grid-column:span 2}.prov{grid-template-columns:100px 1fr}}
"""

# ---------------- MED SPA ----------------
MS = '/samples/med-spa/'
MI = MS + 'img/'
MS_THEME = """:root{--serif:'Fraunces',Georgia,serif;--sans:'Manrope',system-ui,sans-serif;--ink:#2a2422;--bg:#fbf7f3;--soft:#f3eae2;--line:#e8dccf;--acc:#c48f7a;--acc2:#a06a55;--accink:#fff;--deep:#3a2c27;--foot:#2a201c;--navbg:#fbf7f3;--navink:#2a2422;--wt:400;--hw:300}"""
MS_FONTS = 'family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=Manrope:wght@400;500;600'
MS_BRAND = 'Ourelle<small>Skin Studio</small>'
MS_MENU = [('Treatments', MS + '#treatments'), ('Botox', MS + 'botox-larkspur-vale/'), ('Pricing', MS + '#pricing'), ('Providers', MS + '#providers'), ('Questions', MS + '#faq')]
MS_CTA = ('Book a consult', MS + '#book')
MS_SAMPLE = 'Sample concept by LocalLift. Ourelle Skin Studio, its providers and Larkspur Vale are fictional.'
MS_FOOT = footer(MS_BRAND, 'Medical aesthetics in Larkspur Vale. Address, hours and medical director details go here.',
                 [('Treatments', [('Botox', MS + 'botox-larkspur-vale/'), ('Fillers', MS + '#treatments'), ('Facials', MS + '#treatments')]),
                  ('Studio', [('Providers', MS + '#providers'), ('Pricing', MS + '#pricing')]), ('Visit', [('Book a consult', MS + '#book'), ('Questions', MS + '#faq')])],
                 'Treatments are performed by licensed providers. Results vary. Prices shown are sample placeholders.')


def ms_page(path, title, desc, body, schema=None, over=False):
    page('med-spa', path, title=title + ' | Sample concept by LocalLift', desc=desc, theme_css=MS_THEME, fonts=MS_FONTS, brand_html=MS_BRAND,
         menu=MS_MENU, cta=MS_CTA, body=body, footer_html=MS_FOOT, schema=schema, over=over, extra_css=EXTRA, sample_line=MS_SAMPLE)


MS_FAQ = [('Who performs treatments at Ourelle?', 'Every injectable and laser treatment is performed by a licensed provider. Provider names and credentials are listed in our Providers section and confirmed at your consult.'),
          ('Do I need a consult first?', 'Yes for injectables and lasers. A consult is a conversation about goals, safety and options, not a commitment.'),
          ('How much does Botox cost?', 'Pricing depends on the areas treated. Current pricing is shown at booking and confirmed at your consult.'),
          ('Is there downtime?', 'It depends on the treatment. Each treatment page lists typical downtime, and your provider confirms it for you.')]


def med_spa():
    treat = [('Botox and Dysport', 't2', 'Softer expression lines in a quick visit.', MS + 'botox-larkspur-vale/'),
             ('Dermal fillers', 't5', 'Restore volume with a natural look.', MS + '#book'), ('HydraFacial', 't1', 'Deep cleanse and hydration, little to no downtime.', MS + '#book'),
             ('Laser and light', 't3', 'Tone, texture and sun spots.', MS + '#book'), ('Chemical peels', 't6', 'Brighter, smoother skin.', MS + '#book'), ('Membership', 't4', 'Monthly care with member pricing.', MS + '#pricing')]
    tc = ''.join(f'<a class="svc reveal" href="{u}"><div class="ph"><img src="{MI}{i}.jpg" alt="{n}" loading="lazy"></div><div class="t"><h3>{n}</h3><p>{d}</p><span class="more">Learn more &rarr;</span></div></a>' for n, i, d, u in treat)
    price = [('Botox', 'Per unit, total shown at booking', 'from $XX'), ('Lip filler', 'One syringe', 'from $XXX'), ('HydraFacial', 'Signature, 60 minutes', '$XXX'),
             ('Laser facial', 'Single session', 'from $XXX'), ('Ourelle membership', 'Monthly facial plus member pricing', '$XX / mo')]
    pt = ''.join(f'<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>' for a, b, c in price)
    body = f"""<section class="hero" style="padding:0"><div class="bg" style="background-image:url({MI}hero.jpg)"></div><div class="in"><div class="eyebrow" style="color:#fff;opacity:.9">Medical aesthetics &nbsp;&middot;&nbsp; Larkspur Vale</div>
<h1>Skin that looks like <i>you, rested.</i></h1><p>Botox, fillers, lasers and facials planned by licensed providers, with natural results as the goal.</p><a class="btn" href="#book">Book a consult</a> &nbsp; <a class="btn line" href="#treatments">See treatments</a></div><span class="tag">Stock photo. Client photos go here.</span></section>
<div class="stats wrap"><div><b>Licensed</b><span>Provider on every treatment</span></div><div><b>Consult</b><span>Before any injectable</span></div><div><b>Clear</b><span>Pricing shown at booking</span></div><div><b>Follow up</b><span>Two-week check-in</span></div></div>
<section id="treatments"><div class="wrap"><div class="eyebrow">Treatments</div><h2>Every treatment has its own page</h2><p class="lead">So people can read what it is, who it suits and what to expect, and so search engines and AI assistants can quote it.</p><div class="grid g3" style="margin-top:34px">{tc}</div></div></section>
<section class="band" style="padding:0"><div class="split" style="gap:0"><div class="ph" style="min-height:520px"><img src="{MI}room.jpg" alt="Calm treatment room" loading="lazy"></div><div style="padding:clamp(48px,7vw,100px)"><div class="eyebrow">The Ourelle way</div><h2 style="color:#fff">A plan, <i>not a pitch.</i></h2>
<ol class="steps" style="border-color:rgba(255,255,255,.2)"><li><div><b>Consult</b>Your goals, history and what is realistic.</div></li><li><div><b>Plan</b>A written plan with pricing before anything starts.</div></li><li><div><b>Treat</b>Licensed providers, calm rooms, no rush.</div></li><li><div><b>Check in</b>A follow up to see how it settled.</div></li></ol></div></div></section>
<section id="pricing"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Pricing</div><h2>Know the price before you book</h2><p class="lead">Clear starting prices build trust and answer the first question people ask.</p><p class="note">Prices on this sample are placeholders.</p></div><table class="menu-t">{pt}</table></div></section>
<section id="providers" style="padding-top:0"><div class="wrap"><div class="eyebrow">Providers</div><h2>Who treats you</h2><div class="prov reveal" style="margin-top:26px"><div class="ph"><img src="{MI}prov.jpg" alt="Provider portrait (stock photo stand in)" loading="lazy"></div><div><h3>Provider name, credentials</h3><p style="opacity:.85;margin-top:8px">Real provider bios with license type, training and years in practice go here. Credentials up front are what make a med spa site credible to patients and to AI.</p><div class="badges"><span>License type</span><span>Training</span><span>Years in practice</span></div></div></div></div></section>
<section id="faq" style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>What people ask first</h2></div><div>{faq_html(MS_FAQ)}</div></div></section>
<section id="book" class="band" style="text-align:center"><div class="wrap"><div class="eyebrow">Book</div><h2 style="color:#fff">Start with a consult</h2><p class="lead" style="margin:0 auto 26px">Buttons connect to the booking system the studio already uses.</p><a class="btn" href="#book">Book a consult (sample)</a></div></section>"""
    sch = {"@context": "https://schema.org", "@type": "MedicalBusiness", "name": "Ourelle Skin Studio (sample)", "description": "Fictional sample med spa site by LocalLift."}
    ms_page('', 'Ourelle Skin Studio | Med spa in Larkspur Vale', 'Sample med spa website concept (fictional).', body, schema=[sch, faq_schema(MS_FAQ)], over=True)

    faqs = [('How long does Botox last?', 'For most people about three to four months. Results vary.'),
            ('Does Botox hurt?', 'Most people describe a quick pinch. Your provider can use ice or numbing cream if you want it.'),
            ('What is the difference between Botox and Dysport?', 'Both relax expression lines. Your provider will explain which fits your goals at your consult.'),
            ('Can I work out after Botox?', 'Most providers suggest skipping hard workouts for the rest of the day. Your provider gives you aftercare instructions.'),
            ('Where in Larkspur Vale are you?', "The client's address, parking notes and nearby landmarks go here.")]
    tl = [('Day 0', 'Consult and treatment, under 30 minutes.'), ('Days 3 to 5', 'Lines start to soften.'), ('Weeks 1 to 2', 'Full result usually shows. Follow-up visit.'), ('Months 3 to 4', 'Effect fades gradually. Time to plan the next visit.')]
    tlh = ''.join(f'<li><div><b>{a}</b>{b}</div></li>' for a, b in tl)
    body = f"""<section class="hero" style="padding:0;min-height:76vh"><div class="bg" style="background-image:url({MI}t2.jpg)"></div><div class="in"><div class="crumbs"><a href="{MS}">Home</a> / Treatments / Botox in Larkspur Vale</div><div class="eyebrow" style="color:#fff;opacity:.9">Botox and Dysport in Larkspur Vale</div><h1>Botox in Larkspur Vale, <i>planned around your face.</i></h1><a class="btn" href="{MS}#book">Book a consult</a></div><span class="tag">Stock photo</span></section>
<section><div class="wrap"><div class="short"><b>The short answer</b>Botox is a quick treatment done in the office that relaxes the muscles behind expression lines. Most visits take under 30 minutes, and results usually show within one to two weeks. Results vary from person to person.</div></div>
<div class="stats wrap" style="margin-top:30px"><div><b>&lt;30 min</b><span>Typical appointment</span></div><div><b>1 to 2 wks</b><span>When results usually show</span></div><div><b>3 to 4 mo</b><span>How long it usually lasts</span></div><div><b>Licensed</b><span>Provider on every treatment</span></div></div></section>
<section style="padding-top:0"><div class="wrap split"><div class="reveal"><div class="eyebrow">Who it suits</div><h2>Softer lines, still you</h2><p class="lead">People who want softer forehead lines, frown lines or crow's feet, with a natural look as the goal. It is not right for everyone, which is why every plan starts with a consult.</p>
<div class="alert" style="margin-top:22px">Like any medical treatment, Botox has possible side effects, such as bruising or headache. Your provider will go over them, and whether it is right for you, at your consult.</div></div><div class="ph reveal" style="aspect-ratio:4/5"><img src="{MI}t3.jpg" alt="Provider consulting with a patient" loading="lazy"></div></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">What to expect</div><h2>From consult to result</h2></div><ol class="steps">{tlh}</ol></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>Botox questions people ask</h2></div><div>{faq_html(faqs)}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="eyebrow">Related treatments</div><div class="grid g3" style="margin-top:20px"><a class="svc" href="{MS}#treatments"><div class="ph"><img src="{MI}t5.jpg" alt="" loading="lazy"></div><div class="t"><h3>Dermal fillers</h3></div></a><a class="svc" href="{MS}#treatments"><div class="ph"><img src="{MI}t3.jpg" alt="" loading="lazy"></div><div class="t"><h3>Laser and light</h3></div></a><a class="svc" href="{MS}#faq"><div class="ph"><img src="{MI}t1.jpg" alt="" loading="lazy"></div><div class="t"><h3>All questions</h3></div></a></div></div></section>
<section class="band" style="text-align:center"><div class="wrap"><h2 style="color:#fff">Ready to talk it through?</h2><p class="lead" style="margin:0 auto 26px">A consult is a conversation, not a commitment.</p><a class="btn" href="{MS}#book">Book a consult (sample)</a></div></section>"""
    ms_page('botox-larkspur-vale', 'Botox in Larkspur Vale', 'Sample Botox landing page with short answer, timeline and FAQs (fictional).', body, schema=[faq_schema(faqs)])


# ---------------- MEDICAL ----------------
MD = '/samples/medical/'
DI = MD + 'img/'
MD_THEME = """:root{--serif:'Newsreader',Georgia,serif;--sans:'Inter',system-ui,sans-serif;--ink:#16263a;--bg:#f7f9fb;--soft:#eaf1f6;--line:#d9e3ec;--acc:#1f6f8b;--acc2:#1f6f8b;--accink:#fff;--deep:#0f2436;--foot:#0b1a28;--navbg:#ffffff;--navink:#16263a;--wt:400;--hw:500}"""
MD_FONTS = 'family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Inter:wght@400;500;600'
MD_BRAND = 'Sable Ridge<small>Surgical</small>'
MD_MENU = [('Conditions', MD + '#conditions'), ('Hernia repair', MD + 'hernia-repair-larkspur-vale/'), ('Patients', MD + '#patients'), ('Referring doctors', MD + '#referrals'), ('Questions', MD + '#faq')]
MD_CTA = ('Request an appointment', MD + '#appointment')
MD_SAMPLE = 'Sample concept by LocalLift. Sable Ridge Surgical, its surgeons and Larkspur Vale are fictional.'
MD_FOOT = footer(MD_BRAND, 'General surgery in Larkspur Vale. Address, hours, phone and hospital affiliations go here.',
                 [('Care', [('Hernia repair', MD + 'hernia-repair-larkspur-vale/'), ('Gallbladder', MD + '#conditions'), ('Colon and rectal', MD + '#conditions')]),
                  ('Patients', [('New patients', MD + '#patients'), ('Insurance', MD + '#patients')]), ('Doctors', [('Refer a patient', MD + '#referrals')])],
                 'General information only, not medical advice. In an emergency, call 911.')


def md_page(path, title, desc, body, schema=None, over=False):
    page('medical', path, title=title + ' | Sample concept by LocalLift', desc=desc, theme_css=MD_THEME, fonts=MD_FONTS, brand_html=MD_BRAND,
         menu=MD_MENU, cta=MD_CTA, body=body, footer_html=MD_FOOT, schema=schema, over=over, extra_css=EXTRA, sample_line=MD_SAMPLE)


MD_FAQ = [('Do I need a referral?', "It depends on your insurance plan. The client's referral policy and accepted plans go here."),
          ('What should I bring to my first visit?', 'Photo ID, insurance card, a list of medicines and any imaging or reports you have.'),
          ('Will I have surgery at my first visit?', 'No. The first visit is an exam and a conversation about your options.'),
          ('How soon can I be seen?', "The client's typical wait for a new patient visit goes here.")]


def medical():
    conds = [('Hernia repair', 'Groin, belly button and incisional hernias.', MD + 'hernia-repair-larkspur-vale/'), ('Gallbladder', 'Gallstones and gallbladder removal.', MD + '#appointment'),
             ('Colon and rectal', 'Diverticulitis, polyps and more.', MD + '#appointment'), ('Skin and soft tissue', 'Cysts, lipomas and lesions.', MD + '#appointment'),
             ('Reflux surgery', 'When medicine is not enough.', MD + '#appointment'), ('Second opinions', 'A clear view before you decide.', MD + '#appointment')]
    cc = ''.join(f'<a class="svc reveal" href="{u}" style="padding:28px"><h3>{n}</h3><p>{d}</p><span class="more">Learn more &rarr;</span></a>' for n, d, u in conds)
    body = f"""<section class="hero" style="padding:0;min-height:84vh"><div class="bg" style="background-image:url({DI}hero.jpg)"></div><div class="in"><div class="eyebrow" style="color:#fff;opacity:.9">General surgery &nbsp;&middot;&nbsp; Larkspur Vale</div>
<h1>Surgical care, <i>explained before you decide.</i></h1><p>Board-certified surgeons who walk you through every option, including whether you need surgery at all.</p><a class="btn" href="#appointment">Request an appointment</a> &nbsp; <a class="btn line" href="#referrals">For referring doctors</a></div><span class="tag">Stock photo. Client photos go here.</span></section>
<div class="wrap" style="padding:18px 5vw"><div class="alert"><b>New patients:</b> appointments usually within a few days (sample). Accepted insurance plans are listed below. In an emergency, call 911.</div></div>
<section id="conditions"><div class="wrap"><div class="eyebrow">What we treat</div><h2>One clear page per condition</h2><p class="lead">Plain language pages that answer what patients search, written so AI assistants and referring doctors can understand them.</p><div class="grid g3" style="margin-top:34px">{cc}</div></div></section>
<section style="padding-top:0"><div class="wrap split"><div class="ph reveal" style="aspect-ratio:4/5"><img src="{DI}doc.jpg" alt="Surgeon portrait (stock photo stand in)" loading="lazy"></div><div class="reveal"><div class="eyebrow">Your surgeon</div><h2>Surgeon name, MD, FACS</h2><p class="lead">Real bios list board certification, training, hospital privileges and the procedures done most often. This is the trust layer patients and AI look for first.</p><div class="badges"><span>Board-certified</span><span>Fellowship-trained</span><span>Hospital privileges</span><span>Languages</span></div></div></div></section>
<section id="patients" class="band"><div class="wrap grid g3"><div><div class="eyebrow">Before your visit</div><h3 style="margin-top:12px">New patient forms</h3><p style="opacity:.8;margin-top:8px">Fill them out online before you arrive.</p></div><div><div class="eyebrow">Insurance</div><h3 style="margin-top:12px">Plans we accept</h3><p style="opacity:.8;margin-top:8px">The client's accepted plans go here, kept current.</p></div><div><div class="eyebrow">Locations</div><h3 style="margin-top:12px">Where to find us</h3><p style="opacity:.8;margin-top:8px">Address, parking and the hospital campus map go here.</p></div></div></section>
<section id="referrals"><div class="wrap split"><div class="reveal"><div class="eyebrow">For referring doctors</div><h2>Easy to refer, easy to follow up</h2><p class="lead">Referral fax and portal details, what to send, and a promise to report back after every visit.</p><p style="margin-top:24px"><a class="btn dark" href="#appointment">Refer a patient (sample)</a></p></div><div class="ph reveal" style="aspect-ratio:4/3"><img src="{DI}desk.jpg" alt="Clinic front desk" loading="lazy"></div></div></section>
<section id="faq" style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>New patient questions</h2></div><div>{faq_html(MD_FAQ)}</div></div></section>
<section id="appointment" class="band" style="text-align:center"><div class="wrap"><h2 style="color:#fff">Request an appointment</h2><p class="lead" style="margin:0 auto 26px">Buttons connect to the practice's own scheduling or request form.</p><a class="btn" href="#appointment">Request an appointment (sample)</a></div></section>"""
    sch = {"@context": "https://schema.org", "@type": "MedicalClinic", "name": "Sable Ridge Surgical (sample)", "medicalSpecialty": "Surgical", "description": "Fictional sample practice site by LocalLift."}
    md_page('', 'Sable Ridge Surgical | General surgery in Larkspur Vale', 'Sample surgical practice website concept (fictional).', body, schema=[sch, faq_schema(MD_FAQ)], over=True)

    faqs = [('Can a hernia go away on its own?', 'Hernias do not heal on their own, but some small ones can be watched. Your surgeon will tell you what fits your case.'),
            ('Is hernia repair done laparoscopically?', 'Sometimes. Your surgeon will explain which approach fits your hernia and health.'),
            ('When can I go back to work?', 'It depends on the repair and your job. You will get a plan before surgery.'),
            ('Does insurance cover hernia repair?', 'Many plans cover medically necessary hernia repair. The office checks your benefits before scheduling.'),
            ('Where are you located in Larkspur Vale?', "The client's address, parking notes and nearby landmarks go here.")]
    steps = [('Consult', 'Exam, questions and your options, including watching it for now.'), ('Plan', 'If surgery fits, a written plan with what to expect.'), ('Surgery day', 'Many repairs are outpatient. You get clear arrival and recovery instructions.'), ('Recovery', 'A follow-up visit and a return-to-activity plan for your job.')]
    sh = ''.join(f'<li><div><b>{a}</b>{b}</div></li>' for a, b in steps)
    body = f"""<section style="padding-bottom:30px;background:var(--soft)"><div class="wrap split"><div><div class="crumbs"><a href="{MD}">Home</a> / Conditions / Hernia repair in Larkspur Vale</div><div class="eyebrow">Hernia repair in Larkspur Vale</div><h2 style="font-size:clamp(38px,5vw,64px)">Hernia repair in Larkspur Vale, <i>explained before you decide.</i></h2><a class="btn" href="{MD}#appointment">Request an appointment</a></div><div class="ph" style="aspect-ratio:4/3"><img src="{DI}room.jpg" alt="Clean exam room" loading="lazy"></div></div></section>
<section><div class="wrap"><div class="short"><b>The short answer</b>A hernia happens when tissue pushes through a weak spot in the muscle wall. Many hernias are repaired with a planned outpatient surgery. Your surgeon will explain your options, including whether watching it is reasonable for now.</div>
<div class="alert" style="margin-top:18px"><b>Get care right away</b> if a bulge becomes painful, firm or will not go back in, or if you have nausea or vomiting. Call 911 in an emergency.</div></div>
<div class="stats wrap" style="margin-top:30px"><div><b>Consult</b><span>No surgery at the first visit</span></div><div><b>Outpatient</b><span>Many patients go home the same day</span></div><div><b>Written</b><span>Recovery plan for your situation</span></div><div><b>Certified</b><span>Board-certified surgeon</span></div></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Symptoms</div><h2>Signs people notice</h2><p class="lead">A bulge or discomfort in the groin or near the belly button, often noticed when lifting or coughing. Your surgeon confirms the diagnosis at your consult.</p><p style="margin-top:16px;opacity:.85">Like any surgery, hernia repair has risks, such as infection or the hernia coming back. Your surgeon will go over them with you.</p></div><ol class="steps">{sh}</ol></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>What patients ask</h2></div><div>{faq_html(faqs)}</div></div></section>
<section class="band" style="text-align:center"><div class="wrap"><h2 style="color:#fff">Ready to talk it through?</h2><p class="lead" style="margin:0 auto 26px">General information only, not medical advice.</p><a class="btn" href="{MD}#appointment">Request an appointment (sample)</a></div></section>"""
    md_page('hernia-repair-larkspur-vale', 'Hernia repair in Larkspur Vale', 'Sample hernia repair landing page (fictional).', body, schema=[faq_schema(faqs)])


# ---------------- HOSPITALITY ----------------
HO = '/samples/hospitality/'
HI = HO + 'img/'
HO_THEME = """:root{--serif:'Italiana',Georgia,serif;--sans:'Montserrat',system-ui,sans-serif;--ink:#1f2a2a;--bg:#f8f5ef;--soft:#efe8db;--line:#e2d8c6;--acc:#c9a46a;--acc2:#9a7a45;--accink:#1f2a2a;--deep:#16302e;--foot:#0f2220;--navbg:#f8f5ef;--navink:#1f2a2a;--wt:400;--hw:400;--brandls:.18em}
.brand{text-transform:uppercase;font-size:24px}h1,h2{letter-spacing:.01em}"""
HO_FONTS = 'family=Italiana&family=Montserrat:wght@400;500;600'
HO_BRAND = 'Hotel Solenne<small>Larkspur Vale</small>'
HO_MENU = [('Rooms', HO + '#rooms'), ('Pool cabanas', HO + 'pool-cabanas-larkspur-vale/'), ('Dining', HO + '#dining'), ('Events', HO + '#events'), ('Questions', HO + '#faq')]
HO_CTA = ('Book a stay', HO + '#book')
HO_SAMPLE = 'Sample concept by LocalLift. Hotel Solenne and Larkspur Vale are fictional.'
HO_FOOT = footer(HO_BRAND, 'A boutique hotel in Larkspur Vale. Address, phone and directions go here.',
                 [('Stay', [('Rooms and suites', HO + '#rooms'), ('Pool cabanas', HO + 'pool-cabanas-larkspur-vale/')]),
                  ('Dine', [('Restaurant and bar', HO + '#dining')]), ('Gather', [('Events', HO + '#events'), ('Questions', HO + '#faq')])],
                 'Rates, hours and availability change by season and are confirmed when you book.')


def ho_page(path, title, desc, body, schema=None, over=False):
    page('hospitality', path, title=title + ' | Sample concept by LocalLift', desc=desc, theme_css=HO_THEME, fonts=HO_FONTS, brand_html=HO_BRAND,
         menu=HO_MENU, cta=HO_CTA, body=body, footer_html=HO_FOOT, schema=schema, over=over, extra_css=EXTRA, sample_line=HO_SAMPLE)


HO_FAQ = [('What time is check in and check out?', "The client's check in and check out times go here."),
          ('Is parking available?', "Parking options and rates go here."),
          ('Are pets allowed?', "The client's pet policy goes here."),
          ('Is the pool open year round?', 'Pool hours change with the season. Current hours are shown when you book.')]


def hospitality():
    rooms = [('King room', 'room', 'Quiet, bright and made for a long weekend.'), ('Pool view suite', 'room2', 'A separate sitting room and morning light.'), ('Garden villa', 'suite', 'Private terrace and an outdoor shower.')]
    rc = ''.join(f'<a class="svc reveal" href="#book"><div class="ph"><img src="{HI}{i}.jpg" alt="{n}" loading="lazy"></div><div class="t"><h3>{n}</h3><p>{d}</p><span class="more">Check rates &rarr;</span></div></a>' for n, i, d in rooms)
    book = f"""<form class="bookbar" data-demo><label>Check in<input type="date" aria-label="Check in"></label><label>Check out<input type="date" aria-label="Check out"></label><label>Guests<select aria-label="Guests"><option>2 adults</option><option>1 adult</option><option>2 adults, 1 child</option></select></label><label>Rooms<select aria-label="Rooms"><option>1</option><option>2</option></select></label><button class="btn">Check rates</button></form><p class="ok note" hidden style="color:#fff">Sample form. On a live site this opens the hotel's own booking engine.</p>"""
    body = f"""<section class="hero" style="padding:0"><div class="bg" style="background-image:url({HI}hero.jpg)"></div><div class="in"><div class="eyebrow" style="color:#fff;opacity:.9">Boutique hotel &nbsp;&middot;&nbsp; Larkspur Vale</div><h1>Slow mornings. <i>Long golden evenings.</i></h1><p>Garden rooms, a sunset pool and a kitchen that cooks with the valley.</p><div id="book">{book}</div></div><span class="tag">Stock photo. Client photos go here.</span></section>
<div class="marquee"><span>Sunset pool &nbsp;&middot;&nbsp; Garden villas &nbsp;&middot;&nbsp; Rooftop bar &nbsp;&middot;&nbsp; Private cabanas &nbsp;&middot;&nbsp; Weddings and gatherings &nbsp;&middot;&nbsp; Walk to the lake</span></div>
<section id="rooms"><div class="wrap"><div class="eyebrow">Stay</div><h2>Rooms and suites</h2><p class="lead">Each room type gets its own page with photos, size, beds and what is included, so guests can book with confidence.</p><div class="grid g3" style="margin-top:34px">{rc}</div></div></section>
<section class="band" style="padding:0"><div class="split" style="gap:0"><div class="ph" style="min-height:540px"><img src="{HI}infinity.jpg" alt="Hotel pool at sunset" loading="lazy"></div><div style="padding:clamp(48px,7vw,100px)"><div class="eyebrow">The pool</div><h2 style="color:#fff">Cabanas facing the sunset</h2><p class="lead" style="opacity:.85">Reserve a cabana for the afternoon, a birthday or just a slower day.</p><p style="margin-top:26px"><a class="btn" href="{HO}pool-cabanas-larkspur-vale/">Pool cabanas</a></p></div></div></section>
<section id="dining"><div class="wrap split"><div class="reveal"><div class="eyebrow">Dining</div><h2>The restaurant and rooftop bar</h2><p class="lead">Breakfast on the terrace, dinner from the wood fire, and cocktails as the light goes. Menus and hours live on their own pages so locals find them too.</p></div><div class="ph reveal" style="aspect-ratio:4/3"><img src="{HI}bar.jpg" alt="Guests at the bar" loading="lazy"></div></div></section>
<section id="events" style="padding-top:0"><div class="wrap split"><div class="ph reveal" style="aspect-ratio:4/3"><img src="{HI}beach.jpg" alt="Waterfront terrace at sunset" loading="lazy"></div><div class="reveal"><div class="eyebrow">Gatherings</div><h2>Weddings, retreats and dinners</h2><p class="lead">Spaces for 20 to 140 guests (sample), with one planner from first call to last dance.</p><p style="margin-top:24px"><a class="btn dark" href="#book">Plan an event (sample)</a></p></div></div></section>
<section id="faq" style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>Before you arrive</h2></div><div>{faq_html(HO_FAQ)}</div></div></section>"""
    sch = {"@context": "https://schema.org", "@type": "Hotel", "name": "Hotel Solenne (sample)", "description": "Fictional sample hotel site by LocalLift."}
    ho_page('', 'Hotel Solenne | Boutique hotel in Larkspur Vale', 'Sample boutique hotel website concept (fictional).', body, schema=[sch, faq_schema(HO_FAQ)], over=True)

    faqs = [('How many people fit in a cabana?', "The client's cabana size and capacity go here."),
            ('Can I reserve a cabana for a birthday?', 'Yes. Add a note when you book and the team will help plan it.'),
            ('Are cabanas available year round?', "The client's seasonal schedule goes here."),
            ('Do I need to be a hotel guest?', "The client's policy for day guests goes here."),
            ('Where is the hotel?', "The client's address and directions go here.")]
    inc = ''.join(f'<li>{x}</li>' for x in ['Covered shade for the afternoon', 'Lounge seating for a small group', 'Poolside drinks and bites', 'Towels and water service', 'Front row for the sunset', 'Reserve online or at the front desk'])
    body = f"""<section class="hero" style="padding:0;min-height:80vh"><div class="bg" style="background-image:url({HI}pool.jpg)"></div><div class="in"><div class="crumbs"><a href="{HO}">Home</a> / Pool cabanas in Larkspur Vale</div><div class="eyebrow" style="color:#fff;opacity:.9">Pool cabanas in Larkspur Vale</div><h1>Pool cabanas, <i>with the sunset included.</i></h1><a class="btn" href="{HO}#book">Check availability</a></div><span class="tag">Stock photo</span></section>
<section><div class="wrap"><div class="short"><b>The short answer</b>Our cabanas sit along the east side of the pool, facing the sunset, with covered shade for the afternoon. Each one seats a small group and can be reserved ahead. Availability changes by season.</div></div></section>
<section style="padding-top:0"><div class="wrap split"><div class="reveal"><div class="eyebrow">What is included</div><h2>Your spot, reserved</h2><ul class="list" style="columns:1">{inc}</ul></div><div class="ph reveal" style="aspect-ratio:4/5"><img src="{HI}sunset.jpg" alt="Pool deck at sunset" loading="lazy"></div></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>Cabana questions people ask</h2></div><div>{faq_html(faqs)}</div></div></section>
<section class="band" style="text-align:center"><div class="wrap"><h2 style="color:#fff">Make an afternoon of it</h2><p class="lead" style="margin:0 auto 26px">Pricing and availability are shown when you book.</p><a class="btn" href="{HO}#book">Check availability (sample)</a></div></section>"""
    ho_page('pool-cabanas-larkspur-vale', 'Pool cabanas in Larkspur Vale', 'Sample pool cabana landing page (fictional).', body, schema=[faq_schema(faqs)])


if __name__ == '__main__':
    med_spa(); medical(); hospitality(); print('others done')
