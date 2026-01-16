import streamlit as st
import random
import time
import utils

def app():
    st.title("🌗 Zıt Anlamlar")

    if 'score_zit' not in st.session_state: st.session_state.score_zit = 0
    if 'zit_soru' not in st.session_state: st.session_state.zit_soru = ""

    zit_words = {
        "SİYAH ⚫": "BEYAZ", "UZUN 🦒": "KISA", "ZENGİN 💰": "FAKİR", "ACI 🌶️": "TATLI",
        "BÜYÜK 🐘": "KÜÇÜK", "GECE 🌑": "GÜNDÜZ", "SICAK 🔥": "SOĞUK", "GÜZEL 🌸": "ÇİRKİN",
        "VAR ✅": "YOK", "AÇIK 🔓": "KAPALI", "TEMİZ ✨": "KİRLİ", "HIZLI 🐇": "YAVAŞ"
    }

    if st.session_state.zit_soru == "": 
        st.session_state.zit_soru = random.choice(list(zit_words.keys()))
    
    q_text = st.session_state.zit_soru
    correct_val = zit_words[q_text]

    if 'zit_opts' not in st.session_state:
        opts = [correct_val]
        all_vals = list(zit_words.values())
        while len(opts) < 3:
            w = random.choice(all_vals)
            if w != correct_val and w not in opts: opts.append(w)
        random.shuffle(opts)
        st.session_state.zit_opts = opts
    options = st.session_state.zit_opts

    st.markdown(f"""
    <div class="question-box" style="border-color: #8E24AA;">
        <h3 style='margin:0;'>Zıttı nedir?</h3>
        <h1 style="color: #8E24AA !important; font-size: 40px !important; margin: 0;">{q_text}</h1>
    </div>
    """, unsafe_allow_html=True)

    def check(selected):
        if selected == correct_val:
            utils.ses_cal("dogru")
            st.toast("🌟 HARİKASIN!", icon="🦄")
            st.session_state.score_zit += 10
            time.sleep(0.5)
            st.session_state.zit_soru = random.choice(list(zit_words.keys()))
            del st.session_state.zit_opts
            st.rerun()
        else:
            utils.ses_cal("yanlis")
            st.toast("🐢 Tekrar dene!", icon="🐢")

    for opt in options:
        st.button(str(opt), on_click=check, args=(opt,), use_container_width=True)
