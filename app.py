import streamlit as st
import utils
# Oyunlarımızı klasörden çağırıyoruz
from games import matematik, ingilizce, zit_anlam

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Roza",
    page_icon="🦄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Tasarımı ve Sesleri Yükle (Utils dosyasından)
utils.css_yukle()

# --- YAN MENÜ ---
st.sidebar.title("Menü 🍭")
page = st.sidebar.radio("Oyun Seç:", ["Çarpım Tablosu", "İngilizce", "Zıt Anlamlar"])

# Puan Sıfırlama Butonu
if st.sidebar.button("Puanları Sıfırla 🔄"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- SAYFA YÖNLENDİRME ---
# Seçilen oyuna göre ilgili dosyayı çalıştır
if page == "Çarpım Tablosu":
    matematik.app()
    current_score = st.session_state.get('score_math', 0)
elif page == "İngilizce":
    ingilizce.app()
    current_score = st.session_state.get('score_eng', 0)
else:
    zit_anlam.app()
    current_score = st.session_state.get('score_zit', 0)

# --- ALT BİLGİ VE KUTLAMA (Tüm oyunlar için ortak) ---
st.write("---")
st.progress(min(current_score, 100) / 100)
st.markdown(f"<h3 style='text-align:center;'>🏆 Puan: {current_score}</h3>", unsafe_allow_html=True)

if current_score >= 100:
    utils.ses_cal("kazandi")
    st.balloons()
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 20px; border-radius: 20px; text-align: center; border: 5px solid orange; margin-top: 20px;">
        <h1 style='font-size: 60px !important;'>🏆</h1>
        <h2 style='color: #d32f2f !important;'>TEBRİKLER ROZA!</h2>
        <p style='color: black !important;'>Bölümü Bitirdin!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif", use_container_width=True)
