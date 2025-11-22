// ============================================
// NAVBAR Y SCROLL SUAVE - VANILLA JAVASCRIPT
// ============================================

(function() {
    'use strict';
    
    // Elementos del DOM
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    const menuOverlay = document.querySelector('.menu-overlay');
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    const navbar = document.querySelector('.navbar');
    const body = document.body;
    
    // ============================================
    // TOGGLE MENÚ HAMBURGUESA
    // ============================================
    function toggleMenu() {
        const isActive = hamburger && hamburger.classList.contains('active');
        
        if (isActive) {
            closeMenu();
        } else {
            openMenu();
        }
    }
    
    function openMenu() {
        if (hamburger) hamburger.classList.add('active');
        if (mobileMenu) mobileMenu.classList.add('active');
        if (menuOverlay) menuOverlay.classList.add('active');
        body.classList.add('menu-open');
    }
    
    function closeMenu() {
        if (hamburger) hamburger.classList.remove('active');
        if (mobileMenu) mobileMenu.classList.remove('active');
        if (menuOverlay) menuOverlay.classList.remove('active');
        body.classList.remove('menu-open');
    }
    
    // Event listeners para el hamburguesa
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }
    
    // Cerrar menú al hacer clic en overlay
    if (menuOverlay) {
        menuOverlay.addEventListener('click', closeMenu);
    }
    
    // ============================================
    // SCROLL SUAVE A SECCIONES
    // ============================================
    function smoothScroll(e) {
        e.preventDefault();
        
        let targetId = this.getAttribute('href');
        if (!targetId) return;
        
        // Manejar enlaces con index.html#seccion o solo #seccion
        if (targetId.includes('#')) {
            targetId = '#' + targetId.split('#')[1];
        } else if (!targetId.startsWith('#')) {
            return; // No es un enlace de anchor, dejar que el navegador lo maneje
        }
        
        const targetSection = document.querySelector(targetId);
        if (!targetSection) {
            // Si no encuentra la sección, puede ser que estemos en otra página
            // Intentar navegar a index.html con el anchor
            if (targetId.startsWith('#')) {
                window.location.href = `index.html${targetId}`;
            }
            return;
        }
        
        const navbarHeight = navbar ? navbar.offsetHeight : 0;
        const targetPosition = targetSection.offsetTop - navbarHeight;
        
        // Cerrar menú móvil si está abierto
        closeMenu();
        
        // Actualizar enlace activo
        updateActiveLink(this);
        
        // Scroll suave
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
    
    // Aplicar scroll suave a todos los enlaces
    navLinks.forEach(link => {
        link.addEventListener('click', smoothScroll);
    });
    
    // ============================================
    // ACTUALIZAR ENLACE ACTIVO AL SCROLL
    // ============================================
    function updateActiveLink(clickedLink) {
        // Remover clase active de todos los enlaces
        navLinks.forEach(link => {
            link.classList.remove('active');
        });
        
        // Agregar clase active al enlace clickeado
        if (clickedLink) {
            clickedLink.classList.add('active');
            
            // Si es un enlace móvil, también activar el enlace desktop correspondiente
            const href = clickedLink.getAttribute('href');
            if (href) {
                const correspondingLink = document.querySelector(`.nav-link[href="${href}"], .mobile-nav-link[href="${href}"]`);
                if (correspondingLink && correspondingLink !== clickedLink) {
                    correspondingLink.classList.add('active');
                }
            }
        }
    }
    
    // ============================================
    // HIGHLIGHT NAVBAR AL SCROLL
    // ============================================
    function handleScroll() {
        if (!navbar) return;
        
        const scrollY = window.scrollY;
        
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Actualizar enlace activo basado en la sección visible
        updateActiveLinkOnScroll();
    }
    
    // ============================================
    // ACTUALIZAR ENLACE ACTIVO BASADO EN SCROLL
    // ============================================
    function updateActiveLinkOnScroll() {
        const sections = document.querySelectorAll('.section');
        if (sections.length === 0) return;
        
        const navbarHeight = navbar ? navbar.offsetHeight : 0;
        const scrollPosition = window.scrollY + navbarHeight + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remover active de todos los enlaces
                navLinks.forEach(link => {
                    link.classList.remove('active');
                });
                
                // Activar enlaces correspondientes
                const activeLinks = document.querySelectorAll(`.nav-link[href="#${sectionId}"], .mobile-nav-link[href="#${sectionId}"]`);
                activeLinks.forEach(link => {
                    link.classList.add('active');
                });
            }
        });
    }
    
    // ============================================
    // EVENT LISTENERS
    // ============================================
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('load', handleScroll);
    
    // Cerrar menú al redimensionar ventana (si pasa a desktop)
    window.addEventListener('resize', function() {
        if (window.innerWidth >= 992) {
            closeMenu();
        }
    });
    
    // Prevenir scroll cuando el menú está abierto
    if (mobileMenu) {
        mobileMenu.addEventListener('touchmove', function(e) {
            if (mobileMenu.classList.contains('active')) {
                e.preventDefault();
            }
        }, { passive: false });
    }
    
    // Inicializar
    handleScroll();
    
})();

