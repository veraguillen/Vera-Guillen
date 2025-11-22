"""
Portfolio SPA - Single Page Application
Navbar fija con scroll suave entre secciones
"""
import streamlit as st
from pathlib import Path
import base64

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
PROFILE_PIC = ASSETS_DIR / "foto_perfil.jpg"
CSS_FILE = BASE_DIR / "spa_styles.css"
JS_FILE = BASE_DIR / "spa_script.js"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vera Guillen | Data Scientist & ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"  # Ocultar sidebar por defecto
)

# Ocultar sidebar completamente
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    .stApp > header {
        display: none !important;
    }
    
    .stApp {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CARGAR CSS Y JS ---
def load_css():
    """Carga el archivo CSS de la SPA"""
    try:
        with open(CSS_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

def load_js():
    """Carga el archivo JavaScript de la SPA"""
    try:
        with open(JS_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

# Cargar estilos y scripts
css_content = load_css()
js_content = load_js()

# --- OBTENER IMAGEN DE PERFIL ---
def get_profile_image():
    """Obtiene la imagen de perfil en base64"""
    try:
        if PROFILE_PIC.exists():
            with open(PROFILE_PIC, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                return f'data:image/jpeg;base64,{img_data}'
    except:
        pass
    return None

profile_image = get_profile_image()

# --- ESTRUCTURA HTML COMPLETA ---
html_structure = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vera Guillen | Data Scientist & ML Engineer</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    <!-- NAVBAR -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="#inicio" class="logo-link">VG</a>
            </div>
            <ul class="nav-menu" id="nav-menu">
                <li class="nav-item">
                    <a href="#inicio" class="nav-link">Inicio</a>
                </li>
                <li class="nav-item">
                    <a href="#sobre-mi" class="nav-link">Sobre mí</a>
                </li>
                <li class="nav-item">
                    <a href="#habilidades" class="nav-link">Habilidades</a>
                </li>
                <li class="nav-item">
                    <a href="#proyectos" class="nav-link">Proyectos</a>
                </li>
                <li class="nav-item">
                    <a href="#contacto" class="nav-link">Contacto</a>
                </li>
            </ul>
            <div class="nav-toggle" id="nav-toggle" aria-label="Toggle menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section id="inicio" class="hero-section">
        <div class="hero-container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1 class="hero-title">
                        <span class="greeting">Hola, soy</span>
                        <span class="name">Vera Guillen</span>
                    </h1>
                    <p class="hero-subtitle">Transformo datos complejos en soluciones de IA</p>
                    <p class="hero-description">
                        Data Scientist & Machine Learning Engineer especializada en diseñar e implementar 
                        soluciones escalables que optimizan procesos y automatizan decisiones.
                    </p>
                    <div class="hero-buttons">
                        <a href="#proyectos" class="btn btn-primary">Ver Proyectos</a>
                        <a href="#contacto" class="btn btn-secondary">Contáctame</a>
                    </div>
                </div>
                <div class="hero-image">
                    {"<img src='" + profile_image + "' alt='Vera Guillen' class='profile-img'>" if profile_image else "<div class='profile-placeholder'><span>VG</span></div>"}
                </div>
            </div>
        </div>
    </section>

    <!-- SOBRE MÍ SECTION -->
    <section id="sobre-mi" class="section">
        <div class="container">
            <h2 class="section-title">Sobre Mí</h2>
            <div class="about-content">
                <div class="about-card">
                    <div class="card-icon">💻</div>
                    <h3>Data Scientist & ML Engineer</h3>
                    <p>Mi experiencia abarca desde la ingeniería de datos hasta el despliegue y la orquestación en producción (MLOps).</p>
                </div>
                <div class="about-card">
                    <div class="card-icon">🧠</div>
                    <h3>Rigor Técnico + Creatividad</h3>
                    <p>Combino rigor técnico con creatividad estratégica para resolver desafíos complejos mediante Machine Learning, NLP y Computer Vision.</p>
                </div>
                <div class="about-card">
                    <div class="card-icon">📊</div>
                    <h3>Soluciones Escalables</h3>
                    <p>Diseño e implemento soluciones de IA escalables que optimizan procesos, automatizan decisiones y descubren insights accionables.</p>
                </div>
                <div class="about-card">
                    <div class="card-icon">🎭</div>
                    <h3>Diferencial Creativo</h3>
                    <p>Mi sólida formación en artes escénicas me aporta una perspectiva única: abordo sistemas complejos como narrativas y comunico insights técnicos con claridad excepcional.</p>
                </div>
            </div>
            
            <div class="languages-section">
                <h3 class="subsection-title">Idiomas</h3>
                <div class="languages-grid">
                    <div class="language-card">
                        <h4>Español</h4>
                        <div class="language-level">Nativo</div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 100%"></div>
                        </div>
                    </div>
                    <div class="language-card">
                        <h4>Inglés</h4>
                        <div class="language-level">B2 Avanzado</div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 75%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- HABILIDADES SECTION -->
    <section id="habilidades" class="section section-alt">
        <div class="container">
            <h2 class="section-title">Habilidades Técnicas</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>💻 Lenguajes y Bases de Datos</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">SQL</span>
                        <span class="skill-tag">TypeScript</span>
                        <span class="skill-tag">PostgreSQL</span>
                        <span class="skill-tag">Redis</span>
                        <span class="skill-tag">pgvector</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>🤖 Análisis y Machine Learning</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">Pandas</span>
                        <span class="skill-tag">Scikit-learn</span>
                        <span class="skill-tag">NLTK</span>
                        <span class="skill-tag">TensorFlow</span>
                        <span class="skill-tag">PyTorch</span>
                        <span class="skill-tag">BeautifulSoup</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>🎨 Frontend y Visualización</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">React 19</span>
                        <span class="skill-tag">Leaflet</span>
                        <span class="skill-tag">Power BI</span>
                        <span class="skill-tag">Matplotlib</span>
                        <span class="skill-tag">Seaborn</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>☁️ Backend, Cloud y Despliegue</h3>
                    <div class="skill-tags">
                        <span class="skill-tag">FastAPI</span>
                        <span class="skill-tag">Flask</span>
                        <span class="skill-tag">Docker</span>
                        <span class="skill-tag">Azure</span>
                        <span class="skill-tag">WhatsApp API</span>
                        <span class="skill-tag">Google APIs</span>
                    </div>
                </div>
            </div>
            
            <div class="soft-skills-section">
                <h3 class="subsection-title">Habilidades Blandas</h3>
                <div class="soft-skills-grid">
                    <div class="soft-skill-card">
                        <h4>🧩 Resolución de Problemas</h4>
                        <p>Capacidad para analizar problemas complejos y encontrar soluciones efectivas y creativas.</p>
                    </div>
                    <div class="soft-skill-card">
                        <h4>👥 Trabajo en Equipo</h4>
                        <p>Excelente capacidad para colaborar en equipos multidisciplinarios y fomentar un ambiente de trabajo positivo.</p>
                    </div>
                    <div class="soft-skill-card">
                        <h4>💬 Comunicación Efectiva</h4>
                        <p>Habilidad para explicar conceptos técnicos de manera clara a diferentes audiencias.</p>
                    </div>
                    <div class="soft-skill-card">
                        <h4>📚 Aprendizaje Continuo</h4>
                        <p>Compromiso con el aprendizaje constante y la actualización en las últimas tecnologías.</p>
                    </div>
                    <div class="soft-skill-card">
                        <h4>⏰ Gestión del Tiempo</h4>
                        <p>Habilidad para priorizar tareas y cumplir con los plazos establecidos de manera eficiente.</p>
                    </div>
                    <div class="soft-skill-card">
                        <h4>🧠 Pensamiento Crítico</h4>
                        <p>Capacidad para analizar información de manera objetiva y tomar decisiones fundamentadas.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PROYECTOS SECTION -->
    <section id="proyectos" class="section">
        <div class="container">
            <h2 class="section-title">Proyectos</h2>
            <p class="section-subtitle">Una selección de mis trabajos más recientes y relevantes</p>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">🚗</div>
                    </div>
                    <div class="project-content">
                        <h3>Modelado de Movilidad Sostenible</h3>
                        <p class="project-subtitle">Análisis de viabilidad para la transición a flotas de vehículos ecológicos</p>
                        <p class="project-description">Estudio integral que evalúa la viabilidad de transición a vehículos ecológicos en flotas urbanas.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">Scikit-learn</span>
                            <span class="tech-tag">Streamlit</span>
                        </div>
                        <a href="https://github.com/veraguillen/New_York_Taxis_IA" target="_blank" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">🤖</div>
                    </div>
                    <div class="project-content">
                        <h3>Chatbot RAG Multimarca</h3>
                        <p class="project-subtitle">Sistema de IA conversacional para atención al cliente multicanal</p>
                        <p class="project-description">Chatbot avanzado con arquitectura RAG que permite soporte multicanal con respuestas precisas basadas en base de conocimiento.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">FastAPI</span>
                            <span class="tech-tag">Llama 3</span>
                            <span class="tech-tag">RAG</span>
                            <span class="tech-tag">Docker</span>
                        </div>
                        <a href="https://github.com/veraguillen/Bot-Multimarcas-RAG" target="_blank" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">🏘️</div>
                    </div>
                    <div class="project-content">
                        <h3>Plataforma Inmobiliaria Inteligente</h3>
                        <p class="project-subtitle">Solución integral de gestión y búsqueda de propiedades con IA</p>
                        <p class="project-description">Plataforma que utiliza NLP y visión por computadora para analizar y categorizar propiedades, ofreciendo búsquedas semánticas.</p>
                        <div class="project-tech">
                            <span class="tech-tag">React</span>
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">FastAPI</span>
                            <span class="tech-tag">PostgreSQL</span>
                            <span class="tech-tag">OpenCV</span>
                        </div>
                        <a href="https://github.com/veraguillen/Real-State-IA" target="_blank" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">💊</div>
                    </div>
                    <div class="project-content">
                        <h3>Monitoreo farmacéutico IoT</h3>
                        <p class="project-subtitle">Sistema de monitoreo en tiempo real</p>
                        <p class="project-description">Sistema de monitoreo en tiempo real para el control de condiciones ambientales en la industria farmacéutica.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">MQTT</span>
                            <span class="tech-tag">InfluxDB</span>
                            <span class="tech-tag">Grafana</span>
                            <span class="tech-tag">Raspberry Pi</span>
                        </div>
                        <a href="#" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">🛰️</div>
                    </div>
                    <div class="project-content">
                        <h3>Data Acquisition Platform</h3>
                        <p class="project-subtitle">Plataforma de adquisición y procesamiento de datos</p>
                        <p class="project-description">Sistema de adquisición de datos de múltiples fuentes con capacidades de procesamiento y análisis en tiempo real.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Airflow</span>
                            <span class="tech-tag">Kafka</span>
                            <span class="tech-tag">Elasticsearch</span>
                            <span class="tech-tag">Docker</span>
                        </div>
                        <a href="https://github.com/veraguillen/AGENTE-Busqueda-APIS" target="_blank" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <div class="project-placeholder">🎮</div>
                    </div>
                    <div class="project-content">
                        <h3>Sistema de Recomendación</h3>
                        <p class="project-subtitle">Sistema de recomendación personalizado</p>
                        <p class="project-description">Sistema de recomendación avanzado utilizando técnicas de Machine Learning y análisis de comportamiento.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Scikit-learn</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">Streamlit</span>
                        </div>
                        <a href="#" class="project-link">Ver en GitHub →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTACTO SECTION -->
    <section id="contacto" class="section section-alt">
        <div class="container">
            <h2 class="section-title">Contáctame</h2>
            <p class="section-subtitle">¿Tienes un proyecto en mente o quieres trabajar juntos?</p>
            <div class="contact-grid">
                <div class="contact-card">
                    <div class="contact-icon">📧</div>
                    <h3>Correo Electrónico</h3>
                    <p>Envíame un mensaje directamente</p>
                    <a href="mailto:vera.guillen27@gmail.com" class="contact-link">vera.guillen27@gmail.com</a>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">💼</div>
                    <h3>LinkedIn</h3>
                    <p>Conecta conmigo profesionalmente</p>
                    <a href="https://www.linkedin.com/in/vera-guillen-9b464a303/" target="_blank" class="contact-link">Ver Perfil</a>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">💻</div>
                    <h3>GitHub</h3>
                    <p>Revisa mis proyectos en GitHub</p>
                    <a href="https://github.com/veraguillen" target="_blank" class="contact-link">Ver Perfil</a>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Vera Guillen. Todos los derechos reservados.</p>
            <div class="footer-links">
                <a href="#inicio">Inicio</a>
                <a href="#sobre-mi">Sobre mí</a>
                <a href="#habilidades">Habilidades</a>
                <a href="#proyectos">Proyectos</a>
                <a href="#contacto">Contacto</a>
            </div>
        </div>
    </footer>

    <script>
        {js_content}
    </script>
</body>
</html>
"""

# Renderizar la estructura completa
st.markdown(html_structure, unsafe_allow_html=True)

