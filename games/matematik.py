import streamlit as st
import random
import time
import utils  # Alet çantamızı çağırıyoruz

def app():
    st.title("🧮 Çarpım Tablosu")
    
    # Hafıza Ayarları
    if 'score_math' not in st.session_state: st.session_state.score_math = 0
    if 'math_q' not in st.session_state: st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}

    current_score = st.session_state.score_math
    n1, n2 = st.session_state.math_q['n1'], st.session_state.math_q['n2']
    correct_val = n1 * n2
    
    # Şık Hazırlama
    if 'math_opts' not in st.session_state:
        opts = [correct_val]
        while len(opts) < 3:
            w = random.randint(max(1, correct_val - 10), correct_val + 10)
            if w != correct_val and w not in opts: opts.append(w)
        random.shuffle(opts)
        st.session_state.math_opts = opts
    options = st.session_state.math_opts

    # Soru Gösterimi
    st.markdown(f"""
    <div class="question-box" style="border-color: #FF4B4B;">
        <h1 style="color: #FF4B4B !important; font-size: 40px !important; margin: 0;">{n1} x {n2} = ?</h1>
    </div>
    """, unsafe_allow_html=True)

    # Buton Kontrolü
    def check(selected):
        if selected == correct_val:
            utils.ses_cal("dogru")
            st.toast("🌟 HARİKASIN!", icon="🦄")
            st.session_state.score_math += 10
            time.sleep(0.5)
            st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
            del st.session_state.math_opts
            st.rerun()
        else:
            utils.ses_cal("yanlis")
            st.toast("🐢 Tekrar dene!", icon="🐢")

    for opt in options:
        st.button(str(opt), on_click=check, args=(opt,), use_container_width=True)
