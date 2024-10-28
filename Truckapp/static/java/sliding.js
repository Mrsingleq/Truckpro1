// Function to show the next image in the slider
function nextImage(sliderId) {
    let slider = document.getElementById(sliderId);
    let images = slider.getElementsByTagName('img');
    let activeIndex = Array.from(images).findIndex(image => image.classList.contains('active'));
    
    // Remove the active class from the current image
    images[activeIndex].classList.remove('active');
    
    // Show the next image, looping back to the first one
    let nextIndex = (activeIndex + 1) % images.length;
    images[nextIndex].classList.add('active');
}

// Function to show the previous image in the slider
function prevImage(sliderId) {
    let slider = document.getElementById(sliderId);
    let images = slider.getElementsByTagName('img');
    let activeIndex = Array.from(images).findIndex(image => image.classList.contains('active'));
    
    // Remove the active class from the current image
    images[activeIndex].classList.remove('active');
    
    // Show the previous image, looping back to the last one
    let prevIndex = (activeIndex - 1 + images.length) % images.length;
    images[prevIndex].classList.add('active');
}