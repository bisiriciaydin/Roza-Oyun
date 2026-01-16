import streamlit as st
import random
import time
import utils

def app():
    st.title("🇬🇧 İngilizce")

    if 'score_eng' not in st.session_state: st.session_state.score_eng = 0
    if 'eng_index' not in st.session_state: st.session_state.eng_index = 0

    words = [
        {"eng": "Cat 🐱", "tr": "Kedi"}, {"eng": "Dog 🐶", "tr": "Köpek"},
        {"eng": "Apple 🍎", "tr": "Elma"}, {"eng": "School 🏫", "tr": "Okul"},
        {"eng": "Red 🔴", "tr": "Kırmızı"}, {"eng": "Blue 🔵", "tr": "Mavi"},
        {"eng": "Sun ☀️", "tr": "Güneş"}, {"eng": "Moon 🌙", "tr": "Ay"},
        {"eng": "Bird 🐦", "tr": "Kuş"}, {"eng": "Fish 🐟", "tr": "Balık"},
        {"eng": "Car 🚗", "tr": "Araba"}, {"eng": "Mother 👩", "tr": "Anne"}
    ]
    
    if st.session_state.eng_index >= len(words): st.session_state.eng_index = 0
    q_data = words[st.session_state.eng_index]
    correct_val = q_data['tr']

    if 'eng_opts' not in st.session_state:
        opts = [correct_val]
        all_tr = [w['tr'] for w in words]
        while len(opts) < 3:
            w = random.choice(all_tr)
            if w != correct_val and w not in opts: opts.append(w)
        random.shuffle(opts)
        st.session_state.eng_opts = opts
    options = st.session_state.eng_opts

    st.markdown(f"""
    <div class="question-box" style="border-color: #0097A7;">
        <h3 style='margin:0;'>Bu ne demek?</h3>
        <h1 style="color: #0097A7 !important; font-size: 40px !important; margin: 0;">{q_data['eng']}</h1>
    </div>
    """, unsafe_allow_html=True)

    def check(selected):
        if selected == correct_val:
            utils.ses_cal("dogru")
            st.toast("🌟 HARİKASIN!", icon="🦄")
            st.session_state.score_eng += 10
            time.sleep(0.5)
            st.session_state.eng_index += 1
            del st.session_state.eng_opts
            st.rerun()
        else:
            utils.ses_cal("yanlis")
            st.toast("🐢 Tekrar dene!", icon="🐢")

    for opt in options:
        st.button(str(opt), on_click=check, args=(opt,), use_container_width=True)
