import streamlit as st
from pathlib import Path
from pages.project_styles import load_project_styles, github_button

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Proyectos | Vera Guillen", layout="wide")

# Load project styles
load_project_styles()

# --- STYLES ---
st.markdown("""
<style>
.project-card {
    background: #161B22;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 106, 0, 0.2);
}
.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                0 10px 30px rgba(0, 0, 0, 0.4);
    border-color: #FF6A00;
}
.tech-tag {
    display: inline-block;
    background: rgba(255, 106, 0, 0.1);
    color: #FF6A00;
    padding: 0.3rem 0.8rem;
    border-radius: 8px;
    font-size: 0.8rem;
    margin: 0.2rem;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid rgba(255, 106, 0, 0.3);
    transition: all 0.3s ease;
}
.tech-tag:hover {
    background: rgba(255, 106, 0, 0.2);
    border-color: #FF6A00;
    box-shadow: 0 0 15px rgba(255, 106, 0, 0.3);
}
.project-title {
    color: #FF8C2B;
    margin-bottom: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    text-shadow: 0 0 20px rgba(255, 140, 43, 0.5);
}
.project-subtitle {
    color: #8B949E;
    margin-bottom: 1rem;
}
.section-title {
    color: #FF8C2B;
    margin: 2rem 0 1rem 0;
    font-family: 'JetBrains Mono', monospace;
    text-shadow: 0 0 20px rgba(255, 140, 43, 0.5);
}
</style>
""", unsafe_allow_html=True)

# --- PROJECTS DATA ---
PROJECTS = [
    {
        "title": "Modelado de Movilidad Sostenible",
        "subtitle": "Análisis de viabilidad para la transición a flotas de vehículos ecológicos",
        "description": "Estudio integral que evalúa la viabilidad de transición a vehículos ecológicos en flotas urbanas, incluyendo análisis de costos, infraestructura necesaria y beneficios ambientales.",
        "technologies": ["Python", "Pandas", "Matplotlib", "Scikit-learn", "Streamlit"],
        "page": "movilidad_sostenible.py",
        "image": "assets/proyectos/movilidad_sostenible.jpg",
        "github_url": "https://github.com/veraguillen/New_York_Taxis_IA"
    },
    {
        "title": "Chatbot RAG Multimarca",
        "subtitle": "Sistema de IA conversacional para atención al cliente multicanal",
        "description": "Desarrollo de un chatbot avanzado con arquitectura RAG (Retrieval-Augmented Generation) que permite a las empresas ofrecer soporte multicanal (WhatsApp, web, aplicaciones móviles) con respuestas precisas basadas en su base de conocimiento.",
        "technologies": ["Python", "FastAPI", "Llama 3", "RAG", "pgvector", "Docker", "Kubernetes"],
        "page": "proyecto_chatbot_legacy.py",
        "image": "assets/proyectos/chatbot_rag.jpg",
        "github_url": "https://github.com/veraguillen/Bot-Multimarcas-RAG"
    },
    {
        "title": "Plataforma Inmobiliaria Inteligente",
        "subtitle": "Solución integral de gestión y búsqueda de propiedades con IA",
        "description": "Plataforma que utiliza procesamiento de lenguaje natural y visión por computadora para analizar y categorizar propiedades, ofreciendo búsquedas semánticas y recomendaciones personalizadas.",
        "technologies": ["React", "Python", "FastAPI", "PostgreSQL", "OpenCV", "Docker"],
        "page": "proyecto_realestate.py",
        "image": "assets/proyectos/plataforma_inmobiliaria.jpg",
        "github_url": "https://github.com/veraguillen/Real-State-IA"
    },
    {
        "title": "Monitoreo farmacéutico IoT",
        "subtitle": "Sistema de monitoreo en tiempo real",
        "description": "Sistema de monitoreo en tiempo real para el control de condiciones ambientales en la industria farmacéutica, con alertas y análisis predictivo para garantizar la cadena de frío de medicamentos sensibles.",
        "technologies": ["Python", "MQTT", "InfluxDB", "Grafana", "Raspberry Pi", "Docker"],
        "page": "proyecto_pharmawatch.py",
        "image": "assets/proyectos/pharmawatch_iot.jpg",
        "github_url": "https://github.com/tu-usuario/pharmawatch"
    },
    {
        "title": "Data Acquisition Platform",
        "subtitle": "Plataforma de adquisición y procesamiento de datos",
        "description": "Sistema de adquisición de datos de múltiples fuentes con capacidades de procesamiento y análisis en tiempo real, diseñado para manejar grandes volúmenes de información con alta disponibilidad.",
        "technologies": ["Python", "Airflow", "Kafka", "Elasticsearch", "Docker"],
        "page": "proyecto_data_acquisition.py",
        "image": "assets/proyectos/data_acquisition.jpg",
        "github_url": "https://github.com/veraguillen/AGENTE-Busqueda-APIS"
    }
]

# --- PAGE CONTENT ---
st.markdown("# Mis Proyectos")
st.markdown("#### Una selección de mis trabajos más recientes y relevantes")
st.markdown("---")

# Display all projects
for project in PROJECTS:
    with st.container():
        col1, col2 = st.columns([0.7, 0.3])
        
        with col1:
            st.markdown(f"### {project['title']}")
            st.markdown(f"#### {project['subtitle']}")
            st.markdown(project['description'])
            
            # Display technologies
            st.markdown("**Tecnologías:**")
            tech_html = "".join([f"<span class='tech-tag'>{tech}</span>" for tech in project['technologies']])
            st.markdown(tech_html, unsafe_allow_html=True)
            
            # Add GitHub button
            github_button(project['github_url'], "🔗 Ver en GitHub")
            
        with col2:
            # Display project image
            try:
                st.image(project['image'], width='stretch')
            except:
                st.warning("Imagen no encontrada")
                
            # View details button
            if st.button(f"Ver detalles de {project['title']}", key=f"btn_{project['page']}"):
                st.switch_page(f"pages/{project['page']}")
        
        st.markdown("---")

# --- RESULTS AND IMPACT ---
st.markdown("### Resultados e Impacto")
results = {
    "Automatización de Consultas": "70-80%",
    "Reducción Tiempo de Respuesta": "De horas a < 5 segundos",
    "Manejo de Concurrencia": "100+ solicitudes concurrentes (latencia p95 < 500ms)",
    "Disponibilidad": "99%+ en Azure, monitoreada con Application Insights"
}

for key, value in results.items():
    st.markdown(f"- **{key}:** {value}")

st.page_link("pages/proyecto_inmobiliario.py", label=":bar_chart: Ver Análisis Técnico Detallado", icon="📊")

# --- STRUCTURE FOR NEXT PROJECTS ---
# This section is ready for the next case study.
st.markdown("---")
# st.markdown("## Case Study 2: ...")