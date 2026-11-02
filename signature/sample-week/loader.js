/* LocalLift Signature: weekly sample loader. Built in images stay as the fallback. */
(function(){
  var B="https://thesocialdm.github.io/locallift-pulses/signature/sample-week/";
  var m=new Date().toLocaleString("en-US",{month:"long",year:"numeric"});
  function all(q,f){document.querySelectorAll(q).forEach(f)}
  function esc(s){return String(s).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
  function tpl(src,alt){return function(){return '<img class="full" src="'+src+'" alt="'+esc(alt)+'">'}}
  all(".js-month",function(e){e.textContent=m});
  fetch(B+"week.json?d="+new Date().toISOString().slice(0,10)).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(w){
    var v="?v="+w.date, cards=document.querySelectorAll("#week .ig");
    w.posts.forEach(function(p,i){
      if(window.SIGT) window.SIGT[p.key]=tpl(B+p.img+v,p.alt);
      if(window.SIGCAP) window.SIGCAP[p.key]=p.caption;
      var c=cards[i]; if(c){var b=c.querySelector(".day b"),s=c.querySelector(".day span"); if(b)b.textContent=p.label; if(s)s.textContent=p.day}
    });
    (w.tiles||[]).forEach(function(t){if(window.SIGT) window.SIGT[t.key]=tpl(B+t.img+v,t.alt)});
    if(window.sigRender) window.sigRender();
    if(window.sigSetG) window.sigSetG(w.posts.map(function(p){return [B+p.google_img+v,p.google]}));
    if(w.data_note) all(".js-datanote",function(e){e.textContent=w.data_note});
    if(w.float){var fg=document.querySelector(".f-g");if(fg&&fg.lastChild)fg.lastChild.textContent=w.float}
    if(w.brief){
      var x=document.querySelector(".js-bstats");
      if(x&&w.brief.stats) x.innerHTML=w.brief.stats.map(function(a){return "<div><b>"+esc(a[0])+"</b><span>"+esc(a[1])+"</span></div>"}).join("");
      if(w.brief.line) all(".js-bline",function(e){e.textContent=w.brief.line});
      if(w.brief.say) all(".js-bsay",function(e){e.textContent=w.brief.say});
      if(w.brief.src) all(".js-briefsrc",function(e){e.textContent=w.brief.src});
      if(w.brief.headline) all(".bp-hero strong",function(e){e.textContent=w.brief.headline});
      var bs=document.querySelector(".bp-stats");
      if(bs&&w.brief.stats) bs.innerHTML=w.brief.stats.map(function(a){return "<div><b>"+esc(a[0])+"</b><span>"+esc(a[1])+"</span></div>"}).join("");
      var bq=document.querySelector(".bp-say");
      if(bq&&w.brief.say){var ti=bq.querySelector("i");bq.textContent=w.brief.say.replace(/[“”]/g,"");if(ti)bq.insertBefore(ti,bq.firstChild)}
    }
  }).catch(function(){});
})();
