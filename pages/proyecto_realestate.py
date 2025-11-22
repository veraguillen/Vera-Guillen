import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Plataforma Inmobiliaria | Proyectos",
    page_icon="🏠",
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
        <i class='fas fa-home'></i> Plataforma de Análisis Inmobiliario
    </h1>
    <p class='project-subtitle'>Solución integral para análisis de inversiones inmobiliarias con datos en tiempo real</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "real_estate_platform.jpg"), width='stretch')
        st.caption("Vista general de la plataforma de análisis inmobiliario")
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: real_estate_platform.jpg")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Plataforma full-stack que consolida datos de múltiples fuentes (Zillow, OpenStreetMap, OpenWeatherMap, 
        y bases de datos públicas) para proporcionar un análisis completo de propiedades inmobiliarias. 
        La solución incluye visualización geoespacial interactiva, análisis comparativo de mercado y herramientas 
        para la evaluación de inversiones.
    </p>
</div>
""", unsafe_allow_html=True)

# --- KEY METRICS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Métricas Clave</span>
</h2>
""", unsafe_allow_html=True)

metrics = [
    {"title": "Fuentes de Datos", "value": "5+", "icon": "🔗", "progress": 100},
    {"title": "Tiempo de Respuesta", "value": "<2s", "icon": "⚡", "progress": 95},
    {"title": "Precisión", "value": "98%", "icon": "🎯", "progress": 98},
    {"title": "Disponibilidad", "value": "99.9%", "icon": "🟢", "progress": 99.9}
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

# --- CARACTERÍSTICAS PRINCIPALES ---
st.markdown("## ✨ Características Clave")

# Feature 1
with st.container():
    st.markdown("### 🌐 Integración de Datos")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔄 Fuentes Múltiples")
        st.markdown("""
        - 🌍 Datos geoespaciales (OpenStreetMap)
        - 🏘️ Listados de propiedades (Zillow API)
        - 🌤️ Clima local (OpenWeatherMap)
        - 📊 Datos demográficos (APIs públicas)
        """)
    with col2:
        st.markdown("#### 🛠️ Procesamiento")
        st.markdown("""
        - 🔄 Sincronización en tiempo real
        - 🧹 Limpieza automática de datos
        - 🔗 Normalización de formatos
        - 📈 Enriquecimiento de información
        """)

# Feature 2
with st.container():
    st.markdown("### 🗺️ Visualización Interactiva")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🎯 Mapa Interactivo")
        st.markdown("""
        - 🖱️ Navegación fluida
        - 🔍 Búsqueda por ubicación
        - 📍 Marcadores agrupados
        - 🎨 Capas personalizables
        """)
    with col2:
        st.markdown("#### 📊 Análisis")
        st.markdown("""
        - 📈 Tendencias de precios
        - 📊 Comparativas de mercado
        - 💰 Estimación de ROI
        - 📱 Diseño responsive
        """)

# --- TECNOLOGÍAS UTILIZADAS ---
st.markdown("## 🛠️ Tecnologías Utilizadas")

tech_cols = st.columns(3)

with tech_cols[0]:
    st.markdown("#### 🖥️ Frontend")
    st.markdown("""
    - React.js
    - Leaflet.js
    - Material-UI
    - Axios
    """)

with tech_cols[1]:
    st.markdown("#### 🏗️ Backend")
    st.markdown("""
    - Python 3.9+
    - Flask
    - SQLAlchemy
    - PostgreSQL
    """)

with tech_cols[2]:
    st.markdown("#### ☁️ Infraestructura")
    st.markdown("""
    - Docker
    - AWS EC2
    - Nginx
    - GitHub Actions
    """)

# --- RESULTADOS ---
st.markdown("## 📊 Resultados Alcanzados")

result_cols = st.columns(2)

with result_cols[0]:
    st.markdown("### 📈 Métricas Clave")
    st.markdown("""
    - ⏱️ **80%** reducción en tiempo de investigación
    - 💰 **65%** más eficiencia en análisis
    - 📊 **95%** precisión en valoraciones
    - 🚀 **3x** más rápido que soluciones similares
    """)

with result_cols[1]:
    st.markdown("### 🎯 Impacto")
    st.markdown("""
    - 🏆 Ganador del Hackathon Inmobiliario 2023
    - 📱 +500 usuarios activos mensuales
    - ⭐ 4.9/5 en satisfacción
    - 🔄 Actualizaciones semanales
    """)

# --- GALERÍA ---
st.markdown("## 📸 Galería")

gallery_cols = st.columns(2)

with gallery_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "real1.jpg"), caption="Mapa interactivo de propiedades", width='stretch')
    except:
        st.warning("real1.jpg no encontrada")

with gallery_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "real2.jpg"), caption="Detalles de propiedad y valoración", width='stretch')
    except:
        st.warning("real2.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "real4.png"), caption="Dashboard de métricas y estadísticas", width='stretch')
    except:
        st.warning("real4.png no encontrada")

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/Real-State-IA", "🔗 Ver en GitHub")

