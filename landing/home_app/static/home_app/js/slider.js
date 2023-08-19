var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 60,
  loop: true,
  autoplay: {
    delay: 5000,
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
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
  spaceBetween: 50,
  loop: true,
  autoplay: {
    delay: 2000,
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10
    },
    480: {
      slidesPerView: 1,
      spaceBetween: 30
    },
    720: {
      slidesPerView: 2,
      spaceBetween: 40
    },
    920: {
      slidesPerView: 3,
      spaceBetween: 50
    }
  }
});
