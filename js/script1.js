document.querySelectorAll('.image-item').forEach(item => {
    item.addEventListener('mouseover', () => {
        item.classList.add('hovered');
    });

    item.addEventListener('mouseleave', () => {
        item.classList.remove('hovered');
    });
});
