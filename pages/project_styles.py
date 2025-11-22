"""
Módulo de estilos compartidos para todas las páginas de proyectos.
Estilo Cyberpunk/Hacker con paleta naranja oscura.
"""

PROJECT_STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&display=swap');
    
    /* Variables Cyberpunk Responsive */
    :root {
        --bg-main: #0D1117;
        --bg-card: #161B22;
        --text-primary: #E6EDF3;
        --text-secondary: #8B949E;
        --accent-orange: #FF6A00;
        --accent-orange-glow: #FF8C2B;
        --matrix-green: #00FF9F;
        --cyan-detail: #00D4FF;
        --font-mono: 'JetBrains Mono', monospace;
        --touch-target-min: 2.75rem; /* 44px */
        --spacing-xs: 0.5rem;
        --spacing-sm: 1rem;
        --spacing-md: 1.5rem;
        --spacing-lg: 2rem;
        --spacing-xl: 3rem;
    }
    
    /* Reset básico */
    * {
        box-sizing: border-box;
        max-width: 100%;
    }
    
    /* Scrollbar personalizada */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0D1117;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #FF6A00 0%, #FF8C2B 100%);
        border-radius: 6px;
        border: 2px solid #0D1117;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #FF8C2B 0%, #FF6A00 100%);
        box-shadow: 0 0 10px rgba(255, 106, 0, 0.6);
    }
    
    .project-header-enhanced {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
    }
    
    .project-title-enhanced {
        font-family: var(--font-mono);
        font-size: clamp(1.75rem, 1.5rem + 4vw, 3.5rem); /* 28px - 56px */
        font-weight: 800;
        color: var(--accent-orange-glow);
        text-shadow: 0 0 clamp(0.9375rem, 0.75rem + 1.5vw, 1.875rem) rgba(255, 140, 43, 0.6),
                     0 0 clamp(1.875rem, 1.5rem + 3vw, 3.75rem) rgba(255, 140, 43, 0.3);
        margin-bottom: var(--spacing-sm);
        line-height: 1.2;
        position: relative;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .project-title-enhanced.typing {
        border-right: 2px solid var(--accent-orange-glow);
        animation: blink 1s infinite;
        white-space: nowrap;
        overflow: hidden;
        display: inline-block;
    }
    
    @keyframes blink {
        0%, 49% { border-color: var(--accent-orange-glow); }
        50%, 100% { border-color: transparent; }
    }
    
    .project-subtitle {
        font-family: var(--font-mono);
        font-size: clamp(1rem, 0.9rem + 1.5vw, 1.4rem); /* 16px - 22.4px */
        color: var(--text-secondary);
        margin-top: var(--spacing-sm);
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .section-title-enhanced {
        font-family: var(--font-mono);
        font-size: clamp(1.5rem, 1.3rem + 2vw, 2.2rem); /* 24px - 35.2px */
        font-weight: 800;
        color: var(--text-primary);
        margin: clamp(1.5rem, 1rem + 3vw, 3rem) 0 clamp(1rem, 0.8rem + 2vw, 2rem) 0;
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
        flex-wrap: wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .section-title-enhanced i {
        color: var(--accent-orange);
        font-size: 2rem;
        text-shadow: 0 0 15px rgba(255, 106, 0, 0.6);
    }
    
    .content-card {
        background: var(--bg-card);
        border-radius: clamp(0.75rem, 0.6rem + 1vw, 1rem); /* 12px - 16px */
        padding: clamp(1rem, 0.8rem + 1.5vw, 1.8rem); /* 16px - 28.8px */
        border: 0.0625rem solid rgba(255, 106, 0, 0.2); /* 1px */
        margin-bottom: var(--spacing-md);
        box-shadow: 0 clamp(0.375rem, 0.3rem + 0.5vw, 0.5rem) clamp(1.25rem, 1rem + 2vw, 2rem) rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        max-width: 100%;
        width: 100%;
        box-sizing: border-box;
    }
    
    .content-card:hover {
        border-color: var(--accent-orange);
        box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                    0 8px 32px rgba(0, 0, 0, 0.4);
        transform: translateY(-2px);
    }
    
    .metric-box {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        color: var(--text-primary);
        border: 1px solid rgba(255, 106, 0, 0.2);
        transition: all 0.4s ease;
        text-align: center;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .metric-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                    0 20px 50px rgba(0, 0, 0, 0.4);
        border-color: var(--accent-orange);
    }
    
    .metric-card-enhanced {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 106, 0, 0.2);
        transition: all 0.4s ease;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        text-align: center;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .metric-card-enhanced:hover {
        transform: translateY(-8px);
        box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                    0 20px 50px rgba(0, 0, 0, 0.4);
        border-color: var(--accent-orange);
        background: var(--bg-card);
    }
    
    .metric-value {
        font-family: var(--font-mono);
        font-size: clamp(1.5rem, 1.3rem + 2vw, 2.2rem); /* 24px - 35.2px */
        font-weight: 800;
        color: var(--accent-orange-glow);
        margin: 0.8rem 0;
        text-shadow: 0 0 clamp(0.625rem, 0.5rem + 1vw, 1.25rem) rgba(255, 140, 43, 0.5);
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .metric-label {
        font-family: var(--font-mono);
        color: var(--text-secondary);
        font-size: clamp(0.875rem, 0.8rem + 0.4vw, 1rem); /* 14px - 16px */
        line-height: 1.4;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    
    .tech-badge {
        display: inline-block;
        background: rgba(255, 106, 0, 0.1);
        color: var(--accent-orange);
        padding: clamp(0.375rem, 0.3rem + 0.5vw, 0.5rem) clamp(0.75rem, 0.6rem + 1vw, 1rem); /* 6px 12px - 8px 16px */
        border-radius: clamp(0.375rem, 0.3rem + 0.5vw, 0.5rem); /* 6px - 8px */
        margin: 0.3rem;
        font-family: var(--font-mono);
        font-weight: 500;
        font-size: clamp(0.75rem, 0.7rem + 0.3vw, 0.875rem); /* 12px - 14px */
        border: 0.0625rem solid rgba(255, 106, 0, 0.3); /* 1px */
        transition: all 0.3s ease;
        min-height: var(--touch-target-min);
        min-width: var(--touch-target-min);
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    
    .tech-badge:hover {
        background: rgba(255, 106, 0, 0.2);
        border-color: var(--accent-orange);
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(255, 106, 0, 0.3);
    }
    
    .hero-image-container {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5),
                    0 0 30px rgba(255, 106, 0, 0.2);
        margin: 2rem auto;
        max-width: 900px;
        max-height: 500px;
        border: 1px solid rgba(255, 106, 0, 0.2);
    }
    
    .hero-image-container:hover {
        border-color: var(--accent-orange);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5),
                    0 0 40px rgba(255, 106, 0, 0.4);
    }
    
    .hero-image-container img {
        width: 100%;
        height: auto;
        object-fit: cover;
        max-height: clamp(15.625rem, 12rem + 20vw, 31.25rem); /* 250px - 500px */
        display: block;
    }
    
    .gallery-image-container {
        border-radius: clamp(0.75rem, 0.6rem + 1vw, 0.75rem); /* 12px */
        overflow: hidden;
        box-shadow: 0 clamp(0.375rem, 0.3rem + 0.5vw, 0.5rem) clamp(1rem, 0.8rem + 1.5vw, 1.5rem) rgba(0, 0, 0, 0.4);
        margin-bottom: var(--spacing-md);
        transition: all 0.3s ease;
        max-height: clamp(12.5rem, 10rem + 15vw, 18.75rem); /* 200px - 300px */
        border: 0.0625rem solid rgba(255, 106, 0, 0.1); /* 1px */
        width: 100%;
        max-width: 100%;
    }
    
    .gallery-image-container:hover {
        transform: translateY(-0.3125rem); /* -5px */
        box-shadow: 0 0 clamp(0.9375rem, 0.75rem + 1.5vw, 1.875rem) rgba(255, 106, 0, 0.4),
                    0 clamp(0.625rem, 0.5rem + 1vw, 0.75rem) clamp(1.5rem, 1.2rem + 2vw, 2rem) rgba(0, 0, 0, 0.4);
        border-color: var(--accent-orange);
    }
    
    .gallery-image-container img {
        width: 100%;
        height: auto;
        max-height: clamp(12.5rem, 10rem + 15vw, 18.75rem); /* 200px - 300px */
        object-fit: cover;
        display: block;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: var(--bg-card);
        border-radius: clamp(0.75rem, 0.6rem + 1vw, 0.75rem); /* 12px */
        padding: clamp(0.625rem, 0.5rem + 0.8vw, 0.8rem) clamp(1rem, 0.8rem + 1.5vw, 1.5rem); /* 10px 16px - 12.8px 24px */
        font-family: var(--font-mono);
        font-weight: 600;
        font-size: clamp(0.875rem, 0.8rem + 0.4vw, 1rem); /* 14px - 16px */
        color: var(--text-secondary);
        border: 0.0625rem solid rgba(255, 106, 0, 0.2); /* 1px */
        transition: all 0.3s ease;
        min-height: var(--touch-target-min);
        min-width: var(--touch-target-min);
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--bg-card);
        border-color: rgba(255, 106, 0, 0.4);
        color: var(--text-primary);
        box-shadow: 0 0 15px rgba(255, 106, 0, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 106, 0, 0.1);
        color: var(--accent-orange-glow);
        border-color: var(--accent-orange);
        text-shadow: 0 0 10px rgba(255, 140, 43, 0.5);
        box-shadow: 0 0 20px rgba(255, 106, 0, 0.3);
    }
</style>
"""

FONT_AWESOME_LINK = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'

def load_project_styles():
    """Carga los estilos compartidos para proyectos"""
    import streamlit as st
    st.markdown(PROJECT_STYLES, unsafe_allow_html=True)
    st.markdown(FONT_AWESOME_LINK, unsafe_allow_html=True)

def github_button(url, text="🔗 Ver en GitHub"):
    """Crea un botón de GitHub personalizado con estilo cyberpunk naranja"""
    import streamlit as st
    st.markdown(f"""
    <div class="github-button-wrapper">
        <a href="{url}" target="_blank" rel="noopener noreferrer" class="github-button-cyberpunk">
            <span class="github-button-icon">🔗</span>
            <span class="github-button-text">{text.replace('🔗 ', '')}</span>
            <span class="github-button-arrow">→</span>
        </a>
    </div>
    <style>
        .github-button-wrapper {{
            margin: 2rem 0;
            padding: 0;
            width: 100%;
        }}
        
        .github-button-cyberpunk {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: clamp(0.5rem, 0.4rem + 0.8vw, 0.75rem);
            width: 100%;
            padding: clamp(0.75rem, 0.6rem + 0.8vw, 1rem) clamp(1.25rem, 1rem + 1.5vw, 2rem);
            background: linear-gradient(135deg, #FF6A00 0%, #FF8C2B 100%);
            color: #FFFFFF !important;
            border: 0.125rem solid #FF6A00;
            border-radius: clamp(0.75rem, 0.6rem + 1vw, 0.75rem);
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 600;
            font-size: clamp(0.875rem, 0.8rem + 0.4vw, 1.05rem);
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 clamp(0.25rem, 0.2rem + 0.3vw, 0.25rem) clamp(1rem, 0.8rem + 1.5vw, 1.25rem) rgba(255, 106, 0, 0.3),
                        0 0 clamp(1.125rem, 0.9rem + 2vw, 1.875rem) rgba(255, 106, 0, 0.2);
            cursor: pointer;
            box-sizing: border-box;
            position: relative;
            overflow: hidden;
            text-shadow: 0 0 clamp(0.5rem, 0.4rem + 0.8vw, 0.625rem) rgba(255, 255, 255, 0.3);
            letter-spacing: 0.5px;
            min-height: 2.75rem;
            min-width: 2.75rem;
        }}
        
        .github-button-cyberpunk::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.5s;
        }}
        
        .github-button-cyberpunk:hover::before {{
            left: 100%;
        }}
        
        .github-button-cyberpunk:hover {{
            background: linear-gradient(135deg, #FF8C2B 0%, #FF6A00 100%);
            border-color: #FF8C2B;
            transform: translateY(-3px);
            box-shadow: 0 0 30px rgba(255, 106, 0, 0.4),
                        0 8px 30px rgba(255, 106, 0, 0.3),
                        inset 0 0 20px rgba(255, 140, 43, 0.2),
                        0 0 40px rgba(255, 140, 43, 0.6);
            color: #FFFFFF !important;
            text-decoration: none;
            text-shadow: 0 0 20px #FF8C2B;
        }}
        
        .github-button-cyberpunk:active {{
            transform: translateY(-1px);
            box-shadow: 0 0 20px rgba(255, 106, 0, 0.4),
                        inset 0 2px 4px rgba(0, 0, 0, 0.2);
        }}
        
        .github-button-cyberpunk:visited {{
            color: #FFFFFF !important;
        }}
        
        .github-button-icon {{
            font-size: clamp(1rem, 0.9rem + 1vw, 1.2rem);
            display: inline-flex;
            align-items: center;
            transition: transform 0.3s ease;
            filter: drop-shadow(0 0 clamp(0.25rem, 0.2rem + 0.3vw, 0.3125rem) rgba(255, 255, 255, 0.5));
        }}
        
        .github-button-cyberpunk:hover .github-button-icon {{
            transform: rotate(-15deg) scale(1.1);
            filter: drop-shadow(0 0 10px rgba(255, 140, 43, 0.8));
        }}
        
        .github-button-text {{
            flex: 1;
            text-align: center;
            letter-spacing: 0.5px;
        }}
        
        .github-button-arrow {{
            font-size: clamp(1.125rem, 1rem + 1.5vw, 1.3rem);
            opacity: 0.9;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            filter: drop-shadow(0 0 clamp(0.25rem, 0.2rem + 0.3vw, 0.3125rem) rgba(255, 255, 255, 0.5));
        }}
        
        @media (max-width: 35.9375rem) {{
            .github-button-cyberpunk {{
                padding: 1rem 1.5rem;
                font-size: clamp(0.875rem, 0.8rem + 0.4vw, 0.95rem);
            }}
        }}
        
        .github-button-cyberpunk:hover .github-button-arrow {{
            opacity: 1;
            transform: translateX(4px);
            filter: drop-shadow(0 0 10px rgba(255, 140, 43, 0.8));
        }}
    </style>
    """, unsafe_allow_html=True)
