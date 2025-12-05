// ============================================
// CONTACT FORM - FORMSFREE/GETFORM
// ============================================

(function() {
    'use strict';
    
    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');
    
    if (!contactForm) return;
    
        // We use the Formspree endpoint directly
    // In Vercel, we will configure this environment variable in the project configuration
    const FORM_ENDPOINT = 'https://formspree.io/f/xqajdvzr';
    
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form values
        const formData = new FormData(contactForm);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            subject: formData.get('subject'),
            message: formData.get('message')
        };
        
        // Basic validation
        if (!data.name || !data.email || !data.message) {
            showStatus('Please fill in all required fields.', 'error');
            return;
        }
        
        // Show loading status
        showStatus('Sending message...', 'loading');
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
                showStatus('Message sent successfully! I will get back to you soon.', 'success');
                contactForm.reset();
            } else {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Error sending message');
            }
        } catch (error) {
            console.error('Error:', error);
            showStatus('There was an error sending your message. Please try again later or contact me directly by email.', 'error');
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
        
        // Hide after 5 seconds if success
        if (type === 'success') {
            setTimeout(() => {
                formStatus.style.display = 'none';
            }, 5000);
        }
    }
})();

