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

try:
    from streamlit_calendar import calendar as st_calendar
except ImportError:
    st_calendar = None

import streamlit as st


PAGES = [" Home", " Genera Post", " Calendario", " Editor", " Analytics"]


st.set_page_config(
    page_title="Social Manager MVP",
    page_icon="",
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
        st.title(" Social Manager")
        st.markdown("---")
        page = st.radio(
            "Navigazione",
            PAGES,
            index=PAGES.index(st.session_state.page),
            label_visibility="collapsed",
            key="page",
        )

        st.markdown("---")
        with st.expander(" Status Sistema"):
            st.caption(" MongoDB: Non configurato")
            st.caption(" Gemini AI: Non configurato")
            st.caption(" Configura .env e riavvia")

        st.markdown("---")
        st.caption("v0.2.0 - MVP")
        st.caption("Issues #7-25 predisposte")

    return page


def generate_content_mock(prompt: str, social_target: str) -> str:
    snippet = prompt.strip().replace("\n", " ")[:120]
    return (
        f" [MOCK AI] Post generato per {social_target}:\n\n"
        f"{snippet}...\n\n"
        " Questo e un esempio. Configura GEMINI_API_KEY per AI reale!\n\n"
        " Esegui: python test_gemini.py"
    )


@st.cache_data(ttl=60)
def get_mock_metrics():
    return [
        {"label": " Post Programmati", "value": "12", "delta": "+3"},
        {"label": " Reach Totale", "value": "45.2K", "delta": "+12%"},
        {"label": " Engagement", "value": "8.5%", "delta": "+2.1%"},
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


def ensure_mock_posts() -> None:
    if "posts" in st.session_state:
        return
    st.session_state.posts = [
        {
            "id": 1,
            "content": "Lancio del nuovo prodotto! Scopri le nuove funzionalita.",
            "date": "2024-02-05",
            "status": "pubblicato",
            "platform": "Instagram",
            "likes": 1250,
            "comments": 87,
        },
        {
            "id": 2,
            "content": "Dietro le quinte del team e i nostri processi.",
            "date": "2024-02-12",
            "status": "pubblicato",
            "platform": "Facebook",
            "likes": 892,
            "comments": 43,
        },
        {
            "id": 3,
            "content": "Offerta speciale: sconto del 20% fino al 18 febbraio.",
            "date": "2024-02-17",
            "status": "programmato",
            "platform": "Instagram",
            "likes": 0,
            "comments": 0,
        },
    ]


def render_home() -> None:
    st.title("Social Manager MVP")
    st.markdown("###  Piattaforma per gestione social con automazione AI")
    st.markdown("---")

    metric_cols = st.columns(3)
    for col, metric in zip(metric_cols, get_mock_metrics()):
        with col:
            st.markdown('<div class="sm-card">', unsafe_allow_html=True)
            st.metric(metric["label"], metric["value"], metric["delta"])
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader(" Quick Actions")
    action_cols = st.columns(3)

    with action_cols[0]:
        if st.button(" Genera con AI", use_container_width=True):
            _set_page(" Genera Post")
    with action_cols[1]:
        if st.button(" Vedi Calendario", use_container_width=True):
            _set_page(" Calendario")
    with action_cols[2]:
        if st.button(" Gestisci Post", use_container_width=True):
            _set_page(" Editor")


def render_generate() -> None:
    st.title(" Genera Post con AI")
    st.markdown("Crea contenuti ottimizzati per ogni social network")
    st.markdown("---")

    col_main, col_side = st.columns([2, 1], gap="large")

    with col_main:
        tabs = st.tabs([" Brief", " Preview"])

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
                    " Genera Post",
                    type="primary",
                    use_container_width=True,
                )

            if submitted:
                if prompt.strip():
                    with st.spinner(" Generazione in corso con AI..."):
                        generated = generate_content_mock(prompt, social_target)
                        st.session_state.generated_text = generated
                        st.session_state.social_target = social_target.lower()
                        st.session_state.tone = tone.lower()
                        st.success(" Post generato con successo!")
                else:
                    st.warning(" Inserisci una descrizione per generare il post")

        with tabs[1]:
            if st.session_state.get("generated_text"):
                st.markdown('<div class="sm-card">', unsafe_allow_html=True)
                st.write(st.session_state.generated_text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("Nessuna bozza disponibile. Genera un post per vedere la preview.")

    with col_side:
        st.subheader(" Impostazioni")
        schedule_enabled = st.toggle("Programma pubblicazione", value=False)
        if schedule_enabled:
            data_programmazione = st.date_input(" Data pubblicazione")
            ora_programmazione = st.time_input(" Ora pubblicazione")
            st.caption(f"Programmazione: {data_programmazione} alle {ora_programmazione}")
        else:
            st.caption("Pubblicazione manuale")

        if st.session_state.get("generated_text"):
            if st.button(" Salva Bozza", use_container_width=True):
                st.success("Bozza salvata! (TODO: DB integration)")


def render_calendar() -> None:
    st.title(" Calendario Editoriale")
    st.markdown("Visualizza e gestisci i post programmati")
    st.markdown("---")

    def get_color(platform: str) -> str:
        colors = {
            "LinkedIn": "#0077B5",
            "Instagram": "#E1306C",
            "Twitter": "#1DA1F2",
            "Facebook": "#1877F2",
        }
        return colors.get(platform, "#6b7280")

    if "calendar_posts" not in st.session_state:
        st.session_state.calendar_posts = [
            {
                "id": str(index + 1),
                "title": f"{item['title']} ({item['social']})",
                "start": datetime.strptime(item["date"], "%d/%m/%Y").date().isoformat(),
                "color": get_color(item["social"]),
            }
            for index, item in enumerate(get_mock_calendar())
        ]

    if st_calendar is None:
        st.info("Vista calendario interattiva non disponibile. Installa streamlit-calendar per abilitarla.")
        st.markdown("###  Post Programmati (Mock)")
        for idx, item in enumerate(get_mock_calendar(), start=1):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            with col1:
                st.write(f"{idx}. {item['title']}")
            with col2:
                st.write(f" {item['date']}")
            with col3:
                st.write(f" {item['social']}")
            with col4:
                st.button("", key=f"edit_{idx}")
        return

    col1, col2 = st.columns([3, 1])

    with col1:
        calendar_options = {
            "initialView": "dayGridMonth",
            "locale": "it",
            "headerToolbar": {
                "left": "prev,next today",
                "center": "title",
                "right": "dayGridMonth,timeGridWeek,timeGridDay",
            },
            "editable": True,
            "selectable": True,
        }

        calendar_state = st_calendar(
            events=st.session_state.calendar_posts,
            options=calendar_options,
            key="editorial_calendar",
        )

        if calendar_state.get("eventDrop"):
            moved_event = calendar_state["eventDrop"]["event"]
            for event in st.session_state.calendar_posts:
                if event["id"] == moved_event["id"]:
                    event["start"] = moved_event["start"]
            st.rerun()

        if calendar_state.get("eventClick"):
            clicked = calendar_state["eventClick"]["event"]
            st.success(f" Post selezionato: {clicked['title']}")

    with col2:
        st.subheader(" Nuovo Post")

        with st.form("add_calendar_post"):
            titolo = st.text_input("Titolo")
            social = st.selectbox(
                "Social",
                ["LinkedIn", "Instagram", "Twitter", "Facebook"],
            )
            data = st.date_input("Data pubblicazione")
            submit = st.form_submit_button("Aggiungi")

            if submit and titolo:
                new_event = {
                    "id": str(len(st.session_state.calendar_posts) + 1),
                    "title": f"{titolo} ({social})",
                    "start": data.isoformat(),
                    "color": get_color(social),
                }

                st.session_state.calendar_posts.append(new_event)
                st.success("Post aggiunto")
                st.rerun()

        st.divider()

        if st.session_state.calendar_posts:
            selected = st.selectbox(
                " Elimina Post",
                st.session_state.calendar_posts,
                format_func=lambda x: x["title"],
            )

            if st.button("Elimina"):
                st.session_state.calendar_posts = [
                    p for p in st.session_state.calendar_posts if p["id"] != selected["id"]
                ]
                st.warning("Post eliminato")
                st.rerun()


def render_editor() -> None:
    ensure_mock_posts()
    st.title(" Editor Post")
    st.markdown("Gestisci bozze e post programmati")
    st.markdown("---")

    if "editing_post" in st.session_state:
        post_to_edit = next(
            (post for post in st.session_state.posts if post["id"] == st.session_state.editing_post),
            None,
        )

        if post_to_edit:
            st.info(f" Modifica del post programmato per {post_to_edit['date']}")
            edited_content = st.text_area(
                "Contenuto del post",
                value=post_to_edit["content"],
                height=150,
            )

            col1, col2 = st.columns(2)
            with col1:
                edited_date = st.date_input(
                    "Data pubblicazione",
                    value=datetime.strptime(post_to_edit["date"], "%Y-%m-%d"),
                )
            with col2:
                edited_platform = st.selectbox(
                    "Piattaforma",
                    ["Instagram", "Facebook", "Twitter", "LinkedIn"],
                    index=["Instagram", "Facebook", "Twitter", "LinkedIn"].index(post_to_edit["platform"]),
                )

            st.markdown("---")

            col1, col2 = st.columns(2)
            with col1:
                if st.button(" Salva modifiche", type="primary", use_container_width=True):
                    for post in st.session_state.posts:
                        if post["id"] == st.session_state.editing_post:
                            post["content"] = edited_content
                            post["date"] = edited_date.strftime("%Y-%m-%d")
                            post["platform"] = edited_platform
                    del st.session_state.editing_post
                    st.success(" Post aggiornato con successo!")
                    st.rerun()

            with col2:
                if st.button(" Annulla", use_container_width=True):
                    del st.session_state.editing_post
                    st.rerun()

        return

    st.markdown("###  Tutti i post")
    if not st.session_state.posts:
        st.info("Nessun post generato. Vai alla sezione Genera Post per creare il primo.")
        return

    for post in st.session_state.posts:
        status_color = "#16a34a" if post["status"] == "pubblicato" else "#f59e0b"
        status_text = " Pubblicato" if post["status"] == "pubblicato" else " Programmato"

        st.markdown(
            f"""
            <div class="sm-card" style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <div style="color: {status_color}; font-weight: 600; font-size: 0.9rem;">{status_text}</div>
                    <div style="color: #6b7280; font-size: 0.85rem;"> {post['date']} | {post['platform']}</div>
                </div>
                <div style="font-size: 1rem; margin-bottom: 0.75rem;">{post['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            if post["status"] == "programmato":
                if st.button(" Modifica", key=f"edit_{post['id']}", use_container_width=True):
                    st.session_state.editing_post = post["id"]
                    st.rerun()
        with col2:
            if st.button(" Elimina", key=f"delete_{post['id']}", use_container_width=True):
                st.session_state.posts = [p for p in st.session_state.posts if p["id"] != post["id"]]
                st.rerun()


def render_analytics() -> None:
    st.title(" Analytics & Insights")
    st.markdown("Monitora performance e engagement dei tuoi post")
    st.markdown("---")

    st.info(" TODO Danilo: Implementare dashboard analytics con metriche engagement (issue #8)")

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
if current_page == " Home":
    render_home()
elif current_page == " Genera Post":
    render_generate()
elif current_page == " Calendario":
    render_calendar()
elif current_page == " Editor":
    render_editor()
elif current_page == " Analytics":
    render_analytics()

st.markdown("---")
st.caption("Social Manager MVP - Powered by Streamlit & AI")
