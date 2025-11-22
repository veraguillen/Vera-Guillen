import streamlit as st
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Habilidades Técnicas | Portafolio Data Science", 
    layout="wide",
    page_icon="🛠️"
)

# Add Font Awesome for icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
    unsafe_allow_html=True
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Cyberpunk Color Variables */
    :root {
        --bg-main: #0D1117;
        --bg-card: #161B22;
        --text-primary: #E6EDF3;
        --text-secondary: #8B949E;
        --accent-orange: #FF6A00;
        --accent-orange-glow: #FF8C2B;
        --matrix-green: #00FF9F;
        --cyan-detail: #00D4FF;
    }
    
    /* Force dark background */
    body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-main) !important;
        color: var(--text-primary) !important;
    }
    
    .stApp > header {
        background-color: var(--bg-card) !important;
    }
    
    .main .block-container {
        background-color: transparent !important;
        padding-top: 2rem;
    }
    
    .skills-header-enhanced {
        text-align: center;
        margin: 0 auto 4rem;
        max-width: 1000px;
        padding: 0 1.5rem;
    }
    
    .skills-title-enhanced {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-orange) 50%, var(--text-primary) 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 3s ease infinite;
        margin-bottom: 1.5rem;
        line-height: 1.2;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
    }
    
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .skills-title-enhanced i {
        background: linear-gradient(135deg, var(--accent-orange), var(--accent-orange-glow));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 20px rgba(255, 106, 0, 0.5));
        font-size: 3rem;
        animation: icon-pulse 2s ease-in-out infinite;
    }
    
    @keyframes icon-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .skills-subtitle {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        margin: 0 auto;
        line-height: 1.8;
        font-size: 1.2rem;
        max-width: 800px;
    }
    
    .skills-container-enhanced {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 0 auto 4rem;
        max-width: 1400px;
        padding: 0 1.5rem;
    }
    
    .skill-category-enhanced {
        background: var(--bg-card);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 106, 0, 0.2);
        height: 100%;
        box-sizing: border-box;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .skill-category-enhanced::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--accent-orange), var(--accent-orange-glow), var(--accent-orange));
        background-size: 200% 100%;
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s ease;
    }
    
    .skill-category-enhanced:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 50px rgba(255, 106, 0, 0.3), 0 0 40px rgba(255, 106, 0, 0.1), 0 0 30px rgba(255, 106, 0, 0.4);
        border-color: rgba(255, 106, 0, 0.5);
        background: var(--bg-card);
    }
    
    .skill-category-enhanced:hover::before {
        transform: scaleX(1);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .skill-category-enhanced h3 {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
        margin: 0 0 1.5rem 0;
        display: flex;
        align-items: center;
        font-size: 1.5rem;
        font-weight: 700;
        padding-bottom: 1rem;
        border-bottom: 2px solid rgba(255, 106, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .skill-category-enhanced:hover h3 {
        color: var(--text-primary);
        border-bottom-color: rgba(255, 106, 0, 0.4);
        text-shadow: 0 0 20px var(--accent-orange);
    }
    
    .skill-category-enhanced h3 i {
        margin-right: 12px;
        color: var(--accent-orange);
        font-size: 1.8rem;
        transition: all 0.3s ease;
    }
    
    .skill-category-enhanced:hover h3 i {
        color: var(--accent-orange-glow);
        transform: scale(1.2) rotate(5deg);
        filter: drop-shadow(0 0 10px rgba(255, 106, 0, 0.6));
    }
    
    .skill-items-enhanced {
        display: flex;
        flex-wrap: wrap;
        gap: 0.9rem;
    }
    
    .skill-item-enhanced {
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.15), rgba(255, 140, 43, 0.15));
        color: var(--accent-orange-glow);
        padding: 0.7rem 1.2rem;
        border-radius: 20px;
        font-size: 0.95rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        display: inline-flex;
        align-items: center;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 106, 0, 0.3);
        margin-bottom: 0.6rem;
        position: relative;
        overflow: hidden;
    }
    
    .skill-item-enhanced::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .skill-item-enhanced:hover::before {
        left: 100%;
    }
    
    .skill-item-enhanced i {
        margin-right: 8px;
        font-size: 1.1rem;
        transition: transform 0.3s ease;
    }
    
    .skill-item-enhanced:hover {
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.25), rgba(255, 140, 43, 0.25));
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 20px rgba(255, 106, 0, 0.3), 0 0 30px rgba(255, 106, 0, 0.4);
        border-color: rgba(255, 106, 0, 0.5);
        color: var(--accent-orange);
        text-shadow: 0 0 20px var(--accent-orange);
    }
    
    .skill-item-enhanced:hover i {
        transform: scale(1.2) rotate(10deg);
    }
    
    .soft-skills-section {
        margin-top: 4rem;
        padding: 3rem 0;
        background: var(--bg-card);
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 106, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .soft-skills-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 106, 0, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        animation: float-glow 6s ease-in-out infinite;
    }
    
    @keyframes float-glow {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
        50% { transform: translate(20px, -20px) scale(1.1); opacity: 0.8; }
    }
    
    .soft-skills-header-enhanced {
        text-align: center !important;
        margin-bottom: 3rem;
        position: relative;
        z-index: 1;
    }
    
    .soft-skills-header-enhanced * {
        text-align: center !important;
    }
    
    .soft-skills-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--text-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 1rem;
        text-align: center !important;
    }
    
    .soft-skills-title i {
        color: var(--accent-orange);
        font-size: 2.5rem;
        background: linear-gradient(135deg, var(--accent-orange), var(--accent-orange-glow));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 20px rgba(255, 106, 0, 0.5));
    }
    
    .soft-skills-description {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        max-width: 800px;
        margin: 0 auto !important;
        line-height: 1.8;
        font-size: 1.1rem;
        padding: 0 1.5rem;
        text-align: center !important;
        display: block !important;
        width: 100%;
        box-sizing: border-box;
    }
    
    .soft-skills-header-enhanced p {
        text-align: center !important;
        margin: 0 auto !important;
    }
    
    .soft-skills-container-enhanced {
        max-width: 1000px;
        margin: 0 auto;
        padding: 0 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .soft-skill-card-enhanced {
        background: var(--bg-card);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 106, 0, 0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .soft-skill-card-enhanced::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(to bottom, var(--accent-orange), var(--accent-orange-glow));
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .soft-skill-card-enhanced:hover {
        transform: translateX(10px) translateY(-5px);
        box-shadow: 0 20px 50px rgba(255, 106, 0, 0.3), 0 0 30px rgba(255, 106, 0, 0.4);
        border-color: rgba(255, 106, 0, 0.5);
        background: var(--bg-card);
    }
    
    .soft-skill-card-enhanced:hover::before {
        opacity: 1;
    }
    
    .soft-skill-header-enhanced {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .soft-skill-icon-wrapper {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.2), rgba(255, 140, 43, 0.2));
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid rgba(255, 106, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .soft-skill-card-enhanced:hover .soft-skill-icon-wrapper {
        transform: rotate(-5deg) scale(1.1);
        background: linear-gradient(135deg, rgba(255, 106, 0, 0.4), rgba(255, 140, 43, 0.4));
        border-color: rgba(255, 106, 0, 0.6);
        box-shadow: 0 0 20px rgba(255, 106, 0, 0.4);
    }
    
    .soft-skill-header-enhanced i {
        color: var(--accent-orange);
        font-size: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .soft-skill-card-enhanced:hover .soft-skill-header-enhanced i {
        color: var(--accent-orange-glow);
        transform: scale(1.2);
    }
    
    .soft-skill-card-enhanced h3 {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0;
        transition: color 0.3s ease;
    }
    
    .soft-skill-card-enhanced:hover h3 {
        color: var(--text-primary);
        text-shadow: 0 0 20px var(--accent-orange);
    }
    
    .soft-skill-card-enhanced p {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        line-height: 1.8;
        font-size: 1.05rem;
        margin: 0;
        transition: color 0.3s ease;
    }
    
    .soft-skill-card-enhanced:hover p {
        color: var(--text-primary);
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .skill-category-enhanced {
        animation: slideInUp 0.6s ease-out forwards;
        opacity: 0;
    }
    
    .skill-category-enhanced:nth-child(1) { animation-delay: 0.1s; }
    .skill-category-enhanced:nth-child(2) { animation-delay: 0.2s; }
    .skill-category-enhanced:nth-child(3) { animation-delay: 0.3s; }
    .skill-category-enhanced:nth-child(4) { animation-delay: 0.4s; }
    
    @media (max-width: 1200px) {
        .skills-container-enhanced {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .skills-title-enhanced {
            font-size: 2.5rem;
        }
    }
    
    @media (max-width: 768px) {
        .skills-container-enhanced {
            grid-template-columns: 1fr;
        }
        
        .skills-title-enhanced {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- SKILLS DATA WITH ICONS ---
TECH_SKILLS = {
    "Lenguajes y Bases de Datos": [
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "SQL", "icon": "fas fa-database"},
        {"name": "TypeScript", "icon": "fab fa-js-square"},
        {"name": "PostgreSQL", "icon": "fas fa-database"},
        {"name": "Redis", "icon": "fas fa-memory"},
        {"name": "pgvector", "icon": "fas fa-vector-square"}
    ],
    "Análisis y Machine Learning": [
        {"name": "Pandas", "icon": "fas fa-table"},
        {"name": "Scikit-learn", "icon": "fas fa-robot"},
        {"name": "NLTK", "icon": "fas fa-language"},
        {"name": "BeautifulSoup", "icon": "fas fa-code"},
        {"name": "TensorFlow", "icon": "fas fa-brain"},
        {"name": "PyTorch", "icon": "fas fa-brain"}
    ],
    "Frontend y Visualización": [
        {"name": "React 19", "icon": "fab fa-react"},
        {"name": "Leaflet", "icon": "fas fa-map-marked-alt"},
        {"name": "Power BI", "icon": "fas fa-chart-bar"},
        {"name": "Matplotlib", "icon": "fas fa-chart-line"},
        {"name": "Seaborn", "icon": "fas fa-chart-area"}
    ],
    "Backend, Cloud y Despliegue": [
        {"name": "FastAPI", "icon": "fas fa-bolt"},
        {"name": "Flask", "icon": "fas fa-flask"},
        {"name": "Docker", "icon": "fab fa-docker"},
        {"name": "Azure", "icon": "fas fa-cloud"},
        {"name": "WhatsApp API", "icon": "fab fa-whatsapp"},
        {"name": "Google APIs", "icon": "fab fa-google"}
    ]
}

# SOFT SKILLS DATA
SOFT_SKILLS = [
    {
        "title": "Resolución de Problemas",
        "icon": "fas fa-puzzle-piece",
        "description": "Capacidad para analizar problemas complejos y encontrar soluciones efectivas y creativas."
    },
    {
        "title": "Trabajo en Equipo",
        "icon": "fas fa-users",
        "description": "Excelente capacidad para colaborar en equipos multidisciplinarios y fomentar un ambiente de trabajo positivo."
    },
    {
        "title": "Comunicación Efectiva",
        "description": "Habilidad para explicar conceptos técnicos de manera clara a diferentes audiencias, tanto técnicas como no técnicas.",
        "icon": "fas fa-comments"
    },
    {
        "title": "Aprendizaje Continuo",
        "icon": "fas fa-graduation-cap",
        "description": "Compromiso con el aprendizaje constante y la actualización en las últimas tecnologías y metodologías."
    },
    {
        "title": "Gestión del Tiempo",
        "icon": "fas fa-clock",
        "description": "Habilidad para priorizar tareas y cumplir con los plazos establecidos de manera eficiente."
    },
    {
        "title": "Pensamiento Crítico",
        "icon": "fas fa-brain",
        "description": "Capacidad para analizar información de manera objetiva y tomar decisiones fundamentadas."
    }
]

# --- SKILLS SECTION ---
st.markdown("""
<div class='skills-header-enhanced'>
    <h1 class='skills-title-enhanced'>
        <i class='fas fa-code'></i>
        <span>Habilidades Técnicas</span>
    </h1>
    <p class='skills-subtitle'>Tecnologías y herramientas con las que trabajo regularmente. Cada categoría representa un área de experiencia donde he desarrollado habilidades sólidas a lo largo de mi carrera.</p>
</div>
""", unsafe_allow_html=True)

# --- FUNCTION TO DISPLAY SKILLS ---
def display_skills(category, skills, icon_map):
    category_icons = {
        "Lenguajes y Bases de Datos": "fas fa-code",
        "Análisis y Machine Learning": "fas fa-brain",
        "Frontend y Visualización": "fas fa-paint-brush",
        "Backend, Cloud y Despliegue": "fas fa-server"
    }
    icon = icon_map.get(category, "fas fa-code")
    
    skills_html = "".join(
        [f"<div class='skill-item-enhanced'><i class='{skill['icon']}'></i> {skill['name']}</div>" for skill in skills]
    )
    
    return f"<div class='skill-category-enhanced'><h3><i class='{icon}'></i> {category}</h3><div class='skill-items-enhanced'>{skills_html}</div></div>"

# --- DISPLAY ALL SKILL CATEGORIES ---
icon_map = {
    "Lenguajes y Bases de Datos": "fas fa-code",
    "Análisis y Machine Learning": "fas fa-brain",
    "Frontend y Visualización": "fas fa-paint-brush",
    "Backend, Cloud y Despliegue": "fas fa-server"
}

# Crear el HTML para todas las categorías de habilidades
skills_sections = []
for category, skills in TECH_SKILLS.items():
    skills_sections.append(display_skills(category, skills, icon_map))

# Unir todas las secciones y mostrar en un solo contenedor
st.markdown(
    f"<div class='skills-container-enhanced'>{''.join(skills_sections)}</div>", 
    unsafe_allow_html=True
)

# --- SOFT SKILLS SECTION ---
st.markdown("""
<div class='soft-skills-section'>
    <div class='soft-skills-header-enhanced'>
        <h2 class='soft-skills-title'>
            <i class='fas fa-user-tie'></i>
            <span>Habilidades Blandas</span>
        </h2>
        <p class='soft-skills-description'>Habilidades interpersonales esenciales que potencian mi desempeño profesional. Me permiten colaborar efectivamente, resolver problemas complejos y liderar equipos con éxito en entornos desafiantes.</p>
    </div>
    <div class='soft-skills-container-enhanced'>
""", unsafe_allow_html=True)

# Dividir las habilidades blandas en dos columnas
col1, col2 = st.columns(2, gap="large")

with col1:
    for skill in SOFT_SKILLS[:len(SOFT_SKILLS)//2]:
        st.markdown(f"""
        <div class='soft-skill-card-enhanced'>
            <div class='soft-skill-header-enhanced'>
                <div class='soft-skill-icon-wrapper'>
                    <i class='{skill['icon']}'></i>
                </div>
                <h3>{skill['title']}</h3>
            </div>
            <p>{skill['description']}</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    for skill in SOFT_SKILLS[len(SOFT_SKILLS)//2:]:
        st.markdown(f"""
        <div class='soft-skill-card-enhanced'>
            <div class='soft-skill-header-enhanced'>
                <div class='soft-skill-icon-wrapper'>
                    <i class='{skill['icon']}'></i>
                </div>
                <h3>{skill['title']}</h3>
            </div>
            <p>{skill['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)