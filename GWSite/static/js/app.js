let controller;
let slideScene;

function animateSlides() {
  controller = new ScrollMagic.Controller();
  const sliders = document.querySelectorAll(".card-page");
  sliders.forEach((slide, index, slides) => {
    const revealImg = slide.querySelector(".reveal-img");
    const revealText = slide.querySelector(".reveal-text");
    const slideTl = gsap.timeline({
      defaults: { duration: 0.8, ease: "power2.out" },
    });
    slideTl.fromTo(revealImg, { scale: "0.9", opacity: "0" }, { scale: "1", opacity:"1" });
    slideTl.fromTo(revealText, { scale: "0.9", opacity: "0" }, { scale: "1", opacity:"1" });
    slideScene = new ScrollMagic.Scene({
      triggerElement: slide,
      triggerHook: 0.6,
      reverse: false,
    })
      .setTween(slideTl)
      .addIndicators({
        colorStart: "black",
        colorTrigger: "black",
        name: "slide",
      })
      .addTo(controller);
    //New Animation
    // const pageTl = gsap.timeline();
    // let nextSlide = slides.length - 1 === index ? "end" : slides[index + 1];
    // pageTl.fromTo(nextSlide, { y: "0%" }, { y: "50%" });
    // pageTl.fromTo(slide, { opacity: 1, scale: 1 }, { opacity: 0, scale: 0.5 });
    // pageTl.fromTo(nextSlide, { y: "50%" }, { y: "0%" }, "-=0.5");
    // //Create new scene
    // pageScene = new ScrollMagic.Scene({
    //   triggerElement: slide,
    //   duration: "100%",
    //   triggerHook: 0,
    // })
    //   // .addIndicators({
    //   //   colorStart: "black",
    //   //   colorTrigger: "black",
    //   //   name: "page",
    //   //   indent: 200,
    //   // })
    //   .setPin(slide, { pushFollowers: false })
    //   .setTween(pageTl)
    //   .addTo(controller);
  });
}

animateSlides();

$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav').addClass('shrink');
  } else {
    $('nav').removeClass('shrink');
  }
});

document.addEventListener('DOMContentLoaded', () => {
  function animateSgv (id, anim_time, delay, delayIncrement){
      const logo = document.getElementById(id);
      const logoPaths = document.querySelectorAll(`#${id} path`);
      delay = delay;
      for(let i = 0; i < logoPaths.length;i++){
          //console.log(logoPaths[i].getTotalLength());
          logoPaths[i].style.strokeDasharray  = logoPaths[i].getTotalLength();
          logoPaths[i].style.strokeDashoffset = logoPaths[i].getTotalLength();
          logoPaths[i].style.animation = `line-anim ${anim_time}s ease forwards ${delay}s`;
          delay+=delayIncrement;
          console.log(delay)
      }
      logo.style.animation = `fill 0.5s ease forwards ${delay}s`;
  }
  animateSgv('logo', 1.5, 0, 0.43)
  animateSgv('logo2', 15, 0, 3.1)
}, false);


document.addEventListener('DOMContentLoaded', () => {
  function animateSgv2 (id, delay, delayIncrement){
      const logo = document.getElementById(id);
      const logoPaths = document.querySelectorAll(`#${id} path`);
      delay = delay;
      for(let i = 0; i < logoPaths.length;i++){
          //console.log(logoPaths[i].getTotalLength());
          logoPaths[i].style.strokeDasharray  = logoPaths[i].getTotalLength();
          logoPaths[i].style.strokeDashoffset = logoPaths[i].getTotalLength();
          logoPaths[i].style.animation = `line-anim 8s ease forwards ${delay}s`;
          delay+=delayIncrement;
          console.log(delay)
      }
      logo.style.animation = `fill3 0.5s ease forwards ${delay}s`;
  }
  animateSgv2('logo3', 0, 6)
}, false);