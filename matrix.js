// ============================================
// MATRIX RAIN ANIMATION - CYBERPUNK/HACKER
// ============================================

(function() {
    'use strict';
    
    const canvas = document.getElementById('matrix-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    
    // Configuración
    const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
    const fontSize = 14;
    let columns = 0;
    let drops = [];
    
    // Inicializar
    function init() {
        // Ajustar tamaño del canvas
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Calcular columnas
        columns = Math.floor(canvas.width / fontSize);
        
        // Inicializar drops
        drops = [];
        for (let i = 0; i < columns; i++) {
            drops[i] = Math.random() * -100;
        }
    }
    
    // Dibujar
    function draw() {
        // Fondo semi-transparente para efecto de rastro
        ctx.fillStyle = 'rgba(13, 17, 23, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Color del texto (verde matrix con variación)
        ctx.fillStyle = '#00FF9F';
        ctx.font = `${fontSize}px 'JetBrains Mono', monospace`;
        
        // Dibujar caracteres
        for (let i = 0; i < drops.length; i++) {
            // Carácter aleatorio
            const text = chars[Math.floor(Math.random() * chars.length)];
            
            // Posición Y
            const y = drops[i] * fontSize;
            
            // Opacidad variable (más brillante arriba)
            const opacity = Math.max(0.1, 1 - (y / canvas.height) * 0.9);
            ctx.fillStyle = `rgba(0, 255, 159, ${opacity})`;
            
            // Dibujar carácter
            ctx.fillText(text, i * fontSize, y);
            
            // Resetear drop si llega al final o aleatoriamente
            if (y > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            
            // Incrementar posición
            drops[i]++;
        }
    }
    
    // Loop de animación
    function animate() {
        draw();
        requestAnimationFrame(animate);
    }
    
    // Inicializar y empezar
    init();
    animate();
    
    // Redimensionar canvas cuando cambia el tamaño de la ventana
    window.addEventListener('resize', function() {
        init();
    });
    
})();

