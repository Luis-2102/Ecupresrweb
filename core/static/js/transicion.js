const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        requestAnimationFrame(() => {
          entry.target.classList.add('visible');
        });
      } else {
        entry.target.classList.remove('visible');
      }
    });
  }, {
    threshold: 0.0000001
  });
  
  document.querySelectorAll('.animado').forEach(el => observer.observe(el));
  