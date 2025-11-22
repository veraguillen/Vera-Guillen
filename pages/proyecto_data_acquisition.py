import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Data Acquisition | Proyectos",
    page_icon="📊",
    layout="wide"
)

# --- CUSTOM CSS ---
from pages.project_styles import load_project_styles, github_button
load_project_styles()

# --- PATH SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
PROYECTOS_DIR = ASSETS_DIR / "proyectos"

# --- HEADER SECTION ---
st.markdown("""
<div class='project-header-enhanced'>
    <h1 class='project-title-enhanced'>
        <i class='fas fa-database'></i> Data Acquisition & Processing Pipeline
    </h1>
    <p class='project-subtitle'>Automatización de la recolección y procesamiento de datos para análisis avanzado</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "data_acquisition_hero.jpg"), width='stretch', caption="Arquitectura del Sistema de Adquisición de Datos")
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: data_acquisition_hero.jpg")

# --- KEY METRICS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Métricas Clave</span>
</h2>
""", unsafe_allow_html=True)

metrics = [
    {"title": "Fuentes de Datos", "value": "100+", "icon": "🔗", "progress": 100},
    {"title": "Reducción de Tiempo", "value": "80%", "icon": "⚡", "progress": 80},
    {"title": "Tasa de Éxito", "value": "95%", "icon": "🎯", "progress": 95},
    {"title": "Ahorro de Costos", "value": "60%", "icon": "💰", "progress": 60}
]

metric_cols = st.columns(4)
for idx, metric in enumerate(metrics):
    with metric_cols[idx]:
        st.markdown(f"<div class='metric-box'>"
                   f"<h3 style='margin-top: 0; font-size: 1rem; font-family: Inter, sans-serif;'>{metric['icon']} {metric['title']}</h3>"
                   f"<h2 style='color: #FF8C00; margin: 0.8rem 0; font-size: 2rem; font-family: Inter, sans-serif; font-weight: 800;'>{metric['value']}</h2>"
                   f"<div style='height: 6px; background: rgba(58, 75, 92, 0.8); border-radius: 3px; margin-top: 0.5rem;'>"
                   f"<div style='height: 100%; width: {metric['progress']}%; background: linear-gradient(90deg, #FF8C00, #FFB74D); border-radius: 3px;'></div>"
                   "</div></div>", 
                   unsafe_allow_html=True)

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Solución integral para la adquisición, limpieza y transformación de datos de múltiples fuentes.
        El sistema automatiza la recolección de datos, garantizando su calidad y disponibilidad para análisis posteriores.
    </p>
</div>
""", unsafe_allow_html=True)

# --- CARACTERÍSTICAS PRINCIPALES ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-star'></i>
    <span>Características Clave</span>
</h2>
""", unsafe_allow_html=True)

# Feature 1
with st.container():
    st.markdown("### 🌐 Extracción de Datos")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔄 Múltiples Fuentes")
        st.markdown("""
        - 🌍 Web Scraping Avanzado
        - 🔌 Integración con APIs
        - 📂 Procesamiento de Archivos
        - 🔍 Búsqueda Automatizada
        """)
    with col2:
        st.markdown("#### 🛠️ Procesamiento")
        st.markdown("""
        - 🧹 Limpieza Automática
        - 🔗 Normalización de Datos
        - 📊 Transformación
        - 📦 Almacenamiento Eficiente
        """)

# --- TECNOLOGÍAS UTILIZADAS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-tools'></i>
    <span>Tecnologías Utilizadas</span>
</h2>
""", unsafe_allow_html=True)

tech_cols = st.columns(3)

with tech_cols[0]:
    st.markdown("#### 🐍 Backend")
    st.markdown("""
    - Python 3.9+
    - BeautifulSoup
    - Requests
    - Tenacity
    """)

with tech_cols[1]:
    st.markdown("#### ☁️ Infraestructura")
    st.markdown("""
    - Azure Functions
    - Redis Cache
    - Azure Blob Storage
    - Docker
    """)

with tech_cols[2]:
    st.markdown("#### 🔍 APIs y Herramientas")
    st.markdown("""
    - Google Custom Search
    - Selenium
    - Pandas
    - NLTK
    """)

# --- ARQUITECTURA ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-sitemap'></i>
    <span>Arquitectura del Sistema</span>
</h2>
""", unsafe_allow_html=True)

st.markdown("### 🔄 Flujo de Datos")
st.markdown("""
1. **Extracción**: Obtención de datos de múltiples fuentes
2. **Procesamiento**: Limpieza y normalización
3. **Almacenamiento**: Guardado estructurado
4. **Análisis**: Procesamiento para obtener insights
""")

# --- RESULTADOS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-trophy'></i>
    <span>Resultados Alcanzados</span>
</h2>
""", unsafe_allow_html=True)

result_cols = st.columns(2)

with result_cols[0]:
    st.markdown("### 🎯 Impacto")
    st.markdown("""
    - ⏱️ **80%** reducción en tiempo de procesamiento
    - 💰 **60%** ahorro en costos de API
    - 📊 **95%** de precisión en extracción
    - 🚀 **100+** fuentes integradas
    """)

with result_cols[1]:
    st.markdown("### 🏆 Logros")
    st.markdown("""
    - 🏅 Sistema escalable y mantenible
    - 📈 Mayor calidad de datos
    - 🔄 Procesamiento en tiempo real
    - 🌐 Compatibilidad multiplataforma
    """)

# --- GALERÍA ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-images'></i>
    <span>Galería</span>
</h2>
""", unsafe_allow_html=True)

gallery_cols = st.columns(2)

with gallery_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "search1.jpg"), caption="Sistema de búsqueda y extracción de datos", width='stretch')
    except:
        st.warning("search1.jpg no encontrada")

with gallery_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "search2.jpg"), caption="Arquitectura del pipeline de adquisición", width='stretch')
    except:
        st.warning("search2.jpg no encontrada")

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/AGENTE-Busqueda-APIS", "🔗 Ver en GitHub")

