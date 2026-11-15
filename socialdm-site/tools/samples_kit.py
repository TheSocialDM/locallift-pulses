"""Shared kit for the /samples demo sites (fictional businesses, noindex).
Each industry script calls page(...) to write src/samples/<ind>/<path>/index.html.
"""
import json, os, html

ROOT = os.path.join(os.path.dirname(__file__), '..', 'src', 'samples')

BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--sans);color:var(--ink);background:var(--bg);line-height:1.65;font-weight:var(--wt,400);-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
.sample{background:#111;color:#fff;font:500 11px/1.4 var(--sans);letter-spacing:.14em;text-transform:uppercase;text-align:center;padding:8px 12px;position:relative;z-index:60}
.sample a{text-decoration:underline}
.nav{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:18px 5vw;background:var(--navbg);color:var(--navink);transition:background .3s,box-shadow .3s}
.nav.over{position:absolute;left:0;right:0;top:auto;background:transparent;color:#fff}
.nav.solid{position:fixed;top:0;background:var(--navbg);color:var(--navink);box-shadow:0 1px 0 var(--line)}
.brand{font-family:var(--serif);font-size:24px;line-height:1.05;letter-spacing:var(--brandls,.02em)}
.brand small{display:block;font:500 9.5px/1.6 var(--sans);letter-spacing:.32em;text-transform:uppercase;opacity:.8;margin-top:3px}
.menu{display:flex;gap:26px;align-items:center;font-size:12.5px;letter-spacing:.16em;text-transform:uppercase}
.menu a{opacity:.92}.menu a:hover{opacity:1;text-decoration:underline;text-underline-offset:6px}
.burger{display:none;background:none;border:0;color:inherit;font-size:26px;cursor:pointer}
.btn{display:inline-block;font:500 12px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;padding:16px 26px;background:var(--acc);color:var(--accink);border:1px solid var(--acc);cursor:pointer;transition:transform .2s,opacity .2s}
.btn:hover{transform:translateY(-1px);opacity:.92}
.btn.line{background:transparent;color:inherit;border-color:currentColor}
.btn.dark{background:var(--deep);border-color:var(--deep);color:#fff}
.eyebrow{font:500 11.5px/1.4 var(--sans);letter-spacing:.3em;text-transform:uppercase;color:var(--acc2)}
h1,h2,h3,h4{font-family:var(--serif);font-weight:var(--hw,400);line-height:1.08;letter-spacing:var(--hls,0)}
h2{font-size:clamp(32px,4vw,52px);margin:12px 0 18px}
h3{font-size:clamp(21px,2vw,27px)}
section{padding:clamp(64px,9vw,120px) 5vw}
.wrap{max-width:1200px;margin:0 auto}
.lead{font-size:18px;max-width:620px;opacity:.88}
.hero{position:relative;min-height:94vh;display:flex;align-items:flex-end;color:#fff;overflow:hidden}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;transform:scale(1.06);animation:slow 18s ease-out forwards}
@keyframes slow{to{transform:scale(1)}}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.42) 0%,rgba(0,0,0,.05) 38%,rgba(0,0,0,.62) 100%)}
.hero .in{position:relative;z-index:2;padding:0 5vw 9vh;width:100%}
.hero h1{font-size:clamp(46px,7.4vw,108px);max-width:1000px}
.hero p{font-size:19px;max-width:560px;margin:18px 0 30px;opacity:.95}
.tag{position:absolute;right:14px;bottom:12px;z-index:3;font:500 10px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;background:rgba(0,0,0,.45);color:#fff;padding:6px 8px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,6vw,90px);align-items:center}
.ph{position:relative;overflow:hidden;background:var(--line)}
.ph img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s}
.ph:hover img{transform:scale(1.04)}
.ph[style*="min-height"] img{position:absolute;inset:0;height:100%}
.grid{display:grid;gap:28px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
.card .ph{aspect-ratio:4/3}
.card h3{margin:16px 0 6px}
.meta{font-size:13.5px;letter-spacing:.06em;opacity:.75}
.price{font-family:var(--serif);font-size:26px}
.pill{position:absolute;top:14px;left:14px;z-index:2;background:var(--bg);color:var(--ink);font:500 10.5px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;padding:8px 10px}
.save{position:absolute;top:12px;right:12px;z-index:2;width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.9);display:grid;place-items:center;font-size:17px;cursor:pointer;border:0;color:#222}
.save.on{color:#c0392b}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats div{padding:34px 24px;border-right:1px solid var(--line)}
.stats div:last-child{border-right:0}
.stats b{display:block;font-family:var(--serif);font-weight:400;font-size:clamp(34px,3.6vw,50px);line-height:1}
.stats span{font-size:13px;letter-spacing:.12em;text-transform:uppercase;opacity:.7}
.band{background:var(--deep);color:#fff}
.band .eyebrow{color:var(--acc)}
.short{border-left:3px solid var(--acc);background:var(--soft);padding:22px 26px;margin:26px 0;font-size:17px}
.short b{display:block;font:600 11px/1.4 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--acc2);margin-bottom:6px}
details{border-bottom:1px solid var(--line);padding:20px 0}
summary{cursor:pointer;list-style:none;font-size:18px;font-family:var(--serif);display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";color:var(--acc2);font-family:var(--sans)}
details[open] summary:after{content:"\2212"}
details p{margin-top:12px;font-size:15.5px;opacity:.88;max-width:760px}
.form{display:grid;gap:12px}
.form input,.form select,.form textarea{font:400 15px var(--sans);padding:15px 16px;border:1px solid var(--line);background:#fff;color:#222;width:100%}
.form .row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.note{font-size:12.5px;opacity:.7;margin-top:10px}
.crumbs{font-size:12px;letter-spacing:.12em;text-transform:uppercase;opacity:.7;margin-bottom:14px}
.crumbs a{text-decoration:underline;text-underline-offset:4px}
.list{list-style:none;columns:2;gap:40px}
.list li{padding:10px 0;border-bottom:1px solid var(--line);break-inside:avoid;font-size:15.5px}
.steps{counter-reset:s;display:grid;gap:0}
.steps li{list-style:none;counter-increment:s;display:grid;grid-template-columns:70px 1fr;gap:10px;padding:26px 0;border-top:1px solid var(--line)}
.steps li:before{content:"0" counter(s);font-family:var(--serif);font-size:30px;color:var(--acc2)}
.steps b{display:block;font-family:var(--serif);font-weight:400;font-size:22px;margin-bottom:4px}
footer{background:var(--foot);color:#d9d6d0;padding:70px 5vw 34px;font-size:14px}
footer .cols{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;max-width:1200px;margin:0 auto}
footer h4{font:600 11px/1.4 var(--sans);letter-spacing:.24em;text-transform:uppercase;color:#fff;margin-bottom:14px}
footer a{display:block;padding:4px 0;opacity:.85}
footer .legal{max-width:1200px;margin:46px auto 0;padding-top:22px;border-top:1px solid rgba(255,255,255,.15);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:12px;opacity:.75}
.reveal{opacity:0;transform:translateY(26px);transition:opacity .9s ease,transform .9s ease}
.reveal.in{opacity:1;transform:none}
.marquee{overflow:hidden;white-space:nowrap;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:18px 0;font-family:var(--serif);font-size:clamp(22px,2.6vw,34px)}
.marquee span{display:inline-block;animation:mq 38s linear infinite;padding-left:100%}
@keyframes mq{to{transform:translateX(-100%)}}
@media(max-width:900px){
 .menu{display:none;position:absolute;top:100%;left:0;right:0;flex-direction:column;align-items:flex-start;gap:0;background:var(--navbg);color:var(--navink);padding:10px 5vw 20px;box-shadow:0 10px 30px rgba(0,0,0,.12)}
 .menu.open{display:flex}.menu a{padding:12px 0;width:100%}
 .burger{display:block}
 .split,.g2,.g3{grid-template-columns:1fr}.g4,.stats{grid-template-columns:1fr 1fr}
 .stats div:nth-child(2){border-right:0}
 footer .cols{grid-template-columns:1fr 1fr}
 .list{columns:1}.form .row{grid-template-columns:1fr}
 .hero{min-height:86vh}
 .ph[style*="min-height"]{min-height:320px!important}
}
@media(max-width:560px){.g4{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none}.hero .bg,.marquee span{animation:none}}
"""

BASE_JS = r"""
(function(){
var n=document.querySelector('.nav'),b=document.querySelector('.burger'),m=document.querySelector('.menu');
if(b)b.addEventListener('click',function(){m.classList.toggle('open');b.setAttribute('aria-expanded',m.classList.contains('open'))});
if(n&&n.classList.contains('over')){var h=document.querySelector('.hero');window.addEventListener('scroll',function(){n.classList.toggle('solid',window.scrollY>(h?h.offsetHeight-90:200))},{passive:true})}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});
document.querySelectorAll('.save').forEach(function(s){s.addEventListener('click',function(ev){ev.preventDefault();s.classList.toggle('on');s.textContent=s.classList.contains('on')?'♥':'♡'})});
document.querySelectorAll('form[data-demo]').forEach(function(f){f.addEventListener('submit',function(ev){ev.preventDefault();var o=f.querySelector('.ok');if(o){o.hidden=false}})});
})();
"""


def esc(s):
    return html.escape(s, quote=True)


def page(ind, path, *, title, desc, theme_css, fonts, brand_html, menu, cta, body,
         footer_html, schema=None, over=False, extra_css='', extra_js='', sample_line=''):
    out_dir = os.path.join(ROOT, ind, path) if path else os.path.join(ROOT, ind)
    os.makedirs(out_dir, exist_ok=True)
    menu_html = ''.join(f'<a href="{h}">{esc(t)}</a>' for t, h in menu)
    sc = ''
    for s in (schema or []):
        sc += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>'
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>{theme_css}{BASE_CSS}{extra_css}</style>{sc}</head><body>
<div class="sample">{sample_line}</div>
<header class="nav{' over' if over else ''}"><a class="brand" href="/samples/{ind}/">{brand_html}</a>
<nav class="menu" id="menu">{menu_html}<a class="btn" href="{cta[1]}">{esc(cta[0])}</a></nav>
<button class="burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false">&#9776;</button></header>
<main>{body}</main>
{footer_html}
<script>{BASE_JS}{extra_js}</script></body></html>"""
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(doc)
    return out_dir
