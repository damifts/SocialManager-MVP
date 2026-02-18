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

from __future__ import annotations

from datetime import datetime
import random

import streamlit as st


PAGES = ["🏠 Home", "✨ Genera Post", "📅 Calendario", "📊 Analytics"]


st.set_page_config(
    page_title="Social Manager MVP",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    :root {
        --sm-accent: #f59e0b;
        --sm-accent-dark: #d97706;
        --sm-ink: #0f172a;
        --sm-muted: #475569;
        --sm-panel: #ffffff;
    }
    .main {
        background: radial-gradient(circle at top left, #fff7ed 0%, #f8fafc 55%, #fef3c7 100%);
    }
    .sm-card {
        background: var(--sm-panel);
        padding: 1.25rem 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
    }
    .sm-pill {
        display: inline-block;
        padding: 0.15rem 0.6rem;
        border-radius: 9999px;
        background: #e2e8f0;
        color: var(--sm-muted);
        font-size: 0.75rem;
        font-weight: 600;
    }
    .stButton>button {
        background-color: var(--sm-accent);
        color: #ffffff;
        border-radius: 9999px;
        padding: 0.7rem 1.4rem;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: var(--sm-accent-dark);
    }
    h1, h2, h3 {
        color: var(--sm-ink);
    }
</style>
""",
    unsafe_allow_html=True,
)


def _set_page(target: str) -> None:
    st.session_state.page = target
    st.rerun()


def render_sidebar() -> str:
    if "page" not in st.session_state:
        st.session_state.page = PAGES[0]

    with st.sidebar:
        st.title("📱 Social Manager")
        st.markdown("---")
        page = st.radio(
            "Navigazione",
            PAGES,
            index=PAGES.index(st.session_state.page),
            label_visibility="collapsed",
            key="page",
        )

        st.markdown("---")
        with st.expander("🔧 Status Sistema"):
            st.caption("💾 MongoDB: Non configurato")
            st.caption("🤖 Gemini AI: Non configurato")
            st.caption("📝 Configura .env e riavvia")

        st.markdown("---")
        st.caption("v0.2.0 - MVP")
        st.caption("Issues #7-25 predisposte")

    return page


def generate_content_mock(prompt: str, social_target: str) -> str:
    """
    Mock function per generazione AI
    """
    snippet = prompt.strip().replace("\n", " ")[:120]
    return (
        f"🤖 [MOCK AI] Post generato per {social_target}:\n\n"
        f"{snippet}...\n\n"
        "✨ Questo e un esempio. Configura GEMINI_API_KEY per AI reale!\n\n"
        "📝 Esegui: python test_gemini.py"
    )


@st.cache_data(ttl=60)
def get_mock_metrics():
    return [
        {"label": "📝 Post Programmati", "value": "12", "delta": "+3"},
        {"label": "👀 Reach Totale", "value": "45.2K", "delta": "+12%"},
        {"label": "💬 Engagement", "value": "8.5%", "delta": "+2.1%"},
    ]


@st.cache_data(ttl=120)
def get_mock_calendar():
    today = datetime.now()
    return [
        {
            "title": "Post esempio: lancio prodotto",
            "date": today.strftime("%d/%m/%Y"),
            "social": "LinkedIn",
        },
        {
            "title": "Post esempio: tips settimanali",
            "date": today.strftime("%d/%m/%Y"),
            "social": "Instagram",
        },
        {
            "title": "Post esempio: behind the scenes",
            "date": today.strftime("%d/%m/%Y"),
            "social": "Twitter",
        },
    ]


def render_home() -> None:
    st.title("Social Manager MVP")
    st.markdown("### 🚀 Piattaforma per gestione social con automazione AI")
    st.markdown("---")

    metric_cols = st.columns(3)
    for col, metric in zip(metric_cols, get_mock_metrics()):
        with col:
            st.markdown('<div class="sm-card">', unsafe_allow_html=True)
            st.metric(metric["label"], metric["value"], metric["delta"])
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🚀 Quick Actions")
    action_cols = st.columns(3)

    with action_cols[0]:
        if st.button("✨ Genera con AI", use_container_width=True):
            _set_page("✨ Genera Post")
    with action_cols[1]:
        if st.button("📅 Vedi Calendario", use_container_width=True):
            _set_page("📅 Calendario")
    with action_cols[2]:
        if st.button("📊 Analizza", use_container_width=True):
            _set_page("📊 Analytics")


def render_generate() -> None:
    st.title("✨ Genera Post con AI")
    st.markdown("Crea contenuti ottimizzati per ogni social network")
    st.markdown("---")

    col_main, col_side = st.columns([2, 1], gap="large")

    with col_main:
        tabs = st.tabs(["🧠 Brief", "👁️ Preview"])

        with tabs[0]:
            with st.form("generate_form", clear_on_submit=False):
                prompt = st.text_area(
                    "Descrivi cosa vuoi comunicare",
                    placeholder="Es: Annuncio nuovo prodotto, tips professionali, behind the scenes...",
                    height=160,
                )
                col_a, col_b = st.columns(2)
                with col_a:
                    social_target = st.selectbox(
                        "Social target",
                        ["LinkedIn", "Instagram", "Twitter", "Facebook"],
                    )
                with col_b:
                    tone = st.selectbox(
                        "Tono",
                        ["Professionale", "Informativo", "Ispirazionale", "Umoristico"],
                    )
                submitted = st.form_submit_button(
                    "🚀 Genera Post",
                    type="primary",
                    use_container_width=True,
                )

            if submitted:
                if prompt.strip():
                    with st.spinner("✨ Generazione in corso con AI..."):
                        generated = generate_content_mock(prompt, social_target)
                        st.session_state.generated_text = generated
                        st.session_state.social_target = social_target.lower()
                        st.session_state.tone = tone.lower()
                        st.success("✅ Post generato con successo!")
                else:
                    st.warning("⚠️ Inserisci una descrizione per generare il post")

        with tabs[1]:
            if st.session_state.get("generated_text"):
                st.markdown('<div class="sm-card">', unsafe_allow_html=True)
                st.write(st.session_state.generated_text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("Nessuna bozza disponibile. Genera un post per vedere la preview.")

    with col_side:
        st.subheader("⚙️ Impostazioni")
        schedule_enabled = st.toggle("Programma pubblicazione", value=False)
        if schedule_enabled:
            data_programmazione = st.date_input("📅 Data pubblicazione")
            ora_programmazione = st.time_input("⏰ Ora pubblicazione")
            st.caption(f"Programmazione: {data_programmazione} alle {ora_programmazione}")
        else:
            st.caption("Pubblicazione manuale")

        if st.session_state.get("generated_text"):
            if st.button("💾 Salva Bozza", use_container_width=True):
                st.success("Bozza salvata! (TODO: DB integration)")


def render_calendar() -> None:
    st.title("📅 Calendario Editoriale")
    st.markdown("Visualizza e gestisci i post programmati")
    st.markdown("---")

    st.info("📋 TODO Thomas: Implementare vista calendario con post programmati (issue #7)")
    st.markdown("### 📝 Post Programmati (Mock)")

    for idx, item in enumerate(get_mock_calendar(), start=1):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        with col1:
            st.write(f"{idx}. {item['title']}")
        with col2:
            st.write(f"📅 {item['date']}")
        with col3:
            st.write(f"🔵 {item['social']}")
        with col4:
            st.button("✏️", key=f"edit_{idx}")


def render_analytics() -> None:
    st.title("📊 Analytics & Insights")
    st.markdown("Monitora performance e engagement dei tuoi post")
    st.markdown("---")

    st.info("📈 TODO Danilo: Implementare dashboard analytics con metriche engagement (issue #8)")

    rng = random.Random(42)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Views Settimanali")
        chart_data = {
            "Giorno": ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"],
            "Views": [rng.randint(100, 1000) for _ in range(7)],
        }
        st.line_chart(chart_data, x="Giorno", y="Views")

    with col2:
        st.subheader("Engagement per Social")
        chart_data = {
            "Social": ["LinkedIn", "Twitter", "Instagram"],
            "Engagement": [850, 620, 1200],
        }
        st.bar_chart(chart_data, x="Social", y="Engagement")


current_page = render_sidebar()
if current_page == "🏠 Home":
    render_home()
elif current_page == "✨ Genera Post":
    render_generate()
elif current_page == "📅 Calendario":
    render_calendar()
elif current_page == "📊 Analytics":
    render_analytics()

st.markdown("---")
st.caption("Social Manager MVP - Powered by Streamlit & AI")
