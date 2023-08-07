var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 60,
  loop: true,
  autoplay: {
    delay: 1000,
  },
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    // when window width is >= 640px
    720: {
      slidesPerView: 2,
      spaceBetween: 40
    },
    920: {
      slidesPerView: 3,
      spaceBetween: 60
    }
  }
});


var swiper = new Swiper(".mySwiper_1", {
  slidesPerView: 3,
  spaceBetween: 60,
  loop: true,
  autoplay: {
    delay: 1000,
  },
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    // when window width is >= 480px
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    // when window width is >= 640px
    720: {
      slidesPerView: 2,
      spaceBetween: 40
    },
    920: {
      slidesPerView: 3,
      spaceBetween: 60
    }
  }
});
