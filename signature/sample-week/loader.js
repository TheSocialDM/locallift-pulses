/* LocalLift Signature: weekly sample loader. Built in images stay as the fallback. */
(function(){
  var B="https://cdn.jsdelivr.net/gh/TheSocialDM/locallift-pulses@main/signature/sample-week/";
  var m=new Date().toLocaleString("en-US",{month:"long",year:"numeric"});
  document.querySelectorAll(".js-month").forEach(function(e){e.textContent=m});
  fetch(B+"week.json?d="+new Date().toISOString().slice(0,10)).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(w){
    var v="?v="+w.date, cards=document.querySelectorAll("#week .ig");
    w.posts.forEach(function(p,i){
      var src=B+p.img+v, alt=p.alt;
      if(window.SIGT) window.SIGT[p.key]=function(){return '<img class="full" src="'+src+'" alt="'+alt.replace(/"/g,"&quot;")+'">'};
      if(window.SIGCAP) window.SIGCAP[p.key]=p.caption;
      var c=cards[i]; if(c){var b=c.querySelector(".day b"),s=c.querySelector(".day span"); if(b)b.textContent=p.label; if(s)s.textContent=p.day}
    });
    if(window.sigRender) window.sigRender();
    if(window.sigSetG) window.sigSetG(w.posts.map(function(p){return [B+p.google_img+v,p.google]}));
    var n=document.querySelector(".js-datanote"); if(n&&w.data_note) n.textContent=w.data_note;
  }).catch(function(){});
})();
