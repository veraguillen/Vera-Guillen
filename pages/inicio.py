import streamlit as st
from pathlib import Path

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
PROFILE_PIC = ASSETS_DIR / "foto_perfil.jpg"

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Sobre Mí | Portafolio Data Science", layout="wide")

# --- CUSTOM CSS ---
def load_css():
    try:
        # Cargar el archivo CSS principal
        css_path = Path(__file__).parent.parent / "style.css"
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
        
        # Cargar el archivo CSS personalizado
        custom_css_path = Path(__file__).parent.parent / "assets" / "custom.css"
        with open(custom_css_path, "r", encoding="utf-8") as f:
            custom_css = f.read()
        st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error al cargar los estilos: {str(e)}")
        # Cargar estilos mínimos como respaldo
        st.markdown("""
        <style>
            /* Colores principales */
            :root {
                --dark-navy: #2F3C4B;
                --light-navy: #3A4B5C;
                --lightest-slate: #E8F0FF;
                --light-slate: #C8D1E0;
                --accent-color: #FF8C00;
            }
            
            /* Aplicar colores a los elementos principales */
            .stApp, body, .main, .stApp > div {
                background-color: #2F3C4B !important;
                color: #C8D1E0 !important;
            }
            
            /* Encabezados */
            h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
                color: #E8F0FF !important;
            }
            
            /* Tarjetas y contenedores */
            .card, .specialty-card, .approach-item {
                background-color: #3A4B5C !important;
                border-left: 3px solid #FF8C00 !important;
                color: #E8F0FF !important;
                padding: 1rem;
                border-radius: 0 8px 8px 0;
                margin: 1rem 0;
            }
            
            /* Texto y enlaces */
            body, p, div, span {
                color: #C8D1E0 !important;
            }
            
            a {
                color: #FF8C00 !important;
            }
            
            a:hover {
                color: #FFA500 !important;
            }
            
            /* Sección de Diferencial Creativo */
            .creative-section {
                background-color: #3A4B5C !important;
                border-left: 4px solid #FF8C00 !important;
                padding: 1.5rem !important;
                margin: 1.5rem 0 !important;
                border-radius: 0 8px 8px 0;
            }
            
            .creative-section h3 {
                color: #FF8C00 !important;
                margin-top: 0 !important;
            }
            
            .creative-section p {
                color: #E8F0FF !important;
                margin-bottom: 0 !important;
                line-height: 1.6 !important;
            }
            .card {
                background: var(--light-navy);
                padding: 1.5rem;
                border-radius: 8px;
                margin: 1rem 0;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            }
            
            .about-me-item {
                display: flex;
                gap: 1rem;
                margin-bottom: 1rem;
                align-items: flex-start;
            }
            
            .about-me-item i {
                color: var(--accent-color);
                margin-top: 0.3rem;
                flex-shrink: 0;
            }
            
            .about-me-item div {
                flex: 1;
            }
            
            .profile-image-container {
                display: flex;
                justify-content: center;
                margin-bottom: 1.5rem;
            }
            
            .profile-image img {
                border-radius: 50%;
                border: 4px solid var(--accent-color);
                width: 200px;
                height: 200px;
                object-fit: cover;
            }
        </style>
        """, unsafe_allow_html=True)
    
    # Añadir Font Awesome para iconos
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">',
        unsafe_allow_html=True
    )

load_css()

# Estilos globales adicionales
st.markdown("""
<style>
    .section-spacer {
        height: 3rem;
    }
    
    /* Mejorar el contenedor principal */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Mejorar la tipografía general */
    body {
        font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# Añadir estilos mejorados para el hero
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .hero-container {
        background: #161B22;
        border-radius: 24px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5),
                    0 0 30px rgba(255, 106, 0, 0.2);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 106, 0, 0.2);
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 106, 0, 0.1) 0%, transparent 70%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        gap: 3rem;
    }
    
    .hero-text-section {
        flex: 1.5;
    }
    
    .hero-image-section {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    @media (max-width: 768px) {
        .hero-content {
            flex-direction: column;
            gap: 2rem;
        }
        
        .hero-text-section,
        .hero-image-section {
            flex: 1;
            width: 100%;
        }
    }
    
    .hero-title {
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 3.5rem;
        font-weight: 800;
        color: #FF8C2B;
        text-shadow: 0 0 30px rgba(255, 140, 43, 0.6),
                     0 0 60px rgba(255, 140, 43, 0.3);
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .typing {
        border-right: 2px solid #FF8C2B;
        animation: blink 1s infinite;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
        text-shadow: 0 0 20px #FF8C2B;
    }
    
    @keyframes blink {
        0%, 49% { border-color: #FF8C2B; }
        50%, 100% { border-color: transparent; }
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: #8B949E;
        margin: 1.5rem 0;
        font-weight: 400;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .hero-subtitle i {
        color: #FF6A00;
        font-size: 1.8rem;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 0 15px rgba(255, 106, 0, 0.6);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-card {
        background: #161B22;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid rgba(255, 106, 0, 0.2);
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }
    
    .hero-card:hover {
        transform: translateY(-5px);
        border-color: #FF6A00;
        box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                    0 12px 40px rgba(0, 0, 0, 0.4);
    }
    
    .hero-card-title {
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 1.5rem;
        color: #FF8C2B;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 12px;
        text-shadow: 0 0 15px rgba(255, 140, 43, 0.5);
    }
    
    .hero-card-title i {
        font-size: 1.8rem;
        text-shadow: 0 0 15px rgba(255, 106, 0, 0.6);
    }
    
    .hero-card-text {
        font-family: 'Inter', sans-serif;
        color: #8B949E;
        line-height: 1.8;
        font-size: 1.1rem;
    }
    
    .profile-wrapper {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }
    
    .profile-image-wrapper {
        position: relative;
        width: 280px;
        height: 280px;
        border-radius: 50%;
        padding: 6px;
        background: linear-gradient(135deg, #FF6A00, #FF8C2B, #FF6A00);
        background-size: 200% 200%;
        animation: gradient-rotate 3s ease infinite;
        box-shadow: 0 0 40px rgba(255, 106, 0, 0.5),
                    0 0 80px rgba(255, 106, 0, 0.3);
    }
    
    @keyframes gradient-rotate {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .profile-image-inner {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        overflow: hidden;
        background: #0D1117;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .profile-image-inner img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }
    
    .profile-decoration {
        position: absolute;
        width: 320px;
        height: 320px;
        border-radius: 50%;
        border: 2px solid rgba(255, 106, 0, 0.2);
        animation: rotate 20s linear infinite;
    }
    
    .profile-decoration::before {
        content: '';
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 20px;
        height: 20px;
        background: #FF6A00;
        border-radius: 50%;
        box-shadow: 0 0 20px rgba(255, 106, 0, 0.8);
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .profile-image-wrapper {
            width: 220px;
            height: 220px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section con diseño mejorado - Foto dentro del contenedor animado
# Primero cargar la imagen como base64 o usar la ruta directamente
import base64
from pathlib import Path

profile_image_html = ""
try:
    if PROFILE_PIC.exists():
        # Leer la imagen y convertir a base64
        with open(PROFILE_PIC, "rb") as img_file:
            img_data = base64.b64encode(img_file.read()).decode()
            profile_image_html = f'<img src="data:image/jpeg;base64,{img_data}" alt="Vera Guillen" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;" />'
    else:
        profile_image_html = '<i class="fas fa-user-circle" style="font-size: 200px; color: #FF8C00;"></i>'
except Exception as e:
    profile_image_html = '<i class="fas fa-user-circle" style="font-size: 200px; color: #FF8C00;"></i>'

st.markdown(f"""
<div class="hero-container">
    <div class="hero-content">
        <div class="hero-text-section">
            <h1 class="hero-title typing">Hola, soy<br><span style="color: #FF8C2B;">Vera Guillen</span></h1>
            <div class="hero-subtitle">
                <i class="fas fa-robot"></i>
                <span>Transformo datos complejos en soluciones de IA</span>
            </div>
            <div class="hero-card">
                <div class="hero-card-title">
                    <i class="fas fa-laptop-code"></i>
                    <span>Data Scientist & ML Engineer</span>
                </div>
                <p class="hero-card-text">
                    Diseño e implemento soluciones escalables que optimizan procesos y automatizan decisiones, 
                    impulsando el crecimiento empresarial a través de la inteligencia artificial y el análisis de datos.
                </p>
            </div>
        </div>
        <div class="hero-image-section">
            <div class="profile-wrapper">
                <div class="profile-decoration"></div>
                <div class="profile-image-wrapper">
                    <div class="profile-image-inner">
                        {profile_image_html}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sección de Especialidades - Mejorada
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

# CSS para especialidades
st.markdown("""
<style>
    .specialties-section {
        margin: 3rem 0;
    }
    
    .section-title-enhanced {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: #E8F0FF !important;
        margin-bottom: 2.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .section-title-enhanced i {
        color: #FF8C00;
        font-size: 2.2rem;
        background: linear-gradient(135deg, #FF8C00, #FFB74D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .specialty-card-enhanced {
        background: rgba(42, 53, 66, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2.5rem;
        border: 1px solid rgba(255, 140, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        height: 100%;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .specialty-card-enhanced::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.1), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .specialty-card-enhanced:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 20px 50px rgba(255, 140, 0, 0.3), 0 0 40px rgba(255, 140, 0, 0.1);
        border-color: rgba(255, 140, 0, 0.5);
        background: rgba(42, 53, 66, 0.9);
    }
    
    .specialty-card-enhanced:hover::before {
        opacity: 1;
    }
    
    .specialty-icon-enhanced {
        width: 80px;
        height: 80px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.2), rgba(255, 183, 77, 0.2));
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        border: 2px solid rgba(255, 140, 0, 0.3);
        transition: all 0.4s ease;
        position: relative;
        z-index: 1;
    }
    
    .specialty-card-enhanced:hover .specialty-icon-enhanced {
        transform: rotate(-5deg) scale(1.15);
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.4), rgba(255, 183, 77, 0.4));
        border-color: rgba(255, 140, 0, 0.7);
        box-shadow: 0 0 30px rgba(255, 140, 0, 0.5);
    }
    
    .specialty-icon-enhanced i {
        color: #FF8C00;
        font-size: 2.5rem;
        transition: all 0.4s ease;
    }
    
    .specialty-card-enhanced:hover .specialty-icon-enhanced i {
        color: #FFB74D;
        transform: scale(1.2);
        filter: drop-shadow(0 0 15px rgba(255, 140, 0, 0.8));
    }
    
    .specialty-card-enhanced h4 {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #E8F0FF;
        margin: 0 0 1rem 0;
        position: relative;
        z-index: 1;
        transition: color 0.3s ease;
    }
    
    .specialty-card-enhanced:hover h4 {
        color: #FFFFFF;
    }
    
    .specialty-card-enhanced p {
        font-family: 'Inter', sans-serif;
        color: #C8D1E0;
        line-height: 1.8;
        font-size: 1.05rem;
        margin: 0;
        position: relative;
        z-index: 1;
        transition: color 0.3s ease;
    }
    
    .specialty-card-enhanced:hover p {
        color: #E8F0FF;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h2 class="section-title-enhanced">
    <i class="fas fa-star"></i>
    <span>Mis Especialidades</span>
</h2>
""", unsafe_allow_html=True)

cols = st.columns(3)

with cols[0]:
    st.markdown("""
    <div class="specialty-card-enhanced">
        <div class="specialty-icon-enhanced">
            <i class="fas fa-brain"></i>
        </div>
        <h4>Machine Learning</h4>
        <p>Modelos predictivos y sistemas de recomendación personalizados.</p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div class="specialty-card-enhanced">
        <div class="specialty-icon-enhanced">
            <i class="fas fa-robot"></i>
        </div>
        <h4>IA Generativa</h4>
        <p>Soluciones de IA conversacional y generación de contenido.</p>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div class="specialty-card-enhanced">
        <div class="specialty-icon-enhanced">
            <i class="fas fa-chart-line"></i>
        </div>
        <h4>Análisis Predictivo</h4>
        <p>Extracción de insights y tendencias de grandes volúmenes de datos.</p>
    </div>
    """, unsafe_allow_html=True)

# Sección Sobre Mí - Mejorada
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

with st.container():
    # CSS mejorado para la sección Sobre Mí
    st.markdown("""
    <style>
        .about-section-enhanced {
            background: linear-gradient(145deg, rgba(42, 53, 66, 0.95), rgba(58, 75, 92, 0.95));
            border-radius: 24px;
            padding: 3.5rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 140, 0, 0.2);
            margin: 3rem 0;
            font-family: 'Inter', sans-serif;
            position: relative;
            overflow: hidden;
        }
        
        .about-section-enhanced::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(255, 140, 0, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            animation: float-glow 6s ease-in-out infinite;
        }
        
        .about-section-enhanced::after {
            content: '';
            position: absolute;
            bottom: -30%;
            left: -10%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(255, 140, 0, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            animation: float-glow 8s ease-in-out infinite reverse;
        }
        
        @keyframes float-glow {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
            50% { transform: translate(20px, -20px) scale(1.1); opacity: 0.8; }
        }
        
        .about-title-enhanced {
            font-family: 'Inter', sans-serif;
            color: #E8F0FF !important;
            font-size: 2.8rem !important;
            font-weight: 800 !important;
            margin: 0 0 3rem 0 !important;
            letter-spacing: -1px;
            position: relative;
            display: flex;
            align-items: center;
            gap: 1rem;
            z-index: 1;
        }
        
        .about-title-enhanced i {
            color: #FF8C00 !important;
            font-size: 2.5rem;
            background: linear-gradient(135deg, #FF8C00, #FFB74D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 20px rgba(255, 140, 0, 0.5));
            animation: icon-pulse 2s ease-in-out infinite;
        }
        
        @keyframes icon-pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        .about-title-enhanced::after {
            content: '';
            flex: 1;
            height: 3px;
            background: linear-gradient(90deg, #FF8C00, transparent);
            border-radius: 2px;
            margin-left: 1rem;
        }
        
        .about-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            position: relative;
            z-index: 1;
        }
        
        .about-card-enhanced {
            background: rgba(42, 53, 66, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255, 140, 0, 0.2);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }
        
        .about-card-enhanced::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #FF8C00, #FFB74D, #FF8C00);
            background-size: 200% 100%;
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }
        
        .about-card-enhanced:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(255, 140, 0, 0.2), 0 0 30px rgba(255, 140, 0, 0.1);
            border-color: rgba(255, 140, 0, 0.5);
            background: rgba(42, 53, 66, 0.9);
        }
        
        .about-card-enhanced:hover::before {
            transform: scaleX(1);
            animation: shimmer 2s infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        
        .about-card-icon {
            width: 60px;
            height: 60px;
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(255, 140, 0, 0.2), rgba(255, 183, 77, 0.2));
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
            border: 2px solid rgba(255, 140, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .about-card-enhanced:hover .about-card-icon {
            transform: rotate(5deg) scale(1.1);
            background: linear-gradient(135deg, rgba(255, 140, 0, 0.3), rgba(255, 183, 77, 0.3));
            border-color: rgba(255, 140, 0, 0.6);
            box-shadow: 0 0 20px rgba(255, 140, 0, 0.4);
        }
        
        .about-card-icon i {
            color: #FF8C00;
            font-size: 1.8rem;
            transition: all 0.3s ease;
        }
        
        .about-card-enhanced:hover .about-card-icon i {
            color: #FFB74D;
            transform: scale(1.2);
            filter: drop-shadow(0 0 10px rgba(255, 140, 0, 0.8));
        }
        
        .about-card-text {
            color: #E8F0FF !important;
            line-height: 1.9;
            font-size: 1.05rem;
            font-weight: 400;
            margin: 0;
            transition: color 0.3s ease;
        }
        
        .about-card-enhanced:hover .about-card-text {
            color: #FFFFFF !important;
        }
        
        .about-card-text strong {
            color: #FFB74D;
            font-weight: 600;
            position: relative;
        }
        
        .about-card-enhanced:hover .about-card-text strong {
            color: #FF8C00;
            text-shadow: 0 0 10px rgba(255, 140, 0, 0.5);
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
        
        .about-card-enhanced {
            animation: slideInUp 0.6s ease-out forwards;
            opacity: 0;
        }
        
        .about-card-enhanced:nth-child(1) { animation-delay: 0.1s; }
        .about-card-enhanced:nth-child(2) { animation-delay: 0.2s; }
        .about-card-enhanced:nth-child(3) { animation-delay: 0.3s; }
        .about-card-enhanced:nth-child(4) { animation-delay: 0.4s; }
        
        @media (max-width: 768px) {
            .about-grid {
                grid-template-columns: 1fr;
            }
            .about-title-enhanced {
                font-size: 2.2rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Contenido mejorado
    st.markdown("""
    <div class='about-section-enhanced'>
        <h2 class='about-title-enhanced'>
            <i class='fas fa-user-tie'></i>
            <span>Sobre Mí</span>
        </h2>
        <div class='about-grid'>
    """, unsafe_allow_html=True)
    
    # Items del about con diseño de tarjetas
    about_items = [
        {
            "icon": "fas fa-laptop-code",
            "text": "<strong>Data Scientist & Machine Learning Engineer</strong> con enfoque end-to-end. Mi experiencia abarca desde la ingeniería de datos hasta el despliegue y la orquestación en producción (MLOps)."
        },
        {
            "icon": "fas fa-brain",
            "text": "Combino <strong>rigor técnico</strong> con <strong>creatividad estratégica</strong> para resolver desafíos complejos mediante Machine Learning, NLP y Computer Vision."
        },
        {
            "icon": "fas fa-chart-line",
            "text": "Diseño e implemento soluciones de IA escalables que optimizan procesos, automatizan decisiones y descubren <strong>insights accionables</strong> en grandes volúmenes de datos."
        },
        {
            "icon": "fas fa-theater-masks",
            "text": "Mi sólida formación en <strong>artes escénicas</strong> me aporta una perspectiva única: abordo sistemas complejos como narrativas, comunico insights técnicos con claridad excepcional y diseño soluciones que fusionan funcionalidad con <strong>experiencia de usuario intuitiva</strong>."
        }
    ]
    
    for item in about_items:
        st.markdown(f"""
        <div class='about-card-enhanced'>
            <div class='about-card-icon'>
                <i class='{item['icon']}'></i>
            </div>
            <p class='about-card-text'>{item['text']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sección de Idiomas - Mejorada
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
st.markdown("""
<h2 class="section-title-enhanced">
    <i class="fas fa-language"></i>
    <span>Idiomas</span>
</h2>
""", unsafe_allow_html=True)

# CSS para idiomas
st.markdown("""
<style>
    .language-card {
        background: rgba(42, 53, 66, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 140, 0, 0.2);
        transition: all 0.4s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        height: 100%;
    }
    
    .language-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(255, 140, 0, 0.3);
        border-color: rgba(255, 140, 0, 0.5);
        background: rgba(42, 53, 66, 0.9);
    }
    
    .language-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .language-header h4 {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #E8F0FF;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    .language-header i {
        font-size: 1.3rem;
    }
    
    .language-badge {
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.2), rgba(255, 183, 77, 0.2));
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #FFB74D;
        border: 1px solid rgba(255, 140, 0, 0.3);
    }
    
    .language-progress-container {
        width: 100%;
        height: 12px;
        background-color: rgba(58, 75, 92, 0.8);
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 1rem;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .language-progress-bar {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #FF8C00, #FFB74D);
        box-shadow: 0 0 20px rgba(255, 140, 0, 0.5);
        transition: width 1s ease-in-out;
        position: relative;
        overflow: hidden;
    }
    
    .language-progress-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        animation: shimmer-progress 2s infinite;
    }
    
    @keyframes shimmer-progress {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .language-description {
        color: #C8D1E0;
        font-size: 0.95rem;
        line-height: 1.6;
        margin: 0;
        font-family: 'Inter', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Crear la sección de idiomas mejorada
with st.container():
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        # Español
        st.markdown("""
        <div class='language-card'>
            <div class='language-header'>
                <h4>
                    <i class='fas fa-check-circle' style='color: #4CAF50;'></i>
                    <span>Español</span>
                </h4>
                <span class='language-badge'>Nativo</span>
            </div>
            <div class='language-progress-container'>
                <div class='language-progress-bar' style='width: 100%; background: linear-gradient(90deg, #4CAF50, #66BB6A);'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Inglés
        st.markdown("""
        <div class='language-card'>
            <div class='language-header'>
                <h4>
                    <i class='fas fa-check-circle' style='color: #2196F3;'></i>
                    <span>Inglés</span>
                </h4>
                <span class='language-badge'>B2 Avanzado</span>
            </div>
            <div class='language-progress-container'>
                <div class='language-progress-bar' style='width: 75%; background: linear-gradient(90deg, #2196F3, #42A5F5);'></div>
            </div>
            <p class='language-description'>
                Comprensión y comunicación fluida, tanto escrita como oral.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Mi Diferencial Creativo - Mejorado
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
st.markdown("""
<h2 class="section-title-enhanced">
    <i class="fas fa-palette"></i>
    <span>Mi Diferencial Creativo</span>
</h2>
""", unsafe_allow_html=True)
st.markdown("""
<div class='creative-section'>
    <p>
        Mi sólida formación en <strong>artes escénicas</strong> me aporta una perspectiva única: abordo sistemas complejos como narrativas, 
        comunico insights técnicos con una claridad excepcional y diseño soluciones que fusionan funcionalidad con una 
        <strong>experiencia de usuario intuitiva</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

# Enfoque de Trabajo - Mejorado
st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
st.markdown("""
<h2 class="section-title-enhanced">
    <i class="fas fa-lightbulb"></i>
    <span>Mi Enfoque de Trabajo</span>
</h2>
""", unsafe_allow_html=True)

# Definir los elementos del enfoque de trabajo
approach_items = [
    {
        'icon': 'lightbulb',
        'title': 'Innovación Práctica',
        'description': 'Desarrollo soluciones prácticas que resuelven problemas reales, priorizando la implementación efectiva sobre la tecnología por la tecnología misma.'
    },
    {
        'icon': 'chart-pie',
        'title': 'Análisis Centrado en Datos',
        'description': 'Tomo decisiones basadas en datos, utilizando metodologías cuantitativas para validar hipótesis y medir el impacto real.'
    },
    {
        'icon': 'users',
        'title': 'Colaboración Efectiva',
        'description': 'Trabajo estrechamente con equipos multidisciplinarios, traduciendo necesidades de negocio en soluciones técnicas efectivas.'
    }
]

# CSS para enfoque de trabajo
st.markdown("""
<style>
    .approach-card {
        background: rgba(42, 53, 66, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 140, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        gap: 1.5rem;
        align-items: flex-start;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .approach-card:hover {
        transform: translateX(10px) translateY(-5px);
        box-shadow: 0 20px 50px rgba(255, 140, 0, 0.3);
        border-color: rgba(255, 140, 0, 0.5);
        background: rgba(42, 53, 66, 0.9);
    }
    
    .approach-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.2), rgba(255, 183, 77, 0.2));
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid rgba(255, 140, 0, 0.3);
        flex-shrink: 0;
        transition: all 0.3s ease;
    }
    
    .approach-card:hover .approach-icon {
        transform: rotate(5deg) scale(1.1);
        background: linear-gradient(135deg, rgba(255, 140, 0, 0.4), rgba(255, 183, 77, 0.4));
        border-color: rgba(255, 140, 0, 0.6);
        box-shadow: 0 0 20px rgba(255, 140, 0, 0.4);
    }
    
    .approach-icon i {
        color: #FF8C00;
        font-size: 1.8rem;
        transition: all 0.3s ease;
    }
    
    .approach-card:hover .approach-icon i {
        color: #FFB74D;
        transform: scale(1.2);
    }
    
    .approach-content h4 {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #E8F0FF;
        margin: 0 0 0.8rem 0;
        transition: color 0.3s ease;
    }
    
    .approach-card:hover .approach-content h4 {
        color: #FFFFFF;
    }
    
    .approach-content p {
        font-family: 'Inter', sans-serif;
        color: #C8D1E0;
        line-height: 1.8;
        font-size: 1.05rem;
        margin: 0;
        transition: color 0.3s ease;
    }
    
    .approach-card:hover .approach-content p {
        color: #E8F0FF;
    }
</style>
""", unsafe_allow_html=True)

# Mostrar los elementos del enfoque de trabajo
for item in approach_items:
    st.markdown(f"""
    <div class='approach-card'>
        <div class='approach-icon'>
            <i class='fas fa-{item["icon"]}'></i>
        </div>
        <div class='approach-content'>
            <h4>{item["title"]}</h4>
            <p>{item["description"]}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)