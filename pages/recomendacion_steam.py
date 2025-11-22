import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sistema de Recomendación | Proyectos",
    page_icon="🎮",
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
        <i class='fas fa-gamepad'></i> Sistema de Recomendación para Steam
    </h1>
    <p class='project-subtitle'>Motor de recomendación de videojuegos utilizando NLP y técnicas de aprendizaje automático</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "steam_recommendation.jpg"), width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: steam_recommendation.jpg")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Este proyecto implementa un sistema de recomendación de videojuegos utilizando técnicas avanzadas de Procesamiento de Lenguaje Natural (NLP) y 
        similitud de coseno. El sistema analiza las características de los juegos y las preferencias de los usuarios para ofrecer recomendaciones 
        personalizadas.
    </p>
</div>
""", unsafe_allow_html=True)

# --- FEATURES ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-star'></i>
    <span>Características Principales</span>
</h2>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔍 Búsqueda por Contenido")
    st.markdown("""
    - Análisis de texto con NLP para extraer características
    - Vectorización TF-IDF para representación numérica
    - Cálculo de similitud de coseno entre juegos
    """)

with col2:
    st.markdown("### 🎯 Recomendaciones Personalizadas")
    st.markdown("""
    - Filtrado colaborativo basado en usuarios similares
    - Sistema híbrido que combina múltiples técnicas
    - Personalización según historial de juegos
    """)

# --- TECHNICAL DETAILS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-tools'></i>
    <span>Detalles Técnicos</span>
</h2>
""", unsafe_allow_html=True)
st.markdown("### Stack Tecnológico")

tech_cols = st.columns(4)
with tech_cols[0]:
    st.markdown("#### Backend")
    st.markdown("- Python 3.10\n- FastAPI\n- Scikit-learn\n- NLTK")

with tech_cols[1]:
    st.markdown("#### Procesamiento")
    st.markdown("- Pandas\n- NumPy\n- Scipy\n- Gensim")

with tech_cols[2]:
    st.markdown("#### Visualización")
    st.markdown("- Matplotlib\n- Seaborn\n- Plotly")

with tech_cols[3]:
    st.markdown("#### Despliegue")
    st.markdown("- Docker\n- AWS EC2\n- Nginx")

# --- METHODOLOGY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-brain'></i>
    <span>Metodología</span>
</h2>
""", unsafe_allow_html=True)

with st.expander("1. Recolección y Procesamiento de Datos", expanded=True):
    st.markdown("""
    - Extracción de datos de la API de Steam y fuentes abiertas
    - Limpieza y normalización de texto
    - Procesamiento de características (features) relevantes
    - Ingeniería de características para el modelo
    """)

with st.expander("2. Modelado y Entrenamiento", expanded=False):
    st.markdown("""
    - Implementación de algoritmos de recomendación
    - Entrenamiento con datos históricos
    - Validación cruzada y ajuste de hiperparámetros
    - Evaluación de métricas de rendimiento
    """)

# --- RESULTS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Resultados</span>
</h2>
""", unsafe_allow_html=True)

results = {
    "Precisión del Modelo": "87% en conjunto de prueba",
    "Tiempo de Respuesta": "< 500ms por recomendación",
    "Escalabilidad": "Hasta 1,000 solicitudes por minuto",
    "Satisfacción de Usuarios": "4.8/5 en pruebas de usuario"
}

for metric, value in results.items():
    st.markdown(f"- **{metric}:** {value}")

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
        st.image(str(PROYECTOS_DIR / "videojuegos1.jpg"), caption="Sistema de recomendación - Interfaz principal", width='stretch')
    except:
        st.warning("videojuegos1.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "videojuegos3.jpg"), caption="Análisis de similitud y clustering", width='stretch')
    except:
        st.warning("videojuegos3.jpg no encontrada")

with gallery_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "videojuegos2.jpg"), caption="Dashboard de métricas y recomendaciones", width='stretch')
    except:
        st.warning("videojuegos2.jpg no encontrada")
    try:
        st.image(str(BASE_DIR / "videojuegos4.jpg"), caption="Visualización de datos y resultados", width='stretch')
    except:
        try:
            st.image(str(PROYECTOS_DIR / "videojuegos4.jpg"), caption="Visualización de datos y resultados", width='stretch')
        except:
            st.warning("videojuegos4.jpg no encontrada")

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/MachineLearning-STEAM", "🔗 Ver en GitHub")
