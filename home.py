# Home.py - Single Page Portfolio
import streamlit as st
from pathlib import Path
import base64

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent
CSS_FILE = BASE_DIR / "style.css"
NAVBAR_CSS = BASE_DIR / "navbar.css"
NAVBAR_JS = BASE_DIR / "navbar.js"
ASSETS_DIR = BASE_DIR / "assets"
PROFILE_PIC = ASSETS_DIR / "foto_perfil.jpg"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Portafolio | Vera Guillen",
    layout="wide",
    initial_sidebar_state="collapsed"  # Ocultar sidebar por defecto
)

# Ocultar sidebar completamente
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    .stApp {
        margin-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CARGAR CSS Y JS ---
def load_css_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        st.error(f"Error al cargar {file_path}: {str(e)}")
        return ""

# Cargar todos los CSS
main_css = load_css_file(CSS_FILE)
navbar_css = load_css_file(NAVBAR_CSS)
custom_css = load_css_file(ASSETS_DIR / "custom.css")

# Cargar JavaScript
navbar_js = ""
try:
    with open(NAVBAR_JS, "r", encoding="utf-8") as f:
        navbar_js = f.read()
except:
    pass

# --- VIEWPORT META TAG ---
        st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
""", unsafe_allow_html=True)

# --- CARGAR TODOS LOS ESTILOS ---
st.markdown(f"""
        <style>
{main_css}
{navbar_css}
{custom_css}

/* Asegurar que Streamlit no interfiera */
.stApp > header {
    display: none !important;
}

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Ocultar sidebar */
section[data-testid="stSidebar"] {
    display: none !important;
            }
        </style>
        """, unsafe_allow_html=True)
    
# --- NAVBAR HTML ---
navbar_html = """
<nav class="navbar" id="navbar">
    <a href="#inicio" class="navbar-brand">Vera Guillen</a>
    
    <!-- Menú Desktop -->
    <ul class="navbar-nav">
        <li class="nav-item"><a href="#inicio" class="nav-link">Inicio</a></li>
        <li class="nav-item"><a href="#sobre-mi" class="nav-link">Sobre Mí</a></li>
        <li class="nav-item"><a href="#habilidades" class="nav-link">Habilidades</a></li>
        <li class="nav-item"><a href="#proyectos" class="nav-link">Proyectos</a></li>
        <li class="nav-item"><a href="#contacto" class="nav-link">Contacto</a></li>
    </ul>
    
    <!-- Botón Hamburguesa -->
    <button class="hamburger" id="hamburger" aria-label="Menu">
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
    </button>
</nav>

<!-- Menú Móvil -->
<div class="mobile-menu" id="mobileMenu">
    <ul class="mobile-nav">
        <li class="mobile-nav-item"><a href="#inicio" class="mobile-nav-link">Inicio</a></li>
        <li class="mobile-nav-item"><a href="#sobre-mi" class="mobile-nav-link">Sobre Mí</a></li>
        <li class="mobile-nav-item"><a href="#habilidades" class="mobile-nav-link">Habilidades</a></li>
        <li class="mobile-nav-item"><a href="#proyectos" class="mobile-nav-link">Proyectos</a></li>
        <li class="mobile-nav-item"><a href="#contacto" class="mobile-nav-link">Contacto</a></li>
    </ul>
</div>

<!-- Overlay para menú móvil -->
<div class="menu-overlay" id="menuOverlay"></div>

<div class="main-content">
"""

st.markdown(navbar_html, unsafe_allow_html=True)

# --- PREPARAR IMAGEN DE PERFIL ---
profile_image_html = ""
try:
    if PROFILE_PIC.exists():
        with open(PROFILE_PIC, "rb") as img_file:
            img_data = base64.b64encode(img_file.read()).decode()
            profile_image_html = f'<img src="data:image/jpeg;base64,{img_data}" alt="Vera Guillen" />'
    else:
        profile_image_html = '<div style="width: 100%; height: 100%; background: linear-gradient(135deg, #FF6A00, #FF8C2B); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 4rem; color: white;">VG</div>'
except:
    profile_image_html = '<div style="width: 100%; height: 100%; background: linear-gradient(135deg, #FF6A00, #FF8C2B); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 4rem; color: white;">VG</div>'

# --- SECCIÓN HERO (INICIO) ---
st.markdown(f"""
<section id="inicio" class="section">
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-text-section">
                <h1 class="hero-title typing">Hola, soy<br><span style="color: #FF8C2B;">Vera Guillen</span></h1>
                <div class="hero-subtitle">
                    <span>🤖 Transformo datos complejos en soluciones de IA</span>
                </div>
                <div class="hero-card">
                    <div class="hero-card-title">
                        <span>💻 Data Scientist & ML Engineer</span>
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
</section>
""", unsafe_allow_html=True)

# --- SECCIÓN SOBRE MÍ ---
st.markdown("""
<section id="sobre-mi" class="section">
    <h2 class="section-title">Sobre Mí</h2>
    
    <div class="about-section-enhanced">
        <div class="about-grid">
            <div class="about-card-enhanced">
                <div class="about-card-icon">
                    <span style="font-size: 1.8rem;">💻</span>
                </div>
                <p class="about-card-text">
                    <strong>Data Scientist & Machine Learning Engineer</strong> con enfoque end-to-end. Mi experiencia abarca desde la ingeniería de datos hasta el despliegue y la orquestación en producción (MLOps).
                </p>
            </div>
            
            <div class="about-card-enhanced">
                <div class="about-card-icon">
                    <span style="font-size: 1.8rem;">🧠</span>
                </div>
                <p class="about-card-text">
                    Combino <strong>rigor técnico</strong> con <strong>creatividad estratégica</strong> para resolver desafíos complejos mediante Machine Learning, NLP y Computer Vision.
                </p>
            </div>
            
            <div class="about-card-enhanced">
                <div class="about-card-icon">
                    <span style="font-size: 1.8rem;">📊</span>
                </div>
                <p class="about-card-text">
                    Diseño e implemento soluciones de IA escalables que optimizan procesos, automatizan decisiones y descubren <strong>insights accionables</strong> en grandes volúmenes de datos.
                </p>
            </div>
            
            <div class="about-card-enhanced">
                <div class="about-card-icon">
                    <span style="font-size: 1.8rem;">🎭</span>
                </div>
                <p class="about-card-text">
                    Mi sólida formación en <strong>artes escénicas</strong> me aporta una perspectiva única: abordo sistemas complejos como narrativas, comunico insights técnicos con claridad excepcional y diseño soluciones que fusionan funcionalidad con <strong>experiencia de usuario intuitiva</strong>.
                </p>
            </div>
        </div>
    </div>
    
    <!-- Especialidades -->
    <div style="margin-top: 4rem;">
        <h3 class="section-title-enhanced" style="font-size: clamp(1.5rem, 1.3rem + 2vw, 2.5rem); margin-bottom: 2rem;">
            <span>⭐ Mis Especialidades</span>
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
            <div class="specialty-card-enhanced">
                <div class="specialty-icon-enhanced">
                    <span style="font-size: 2.5rem;">🧠</span>
                </div>
                <h4>Machine Learning</h4>
                <p>Modelos predictivos y sistemas de recomendación personalizados.</p>
            </div>
            
            <div class="specialty-card-enhanced">
                <div class="specialty-icon-enhanced">
                    <span style="font-size: 2.5rem;">🤖</span>
                </div>
                <h4>IA Generativa</h4>
                <p>Soluciones de IA conversacional y generación de contenido.</p>
            </div>
            
            <div class="specialty-card-enhanced">
                <div class="specialty-icon-enhanced">
                    <span style="font-size: 2.5rem;">📈</span>
                </div>
                <h4>Análisis Predictivo</h4>
                <p>Extracción de insights y tendencias de grandes volúmenes de datos.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# --- SECCIÓN HABILIDADES ---
st.markdown("""
<section id="habilidades" class="section">
    <h2 class="section-title">Habilidades Técnicas</h2>
    
    <div class="skills-container-enhanced">
        <div class="skill-category-enhanced">
            <h3><span style="margin-right: 12px;">💻</span> Lenguajes y Bases de Datos</h3>
            <div class="skill-items-enhanced">
                <div class="skill-item-enhanced"><span>🐍</span> Python</div>
                <div class="skill-item-enhanced"><span>🗄️</span> SQL</div>
                <div class="skill-item-enhanced"><span>📘</span> TypeScript</div>
                <div class="skill-item-enhanced"><span>🐘</span> PostgreSQL</div>
                <div class="skill-item-enhanced"><span>⚡</span> Redis</div>
                <div class="skill-item-enhanced"><span>🔢</span> pgvector</div>
            </div>
        </div>
        
        <div class="skill-category-enhanced">
            <h3><span style="margin-right: 12px;">🧠</span> Análisis y Machine Learning</h3>
            <div class="skill-items-enhanced">
                <div class="skill-item-enhanced"><span>🐼</span> Pandas</div>
                <div class="skill-item-enhanced"><span>🤖</span> Scikit-learn</div>
                <div class="skill-item-enhanced"><span>📝</span> NLTK</div>
                <div class="skill-item-enhanced"><span>🕷️</span> BeautifulSoup</div>
                <div class="skill-item-enhanced"><span>🧠</span> TensorFlow</div>
                <div class="skill-item-enhanced"><span>🔥</span> PyTorch</div>
            </div>
        </div>
        
        <div class="skill-category-enhanced">
            <h3><span style="margin-right: 12px;">🎨</span> Frontend y Visualización</h3>
            <div class="skill-items-enhanced">
                <div class="skill-item-enhanced"><span>⚛️</span> React 19</div>
                <div class="skill-item-enhanced"><span>🗺️</span> Leaflet</div>
                <div class="skill-item-enhanced"><span>📊</span> Power BI</div>
                <div class="skill-item-enhanced"><span>📈</span> Matplotlib</div>
                <div class="skill-item-enhanced"><span>📉</span> Seaborn</div>
            </div>
        </div>
        
        <div class="skill-category-enhanced">
            <h3><span style="margin-right: 12px;">⚙️</span> Backend, Cloud y Despliegue</h3>
            <div class="skill-items-enhanced">
                <div class="skill-item-enhanced"><span>⚡</span> FastAPI</div>
                <div class="skill-item-enhanced"><span>🍶</span> Flask</div>
                <div class="skill-item-enhanced"><span>🐳</span> Docker</div>
                <div class="skill-item-enhanced"><span>☁️</span> Azure</div>
                <div class="skill-item-enhanced"><span>💬</span> WhatsApp API</div>
                <div class="skill-item-enhanced"><span>🔍</span> Google APIs</div>
            </div>
        </div>
    </div>
    
    <!-- Habilidades Blandas -->
    <div class="soft-skills-section" style="margin-top: 4rem;">
        <h3 class="soft-skills-title" style="font-size: clamp(1.5rem, 1.3rem + 2vw, 2.8rem);">
            <span>👤</span> <span>Habilidades Blandas</span>
        </h3>
        <p class="soft-skills-description">
            Habilidades interpersonales esenciales que potencian mi desempeño profesional.
        </p>
        
        <div class="soft-skills-container-enhanced">
            <div class="soft-skill-card-enhanced">
                <div class="soft-skill-header-enhanced">
                    <div class="soft-skill-icon-wrapper">
                        <span style="font-size: 1.5rem;">🧩</span>
                    </div>
                    <h3>Resolución de Problemas</h3>
                </div>
                <p>Capacidad para analizar problemas complejos y encontrar soluciones efectivas y creativas.</p>
            </div>
            
            <div class="soft-skill-card-enhanced">
                <div class="soft-skill-header-enhanced">
                    <div class="soft-skill-icon-wrapper">
                        <span style="font-size: 1.5rem;">👥</span>
                    </div>
                    <h3>Trabajo en Equipo</h3>
                </div>
                <p>Excelente capacidad para colaborar en equipos multidisciplinarios y fomentar un ambiente de trabajo positivo.</p>
            </div>
            
            <div class="soft-skill-card-enhanced">
                <div class="soft-skill-header-enhanced">
                    <div class="soft-skill-icon-wrapper">
                        <span style="font-size: 1.5rem;">💬</span>
                    </div>
                    <h3>Comunicación Efectiva</h3>
                </div>
                <p>Habilidad para explicar conceptos técnicos de manera clara a diferentes audiencias.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# --- SECCIÓN PROYECTOS ---
PROJECTS = [
    {
        "title": "Modelado de Movilidad Sostenible",
        "subtitle": "Análisis de viabilidad para la transición a flotas de vehículos ecológicos",
        "description": "Estudio integral que evalúa la viabilidad de transición a vehículos ecológicos en flotas urbanas, incluyendo análisis de costos, infraestructura necesaria y beneficios ambientales.",
        "technologies": ["Python", "Pandas", "Matplotlib", "Scikit-learn", "Streamlit"],
        "github_url": "https://github.com/veraguillen/New_York_Taxis_IA"
    },
    {
        "title": "Chatbot RAG Multimarca",
        "subtitle": "Sistema de IA conversacional para atención al cliente multicanal",
        "description": "Desarrollo de un chatbot avanzado con arquitectura RAG (Retrieval-Augmented Generation) que permite a las empresas ofrecer soporte multicanal (WhatsApp, web, aplicaciones móviles) con respuestas precisas basadas en su base de conocimiento.",
        "technologies": ["Python", "FastAPI", "Llama 3", "RAG", "pgvector", "Docker", "Kubernetes"],
        "github_url": "https://github.com/veraguillen/Bot-Multimarcas-RAG"
    },
    {
        "title": "Plataforma Inmobiliaria Inteligente",
        "subtitle": "Solución integral de gestión y búsqueda de propiedades con IA",
        "description": "Plataforma que utiliza procesamiento de lenguaje natural y visión por computadora para analizar y categorizar propiedades, ofreciendo búsquedas semánticas y recomendaciones personalizadas.",
        "technologies": ["React", "Python", "FastAPI", "PostgreSQL", "OpenCV", "Docker"],
        "github_url": "https://github.com/veraguillen/Real-State-IA"
    },
    {
        "title": "Monitoreo farmacéutico IoT",
        "subtitle": "Sistema de monitoreo en tiempo real",
        "description": "Sistema de monitoreo en tiempo real para el control de condiciones ambientales en la industria farmacéutica, con alertas y análisis predictivo para garantizar la cadena de frío de medicamentos sensibles.",
        "technologies": ["Python", "MQTT", "InfluxDB", "Grafana", "Raspberry Pi", "Docker"],
        "github_url": "https://github.com/tu-usuario/pharmawatch"
    },
    {
        "title": "Data Acquisition Platform",
        "subtitle": "Plataforma de adquisición y procesamiento de datos",
        "description": "Sistema de adquisición de datos de múltiples fuentes con capacidades de procesamiento y análisis en tiempo real, diseñado para manejar grandes volúmenes de información con alta disponibilidad.",
        "technologies": ["Python", "Airflow", "Kafka", "Elasticsearch", "Docker"],
        "github_url": "https://github.com/veraguillen/AGENTE-Busqueda-APIS"
    }
]

projects_html = """
<section id="proyectos" class="section">
    <h2 class="section-title">Mis Proyectos</h2>
    <p style="text-align: center; color: var(--text-secondary); font-size: clamp(1rem, 0.9rem + 1vw, 1.2rem); margin-bottom: 3rem;">
        Una selección de mis trabajos más recientes y relevantes
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; max-width: 1400px; margin: 0 auto; padding: 0 1rem;">
"""

for project in PROJECTS:
    tech_tags = "".join([f'<span class="tech-tag">{tech}</span>' for tech in project["technologies"]])
    projects_html += f"""
        <div class="project-card">
            <h3 style="color: var(--accent-orange-glow); margin-bottom: 0.5rem; font-size: clamp(1.125rem, 1rem + 1.5vw, 1.5rem);">{project["title"]}</h3>
            <h4 style="color: var(--text-secondary); margin-bottom: 1rem; font-size: clamp(1rem, 0.9rem + 1vw, 1.125rem); font-weight: 500;">{project["subtitle"]}</h4>
            <p style="color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.7;">{project["description"]}</p>
            <div style="margin-bottom: 1.5rem;">
                {tech_tags}
            </div>
            <a href="{project["github_url"]}" target="_blank" rel="noopener noreferrer" 
               style="display: inline-flex; align-items: center; gap: 0.5rem; color: var(--accent-orange); text-decoration: none; font-weight: 600; transition: all 0.3s ease;">
                <span>🔗</span> Ver en GitHub →
            </a>
        </div>
    """

projects_html += """
    </div>
</section>
"""

st.markdown(projects_html, unsafe_allow_html=True)

# --- SECCIÓN CONTACTO ---
st.markdown("""
<section id="contacto" class="section">
    <h2 class="section-title">Contáctame</h2>
    <p style="text-align: center; color: var(--text-secondary); font-size: clamp(1rem, 0.9rem + 1vw, 1.3rem); margin-bottom: 3rem; max-width: 700px; margin-left: auto; margin-right: auto;">
        ¿Tienes un proyecto en mente o quieres trabajar juntos? 
        Estoy disponible para oportunidades de colaboración y conversaciones sobre tecnología y datos.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; max-width: 1000px; margin: 0 auto; padding: 0 1rem;">
        <div class="contact-card-enhanced">
            <div class="contact-icon-wrapper">
                <span style="font-size: 2.8rem;">📧</span>
            </div>
            <h3 class="contact-title">Correo Electrónico</h3>
            <p class="contact-description">Envíame un mensaje directamente</p>
            <a href="mailto:vera.guillen27@gmail.com" class="contact-link-enhanced" target="_blank">
                <span>✉️</span> <span>Enviar Email</span>
            </a>
        </div>
        
        <div class="contact-card-enhanced">
            <div class="contact-icon-wrapper">
                <span style="font-size: 2.8rem;">💻</span>
            </div>
            <h3 class="contact-title">GitHub</h3>
            <p class="contact-description">Revisa mis proyectos en GitHub</p>
            <a href="https://github.com/veraguillen" class="contact-link-enhanced" target="_blank">
                <span>🔗</span> <span>Ver Perfil</span>
            </a>
        </div>
        
        <div class="contact-card-enhanced">
            <div class="contact-icon-wrapper">
                <span style="font-size: 2.8rem;">💼</span>
            </div>
            <h3 class="contact-title">LinkedIn</h3>
            <p class="contact-description">Conecta conmigo profesionalmente</p>
            <a href="https://www.linkedin.com/in/vera-guillen-9b464a303/" class="contact-link-enhanced" target="_blank">
                <span>🔗</span> <span>Conectar</span>
            </a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<footer style="background: var(--bg-card); border-top: 0.0625rem solid rgba(255, 106, 0, 0.2); padding: 2rem 1rem; text-align: center; margin-top: 4rem;">
    <p style="color: var(--text-secondary); font-size: clamp(0.875rem, 0.8rem + 0.4vw, 1rem); margin: 0;">
        © 2025 Vera Guillen. Hecho con ❤️ y mucho ☕
    </p>
    <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
        <a href="https://github.com/veraguillen" target="_blank" rel="noopener noreferrer" 
           style="color: var(--text-secondary); text-decoration: none; transition: all 0.3s ease; min-height: 2.75rem; min-width: 2.75rem; display: flex; align-items: center; justify-content: center;">
            GitHub
        </a>
        <a href="https://www.linkedin.com/in/vera-guillen-9b464a303/" target="_blank" rel="noopener noreferrer"
           style="color: var(--text-secondary); text-decoration: none; transition: all 0.3s ease; min-height: 2.75rem; min-width: 2.75rem; display: flex; align-items: center; justify-content: center;">
            LinkedIn
        </a>
    </div>
</footer>
</div>
""", unsafe_allow_html=True)

# --- CARGAR JAVASCRIPT ---
if navbar_js:
    st.markdown(f"""
    <script>
    {navbar_js}
    </script>
    """, unsafe_allow_html=True)

# --- ESTILOS ADICIONALES PARA SECCIONES ---
st.markdown("""
<style>
/* Estilos para las secciones específicas */
.hero-container {
    background: var(--bg-card);
    border-radius: clamp(1rem, 0.8rem + 2vw, 1.5rem);
    padding: clamp(2rem, 3vw, 3rem);
    margin: 2rem auto;
    max-width: 1400px;
    box-shadow: 0 clamp(1rem, 1.5vw, 1.875rem) clamp(3rem, 4vw, 3.75rem) rgba(0, 0, 0, 0.5),
                0 0 clamp(1.5rem, 2vw, 1.875rem) rgba(255, 106, 0, 0.2);
    position: relative;
    overflow: hidden;
    border: 0.0625rem solid rgba(255, 106, 0, 0.2);
}

.hero-content {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    align-items: center;
}

@media (min-width: 48rem) {
    .hero-content {
        grid-template-columns: 1.5fr 1fr;
    }
}

.hero-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(2rem, 1.5rem + 4vw, 3.5rem);
    font-weight: 800;
    color: var(--accent-orange-glow);
    text-shadow: 0 0 clamp(1.125rem, 1.5vw, 1.875rem) rgba(255, 140, 43, 0.6);
    margin-bottom: 1rem;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: clamp(1.125rem, 1rem + 1.5vw, 1.5rem);
    color: var(--text-secondary);
    margin: 1.5rem 0;
    font-weight: 400;
}

.hero-card {
    background: var(--bg-card);
    border-radius: 1rem;
    padding: 2rem;
    margin-top: 2rem;
    border: 0.0625rem solid rgba(255, 106, 0, 0.2);
        transition: all 0.3s ease;
}

.hero-card-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(1.125rem, 1rem + 1.5vw, 1.5rem);
    color: var(--accent-orange-glow);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.hero-card-text {
    color: var(--text-secondary);
    line-height: 1.8;
    font-size: clamp(1rem, 0.9rem + 1vw, 1.1rem);
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
    width: clamp(12rem, 10rem + 15vw, 17.5rem);
    height: clamp(12rem, 10rem + 15vw, 17.5rem);
    border-radius: 50%;
    padding: 0.375rem;
    background: linear-gradient(135deg, #FF6A00, #FF8C2B, #FF6A00);
    background-size: 200% 200%;
    animation: gradient-rotate 3s ease infinite;
    box-shadow: 0 0 clamp(2rem, 3vw, 2.5rem) rgba(255, 106, 0, 0.5);
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
    background: var(--bg-main);
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
    width: clamp(15rem, 12rem + 18vw, 20rem);
    height: clamp(15rem, 12rem + 18vw, 20rem);
    border-radius: 50%;
    border: 0.125rem solid rgba(255, 106, 0, 0.2);
    animation: rotate 20s linear infinite;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Asegurar que las secciones tengan altura mínima */
.section {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* Grid responsive para proyectos */
@media (max-width: 47.9375rem) {
    .section {
        min-height: auto;
        padding: 3rem 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)
