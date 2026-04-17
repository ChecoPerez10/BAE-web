
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('menuBtn');
    const menuLista = document.getElementById('menuLista');
    
    if (menuBtn && menuLista) {
        menuBtn.addEventListener('click', function() {
            menuLista.classList.toggle('activo');
            
            // Animar lineas del menu hamburguesa
            const lineas = menuBtn.querySelectorAll('.navegacion__menu-linea');
            lineas.forEach((linea, index) => {
                linea.classList.toggle('activo');
            });
        });
        
        // Cerrar menu al hacer clic en un enlace
        const enlaces = menuLista.querySelectorAll('.navegacion__enlace');
        enlaces.forEach(enlace => {
            enlace.addEventListener('click', function() {
                menuLista.classList.remove('activo');
            });
        });
    }
    
    // Smooth scroll para navegacion
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animacion de scroll reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Observar elementos animables
    document.querySelectorAll('.caracteristica, .miembro, .flip-card').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
});

// Navbar scroll effect
let lastScroll = 0;
const navbar = document.querySelector('.navegacion');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > lastScroll && currentScroll > 100) {
        navbar.style.transform = 'translateY(-100%)';
    } else {
        navbar.style.transform = 'translateY(0)';
    }
    
    lastScroll = currentScroll;
});

// PWA Install prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    console.log('PWA install prompt available');
});
