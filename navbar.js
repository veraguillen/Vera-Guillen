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
        const isActive = hamburger.classList.contains('active');
        
        if (isActive) {
            closeMenu();
        } else {
            openMenu();
        }
    }
    
    function openMenu() {
        hamburger.classList.add('active');
        mobileMenu.classList.add('active');
        menuOverlay.classList.add('active');
        body.classList.add('menu-open');
    }
    
    function closeMenu() {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        menuOverlay.classList.remove('active');
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
        
        const targetId = this.getAttribute('href');
        if (!targetId || !targetId.startsWith('#')) return;
        
        const targetSection = document.querySelector(targetId);
        if (!targetSection) return;
        
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

