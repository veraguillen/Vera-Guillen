// ============================================
// FORMULARIO DE CONTACTO - FORMSFREE/GETFORM
// ============================================

(function() {
    'use strict';
    
    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');
    
    if (!contactForm) return;
    
        // Usamos el endpoint de Formspree directamente
    // En Vercel, configuraremos esta variable de entorno en la configuración del proyecto
    const FORM_ENDPOINT = 'https://formspree.io/f/xqajdvzr';
    
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Obtener valores del formulario
        const formData = new FormData(contactForm);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            subject: formData.get('subject'),
            message: formData.get('message')
        };
        
        // Validación básica
        if (!data.name || !data.email || !data.message) {
            showStatus('Por favor completa todos los campos obligatorios.', 'error');
            return;
        }
        
        // Mostrar estado de carga
        showStatus('Enviando mensaje...', 'loading');
        contactForm.querySelector('.submit-button').disabled = true;
        
        try {
            const response = await fetch(FORM_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                showStatus('¡Mensaje enviado con éxito! Me pondré en contacto contigo pronto.', 'success');
                contactForm.reset();
            } else {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Error al enviar el mensaje');
            }
        } catch (error) {
            console.error('Error:', error);
            showStatus('Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde o contáctame directamente por email.', 'error');
        } finally {
            contactForm.querySelector('.submit-button').disabled = false;
        }
    });
    
    function showStatus(message, type) {
        if (!formStatus) return;
        
        formStatus.textContent = message;
        formStatus.className = 'form-status';
        formStatus.classList.add(`form-status-${type}`);
        formStatus.style.display = 'block';
        
        // Ocultar después de 5 segundos si es éxito
        if (type === 'success') {
            setTimeout(() => {
                formStatus.style.display = 'none';
            }, 5000);
        }
    }
})();

