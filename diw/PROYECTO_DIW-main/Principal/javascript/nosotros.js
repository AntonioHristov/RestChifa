var slides = document.querySelectorAll('#imagenes img');
var dots = document.querySelectorAll('#dots .dot');
var currentSlide = 0;
var slideInterval = setInterval(nextSlide, 3000);

window.onload = function(){
    for(var i = 0; i > slides; i++){
        slides[i].classList.remove("active");
    }
        slides[0].classList.add("active");
}

function nextSlide() {
  slides[currentSlide].classList.remove('active');
  dots[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
  dots[currentSlide].classList.add('active');
}

for (var i = 0; i < dots.length; i++) {
  dots[i].addEventListener('click', function() {
    var index = Number(this.getAttribute('data-index'));
    if (index !== currentSlide) {
      slides[currentSlide].classList.remove('active');
      dots[currentSlide].classList.remove('active');
      currentSlide = index;
      slides[currentSlide].classList.add('active');
      dots[currentSlide].classList.add('active');
      clearInterval(slideInterval);
      slideInterval = setInterval(nextSlide, 3000);
    }
  });
}
