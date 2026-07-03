/* NorthStar shared interactions */
(function(){
  'use strict';
  var yr=document.getElementById('yr'); if(yr) yr.textContent=new Date().getFullYear();

  var h=document.getElementById('top-header');
  if(h){ var os=function(){h.classList.toggle('scrolled',window.scrollY>18)}; os(); addEventListener('scroll',os,{passive:true}); }

  var mob=document.getElementById('mobile'), burger=document.getElementById('burger'), mclose=document.getElementById('mclose');
  function closeM(){mob.classList.remove('open');mob.setAttribute('aria-hidden','true');document.body.style.overflow='';}
  if(burger) burger.onclick=function(){mob.classList.add('open');mob.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';};
  if(mclose) mclose.onclick=closeM;
  if(mob) mob.querySelectorAll('a').forEach(function(a){a.onclick=closeM;});

  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
  var revs=document.querySelectorAll('.rev');
  if(revs.length&&'IntersectionObserver' in window&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    revs.forEach(function(el){io.observe(el);});
  } else { revs.forEach(function(el){el.classList.add('in');}); }

  // video play/pause toggle
  var vb=document.querySelector('[data-vidbtn]');
  if(vb){
    var v=document.getElementById(vb.getAttribute('data-vidbtn'));
    function lbl(){var p=v&&!v.paused; vb.querySelector('.lb').textContent=p?'Pause':'Play'; vb.querySelector('.ip').style.display=p?'none':'inline'; vb.querySelector('.ipp').style.display=p?'inline':'none';}
    vb.onclick=function(){ if(!v)return; if(v.paused)v.play(); else v.pause(); lbl(); };
    if(v){v.addEventListener('play',lbl);v.addEventListener('pause',lbl);} lbl();
  }

  // contact form (Web3Forms) with graceful fallback
  var f=document.getElementById('contactForm');
  if(f){
    var st=document.getElementById('fstatus');
    f.addEventListener('submit',function(ev){
      var k=f.querySelector('[name=access_key]').value;
      if(!k||k==='YOUR_WEB3FORMS_ACCESS_KEY'){ev.preventDefault();st.style.display='block';st.style.color='#B4913F';st.textContent='Form ready — add your Web3Forms key to enable delivery. Meanwhile, email hello@northstarchilddevelopmentservices.com.';return;}
      ev.preventDefault();st.style.display='block';st.style.color='#5a6b82';st.textContent='Sending…';
      fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}}).then(function(r){if(r.ok){f.reset();st.style.color='#2E7D74';st.textContent='Thank you — we received your message and will reply within one business day.';}else{st.style.color='#b00020';st.textContent='Something went wrong. Please email hello@northstarchilddevelopmentservices.com.';}}).catch(function(){st.style.color='#b00020';st.textContent='Network error. Please email hello@northstarchilddevelopmentservices.com.';});
    });
  }
})();
