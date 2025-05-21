const carouselDiv = document.getElementById('carousel');
const images = JSON.parse(carouselDiv.dataset.images.replace(/&quot;/g, '"'));

let currentIndex = 0;
const imgElement = document.getElementById('carouselImage');

setInterval(() => {
currentIndex = (currentIndex + 1) % images.length;
imgElement.style.opacity = 0;
setTimeout(() => {
    imgElement.src = images[currentIndex];
    imgElement.style.opacity = 1;
}, 500);
}, 3000);