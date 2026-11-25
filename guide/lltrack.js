/* LocalLift lead tracking for prospect facing agent pages (team/<prop>/leasing/ and card/).
   One file for every property. Loaded by tools/lead_track.py:
   <script src="../../../guide/lltrack.js?v=1" data-llprop="montage" defer></script>
   Every tap on a lead button fires ONE GA4 event:
     lead_action {property, staff, action, src, place}
   action: call, text, email, tour, apply, homes, directions, save_contact, mia, special,
           specials_signup, share, website, profile
   src: qr, link, card, app (staff opened their own page from the app), unknown
   No prospect names, phones or emails are ever sent. src=preview (the app's "See what renters see") sends nothing.
   Events go out with transport_type beacon so they survive the page leaving for tel:, sms:, mailto: or another site. */
(function(){
var S=document.currentScript;if(!S||window.__llLT)return;window.__llLT=1;
var GA='G-FC39M4P67G',P=(S.dataset.llprop||'').toLowerCase().replace(/[^a-z-]/g,'');
var q;try{q=new URLSearchParams(location.search)}catch(e){q={get:function(){return null}}}
var raw=String(q.get('src')||'').toLowerCase();
if(raw==='preview')return;
var CARD=/\/card\/?$/.test(location.pathname.replace(/index\.html$/,''));
var SRC=CARD?'card':({qr:'qr',link:'link',card:'card',app:'app'}[raw]||'');
if(!SRC){try{SRC=sessionStorage.getItem('ll-src')||''}catch(e){}}
if(!SRC)SRC='unknown';
try{if(raw)sessionStorage.setItem('ll-src',SRC)}catch(e){}
var cl=function(v){return String(v||'').replace(/[^A-Za-z .'-]/g,'').trim().slice(0,30)};
function staff(){var n=cl(window.llBy)||cl(q.get('by'));if(!n){try{n=cl(sessionStorage.getItem('ll-by')||sessionStorage.getItem('llsw-by'))}catch(e){}}
 if(!n||/^team$/i.test(n))return 'team';return n.split(' ')[0].replace(/\b\w/g,function(c){return c.toUpperCase()})}
/* GA4: load gtag.js once if the page has none */
window.dataLayer=window.dataLayer||[];
if(typeof window.gtag!=='function'){window.gtag=function(){dataLayer.push(arguments)};
 var g=document.createElement('script');g.async=true;g.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(g);
 gtag('js',new Date());}
gtag('config',GA,{property:P,staff:staff(),src:SRC});
function send(action,place){try{gtag('event','lead_action',{property:P,staff:staff(),action:action,src:SRC,place:place||'page',transport_type:'beacon'})}catch(e){}}
window.llLead=send;
function kind(a){var d=a.getAttribute('data-ll');if(d)return d;
 var h=(a.getAttribute('href')||'').toLowerCase(),t=(a.textContent||'').toLowerCase(),id=a.id||'';
 if(id==='share')return 'share';
 if(id==='vcf'||/^data:text\/vcard/.test(h))return 'save_contact';
 if(/^tel:/.test(h))return 'call';
 if(/^sms:/.test(h))return 'text';
 if(/^mailto:/.test(h))return 'email';
 if(/google\.[a-z.]+\/maps|maps\.apple\.com|maps\.google\./.test(h))return 'directions';
 if(/schedule-?tour|\/tour\b|book.*tour/.test(h)||/book my tour|tour/.test(t)&&!/floorplan/.test(h))return 'tour';
 if(/\bapply\b/.test(t)||/\/apply\b/.test(h))return 'apply';
 if(a.closest('#offer')||/special/.test(t))return 'special';
 if(/floorplan|availab|\/homes?\b/.test(h))return 'homes';
 if(CARD&&a.classList.contains('go'))return 'profile';
 if(/^https?:/.test(h))return 'website';
 return ''}
function where(a){if(a.closest('.llg'))return 'mia';if(a.closest('.btns'))return 'top';if(a.closest('.card .stack,.card'))return 'card';if(a.closest('#offer'))return 'offer';if(a.closest('.sec'))return 'section';if(a.closest('.opt'))return 'signup';return 'page'}
document.addEventListener('click',function(e){try{
 var t=e.target;if(!t||!t.closest)return;
 var mia=t.closest('.llg');
 if(mia){if(t.closest('.llg-b')){if(!mia.classList.contains('on'))send('mia','mia');return}
  var ml=t.closest('.llg-a a');if(ml){var k0=kind(ml);send(k0==='homes'?'special':(k0||'mia'),'mia')}return}
 var a=t.closest('a[href],button');if(!a)return;
 if(a.tagName==='BUTTON'&&a.type==='submit')return;
 var k=kind(a);if(k)send(k,where(a))}catch(x){}},true);
/* Specials by email: count a valid sign up, never the address */
document.addEventListener('submit',function(e){try{var f=e.target;if(!f||f.id!=='optF')return;
 var em=f.querySelector('input[type=email]'),hp=f.querySelector('input[name=website]');
 if(em&&/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test((em.value||'').trim())&&!(hp&&hp.value))send('specials_signup','signup')}catch(x){}},true);
/* card sample: the live profile link carries the agent and src=card */
if(CARD){var go=document.querySelector('a.go');if(go){var n=staff();go.setAttribute('href','../?'+(n!=='team'?'by='+encodeURIComponent(n)+'&':'')+'src=card')}}
})();
