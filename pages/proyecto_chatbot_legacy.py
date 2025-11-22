import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Chatbot Multimarca | Proyectos", layout="wide")

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
PROYECTOS_DIR = ASSETS_DIR / "proyectos"

# --- CUSTOM CSS ---
from pages.project_styles import load_project_styles, github_button
load_project_styles()

# --- PROJECT HEADER ---
st.markdown("""
<div class='project-header-enhanced'>
    <h1 class='project-title-enhanced'>
        <i class='fas fa-robot'></i> Chatbot RAG Multimarca
    </h1>
    <p class='project-subtitle'>Plataforma empresarial de asistencia conversacional con IA</p>
    <p style='font-family: Inter, sans-serif; color: #8B949E; margin-top: 1rem;'>
        <strong>Desarrollador:</strong> Vera Guillén | 
        <strong>Versión:</strong> 1.0.1 | 
        <strong>Stack Principal:</strong> Python, FastAPI, PostgreSQL, Docker, Azure | 
        <strong>Repositorio:</strong> <a href='https://github.com/veraguillen/Bot-Multimarcas-RAG' style='color: #FF6A00; text-shadow: 0 0 10px rgba(255, 106, 0, 0.5);'>Ver en GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(PROYECTOS_DIR / "chatbot_rag.jpg"), width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        try:
            st.image("assets/proyectos/chatbot_rag.jpg", width='stretch')
        except:
            st.warning("Imagen de portada no encontrada. Por favor, coloca una imagen en assets/proyectos/chatbot_rag.jpg")

# --- VIDEO DEMO ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-video'></i>
    <span>Demostración en Video</span>
</h2>
<style>
    .video-container {
        max-width: 600px;
        margin: 0 auto;
    }
    .video-container video {
        max-width: 100%;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)
_, col2, _ = st.columns([0.25, 0.5, 0.25])
with col2:
    try:
        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        st.video(str(PROYECTOS_DIR / "bot.mp4"))
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Video de demostración no encontrado")

st.markdown("---")

# --- EXECUTIVE SUMMARY ---
st.markdown("""
<div class='content-card'>
    <p style='font-family: Inter, sans-serif; color: #C8D1E0; font-size: 1.1rem; line-height: 1.8;'>
        <strong style='color: #FF8C00;'>Chatbot Multimarca</strong> es una plataforma empresarial de chatbot inteligente que integra múltiples tecnologías de vanguardia para ofrecer asistencia conversacional automatizada a través de WhatsApp. El sistema utiliza Retrieval-Augmented Generation (RAG) con búsqueda vectorial para proporcionar respuestas contextuales precisas basadas en documentación empresarial.
    </p>
    <h3 style='color: #E8F0FF; font-family: Inter, sans-serif; margin-top: 2rem;'>Características Destacadas</h3>
""", unsafe_allow_html=True)
st.markdown("""
- ✅ **Arquitectura Asíncrona Completa** con FastAPI y SQLAlchemy async
- ✅ **Sistema RAG Avanzado** con PGVector para búsqueda semántica
- ✅ **Integración Multi-Plataforma** (WhatsApp Business API, interfaz web Chainlit)
- ✅ **Máquina de Estados Conversacional** para flujos complejos
- ✅ **Despliegue Containerizado** con Docker y Azure App Service
- ✅ **Observabilidad y Resiliencia** con circuit breakers, caché Redis y logging estructurado
    </div>
</div>
""", unsafe_allow_html=True)

# --- SYSTEM ARCHITECTURE ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-sitemap'></i>
    <span>Arquitectura del Sistema</span>
</h2>
""", unsafe_allow_html=True)
st.markdown("### Stack Tecnológico Completo")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Backend Core")
    st.markdown("- FastAPI 0.115.12\n- Python 3.10\n- Uvicorn/Gunicorn\n- Pydantic 2.11.7")
    st.markdown("#### Inteligencia Artificial")
    st.markdown("- Langchain Core 0.3.65\n- Langchain-Postgres 0.0.14\n- Sentence-Transformers 4.1.0\n- PyTorch 2.7.1")
with col2:
    st.markdown("#### Base de Datos y Persistencia")
    st.markdown("- PostgreSQL 15\n- PGVector 0.3.6\n- SQLAlchemy 2.0.41 (Async)\n- Redis 7")
    st.markdown("#### DevOps e Infraestructura")
    st.markdown("- Docker (Multi-Stage)\n- Azure App Service\n- Azure PostgreSQL")
st.markdown("---")

st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-images'></i>
    <span>Galería del Proyecto</span>
</h2>
""", unsafe_allow_html=True)

# Galería organizada - Primera fila: 3 imágenes multimarca
gallery_row1 = st.columns(3)
with gallery_row1[0]:
    try:
        st.image(str(PROYECTOS_DIR / "multimarca1.png"), caption="Interfaz principal del chatbot", width='stretch')
    except:
        st.warning("multimarca1.png no encontrada")
with gallery_row1[1]:
    try:
        st.image(str(PROYECTOS_DIR / "multimarca2.png"), caption="Sistema de selección de marca", width='stretch')
    except:
        st.warning("multimarca2.png no encontrada")
with gallery_row1[2]:
    try:
        st.image(str(PROYECTOS_DIR / "multimarca3.png"), caption="Chat conversacional con RAG", width='stretch')
    except:
        st.warning("multimarca3.png no encontrada")

# Segunda fila: 2 imágenes (multimarca4 y bot1)
gallery_row2 = st.columns(2)
with gallery_row2[0]:
    try:
        st.image(str(PROYECTOS_DIR / "multimarca4.jpg"), caption="Arquitectura del sistema", width='stretch')
    except:
        st.warning("multimarca4.jpg no encontrada")
with gallery_row2[1]:
    try:
        st.image(str(PROYECTOS_DIR / "bot1.png"), caption="Vista del chatbot en acción", width='stretch')
    except:
        st.warning("bot1.png no encontrada")

# Tercera fila: bot2 si existe
try:
    bot2_path = PROYECTOS_DIR / "bot2.png"
    if bot2_path.exists():
        st.image(str(bot2_path), caption="Interfaz de usuario avanzada", width='stretch')
except:
    pass

st.markdown("---")

# --- KEY TECHNICAL COMPONENTS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-cogs'></i>
    <span>Componentes Técnicos Clave</span>
</h2>
""", unsafe_allow_html=True)
with st.expander("1. Sistema RAG (Retrieval-Augmented Generation)", expanded=True):
    st.markdown("**Archivo:** `app/ai/rag_retriever.py`")
    st.markdown("**Características:** Embeddings multilingües, búsqueda vectorial con filtrado por marca, deduplicación inteligente y scoring de relevancia.")
    st.markdown("**Optimizaciones:** Chunk Size: 1200, Overlap: 150, Similarity Threshold: 0.3, K Final: 4.")

with st.expander("2. Máquina de Estados Conversacional", expanded=True):
    st.markdown("**Archivo:** `app/main/webhook_handler.py`")
    st.markdown("Maneja flujos complejos como selección de marca, chat principal, recolección de datos y agendamiento.")
    st.code("""
# Estados Implementados
STAGE_SELECTING_BRAND
STAGE_AWAITING_ACTION
STAGE_MAIN_CHAT_RAG
STAGE_COLLECTING_NAME
STAGE_SCHEDULING_APPOINTMENT
""", language="python")

with st.expander("3. Cliente LLM con Factory Pattern y Resiliencia", expanded=True):
    st.markdown("**Archivo:** `app/api/llm_client.py`")
    st.markdown("**Características:** Circuit Breaker, Caché Redis, Request ID Tracking y reintentos automáticos con backoff para proteger contra fallos del servicio LLM.")

st.markdown("---")

# --- DEPLOYMENT & SECURITY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fab fa-docker'></i>
    <span>Containerización, Despliegue y Seguridad</span>
</h2>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Dockerfile Multi-Stage")
    st.markdown("Dockerfile optimizado con una etapa de 'builder' para compilar dependencias y una etapa de 'runtime' ligera con un usuario no-root para mayor seguridad.")
    st.markdown("### Script de Inicio (`startup.sh`)")
    st.markdown("Asegura la disponibilidad de la BD y Redis, ejecuta migraciones Alembic e inicia Gunicorn con workers configurables.")
with col2:
    st.markdown("### Medidas de Seguridad")
    st.markdown("- **Gestión de Secretos:** Variables de entorno, sin hardcoding.\n- **SSL/TLS:** Conexiones forzadas en producción.\n- **Validación:** Pydantic para toda la entrada de datos.\n- **Compliance:** Endpoints para Política de Privacidad, Términos de Servicio y Eliminación de Datos.")
st.markdown("---")

# --- DESIGN PATTERNS & SKILLS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-lightbulb'></i>
    <span>Patrones de Diseño y Habilidades Demostradas</span>
</h2>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Patrones Implementados")
    st.markdown("- Factory Pattern\n- Singleton Pattern\n- State Machine Pattern\n- Repository Pattern\n- Circuit Breaker Pattern\n- Middleware Pattern")
with col2:
    st.markdown("### Habilidades Clave")
    st.markdown("- Desarrollo Backend Avanzado (Async)\n- Arquitectura de Sistemas de IA (RAG)\n- DevOps (Docker, Azure)\n- Diseño de BD (PostgreSQL + PGVector)\n- Observabilidad y Resiliencia")
st.markdown("---")

st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Dashboard de Análisis en Tiempo Real</span>
</h2>
""", unsafe_allow_html=True)
st.markdown("**Tecnologías**: Streamlit, Plotly, Pandas, Python")
st.markdown("""
**Características**:
- Monitoreo en tiempo real del rendimiento del chatbot
- Análisis de métricas de usuario
- Visualización de datos con gráficos interactivos
- Filtrado por marca y período de tiempo
""")
st.markdown("### 📈 Galería de Métricas")
metrics_cols = st.columns(3)
with metrics_cols[0]:
    try:
        st.image(str(ASSETS_DIR / "metricas1.png"), caption="Métricas de rendimiento del chatbot", width='stretch')
    except:
        st.warning("metricas1.png no encontrada")
with metrics_cols[1]:
    try:
        st.image(str(ASSETS_DIR / "metricas2.png"), caption="Análisis de interacciones por marca", width='stretch')
    except:
        st.warning("metricas2.png no encontrada")
with metrics_cols[2]:
    try:
        st.image(str(ASSETS_DIR / "metricas3.png"), caption="Estadísticas de uso y satisfacción", width='stretch')
    except:
        st.warning("metricas3.png no encontrada")

# --- GITHUB BUTTONS ---
col1, col2 = st.columns(2)
with col1:
    github_button("https://github.com/veraguillen/Bot-Multimarcas-RAG", "🔗 Chatbot RAG - GitHub")
with col2:
    github_button("https://github.com/veraguillen/Metricas-RAG-Chat-Multimarca", "🔗 Dashboard Métricas - GitHub")
