import streamlit as st
import random
import time

# --- SAYFA AYARLARI (Mobil Odaklı) ---
st.set_page_config(
    page_title="Roza",
    page_icon="🦄",
    layout="centered",
    initial_sidebar_state="collapsed" # Menüyü kapalı başlat
)

# --- 🎨 ULTRA KOMPAKT MOBİL TASARIM (CSS) ---
st.markdown("""
    <style>
    /* 1. TÜM BOŞLUKLARI YOK ET */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100%;
    }
    
    /* 2. ARKA PLAN */
    .stApp {
        background-image: linear-gradient(180deg, #fff0f5 0%, #ffe4e1 100%);
    }
    
    /* 3. SORU KUTUSU (Daha küçük ve sıkı) */
    .question-box {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        border: 2px dashed #FF4B4B;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .question-text {
        color: #FF4B4B;
        font-family: 'Comic Sans MS', cursive;
        font-size: 40px; /* Mobilde ideal büyük boy */
        margin: 0;
        font-weight: bold;
    }
    
    /* 4. CEVAP BUTONLARI (Devrimsel Değişiklik!) */
    /* Streamlit butonlarını büyütüp şık haline getiriyoruz */
    .stButton button {
        width: 100%;
        height: 70px; /* Buton yüksekliği - parmakla basmak için ideal */
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        background-color: white !important;
        color: #4B0082 !important;
        border: 2px solid #9370db !important;
        margin-top: 5px !important;
        margin-bottom: 5px !important;
        box-shadow: 0 4px 0 #9370db !important; /* 3D efekti */
        transition: all 0.1s;
    }
    
    /* Basınca efekt */
    .stButton button:active {
        transform: translateY(4px);
        box-shadow: none !important;
    }

    /* 5. BAŞLIK VE MENÜ */
    [data-testid="stSidebar"] { background-color: #fff0f5; }
    h1 { font-size: 1.2rem !important; margin: 0 !important; padding: 0 !important; color: #C71585 !important; }
    
    /* Gereksiz öğeleri gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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

# --- YAN MENÜ ---
st.sidebar.title("Menü 🍭")
page = st.sidebar.radio("Oyun:", ["Çarpım Tablosu", "İngilizce", "Zıt Anlamlar"])
if st.sidebar.button("Sıfırla 🔄"):
    st.session_state.score_math = 0
    st.session_state.score_eng = 0
    st.session_state.score_zit = 0
    st.rerun()

# --- OYUN MANTIĞI VE DEĞİŞKENLER ---
if page == "Çarpım Tablosu":
    score = st.session_state.score_math
    limit = 100
    color = "#FF4B4B"
    n1, n2 = st.session_state.math_q['n1'], st.session_state.math_q['n2']
    question_text = f"{n1} x {n2} = ?"
    correct_val = n1 * n2
    
    # Şık hazırlama
    if 'math_opts' not in st.session_state:
        opts = [correct_val]
        while len(opts) < 3:
            w = random.randint(max(1, correct_val - 10), correct_val + 10)
            if w != correct_val and w not in opts: opts.append(w)
        random.shuffle(opts)
        st.session_state.math_opts = opts
    options = st.session_state.math_opts

elif page == "İngilizce":
    score = st.session_state.score_eng
    limit = 100
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
    score = st.session_state.score_zit
    limit = 100
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

# --- EKRAN TASARIMI ---

# 1. Başlık ve Puan (En Üst)
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown(f"<h3 style='margin:0; padding-top:10px; color:{color} !important;'>{page}</h3>", unsafe_allow_html=True)
with col_h2:
    st.markdown(f"<h3 style='margin:0; padding-top:10px; text-align:right;'>🏆 {score}</h3>", unsafe_allow_html=True)

# 2. İlerleme Çubuğu (İnce)
st.progress(min(score, 100) / 100)

# 3. KUTLAMA (100 Puan)
if score >= 100:
    ses_cal("kazandi")
    st.balloons()
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 20px; border-radius: 20px; text-align: center; border: 5px solid orange; margin-top: 20px;">
        <h1 style='font-size: 60px !important;'>🏆</h1>
        <h2 style='color: #d32f2f !important;'>TEBRİKLER ROZA!</h2>
        <p>Bu bölüm bitti!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif", use_container_width=True)
    if st.button("Tekrar Oyna 🔄"):
        if page == "Çarpım Tablosu": st.session_state.score_math = 0
        elif page == "İngilizce": st.session_state.score_eng = 0
        else: st.session_state.score_zit = 0
        st.rerun()
    st.stop()

# 4. SORU ALANI (Kompakt Kutu)
st.markdown(f"""
<div class="question-box" style="border-color: {color};">
    <p class="question-text" style="color: {color};">{question_text}</p>
</div>
""", unsafe_allow_html=True)

# 5. CEVAP BUTONLARI (Alt Alta 3 Büyük Buton)
# Butona tıklandığında ne olacağını yöneten fonksiyon
def check_answer(selected):
    if selected == correct_val:
        ses_cal("dogru")
        st.toast("🌟 HARİKASIN ROZA!", icon="🦄") # Ekranda küçük bildirim çıkar
        time.sleep(0.5)
        
        # Puan ve Soru Güncelleme
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

# Butonları oluştur
for opt in options:
    # Her butona tıklanınca check_answer fonksiyonu çalışır
    st.button(str(opt), on_click=check_answer, args=(opt,))

# Alt boşluğu temizle
st.write("")
