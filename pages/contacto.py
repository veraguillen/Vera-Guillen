import streamlit as st
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email(name, email, subject, message_body):
    try:
        # Email configuration
        sender_email = os.getenv("GMAIL_EMAIL")
        receiver_email = "vera.guillen27@gmail.com"
        password = os.getenv("GMAIL_APP_PASSWORD")
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Portfolio Contact: {subject}"
        msg['Reply-To'] = email
        
        # Email body
        body = f"""
        Has recibido un nuevo mensaje del formulario de contacto:

        Nombre: {name}
        Email: {email}
        Asunto: {subject}

        Mensaje:
        {message_body}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Try with SSL first, fallback to TLS if needed
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, password)
                server.send_message(msg)
        except Exception as e:
            print("SSL falló, intentando con TLS...", str(e))
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
        
        return True, "¡Mensaje enviado con éxito! Me pondré en contacto contigo pronto."
    
    except Exception as e:
        error_msg = f"Error al enviar el correo: {str(e)}"
        print("Error detallado:", error_msg)
        return False, "Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde."

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Contacto | Portafolio Data Science",
    page_icon="📧",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Cyberpunk Color Variables */
    :root {
        --bg-main: #0D1117;
        --bg-card: #161B22;
        --text-primary: #E6EDF3;
        --text-secondary: #8B949E;
        --accent-orange: #FF6A00;
        --accent-orange-glow: #FF8C2B;
        --matrix-green: #00FF9F;
        --cyan-detail: #00D4FF;
    }
    
    /* Force dark background */
    body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-main) !important;
        color: var(--text-primary) !important;
    }
    
    .stApp > header {
        background-color: var(--bg-card) !important;
    }
    
    .main .block-container {
        background-color: transparent !important;
        padding-top: 2rem;
    }
    
    .contact-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .contact-header-enhanced {
        text-align: center;
        margin-bottom: 4rem;
        position: relative;
    }
    
    .contact-title-enhanced {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-orange) 50%, var(--text-primary) 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 3s ease infinite;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }
    
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .contact-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        color: var(--text-secondary);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.8;
        text-align: center !important;
        display: block !important;
    }
    
    .contact-header-enhanced p {
        text-align: center !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    .contact-cards-enhanced {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-bottom: 4rem;
    }
    
    .contact-card-enhanced {
        background: var(--bg-card);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        text-align: center;
        border: 1px solid rgba(255, 106, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .contact-card-enhanced::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--accent-orange), var(--accent-orange-glow), var(--accent-orange));
        background-size: 200% 100%;
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s ease;
    }
    
    .contact-card-enhanced:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 20px 50px rgba(255, 106, 0, 0.3), 0 0 40px rgba(255, 106, 0, 0.1), 0 0 30px rgba(255, 106, 0, 0.4);
        border-color: rgba(255, 106, 0, 0.5);
        background: var(--bg-card);
    }
    
    .contact-card-enhanced:hover::before {
        transform: scaleX(1);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .contact-icon-wrapper {
        width: 90px;
        height: 90px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.2), rgba(255, 140, 43, 0.2));
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem;
        border: 2px solid rgba(255, 106, 0, 0.3);
        transition: all 0.4s ease;
        position: relative;
    }
    
    .contact-card-enhanced:hover .contact-icon-wrapper {
        transform: rotate(-5deg) scale(1.15);
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.4), rgba(255, 140, 43, 0.4));
        border-color: rgba(255, 106, 0, 0.7);
        box-shadow: 0 0 30px rgba(255, 106, 0, 0.5);
    }
    
    .contact-icon {
        font-size: 2.8rem;
        color: var(--accent-orange);
        transition: all 0.4s ease;
    }
    
    .contact-card-enhanced:hover .contact-icon {
        color: var(--accent-orange-glow);
        transform: scale(1.2);
        filter: drop-shadow(0 0 15px rgba(255, 106, 0, 0.8));
    }
    
    .contact-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        color: var(--text-primary);
        transition: color 0.3s ease;
    }
    
    .contact-card-enhanced:hover .contact-title {
        color: var(--text-primary);
        text-shadow: 0 0 20px var(--accent-orange);
    }
    
    .contact-description {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
        line-height: 1.6;
        transition: color 0.3s ease;
    }
    
    .contact-card-enhanced:hover .contact-description {
        color: var(--text-primary);
    }
    
    .contact-link-enhanced {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-top: 1rem;
        padding: 0.8rem 2rem;
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.2), rgba(255, 140, 43, 0.2));
        color: var(--accent-orange) !important;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        border: 1px solid rgba(255, 106, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .contact-link-enhanced:hover {
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.4), rgba(255, 140, 43, 0.4));
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(255, 106, 0, 0.3), 0 0 30px rgba(255, 106, 0, 0.4);
        border-color: rgba(255, 106, 0, 0.6);
        text-decoration: none;
        color: var(--accent-orange-glow) !important;
        text-shadow: 0 0 20px var(--accent-orange);
    }
    
    .form-section {
        background: var(--bg-card);
        border-radius: 24px;
        padding: 3rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 106, 0, 0.2);
        margin-top: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .form-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 106, 0, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        animation: float-glow 6s ease-in-out infinite;
    }
    
    @keyframes float-glow {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
        50% { transform: translate(20px, -20px) scale(1.1); opacity: 0.8; }
    }
    
    .form-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .form-title i {
        color: var(--accent-orange);
        font-size: 2rem;
        background: linear-gradient(135deg, var(--accent-orange), var(--accent-orange-glow));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 20px rgba(255, 106, 0, 0.5));
    }
    
    .form-description {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        line-height: 1.8;
        position: relative;
        z-index: 1;
    }
    
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea {
        background-color: var(--bg-card) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(255, 106, 0, 0.3) !important;
        border-radius: 12px !important;
        padding: 0.8rem 1rem !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>div>textarea:focus {
        border-color: rgba(255, 106, 0, 0.6) !important;
        box-shadow: 0 0 20px rgba(255, 106, 0, 0.2) !important;
        outline: none !important;
    }
    
    .stTextInput>label, 
    .stTextArea>label {
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, var(--accent-orange), var(--accent-orange-glow)) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 106, 0, 0.3) !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton>button:hover::before {
        left: 100%;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, var(--accent-orange-glow), var(--accent-orange)) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(255, 106, 0, 0.5), 0 0 30px rgba(255, 106, 0, 0.4) !important;
        text-shadow: 0 0 20px var(--accent-orange) !important;
    }
    
    .stButton>button:active {
        transform: translateY(-1px) !important;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .contact-card-enhanced {
        animation: slideInUp 0.6s ease-out forwards;
        opacity: 0;
    }
    
    .contact-card-enhanced:nth-child(1) { animation-delay: 0.1s; }
    .contact-card-enhanced:nth-child(2) { animation-delay: 0.2s; }
    .contact-card-enhanced:nth-child(3) { animation-delay: 0.3s; }
    
    /* Mejorar mensajes de éxito y error */
    .stSuccess {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(102, 187, 106, 0.2)) !important;
        border: 1px solid rgba(76, 175, 80, 0.5) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        color: #4CAF50 !important;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.2), rgba(239, 83, 80, 0.2)) !important;
        border: 1px solid rgba(244, 67, 54, 0.5) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        color: #F44336 !important;
    }
    
    /* Mejorar el spinner */
    .stSpinner > div {
        border-color: var(--accent-orange) transparent transparent transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTACT SECTION ---
st.markdown("<div class='contact-container'>", unsafe_allow_html=True)

# Header Mejorado
st.markdown("""
<div class='contact-header-enhanced'>
    <h1 class='contact-title-enhanced'>Contáctame</h1>
    <p class='contact-subtitle'>
        ¿Tienes un proyecto en mente o quieres trabajar juntos? 
        Estoy disponible para oportunidades de colaboración y conversaciones sobre tecnología y datos.
    </p>
</div>
""", unsafe_allow_html=True)

# Contact Cards Mejoradas
st.markdown("<div class='contact-cards-enhanced'>", unsafe_allow_html=True)

# Email Card
st.markdown("""
<div class='contact-card-enhanced'>
    <div class='contact-icon-wrapper'>
        <i class='fas fa-envelope contact-icon'></i>
    </div>
    <h3 class='contact-title'>Correo Electrónico</h3>
    <p class='contact-description'>Envíame un mensaje directamente</p>
    <a href='mailto:vera.guillen27@gmail.com' class='contact-link-enhanced' target='_blank'>
        <i class='fas fa-paper-plane'></i>
        <span>Enviar Email</span>
    </a>
</div>
""", unsafe_allow_html=True)

# GitHub Card
st.markdown("""
<div class='contact-card-enhanced'>
    <div class='contact-icon-wrapper'>
        <i class='fab fa-github contact-icon'></i>
    </div>
    <h3 class='contact-title'>GitHub</h3>
    <p class='contact-description'>Revisa mis proyectos en GitHub</p>
    <a href='https://github.com/veraguillen' class='contact-link-enhanced' target='_blank'>
        <i class='fab fa-github'></i>
        <span>Ver Perfil</span>
    </a>
</div>
""", unsafe_allow_html=True)

# LinkedIn Card
st.markdown("""
<div class='contact-card-enhanced'>
    <div class='contact-icon-wrapper'>
        <i class='fab fa-linkedin contact-icon'></i>
    </div>
    <h3 class='contact-title'>LinkedIn</h3>
    <p class='contact-description'>Conecta conmigo profesionalmente</p>
    <a href='https://www.linkedin.com/in/vera-guillen-9b464a303/' class='contact-link-enhanced' target='_blank'>
        <i class='fab fa-linkedin'></i>
        <span>Conectar</span>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close contact-cards-enhanced

# Contact Form Mejorado
st.markdown("""
<div class='form-section'>
    <h2 class='form-title'>
        <i class='fas fa-paper-plane'></i>
        <span>Envíame un Mensaje</span>
    </h2>
    <p class='form-description'>
        O si prefieres, utiliza el siguiente formulario para contactarme directamente.
    </p>
""", unsafe_allow_html=True)

# Create form
with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Nombre *", key="name", placeholder="Tu nombre completo")
    with col2:
        email = st.text_input("Correo Electrónico *", key="email", placeholder="tu@email.com")
    
    subject = st.text_input("Asunto *", key="subject", placeholder="¿Sobre qué quieres hablar?")
    message = st.text_area("Mensaje *", height=150, key="message", placeholder="Escribe tu mensaje aquí...")
    
    submit_button = st.form_submit_button("🚀 Enviar Mensaje")
    
    if submit_button:
        if not name or not email or not message:
            st.error("⚠️ Por favor completa todos los campos obligatorios (*)")
        else:
            with st.spinner('📧 Enviando mensaje...'):
                success, result = send_email(name, email, subject, message)
                if success:
                    st.success(result)
                else:
                    st.error(result)

st.markdown("</div>", unsafe_allow_html=True)  # Close form-section
st.markdown("</div>", unsafe_allow_html=True)  # Close contact-container

# Add Font Awesome (al final para asegurar que se carga)
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
    unsafe_allow_html=True
)