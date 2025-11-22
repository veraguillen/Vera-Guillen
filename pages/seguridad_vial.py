import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Análisis de Seguridad Vial | Proyectos",
    page_icon="🚗",
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
        <i class='fas fa-car'></i> Análisis de Seguridad Vial en Buenos Aires
    </h1>
    <p class='project-subtitle'>Estudio integral de accidentes viales utilizando técnicas de análisis de datos y visualización</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "seguridad_vial_hero.jpg"), width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: seguridad_vial_hero.jpg")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Este proyecto analiza datos de accidentes de tránsito en la Ciudad de Buenos Aires para identificar patrones, 
        factores de riesgo y proponer medidas preventivas. El análisis incluye visualizaciones interactivas 
        y un dashboard completo en Power BI para la toma de decisiones.
    </p>
</div>
""", unsafe_allow_html=True)

# --- KEY FINDINGS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-search'></i>
    <span>Hallazgos Clave</span>
</h2>
""", unsafe_allow_html=True)

findings_cols = st.columns(2)

with findings_cols[0]:
    st.metric("Reducción de Fatalidades", "10%", "Objetivo alcanzable")
    st.markdown("#### Zonas Críticas")
    st.markdown("""
    - Intersecciones con mayor índice de siniestros
    - Horarios de mayor riesgo (noche/madrugada)
    - Tipos de vehículos más involucrados
    """)

with findings_cols[1]:
    st.metric("Datos Analizados", "50,000+", "Registros históricos")
    st.markdown("#### Factores de Riesgo")
    st.markdown("""
    - Condiciones climáticas adversas
    - Estado de la vía
    - Comportamiento del conductor
    """)

# --- METHODOLOGY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-brain'></i>
    <span>Metodología</span>
</h2>
""", unsafe_allow_html=True)

method_tabs = st.tabs(["1. Recolección de Datos", "2. Procesamiento", "3. Análisis", "4. Visualización"])

with method_tabs[0]:
    st.markdown("""
    - Fuentes de datos oficiales (Gobierno de la Ciudad)
    - API de datos abiertos
    - Web scraping de reportes públicos
    - Datos meteorológicos históricos
    """)

with method_tabs[1]:
    st.markdown("""
    - Limpieza y estandarización de datos
    - Geocodificación de direcciones
    - Clasificación de tipos de accidentes
    - Creación de variables derivadas
    """)

with method_tabs[2]:
    st.markdown("""
    - Análisis exploratorio (EDA)
    - Identificación de patrones temporales
    - Análisis espacial (hotspots)
    - Modelado predictivo de riesgo
    """)

with method_tabs[3]:
    st.markdown("""
    - Mapas de calor interactivos
    - Series temporales
    - Gráficos de correlación
    - Dashboard en Power BI
    """)

# --- TECHNICAL STACK ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-tools'></i>
    <span>Stack Tecnológico</span>
</h2>
""", unsafe_allow_html=True)

tech_cols = st.columns(3)

with tech_cols[0]:
    st.markdown("#### Análisis de Datos")
    st.markdown("""
    - Python (Pandas, NumPy)
    - Jupyter Notebooks
    - SQL para consultas
    - GeoPandas
    """)

with tech_cols[1]:
    st.markdown("#### Visualización")
    st.markdown("""
    - Power BI
    - Matplotlib/Seaborn
    - Folium (mapas)
    - Plotly
    """)

with tech_cols[2]:
    st.markdown("#### Despliegue")
    st.markdown("""
    - Streamlit
    - Docker
    - Azure Cloud
    - GitHub Actions
    """)

# --- GALLERY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Visualizaciones</span>
</h2>
""", unsafe_allow_html=True)

viz_cols = st.columns(2)
with viz_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "accidentes1.png"), caption="Análisis de siniestros viales", width='stretch')
    except:
        st.warning("accidentes1.png no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "accidentes3.jpg"), caption="Dashboard interactivo - Power BI", width='stretch')
    except:
        st.warning("accidentes3.jpg no encontrada")

with viz_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "accidentes2.jpg"), caption="Mapa de calor y análisis espacial", width='stretch')
    except:
        st.warning("accidentes2.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "accidentes4.jpg"), caption="Análisis de factores de riesgo y tendencias", width='stretch')
    except:
        st.warning("accidentes4.jpg no encontrada")

# --- IMPACT ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-lightbulb'></i>
    <span>Impacto y Resultados</span>
</h2>
""", unsafe_allow_html=True)

impact_cols = st.columns(3)

with impact_cols[0]:
    st.markdown("#### Para la Comunidad")
    st.markdown("""
    - Reducción de accidentes
    - Mayor conciencia vial
    - Datos para políticas públicas
    """)

with impact_cols[1]:
    st.markdown("#### Para las Autoridades")
    st.markdown("""
    - Herramienta de decisión
    - Optimización de recursos
    - Monitoreo en tiempo real
    """)

with impact_cols[2]:
    st.markdown("#### Para los Ciudadanos")
    st.markdown("""
    - Información accesible
    - Rutas más seguras
    - Conciencia preventiva
    """)

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/Siniestros-Viales-CABA", "🔗 Ver en GitHub")
