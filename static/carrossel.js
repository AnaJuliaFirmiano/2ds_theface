const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const items = document.querySelectorAll('.item');
    let currentIndex = 0;
  
    function updateCarousel() {
      items.forEach((item, index) => {
        if (index === currentIndex) {
          item.classList.add('active');
          item.classList.remove('hidden');
        } else {
          item.classList.remove('active');
          item.classList.add('hidden');
        }
      });
    }
  
    prevButton.addEventListener('click', () => {
      currentIndex = (currentIndex === 0) ? items.length - 1 : currentIndex - 1;
      updateCarousel();
    });
  
    nextButton.addEventListener('click', () => {
      currentIndex = (currentIndex === items.length - 1) ? 0 : currentIndex + 1;
      updateCarousel();
    });
  
    updateCarousel();