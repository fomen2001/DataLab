
document.getElementById("menu-toggle").addEventListener("click", function() {
  document.getElementById("nav-menu").classList.toggle("active");
});


document.addEventListener('DOMContentLoaded', function() {
    // Gestion du formulaire de recherche sur la page d'accueil
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
      searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Recherche effectuée !');
        // Ici, ajouter la logique de recherche
      });
    } // JavaScript pour l'effet de scintillement aléatoire
    document.addEventListener('DOMContentLoaded', () => {
        const title = document.querySelector('.wedding-title');
        
        setInterval(() => {
            title.style.textShadow = `
                0 0 ${10 + Math.random() * 20}px 
                rgba(255,215,0,${0.3 + Math.random() * 0.3})
            `;
        }, 300);

        // Animation au survol améliorée
        const button = document.querySelector('.advisor-button');
        button.addEventListener('mousemove', (e) => {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            button.style.setProperty('--x', `${x}px`);
            button.style.setProperty('--y', `${y}px`);
        });
    });
  
    // Gestion du formulaire de recherche de prestataire
    const providerSearchForm = document.getElementById('providerSearchForm');
    if (providerSearchForm) {
      providerSearchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Recherche de prestataire effectuée !');
      });
    }
  
    // Gestion du formulaire d'inscription pour devenir partenaire
    const partnerRegistrationForm = document.getElementById('partnerRegistrationForm');
    if (partnerRegistrationForm) {
      partnerRegistrationForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Votre demande de partenariat a été envoyée !');
      });
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('.wedding-title');
    const button = document.querySelector('.advisor-button');

    // Apparition progressive du titre et du bouton
    setTimeout(() => {
        title.style.opacity = '1';
        title.style.transition = 'opacity 1s ease-in';
    }, 500);

    setTimeout(() => {
        button.style.opacity = '1';
        button.style.transition = 'opacity 1s ease-in';
    }, 1000);

    // Effet scintillant sur le titre
    setInterval(() => {
        title.style.textShadow = `0 0 ${5 + Math.random() * 10}px rgba(255,215,0,${0.4 + Math.random() * 0.3})`;
    }, 300);
});

document.querySelectorAll('.reception-card').forEach(card => {
  card.addEventListener('mouseover', () => {
      card.classList.add('hovered');
  });
  
  card.addEventListener('mouseleave', () => {
      card.classList.remove('hovered');
  });
});

  
