let currentSlide = 0;

function changeSlide(direction) {
  const slides = document.querySelectorAll('.slide');
  currentSlide += direction;

  if (currentSlide < 0) {
    currentSlide = slides.length - 1;
  } else if (currentSlide >= slides.length) {
    currentSlide = 0;
  }

  const slideWidth = slides[0].clientWidth;
  document.querySelector('.slides').style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}
