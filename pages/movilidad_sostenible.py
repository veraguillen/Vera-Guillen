import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Modelado de Movilidad Sostenible | Proyectos",
    page_icon="🌱",
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
        <i class='fas fa-leaf'></i> Modelado de Movilidad Sostenible
    </h1>
    <p class='project-subtitle'>Análisis de viabilidad para la transición a flotas de vehículos ecológicos en Nueva York</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image("assets/proyectos/movilidad_sostenible.jpg", width='stretch', caption="Análisis de movilidad sostenible para flotas urbanas")
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        try:
            st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
            st.image(str(ASSETS_DIR / "movilidad_hero.jpg"), width='stretch')
            st.markdown('</div>', unsafe_allow_html=True)
        except:
            st.warning("Imagen no encontrada")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Visión General</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Este proyecto evalúa la viabilidad de reemplazar la flota de taxis tradicionales de la ciudad de Nueva York 
        por vehículos eléctricos e híbridos, analizando el impacto económico, ambiental y operativo de esta transición.
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

metric_cols = st.columns(4)

with metric_cols[0]:
    st.metric("Reducción de Emisiones", "45%", "anual")
    
with metric_cols[1]:
    st.metric("Ahorro en Combustible", "$3.2M", "por año")
    
with metric_cols[2]:
    st.metric("Vehículos Analizados", "13,500+", "taxis")
    
with metric_cols[3]:
    st.metric("Período de Retorno", "3.5 años", "de inversión")

# --- METHODOLOGY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-brain'></i>
    <span>Metodología</span>
</h2>
""", unsafe_allow_html=True)

method_tabs = st.tabs(["1. Recopilación de Datos", "2. Modelado", "3. Simulación", "4. Análisis"])

with method_tabs[0]:
    st.markdown("""
    - Datos de viajes de taxis de NYC (NYC TLC)
    - Especificaciones técnicas de vehículos
    - Costos de energía y mantenimiento
    - Infraestructura de carga disponible
    """)

with method_tabs[1]:
    st.markdown("""
    - Modelo de consumo energético
    - Proyección de costos a 10 años
    - Huella de carbono por vehículo
    - Análisis de rutas y rangos
    """)

with method_tabs[2]:
    st.markdown("""
    - Simulación de patrones de uso
    - Estrategias de carga óptimas
    - Escenarios de adopción gradual
    - Análisis de sensibilidad
    """)

with method_tabs[3]:
    st.markdown("""
    - Retorno de inversión (ROI)
    - Impacto ambiental
    - Viabilidad operativa
    - Recomendaciones estratégicas
    """)

# --- FINDINGS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-search'></i>
    <span>Hallazgos Principales</span>
</h2>
""", unsafe_allow_html=True)

findings_cols = st.columns(2)

with findings_cols[0]:
    st.markdown("### Beneficios Ambientales")
    st.markdown("""
    - Reducción de 78,000 toneladas de CO₂ anuales
    - Disminución del 92% en emisiones de NOx
    - Menor contaminación acústica
    - Contribución a objetivos de sostenibilidad
    """)

with findings_cols[1]:
    st.markdown("### Beneficios Económicos")
    st.markdown("""
    - Ahorro de $8,500 por vehículo/año
    - Incentivos fiscales disponibles
    - Menor costo de mantenimiento
    - Mayor vida útil de los vehículos
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
    - GeoPandas
    - Scikit-learn
    - Jupyter Notebooks
    """)

with tech_cols[1]:
    st.markdown("#### Visualización")
    st.markdown("""
    - Matplotlib/Seaborn
    - Plotly
    - Folium
    - Power BI
    """)

with tech_cols[2]:
    st.markdown("#### Modelado")
    st.markdown("""
    - SimPy para simulaciones
    - Optimización con PuLP
    - Análisis de series temporales
    - Modelos predictivos
    """)

# --- VISUALIZATIONS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-line'></i>
    <span>Visualizaciones</span>
</h2>
""", unsafe_allow_html=True)

viz_cols = st.columns(2)
with viz_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "taxi1.jpg"), caption="Análisis de flota de taxis en NYC", width='stretch')
    except:
        st.warning("taxi1.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "taxi3.jpg"), caption="Comparación de costos y emisiones", width='stretch')
    except:
        st.warning("taxi3.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "taxi5.jpg"), caption="Mapa de estaciones de carga y rutas", width='stretch')
    except:
        st.warning("taxi5.jpg no encontrada")

with viz_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "taxi2.jpg"), caption="Proyección de reducción de emisiones", width='stretch')
    except:
        st.warning("taxi2.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "taxi4.jpg"), caption="Análisis de viabilidad económica", width='stretch')
    except:
        st.warning("taxi4.jpg no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "taxi6.jpg"), caption="Dashboard de métricas y KPIs", width='stretch')
    except:
        st.warning("taxi6.jpg no encontrada")

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/New_York_Taxis_IA", "🔗 Ver en GitHub")

# --- RECOMMENDATIONS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-lightbulb'></i>
    <span>Recomendaciones Estratégicas</span>
</h2>
""", unsafe_allow_html=True)

recom_cols = st.columns(2)

with recom_cols[0]:
    st.markdown("### Corto Plazo (1-2 años)")
    st.markdown("""
    - Implementar programa piloto con 500 vehículos
    - Instalar estaciones de carga estratégicas
    - Capacitar a conductores y mecánicos
    - Monitorear desempeño y ajustar modelo
    """)

with recom_cols[1]:
    st.markdown("### Largo Plazo (3-5 años)")
    st.markdown("""
    - Transición completa al 100% de vehículos limpios
    - Integrar con energías renovables
    - Sistema de gestión de flota inteligente
    - Expansión a otras ciudades
    """)
