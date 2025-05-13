// contact-form.js
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('contactForm');
  
  form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      // Mostrar loading
      const loadingDiv = form.querySelector('.loading');
      const errorDiv = form.querySelector('.error-message');
      const successDiv = form.querySelector('.sent-message');
      
      loadingDiv.classList.add('d-block');
      errorDiv.classList.remove('d-block');
      successDiv.classList.remove('d-block');
      
      // Crear FormData
      const formData = new FormData(form);
      
      // Enviar petición
      fetch('/contact/', {  // Asegúrate de que esta ruta coincida con tu urls.py
          method: 'POST',
          body: formData,
          headers: {
              'X-Requested-With': 'XMLHttpRequest'
          }
      })
      .then(response => response.json())
      .then(data => {
          loadingDiv.classList.remove('d-block');
          
          if (data.status === 'success') {
              successDiv.classList.add('d-block');
              form.reset();
          } else {
              errorDiv.textContent = data.message || 'Ocurrió un error al enviar el mensaje';
              errorDiv.classList.add('d-block');
          }
      })
      .catch(error => {
          loadingDiv.classList.remove('d-block');
          errorDiv.textContent = 'Error al enviar el mensaje. Por favor, inténtalo de nuevo.';
          errorDiv.classList.add('d-block');
      });
  });
});