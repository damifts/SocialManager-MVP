import PIL.ImageShow
import streamlit as st
from datetime import datetime, timedelta
import calendar
import pandas as pd

#==========================================
# Configurazione pagina
#==========================================
st.set_page_config(page_title="Social Manager", layout="wide", initial_sidebar_state="collapsed")

# Inizializza session state per la navigazione
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


#==========================================
# import CSS
#==========================================
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("body_css.css")   


#===================================
# SIDEBAR
#===================================
st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <div style="background: white; width: 50px; height: 50px; border-radius: 10px; 
                    display: inline-flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <span style="color: #3B7DC0; font-size: 24px; font-weight: bold;">SM</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.title("MENU")

# Navigazione con bottoni

#bottone home collega alla scehrmata home
if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = 'Home'

#bottone calender collega alla scehrmata calender
if st.sidebar.button("📅 Calendar", use_container_width=True):
    st.session_state.page = 'Calendar'

#bottone editor collega alla scehrmata editor
if st.sidebar.button("� Editor", use_container_width=True):
    st.session_state.page = 'Editor'

# Separatore
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style="color: white; opacity: 0.7; font-size: 0.85rem; text-align: center; margin-top: 20px;">
        <p>👤 Mario Rossi</p>
        <p>Social Manager</p>
    </div>
    """, unsafe_allow_html=True)


#===================================
# ===== PAGINE =====
#===================================
# Titolo dinamico basato sulla pagina corrente
page_titles = {
    'Home': '🏠 Home',
    'Calendar': '📅 Calendar',
    'Editor': '📝 Editor'
}

# Inizializza database post in session_state da modificare .post con accesso al database
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "id": 1,
            "content": "Lancio del nuovo prodotto! 🚀 Scopri tutte le funzionalità innovative che abbiamo preparato per voi.",
            "date": "2024-02-05",
            "status": "pubblicato",
            "platform": "Instagram",
            "likes": 1250,
            "comments": 87
        },
        {
            "id": 2,
            "content": "Dietro le quinte del nostro team! 💼 Ecco come lavoriamo ogni giorno per offrirvi il meglio.",
            "date": "2024-02-12",
            "status": "pubblicato",
            "platform": "Facebook",
            "likes": 892,
            "comments": 43
        },
        {
            "id": 3,
            "content": "Offerta speciale San Valentino ❤️ Sconto del 20% su tutti i prodotti fino al 18 febbraio!",
            "date": "2024-02-17",
            "status": "programmato",
            "platform": "Instagram",
            "likes": 0,
            "comments": 0
        },
        {
            "id": 4,
            "content": "Tutorial completo: come utilizzare al meglio la nostra app 📱 Link in bio!",
            "date": "2024-02-24",
            "status": "programmato",
            "platform": "Facebook",
            "likes": 0,
            "comments": 0
        }
    ]
#===================================
# === PAGINA HOME - Crea Post ===
#===================================
if st.session_state.page == 'Home':
    st.title("SOCIAL MANAGER")
    st.title(page_titles.get(st.session_state.page, 'Social Manager'))

    # Assistente AI da imlplementare funzione che cambia le sistem instruction
    st.markdown("### 👨‍🎨 Crea il tuo post")
    st.radio("Scegli come creare il tuo post", ["Assistente AI - Creativo", "Assistente AI - Professionale"])
    # Area di testo (prompt)
    post_content = st.text_area("Cosa vuoi generare?", height=150, 
                                placeholder="descrivimi il tuo post")
    
    # Opzioni media da implementare funzione che da sistem instruction cambia il tipo di contenuto
    #st.radio("Tipo di contenuto", ["📷 Post", "🖼️ Storia", "🎥 Reel"], horizontal=True, label_visibility="collapsed")

    
    # Bottoni crea/annulla da implementare con funzioni LLM
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("Genera Post", type="primary",width="stretch" )
    with col2:
        st.button("Annulla",width="stretch")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistiche home da passare tramite API
    st.markdown("### 📊 Quick View")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Post Totali", "n_post_totali", "n_post_totali_incremento")
    with col2:
        st.metric("Engagement", "engagement", "engagement_incremento")
    with col3:
        st.metric("Follower", "follower", "follower_incremento")
    with col4:
        st.metric("Post Schedulati", "post_schedulati", "post_schedulati_incremento")

#===================================
# === PAGINA CALENDAR ===
#===================================
elif st.session_state.page == 'Calendar':
    st.title("SOCIAL MANAGER")
    st.title(page_titles.get(st.session_state.page, '📅 Calendar'))

    now = datetime.now()
    if 'current_year' not in st.session_state:
        st.session_state.current_year = datetime.now().year
    if 'current_month' not in st.session_state:
        st.session_state.current_month = datetime.now().month

    st.radio("Mese", ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"], horizontal=True, label_visibility="collapsed")
    st.radio("Anno", ["2024", "2025", "2026", "2027", "2028", "2029", "2030"], horizontal=True, label_visibility="collapsed")
    
    
    
    


#======================================
# === PAGINA EDITOR - Gestione Post ===
#======================================

elif st.session_state.page == 'Editor':
    st.title("SOCIAL MANAGER")
    st.title(page_titles.get(st.session_state.page, '📝 Editor'))
    
    # Se c'è un post in editing
    if 'editing_post' in st.session_state:
        post_to_edit = next((p for p in st.session_state.posts if p['id'] == st.session_state.editing_post), None)
        
        if post_to_edit:
            st.info(f"📝 Modifica del post programmato per {post_to_edit['date']}")
            
            # Form di modifica
            edited_content = st.text_area("Contenuto del post", value=post_to_edit['content'], height=150)
            
            col1, col2 = st.columns(2)
            with col1:
                edited_date = st.date_input("Data pubblicazione", value=datetime.strptime(post_to_edit['date'], "%Y-%m-%d"))
            with col2:
                edited_platform = st.selectbox("Piattaforma", ["Instagram", "Facebook", "Twitter", "LinkedIn"], 
                                               index=["Instagram", "Facebook", "Twitter", "LinkedIn"].index(post_to_edit['platform']))
            
            st.markdown("---")
            
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button("💾 Salva modifiche", type="primary", use_container_width=True):
                    # Aggiorna il post
                    for post in st.session_state.posts:
                        if post['id'] == st.session_state.editing_post:
                            post['content'] = edited_content
                            post['date'] = edited_date.strftime("%Y-%m-%d")
                            post['platform'] = edited_platform
                    del st.session_state.editing_post
                    st.success("✅ Post aggiornato con successo!")
                    st.rerun()
            
            with col2:
                if st.button("❌ Annulla", use_container_width=True):
                    del st.session_state.editing_post
                    st.rerun()
    
    else:
        # Visualizza tutti i post generati
        st.markdown("### 📋 Tutti i post generati")
        
        if st.session_state.posts:
            for post in st.session_state.posts:
                status_color = "#28A745" if post["status"] == "pubblicato" else "#FFA500"
                status_text = "✅ Pubblicato" if post["status"] == "pubblicato" else "⏰ Programmato"
                
                st.markdown(f"""
                    <div style="background: white; padding: 20px; border-radius: 8px; margin-bottom: 15px; 
                                border: 1px solid #E5E9F0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <div style="color: {status_color}; font-weight: 600; font-size: 0.9rem;">
                                {status_text}
                            </div>
                            <div style="color: #6C757D; font-size: 0.85rem;">
                                📅 {post['date']} | {post['platform']}
                            </div>
                        </div>
                        <div style="font-size: 1rem; margin-bottom: 10px; color: #2E6399;">
                            {post['content']}
                        </div>
                """, unsafe_allow_html=True)
                
                if post["status"] == "pubblicato":
                    st.markdown(f"""
                        <div style="color: #6C757D; font-size: 0.9rem; padding-top: 10px; border-top: 1px solid #E5E9F0;">
                            ❤️ {post['likes']} Mi piace • 💬 {post['comments']} Commenti
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Bottoni azione
                col1, col2, col3 = st.columns([1, 1, 3])
                with col1:
                    if post["status"] == "programmato":
                        if st.button("✏️ Modifica", key=f"edit_main_{post['id']}", use_container_width=True):
                            st.session_state.editing_post = post['id']
                            st.rerun()
                with col2:
                    if st.button("🗑️ Elimina", key=f"delete_main_{post['id']}", use_container_width=True):
                        st.session_state.posts = [p for p in st.session_state.posts if p['id'] != post['id']]
                        st.rerun()
        else:
            st.info("Nessun post generato. Vai alla sezione Home per creare il tuo primo post!")
    
    st.markdown('</div>', unsafe_allow_html=True)






