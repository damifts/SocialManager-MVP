"""
Social Manager MVP - Streamlit App
Issues predisposte:
- #7: Frontend sidebar
- #8: Frontend body
- #9: Frontend header
- #11, #18, #19: MongoDB integration (predisposto, da configurare)
- #15, #12, #10: Gemini AI integration (predisposto, da configurare)

TODO: Configurare .env con MONGO_URI e GEMINI_API_KEY
"""

import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add backend to path for imports
sys.path.append(str(Path(__file__).parent / "backend"))

# TODO: Decommentare quando MongoDB è configurato
# from backend.database import connect_to_mongodb, get_database
# from backend.dao import PostDAO

# TODO: Decommentare quando Gemini è configurato
# from backend.ai import get_content_generator

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

# ============================================================================
# SIDEBAR - Issue #7: Frontend sidebar
# ============================================================================
with st.sidebar:
    st.title("📱 Social Manager")
    st.markdown("---")
    
    # Navigazione principale
    page = st.radio(
        "Navigazione",
        ["🏠 Home", "✨ Genera Post", "📅 Calendario", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # TODO: Issue #7 - Estendere sidebar con:
    # - Filtri per social network
    # - Range date per calendario
    # - Quick stats overview
    # - Notifiche post programmati
    
    # Status connessioni (development info)
    with st.expander("🔧 Status Sistema"):
        # TODO: Issue #11, #18 - Check MongoDB
        st.caption("💾 MongoDB: Non configurato")
        st.caption("🤖 Gemini AI: Non configurato")
        st.caption("")
        st.caption("📝 Configura .env e riavvia")
    
    st.markdown("---")
    st.caption("v0.2.0 - MVP")
    st.caption("Issues #7-25 predisposte")

# TODO: Issue #12, #15 - Quando Gemini è configurato, decommentare:
# generator = get_content_generator()

def generate_content_mock(prompt: str, social_target: str) -> str:
    """
    Mock function per generazione AI
    
    TODO: Issue #12 - Sostituire con Gemini reale
    Decommentare quando GEMINI_API_KEY è in .env:
    
    result = await generator.generate_post(
        topic=prompt,
        social=social_target,
        tone="professionale"
    )
    return result["generated_text"] if result["success"] else "Errore generazione"
    """
    return f"🤖 [MOCK AI] Post generato per {social_target}:\n\n{prompt[:100]}...\n\n✨ Questo è un esempio. Configura GEMINI_API_KEY per AI reale!\n\n📝 Esegui: python test_gemini.py"

# ============================================================================
# HOME PAGE - Issue #8: Frontend Body
# ============================================================================
if page == "🏠 Home":
    # Header Issue #9
    st.title("Social Manager MVP")
    st.markdown("### 🚀 Piattaforma per gestione social con automazione AI")
    st.markdown("---")
    
    # TODO: Issue #8 - Dashboard con dati reali da MongoDB
    # Quando MongoDB è configurato, sostituire mock con:
    # post_dao = PostDAO()
    # total_posts = await post_dao.count()
    # scheduled = await post_dao.count({"status": "scheduled"})
    
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

# ============================================================================
# GENERA POST PAGE - Issue #8: Body + Issue #6: Model AI per GUI
# ============================================================================
elif page == "✨ Genera Post":
    # Header Issue #9
    st.title("✨ Genera Post con AI")
    st.markdown("Crea contenuti ottimizzati per ogni social network")
    st.markdown("---")
    
    # TODO: Issue #6 - GUI input/output per AI
    # TODO: Issue #12 - Collegare a Gemini per generazione reale
    
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
            social_target = st.selectbox(, "Umoristico"]
            )
        
        # TODO: Issue #10 - I toni sono definiti in backend/ai/prompts.py
        # Quando Gemini configurato, passare tono al generator
        
        if st.button("🚀 Genera Post", type="primary", use_container_width=True):
            if prompt:
                with st.spinner("✨ Generazione in corso con AI..."):
                    # TODO: Issue #12 - Usare Gemini reale
                    generated = generate_content_mock(prompt, social_target)
                    st.session_state.generated_text = generated
                    st.session_state.social_target = social_target.lower()
                    st.success("✅ Post generato con successo!")
            else:
                st.warning("⚠️ Inserisci una descrizione per generare il post")
    
    with col2:
        st.subheader("⚙️ Impostazioni")
        
        # TODO: Issue #8 - Programmazione pubblicazione
        data_programmazione = st.date_input("📅 Data pubblicazione")
        ora_programmazione = st.time_input("⏰ o con successo!")
            else:
                st.warning("Inserisci una descrizione per generare il post")
    
    with col2:
        st.subheader("Impostazioni")
        Issue #6 - Preview con formattazione social-specific
        # TODO: Patrick - Preview formattata per ogni social
        if "generated_text" in st.session_state:
            st.subheader("👁️ Preview")
            
            # Badge social
            social_emoji = {
                "linkedin": "🔵",
  ============================================================================
# CALENDARIO PAGE - Issue #8: Body + Issue #7: Calendario editoriale
# ============================================================================
elif page == "📅 Calendario":
    # Header Issue #9
    st.title("📅 Calendario Editoriale")
    st.markdown("Visualizza e gestisci i post programmati")
    st.markdown("---")
    
    # TODO: Issue #7 - Thomas: Implementare vista calendario
    # TODO: Issue #22 - Query post per range date da MongoDB
    st.info("📋 TODO Thomas: Implementare vista calendario con post programmati (issue #7)")
    st.markdown("""
    **Features da implementare:**
    - Vista mensile con st.columns() grid
    - Filtri per social network (sidebar)
    - Click su giorno → dettagli post
    - Badge colorati per status (draft/scheduled/published)
    - Drag & drop per rimuovere data (future feature)
    """)
    
    # Mock data
    st.markdown("### 📝 Post Programmati (Mock)")
    
    # TODO: Sostituire con:
  ============================================================================
# ANALYTICS PAGE - Issue #8: Body + Dashboard analytics
# ============================================================================
elif page == "📊 Analytics":
    # Header Issue #9
    st.title("📊 Analytics & Insights")
    st.markdown("Monitora performance e engagement dei tuoi post")
    st.markdown("---")
    
    # TODO: Issue #8 - Danilo: Implementare dashboard analytics
    # TODO: PostDAO.get_analytics_data() per metriche reali
    st.info("📈 TODO Danilo: Implementare dashboard analytics con metriche engagement (issue #8)")
    st.markdown("""
    **Features da implementare:**
    - Aggregazioni MongoDB per stats
    - Filtri temporali (ultima settimana/mese/anno)
    - Confronto performance per social
    - Export report CSV/PDF
    - Insights automatici AI (future)
    ""
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        with col1:
            st.write(f"Post esempio {i+1}: Contenuto social...")
        with col2:
            st.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")
        with col3:
            st.write("🔵 LinkedIn")
        with col4:
            if st.button("✏️", key=f"edit_{i}"):
                st.info("TODO: Edit modal (issue #23)
                if st.button("📤 Programma", use_container_width=True):
                    st.success("✅ Post programmato! (TODO: DB + scheduler)")
                    # TODO: Issue #23 - Update status a "scheduled"
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
