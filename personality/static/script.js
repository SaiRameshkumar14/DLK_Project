  // JavaScript for the hero slider
  let slideIndex = 0;
  const slides = document.querySelectorAll('.hero-slide');

  function showSlides() {
    slides.forEach(slide => slide.style.opacity = 0);
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1; }
    slides[slideIndex - 1].style.opacity = 1;
    setTimeout(showSlides, 3000); // Change slide every 3 seconds
  }

  showSlides();