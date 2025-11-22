import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Chatbot Avanzado | Proyectos",
    page_icon="🤖",
    layout="wide"
)

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
PROYECTOS_DIR = ASSETS_DIR / "proyectos"

# --- CUSTOM CSS ---
from pages.project_styles import load_project_styles, github_button
load_project_styles()

# --- HEADER SECTION ---
st.markdown("""
<div class='project-header-enhanced'>
    <h1 class='project-title-enhanced'>
        <i class='fas fa-robot'></i> Chatbot Inmobiliario Inteligente
    </h1>
    <p class='project-subtitle'>Plataforma Multi-Canal con Integración WhatsApp Business e IA Generativa</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "chatbot_inmobiliaria_hero.jpg"), width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: chatbot_hero.jpg")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Solución empresarial de comunicación automatizada que integra WhatsApp Business API con inteligencia artificial avanzada para el sector inmobiliario. 
        El sistema procesa consultas de clientes en tiempo real utilizando arquitectura asíncrona de alto rendimiento.
    </p>
</div>
""", unsafe_allow_html=True)

# --- KEY METRICS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-line'></i>
    <span>Métricas Clave</span>
</h2>
""", unsafe_allow_html=True)

metrics_cols = st.columns(3)
with metrics_cols[0]:
    st.metric("Rendimiento", "100+", "solicitudes concurrentes")
    st.metric("Eficiencia", "70-80%", "consultas automatizadas")
    
with metrics_cols[1]:
    st.metric("Tiempo de Respuesta", "<5s", "de horas a segundos")
    st.metric("Código", "6,000+", "líneas de Python")
    
with metrics_cols[2]:
    st.metric("Disponibilidad", "99%+", "tiempo de actividad")
    st.metric("Endpoints", "73+", "API asíncronos")

# --- TECHNICAL STACK ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-tools'></i>
    <span>Stack Tecnológico</span>
</h2>
""", unsafe_allow_html=True)

tech_cols = st.columns(3)

with tech_cols[0]:
    st.markdown("#### Backend Core")
    st.markdown("""
    - FastAPI 0.104.1 (Async/Await)
    - PostgreSQL + pgvector
    - SQLAlchemy 2.0 (Async)
    - Redis (Caché)
    -Webhooks
    """)

with tech_cols[1]:
    st.markdown("#### Inteligencia Artificial")
    st.markdown("""
    - OpenRouter AI (Llama 3 8B)
    - Sentence Transformers
    - RAG Architecture
    - NLP Avanzado
    """)

with tech_cols[2]:
    st.markdown("#### Infraestructura")
    st.markdown("""
    - Azure App Service
    - Azure Key Vault
    - Docker
    - GitHub Actions
    """)

# --- ARCHITECTURE ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-sitemap'></i>
    <span>Arquitectura del Sistema</span>
</h2>
""", unsafe_allow_html=True)

st.code("""
┌─────────────────────────────────────────────────────────────┐
│                CAPA DE PRESENTACIÓN                        │
│  • WhatsApp Business API (Webhook + Mensajería)           │
│  • FastAPI REST Endpoints (Swagger/OpenAPI)               │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                CAPA DE APLICACIÓN                          │
│  • Routers FastAPI (chat, properties, webhooks, health)    │
│  • State Manager (Gestión de conversaciones)               │
│  • Webhook Handler (Procesamiento de eventos)              │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                CAPA DE LÓGICA DE NEGOCIO                    │
│  • LLM Client (OpenRouter AI Integration)                  │
│  • RAG Retriever (Vector Search + Embeddings)              │
│  • Calendly Integration (Agendamiento)                     │
│  • Meta API Client (WhatsApp/Messenger)                    │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                CAPA DE DATOS                               │
│  • PostgreSQL + pgvector (Base de datos vectorial)         │
│  • SQLAlchemy ORM (Async)                                  │
│  • Redis Cache (Opcional)                                  │
└─────────────────────────────────────────────────────────────┘
""", language="text")

# --- KEY FEATURES ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-star'></i>
    <span>Características Principales</span>
</h2>
""", unsafe_allow_html=True)

features_cols = st.columns(2)

with features_cols[0]:
    st.markdown("#### 🤖 Chat Inteligente")
    st.markdown("""
    - Respuestas contextuales con IA generativa
    - Memoria de conversación de largo plazo
    - Soporte multilingüe
    - Personalización por cliente
    """)
    
    st.markdown("#### 🔍 Búsqueda Avanzada")
    st.markdown("""
    - Búsqueda semántica con embeddings
    - Filtros inteligentes
    - Búsqueda por ubicación
    - Filtrado por características
    """)

with features_cols[1]:
    st.markdown("#### 🔄 Integraciones")
    st.markdown("""
    - WhatsApp Business API
    - Calendly para agendamiento
    - CRM empresarial
    - Herramientas de marketing
    """)
    
    st.markdown("#### 🛡️ Seguridad")
    st.markdown("""
    - Autenticación JWT
    - Cifrado de extremo a extremo
    - Cumplimiento RGPD
    - Auditoría de accesos
    """)

# --- IMPACT ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-lightbulb'></i>
    <span>Impacto y Resultados</span>
</h2>
""", unsafe_allow_html=True)

impact_cols = st.columns(2)

with impact_cols[0]:
    st.markdown("#### Para los Agentes Inmobiliarios")
    st.markdown("""
    - Reducción del 70% en consultas repetitivas
    - Mejor gestión del tiempo
    - Lead qualification automática
    - Seguimiento de conversiones
    """)

with impact_cols[1]:
    st.markdown("#### Para los Clientes")
    st.markdown("""
    - Respuestas inmediatas 24/7
    - Información precisa y actualizada
    - Experiencia personalizada
    - Agendamiento sin fricciones
    """)

# --- GALLERY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-images'></i>
    <span>Galería</span>
</h2>
""", unsafe_allow_html=True)

gallery_cols = st.columns(2)
with gallery_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "chatinmo1.jpg"), caption="Interfaz de chat inmobiliario - WhatsApp", width='stretch')
    except:
        st.warning("chatinmo1.jpg no encontrada")

with gallery_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "chatinmo2.jpg"), caption="Dashboard y análisis de conversaciones", width='stretch')
    except:
        st.warning("chatinmo2.jpg no encontrada")

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/Real-State-IA", "🔗 Ver en GitHub")

