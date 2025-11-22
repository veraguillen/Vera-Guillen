import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Monitoreo IoT Farmacéutico | Proyectos",
    page_icon="💊",
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
        <i class='fas fa-pills'></i> Monitoreo IoT Farmacéutico
    </h1>
    <p class='project-subtitle'>Sistema de monitoreo en tiempo real para el control de condiciones ambientales en la industria farmacéutica</p>
</div>
""", unsafe_allow_html=True)

# --- HERO IMAGE ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
        st.image(str(ASSETS_DIR / "pharmawatch_hero.jpg"), width='stretch')
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning("Imagen no encontrada: pharmawatch_hero.jpg")

# --- PROJECT OVERVIEW ---
st.markdown("""
<div class='content-card'>
    <h2 class='section-title-enhanced'>
        <i class='fas fa-info-circle'></i>
        <span>Descripción del Proyecto</span>
    </h2>
    <p style='font-family: Inter, sans-serif; color: #8B949E; font-size: 1.1rem; line-height: 1.8;'>
        Solución integral de monitoreo en tiempo real para la industria farmacéutica que garantiza el cumplimiento 
        de normativas de almacenamiento mediante el análisis predictivo y la detección temprana de anomalías 
        en las condiciones ambientales de almacenes de medicamentos.
    </p>
</div>
""", unsafe_allow_html=True)

# --- KEY FINDINGS ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-line'></i>
    <span>Hallazgos Clave</span>
</h2>
""", unsafe_allow_html=True)

findings_cols = st.columns(2)

with findings_cols[0]:
    st.markdown("""
    <div class='metric-card-enhanced'>
        <div class='metric-value'>99.2%</div>
        <div class='metric-label'>Precisión en detección de anomalías</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-star' style='color: #FF8C00;'></i> Características Principales
        </h4>
        <ul style='color: #8B949E; font-family: Inter, sans-serif; line-height: 2;'>
            <li>Monitoreo en tiempo real 24/7</li>
            <li>Alertas tempranas</li>
            <li>Análisis predictivo</li>
            <li>Reportes automatizados</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with findings_cols[1]:
    st.markdown("""
    <div class='metric-card-enhanced'>
        <div class='metric-value'>45%</div>
        <div class='metric-label'>Reducción en pérdidas</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-trophy' style='color: #FF8C00;'></i> Beneficios Clave
        </h4>
        <ul style='color: #8B949E; font-family: Inter, sans-serif; line-height: 2;'>
            <li>Cumplimiento normativo</li>
            <li>Reducción de mermas</li>
            <li>Optimización de recursos</li>
            <li>Toma de decisiones basada en datos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- METHODOLOGY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-cogs'></i>
    <span>Metodología</span>
</h2>
""", unsafe_allow_html=True)

method_tabs = st.tabs(["1. Recolección", "2. Procesamiento", "3. Análisis", "4. Visualización"])

with method_tabs[0]:
    st.markdown("""
    <div class='content-card'>
        <ul style='color: #C8D1E0; font-family: Inter, sans-serif; line-height: 2; font-size: 1.1rem;'>
            <li>Sensores IoT en tiempo real</li>
            <li>API para integración con sistemas existentes</li>
            <li>Almacenamiento seguro de datos</li>
            <li>Validación de calidad de datos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with method_tabs[1]:
    st.markdown("""
    <div class='content-card'>
        <ul style='color: #C8D1E0; font-family: Inter, sans-serif; line-height: 2; font-size: 1.1rem;'>
            <li>Limpieza y normalización</li>
            <li>Agregación de datos</li>
            <li>Cálculo de métricas</li>
            <li>Almacenamiento en base de datos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with method_tabs[2]:
    st.markdown("""
    <div class='content-card'>
        <ul style='color: #C8D1E0; font-family: Inter, sans-serif; line-height: 2; font-size: 1.1rem;'>
            <li>Modelo Isolation Forest</li>
            <li>Detección de patrones</li>
            <li>Predicción de tendencias</li>
            <li>Generación de alertas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with method_tabs[3]:
    st.markdown("""
    <div class='content-card'>
        <ul style='color: #C8D1E0; font-family: Inter, sans-serif; line-height: 2; font-size: 1.1rem;'>
            <li>Dashboard interactivo</li>
            <li>Gráficos en tiempo real</li>
            <li>Reportes personalizables</li>
            <li>Alertas visuales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- TECHNICAL STACK ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-tools'></i>
    <span>Stack Tecnológico</span>
</h2>
""", unsafe_allow_html=True)

tech_cols = st.columns(3)

with tech_cols[0]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fab fa-react' style='color: #FF8C00;'></i> Frontend
        </h4>
        <div>
            <span class='tech-badge'>React 19</span>
            <span class='tech-badge'>TypeScript</span>
            <span class='tech-badge'>Redux Toolkit</span>
            <span class='tech-badge'>Material-UI</span>
            <span class='tech-badge'>Leaflet</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tech_cols[1]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-server' style='color: #FF8C00;'></i> Backend
        </h4>
        <div>
            <span class='tech-badge'>Python 3.10+</span>
            <span class='tech-badge'>FastAPI</span>
            <span class='tech-badge'>PostgreSQL</span>
            <span class='tech-badge'>Redis</span>
            <span class='tech-badge'>Celery</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tech_cols[2]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-brain' style='color: #FF8C00;'></i> Machine Learning
        </h4>
        <div>
            <span class='tech-badge'>Scikit-learn</span>
            <span class='tech-badge'>Pandas</span>
            <span class='tech-badge'>NumPy</span>
            <span class='tech-badge'>MLflow</span>
            <span class='tech-badge'>Prometeo/Grafana</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- GALLERY ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-images'></i>
    <span>Visualizaciones</span>
</h2>
""", unsafe_allow_html=True)

viz_cols = st.columns(2)
with viz_cols[0]:
    try:
        st.image(str(PROYECTOS_DIR / "farma1.png"), caption="Dashboard principal - Monitoreo en tiempo real", width='stretch')
    except:
        st.warning("farma1.png no encontrada")
    try:
        st.image(str(PROYECTOS_DIR / "farma3.jpg"), caption="Análisis de tendencias y métricas", width='stretch')
    except:
        st.warning("farma3.jpg no encontrada")

with viz_cols[1]:
    try:
        st.image(str(PROYECTOS_DIR / "farma2.jpg"), caption="Mapa de sensores IoT y ubicaciones", width='stretch')
    except:
        st.warning("farma2.jpg no encontrada")

# --- IMPACT ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-lightbulb'></i>
    <span>Impacto y Resultados</span>
</h2>
""", unsafe_allow_html=True)

impact_cols = st.columns(3)

with impact_cols[0]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-building' style='color: #FF8C00;'></i> Para la Empresa
        </h4>
        <ul style='color: #8B949E; font-family: Inter, sans-serif; line-height: 2;'>
            <li>Cumplimiento regulatorio</li>
            <li>Reducción de pérdidas</li>
            <li>Optimización de recursos</li>
            <li>Ventaja competitiva</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with impact_cols[1]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-users' style='color: #FF8C00;'></i> Para los Clientes
        </h4>
        <ul style='color: #8B949E; font-family: Inter, sans-serif; line-height: 2;'>
            <li>Mayor confiabilidad</li>
            <li>Calidad garantizada</li>
            <li>Transparencia</li>
            <li>Servicio continuo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with impact_cols[2]:
    st.markdown("""
    <div class='content-card'>
        <h4 style='color: #E6EDF3; font-family: Inter, sans-serif; margin-bottom: 1rem;'>
            <i class='fas fa-user-tie' style='color: #FF8C00;'></i> Para el Equipo
        </h4>
        <ul style='color: #8B949E; font-family: Inter, sans-serif; line-height: 2;'>
            <li>Alertas tempranas</li>
            <li>Menor estrés</li>
            <li>Mejor organización</li>
            <li>Datos accionables</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- RESULTS AND IMPACT ---
st.markdown("""
<h2 class='section-title-enhanced'>
    <i class='fas fa-chart-bar'></i>
    <span>Resultados e Impacto</span>
</h2>
""", unsafe_allow_html=True)

results = {
    "Disponibilidad y Escala": "Sistema en producción con 99.2% de uptime, monitoreando 150+ sensores y procesando 6,000+ lecturas diarias.",
    "Precisión del Modelo": "El modelo de Machine Learning alcanzó una precisión del 92% en la detección de anomalías.",
    "Reducción de Falsos Positivos": "40% en comparación con el sistema de alertas basado en umbrales anterior.",
    "Optimización de Rendimiento": "80% en llamadas a APIs externas gracias a una capa de caché estratégica."
}

for key, value in results.items():
    st.markdown(f"""
    <div class='content-card'>
        <h4 style='color: #FF6A00; font-family: Inter, sans-serif; margin-bottom: 0.5rem;'>
            <i class='fas fa-check-circle' style='margin-right: 0.5rem;'></i>{key}
        </h4>
        <p style='color: #8B949E; font-family: Inter, sans-serif; line-height: 1.8; margin: 0;'>{value}</p>
    </div>
    """, unsafe_allow_html=True)

# --- GITHUB BUTTON ---
github_button("https://github.com/veraguillen/Monitoreo-IoT", "🔗 Ver en GitHub")
