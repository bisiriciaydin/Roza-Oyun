import streamlit as st
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Roza'nın Süper Dünyası",
    page_icon="🦄",
    layout="centered" # Telefonda ortalı durması için en iyisi budur
)

# --- 🎨 ÖZEL MOBİL UYUMLU TASARIM (CSS) ---
st.markdown("""
    <style>
    /* 1. EKRAN BOŞLUKLARINI YOK ETME (EN ÖNEMLİ KISIM) */
    .block-container {
        padding-top: 1rem !important; /* Üst boşluğu azalttık */
        padding-bottom: 0rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    /* 2. ARKA PLAN */
    .stApp {
        background-image: linear-gradient(to top, #dfe9f3 0%, white 100%);
    }
    
    /* 3. YAN MENÜ */
    [data-testid="stSidebar"] {
        background-color: #fff0f5;
        border-right: 5px solid #ff69b4;
    }
    
    /* 4. BAŞLIKLAR (Telefona sığması için biraz küçülttük) */
    h1 {
        color: #C71585 !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        text-shadow: 1px 1px white;
        font-size: 2.5rem !important; /* Mobilde taşmasın diye boyut ayarı */
    }
    h2, h3 {
        color: #6A1B9A !important;
        text-align: center;
        font-size: 1.5rem !important;
    }
    p {
        color: #333333 !important;
        font-size: 1.1rem !important;
    }

    /* 5. İLERLEME ÇUBUĞU */
    .stProgress > div > div > div > div {
        background-color: #00CC66;
        height: 15px; /* Biraz incelttik */
        border-radius: 10px;
    }
    
    /* 6. BUTONLAR (Daha kompakt) */
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 15px;
        font-size: 18px;
        padding: 8px 10px;
        border: 2px solid white;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        width: 100%;
        margin-top: 10px;
    }
    
    /* 7. ŞIKLAR (KUTULAR) - DAHA AZ YER KAPLASIN */
    .stRadio div[role='radiogroup'] > label {
        background-color: rgba(255,255,255,0.95) !important;
        padding: 10px !important; /* Boşluğu azalttık */
        border-radius: 12px !important;
        margin-bottom: 6px !important; /* Aralarındaki mesafeyi azalttık */
        border: 2px solid #ddd !important;
        display: block !important;
        cursor: pointer !important;
    }
    
    /* Şıkların yazı rengi */
    .stRadio div[role='radiogroup'] label p {
        font-size: 20px !important; /* Mobilde çok büyük olmasın */
        font-weight: bold !important;
        color: #4B0082 !important;
    }
    
    /* Seçilen şık */
    .stRadio div[role='radiogroup'] > label:hover {
        background-color: #e6e6fa !important;
        border-color: #9370db !important;
    }
    
    /* Streamlit'in kendi menüsünü (Hamburger) gizleyelim, yer açılsın */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SES ÇALMA FONKSİYONU 🔊 ---
def ses_cal(durum):
    if durum == "kazandi":
        sound_url = "https://www.soundjay.com/human/sounds/applause-2.mp3"
    elif durum == "dogru":
        sound_url = "https://www.soundjay.com/human/sounds/applause-01.mp3"
    else:
        sound_url = "https://www.soundjay.com/misc/sounds/fail-buzzer-01.mp3"
    
    audio_code = f"""
        <audio autoplay="true">
            <source src="{sound_url}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_code, unsafe_allow_html=True)

# --- HAFIZA (SESSION STATE) ---
if 'score_math' not in st.session_state: st.session_state.score_math = 0
if 'score_eng' not in st.session_state: st.session_state.score_eng = 0
if 'score_zit' not in st.session_state: st.session_state.score_zit = 0
if 'math_q' not in st.session_state:
    st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
if 'eng_index' not in st.session_state:
    st.session_state.eng_index = 0
if 'zit_soru' not in st.session_state:
    st.session_state.zit_soru = ""

# --- YAN MENÜ ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/477/477163.png", width=100)
st.sidebar.title("Menü 🍭")
st.sidebar.info("Hadi Roza!") 
page = st.sidebar.radio("Oyun Seç:", ["🧮 Çarpım Canavarı", "🇬🇧 İngilizce Kartları", "🌗 Zıt Anlamlar"])

# Puan Mantığı
if page == "🧮 Çarpım Canavarı":
    current_score = st.session_state.score_math
    score_key = 'score_math'
    game_name = "Çarpım Tablosu"
elif page == "🇬🇧 İngilizce Kartları":
    current_score = st.session_state.score_eng
    score_key = 'score_eng'
    game_name = "İngilizce"
else: 
    current_score = st.session_state.score_zit
    score_key = 'score_zit'
    game_name = "Zıt Anlamlar"

st.sidebar.write("---")
st.sidebar.markdown(f"### 🏆 {game_name}: **{current_score}**")

if st.sidebar.button("Sıfırla 🔄"):
    st.session_state.score_math = 0
    st.session_state.score_eng = 0
    st.session_state.score_zit = 0
    st.rerun()

# İlerleme Çubuğu
progress_val = min(current_score, 100) 
st.write(f"**Hedef: %{progress_val}**")
st.progress(progress_val / 100)

# ========================================================
# 🏆 100 PUAN KUTLAMASI
# ========================================================
if current_score >= 100:
    ses_cal("kazandi")
    st.balloons()
    st.snow()
    
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 20px; border-radius: 20px; text-align: center; border: 5px solid orange;">
        <h1 style='font-size: 50px !important;'>🏆</h1>
        <h1 style='color: #d32f2f !important; font-size: 30px !important;'>TEBRİKLER ROZA!</h1>
        <h2 style='color: #333 !important; font-size: 20px !important;'>{game_name} BÖLÜMÜNÜ BİTİRDİN! 🌟</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif", use_container_width=True)
    
    st.write("")
    if st.button(f"{game_name} Tekrar Oyna 🔄"):
        st.session_state[score_key] = 0
        st.rerun()
    st.stop()

# ========================================================
# 1. OYUN: ÇARPIM CANAVARI
# ========================================================
if page == "🧮 Çarpım Canavarı":
    st.title("🧮 Çarpım Canavarı") 

    n1 = st.session_state.math_q['n1']
    n2 = st.session_state.math_q['n2']
    correct_answer = n1 * n2

    st.markdown(f"""
    <div style="background-color: white; padding: 10px; border-radius: 15px; border: 3px dashed #FF4B4B; text-align:center; margin-bottom: 10px;">
        <h1 style='color: #FF4B4B !important; font-size: 40px !important; margin:0;'>{n1} x {n2} = ?</h1>
    </div>
    """, unsafe_allow_html=True)

    if 'math_options' not in st.session_state:
        opts = [correct_answer]
        while len(opts) < 3:
            wrong = random.randint(max(1, correct_answer - 10), correct_answer + 10)
            if wrong != correct_answer and wrong not in opts:
                opts.append(wrong)
        random.shuffle(opts)
        st.session_state.math_options = opts

    user_ans = st.radio("", st.session_state.math_options, index=None, key="math_radio")

    if st.button("Kontrol Et ✅", key="btn_math"):
        if user_ans is None:
            st.warning("Seçim yapmalısın!")
        elif user_ans == correct_answer:
            ses_cal("dogru")
            st.markdown("<h2 style='color: #28a745 !important;'>🌟 AFERİN ROZA! 🌟</h2>", unsafe_allow_html=True)
            st.session_state.score_math += 10
            time.sleep(1.0)
            st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
            if 'math_options' in st.session_state: del st.session_state.math_options
            st.rerun()
        else:
            ses_cal("yanlis")
            st.markdown("<h2 style='color: #FF4B4B !important;'>🐢 Yapma Roza!! 🐢</h2>", unsafe_allow_html=True)

# ========================================================
# 2. OYUN: İNGİLİZCE KARTLARI
# ========================================================
elif page == "🇬🇧 İngilizce Kartları":
    st.title("🇬🇧 İngilizce Kartları")

    words = [
        {"eng": "Cat 🐱", "tr": "Kedi"}, {"eng": "Dog 🐶", "tr": "Köpek"},
        {"eng": "Apple 🍎", "tr": "Elma"}, {"eng": "School 🏫", "tr": "Okul"},
        {"eng": "Pencil ✏️", "tr": "Kalem"}, {"eng": "Red 🔴", "tr": "Kırmızı"},
        {"eng": "Blue 🔵", "tr": "Mavi"}, {"eng": "Sun ☀️", "tr": "Güneş"},
        {"eng": "Moon 🌙", "tr": "Ay"}, {"eng": "Book 📖", "tr": "Kitap"},
        {"eng": "Bird 🐦", "tr": "Kuş"}, {"eng": "Fish 🐟", "tr": "Balık"},
        {"eng": "Mouse 🐭", "tr": "Fare"}, {"eng": "Horse 🐴", "tr": "At"},
        {"eng": "Cow 🐮", "tr": "İnek"}, {"eng": "Lion 🦁", "tr": "Aslan"},
        {"eng": "Yellow 🟡", "tr": "Sarı"}, {"eng": "Green 🟢", "tr": "Yeşil"},
        {"eng": "Black ⚫", "tr": "Siyah"}, {"eng": "White ⚪", "tr": "Beyaz"},
        {"eng": "Mother 👩", "tr": "Anne"}, {"eng": "Father 👨", "tr": "Baba"},
        {"eng": "Car 🚗", "tr": "Araba"}, {"eng": "Bus 🚌", "tr": "Otobüs"},
        {"eng": "House 🏠", "tr": "Ev"}, {"eng": "Milk 🥛", "tr": "Süt"},
        {"eng": "Water 💧", "tr": "Su"}, {"eng": "Banana 🍌", "tr": "Muz"},
        {"eng": "Flower 🌸", "tr": "Çiçek"}, {"eng": "Happy 😄", "tr": "Mutlu"}
    ]

    if st.session_state.eng_index >= len(words):
        st.session_state.eng_index = 0
        random.shuffle(words)
    
    current_word = words[st.session_state.eng_index]
    correct_
