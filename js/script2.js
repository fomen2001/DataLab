document.addEventListener("DOMContentLoaded", function() {
    let images = [
        "../assets/images/ly.jpg",
        "../assets/images/ly.jpg",
        "../assets/images/ly.jpg",
        "../assets/images/ly.jpg"
    ];
    
    let mainImage = document.getElementById("mainImage");
    let thumbnails = document.querySelectorAll(".thumb");
    let index = 0;

    function changeImage(src) {
        mainImage.style.opacity = "0";
        setTimeout(() => {
            mainImage.src = src;
            mainImage.style.opacity = "1";
        }, 300);
        
        thumbnails.forEach(img => img.classList.remove("active"));
        document.querySelector(`img[src="${src}"]`).classList.add("active");
    }

    document.querySelector(".prev").addEventListener("click", function() {
        index = (index - 1 + images.length) % images.length;
        changeImage(images[index]);
    });

    document.querySelector(".next").addEventListener("click", function() {
        index = (index + 1) % images.length;
        changeImage(images[index]);
    });

    thumbnails.forEach(img => {
        img.addEventListener("click", function() {
            changeImage(this.src);
        });
    });
});
