
magnets = document.querySelectorAll(".magnetic")

magnets.forEach((magnet) => {
    if(window.innerWidth > 540) {
        magnet.addEventListener("mousemove", function(e) {
            const position = magnet.getBoundingClientRect();

            const x = e.pageX - window.scrollX - position.left-position.width/2
            const y = e.pageY - window.scrollY - position.top-position.height/2;

            magnet.style.transform = "translate(" + x * 0.3 + "px, "+ y * 0.5 + "px)";
            magnet.style.transition = "all 0s linear";
            magnet.classList.remove("shake")
            
        })
        magnet.addEventListener("mouseleave", function(e) {
            magnet.style.transition = "all 0.2s cubic-bezier(0, 0, 0.72, 0.21";
            magnet.style.transform = "translate(0px, 0px)";

        })
    }
});

gsap.to("#freelance i", {
    scrollTrigger:{
        trigger: "#back",
        start: "50% 45%",
        end: "60% 60%",
        scrub: 2,
        // markers: true
    },
    rotate: "25deg",
    duration: 1

})
gsap.to("#denis", {
    scrollTrigger:{
        trigger: "#back",
        start: "50% 50%",
        end: "150% 150%",
        scrub: 3,
        // markers: true
    },
    x: 800,
    duration: 20,
})

