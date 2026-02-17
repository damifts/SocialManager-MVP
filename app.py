import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add backend to path for imports
sys.path.append(str(Path(__file__).parent / "backend"))

from backend.schemas.post import PostCreate

# Page config
st.set_page_config(
    page_title="Social Manager MVP",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS per design coerente
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fef3c7 0%, #fff7ed 35%, #f8fafc 70%);
    }
    .stButton>button {
        background-color: #f59e0b;
        color: white;
        border-radius: 9999px;
        padding: 0.75rem 1.5rem;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #d97706;
    }
    .stTextArea>div>div>textarea {
        border-radius: 0.75rem;
        border: 1px solid #cbd5e1;
    }
    h1 {
        color: #0f172a;
        font-weight: 700;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📱 Social Manager")
    st.markdown("---")
    
    page = st.radio(
        "Navigazione",
        ["🏠 Home", "✨ Genera Post", "📅 Calendario", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("v0.1.0 - MVP")

# TODO: Andrea/Filippo - Implementare integrazione LangChain/OpenAI vera
def generate_content_mock(prompt: str, social_target: str) -> str:
    """Mock function per generazione AI"""
    return f"[MOCK AI] Post generato per {social_target}:\n\n{prompt[:100]}...\n\nQuesto è un testo di esempio generato dall'AI. Integra LangChain qui!"

# Home Page
if page == "🏠 Home":
    st.title("Social Manager MVP")
    st.markdown("### Piattaforma per gestione social con automazione AI")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📝 Post Programmati", "12", "+3")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("👀 Reach Totale", "45.2K", "+12%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("💬 Engagement", "8.5%", "+2.1%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🚀 Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✨ Genera con AI", use_container_width=True):
            st.switch_page("pages/1_✨_Genera_Post.py")
    
    with col2:
        if st.button("📅 Vedi Calendario", use_container_width=True):
            st.info("Calendario in sviluppo - TODO: Thomas")
    
    with col3:
        if st.button("📊 Analizza", use_container_width=True):
            st.info("Analytics in sviluppo - TODO: Danilo")

# Genera Post Page
elif page == "✨ Genera Post":
    st.title("✨ Genera Post con AI")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Contenuto")
        
        prompt = st.text_area(
            "Descrivi cosa vuoi comunicare",
            placeholder="Es: Annuncio nuovo prodotto, tips professionali, behind the scenes...",
            height=150
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            social_target = st.selectbox(
                "Social Target",
                ["LinkedIn", "Twitter", "Instagram", "Facebook"]
            )
        
        with col_b:
            tono = st.selectbox(
                "Tono di voce",
                ["Professionale", "Casual", "Ispirazionale", "Educativo"]
            )
        
        if st.button("🚀 Genera Post", type="primary", use_container_width=True):
            if prompt:
                with st.spinner("Generazione in corso..."):
                    generated = generate_content_mock(prompt, social_target)
                    st.session_state.generated_text = generated
                    st.success("Post generato con successo!")
            else:
                st.warning("Inserisci una descrizione per generare il post")
    
    with col2:
        st.subheader("Impostazioni")
        
        data_programmazione = st.date_input("Data pubblicazione")
        ora_programmazione = st.time_input("Ora pubblicazione")
        
        st.markdown("---")
        
        # TODO: Patrick - Aggiungere preview formattata per social
        if "generated_text" in st.session_state:
            st.subheader("Preview")
            st.info(st.session_state.generated_text)
            
            if st.button("💾 Salva Bozza", use_container_width=True):
                st.success("Bozza salvata! (TODO: DB integration)")

# Calendario Page
elif page == "📅 Calendario":
    st.title("📅 Calendario Editoriale")
    st.info("📋 TODO: Thomas - Implementare vista calendario con post programmati")
    
    # Mock data
    st.markdown("### Post Programmati")
    
    for i in range(3):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        with col1:
            st.write(f"Post esempio {i+1}: Contenuto social...")
        with col2:
            st.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
        with col3:
            st.write("🔵 LinkedIn")
        with col4:
            st.button("✏️", key=f"edit_{i}")

# Analytics Page
elif page == "📊 Analytics":
    st.title("📊 Analytics & Insights")
    st.info("📈 TODO: Danilo - Implementare dashboard analytics con metriche engagement")
    
    # Mock charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Views Settimanali")
        import random
        chart_data = {
            "Giorno": ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"],
            "Views": [random.randint(100, 1000) for _ in range(7)]
        }
        st.line_chart(chart_data, x="Giorno", y="Views")
    
    with col2:
        st.subheader("Engagement per Social")
        chart_data = {
            "Social": ["LinkedIn", "Twitter", "Instagram"],
            "Engagement": [850, 620, 1200]
        }
        st.bar_chart(chart_data, x="Social", y="Engagement")

# Footer
st.markdown("---")
st.caption("Social Manager MVP - Powered by Streamlit & AI")
