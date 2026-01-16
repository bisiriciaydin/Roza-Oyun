import streamlit as st
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Roza",
    page_icon="🦄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- TASARIM VE RENK AYARLARI (CSS) ---
st.markdown("""
    <style>
    /* 1. Arka Planı Ayarla */
    .stApp {
        background-color: #ffe4e1;
        background-image: linear-gradient(180deg, #fff0f5 0%, #ffe4e1 100%);
    }

    /* 2. Yazı Renklerini ZORLA SİYAH/KOYU YAP (Görünmeme sorununu çözer) */
    h1, h2, h3, h4, p, span, div, label {
        color: #333333 !important;
    }
    
    /* 3. Yan Menü */
    [data-testid="stSidebar"] {
        background-color: #fff0f5;
        border-right: 3px solid #ff69b4;
    }
    [data-testid="stSidebar"] * {
        color: #333333 !important;
    }

    /* 4. Buton Tasarımı (Daha sade ve şık) */
    .stButton button {
        background-color: white !important;
        border: 2px solid #FF4B4B !important;
        color: #FF4B4B !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 15px !important;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    .stButton button:active {
        background-color: #FF4B4B !important;
        color: white !important;
        transform: scale(0.98);
    }
    
    /* 5. Soru Kutusu */
    .question-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 3px dashed #FF4B4B;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Gereksiz boşlukları sil */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SES ÇALMA ---
def ses_cal(durum):
    if durum == "kazandi":
        sound_url = "https://www.soundjay.com/human/sounds/applause-2.mp3"
    elif durum == "dogru":
        sound_url = "https://www.soundjay.com/human/sounds/applause-01.mp3"
    else:
        sound_url = "https://www.soundjay.com/misc/sounds/fail-buzzer-01.mp3"
    st.markdown(f"""<audio autoplay="true"><source src="{sound_url}" type="audio/mp3"></audio>""", unsafe_allow_html=True)

# --- HAFIZA ---
if 'score_math' not in st.session_state: st.session_state.score_math = 0
if 'score_eng' not in st.session_state: st.session_state.score_eng = 0
if 'score_zit' not in st.session_state: st.session_state.score_zit = 0

if 'math_q' not in st.session_state: st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
if 'eng_index' not in st.session_state: st.session_state.eng_index = 0
if 'zit_soru' not in st.session_state: st.session_state.zit_soru = ""

# --- MENÜ ---
st.sidebar.title("Menü 🍭")
page = st.sidebar.radio("Oyun Seç:", ["Çarpım Tablosu", "İngilizce", "Zıt Anlamlar"])
if st.sidebar.button("Puanları Sıfırla 🔄"):
    st.session_state.score_math = 0
    st.session_state.score_eng = 0
    st.session_state.score_zit = 0
    st.rerun()

# --- OYUN AYARLARI ---
if page == "Çarpım Tablosu":
    current_score = st.session_state.score_math
    color = "#FF4B4B"
    n1, n2 = st.session_state.math_q['n1'], st.session_state.math_q['n2']
    question_text = f"{n1} x {n2} = ?"
    correct_val = n1 * n2
    
    if 'math_opts' not in st.session_state:
        opts = [correct_val]
        while len(opts) < 3:
            w = random.randint(max(1, correct_val - 10), correct_val + 10)
            if w != correct_val and w not in opts: opts.append(w)
        random.shuffle(opts)
        st.session_state.math_opts = opts
    options = st.session_state.math_opts

elif page == "İngilizce":
    current_score = st.session_state.score_eng
    color = "#0097A7"
    words = [
        {"eng": "Cat 🐱", "tr": "Kedi"}, {"eng": "Dog 🐶", "tr": "Köpek"},
        {"eng": "Apple 🍎", "tr": "Elma"}, {"eng": "School 🏫", "tr": "Okul"},
        {"eng": "Pencil ✏️", "tr": "Kalem"}, {"eng": "Red 🔴", "tr": "Kırmızı"},
        {"eng": "Blue 🔵", "tr": "Mavi"}, {"eng": "Sun ☀️", "tr": "Güneş"},
        {"eng": "Moon 🌙", "tr": "Ay"}, {"eng": "Book 📖", "tr": "Kitap"},
        {"eng": "Bird 🐦", "tr": "Kuş"}, {"eng": "Fish 🐟", "tr": "Balık"},
        {"eng": "Car 🚗", "tr": "Araba"}, {"eng": "Mother 👩", "tr": "Anne"}
    ]
    if st.session_state.eng_index >= len(words): st.session_state.eng_index = 0
    q_data = words[st.session_state.eng_index]
    question_text = q_data['eng']
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

else: # Zıt Anlamlar
    current_score = st.session_state.score_zit
    color = "#8E24AA"
    zit_words = {
        "SİYAH ⚫": "BEYAZ", "UZUN 🦒": "KISA", "ZENGİN 💰": "FAKİR", "ACI 🌶️": "TATLI",
        "BÜYÜK 🐘": "KÜÇÜK", "GECE 🌑": "GÜNDÜZ", "SICAK 🔥": "SOĞUK", "GÜZEL 🌸": "ÇİRKİN",
        "VAR ✅": "YOK", "AÇIK 🔓": "KAPALI", "TEMİZ ✨": "KİRLİ", "HIZLI 🐇": "YAVAŞ"
    }
    if st.session_state.zit_soru == "": st.session_state.zit_soru = random.choice(list(zit_words.keys()))
    q_text = st.session_state.zit_soru
    question_text = q_text
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

# --- EKRAN YERLEŞİMİ ---

# 1. Başlık ve Puan (Üst Taraf)
c1, c2 = st.columns([7, 3])
with c1:
    st.markdown(f"<h3 style='margin:0; color:{color} !important;'>{page}</h3>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<h3 style='margin:0; text-align:right; color:#FFD700 !important;'>🏆 {current_score}</h3>", unsafe_allow_html=True)

# 2. İlerleme Çubuğu
st.progress(min(current_score, 100) / 100)

# 3. KUTLAMA (100 Puan)
if current_score >= 100:
    ses_cal("kazandi")
    st.balloons()
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 20px; border-radius: 20px; text-align: center; border: 5px solid orange; margin-top: 20px;">
        <h1 style='font-size: 60px !important;'>🏆</h1>
        <h2 style='color: #d32f2f !important;'>TEBRİKLER ROZA!</h2>
        <p style='color: black !important;'>Bu bölüm bitti!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif", use_container_width=True)
    if st.button("Tekrar Oyna 🔄", use_container_width=True):
        if page == "Çarpım Tablosu": st.session_state.score_math = 0
        elif page == "İngilizce": st.session_state.score_eng = 0
        else: st.session_state.score_zit = 0
        st.rerun()
    st.stop()

# 4. SORU ALANI
st.markdown(f"""
<div class="question-box" style="border-color: {color};">
    <h1 style="color: {color} !important; font-size: 40px !important; margin: 0;">{question_text}</h1>
</div>
""", unsafe_allow_html=True)

# 5. CEVAP BUTONLARI (Alt alta 3 tane)
def check_answer(selected):
    if selected == correct_val:
        ses_cal("dogru")
        st.toast("🌟 HARİKASIN ROZA!", icon="🦄")
        time.sleep(0.5)
        
        if page == "Çarpım Tablosu":
            st.session_state.score_math += 10
            st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
            del st.session_state.math_opts
        elif page == "İngilizce":
            st.session_state.score_eng += 10
            st.session_state.eng_index += 1
            del st.session_state.eng_opts
        else:
            st.session_state.score_zit += 10
            st.session_state.zit_soru = random.choice(list(zit_words.keys()))
            del st.session_state.zit_opts
        st.rerun()
    else:
        ses_cal("yanlis")
        st.toast("🐢 Tekrar dene Roza!", icon="🐢")

# BUTONLARI OLUŞTUR
# use_container_width=True sayesinde butonlar otomatik olarak ekran genişliğine yayılır.
for opt in options:
    st.button(str(opt), on_click=check_answer, args=(opt,), use_container_width=True)
    st.write("") # Butonlar arasına çok az boşluk
