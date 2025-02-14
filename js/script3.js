 // JavaScript pour l'animation au scroll
 const cards = document.querySelectorAll('.provider-card');

 const observer = new IntersectionObserver(entries => {
     entries.forEach(entry => {
         if (entry.isIntersecting) {
             entry.target.style.opacity = 1;
             entry.target.style.transform = 'translateY(0)';
         }
     });
 });

 cards.forEach((card, index) => {
     card.style.transition = `opacity 0.5s ${index * 0.2}s, transform 0.5s ${index * 0.2}s`;
     observer.observe(card);
 });