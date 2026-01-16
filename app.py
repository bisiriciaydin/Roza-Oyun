import streamlit as st
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Roza'nın Süper Dünyası",
    page_icon="🦄",
    layout="centered"
)

# --- 🎨 ÖZEL TASARIM (TELEFON İÇİN GÜÇLENDİRİLMİŞ CSS) ---
st.markdown("""
    <style>
    /* Arka plan */
    .stApp {
        background-image: linear-gradient(to top, #dfe9f3 0%, white 100%);
    }
    
    /* Yan menü */
    [data-testid="stSidebar"] {
        background-color: #fff0f5;
        border-right: 5px solid #ff69b4;
    }
    
    /* BAŞLIKLARI ZORLA RENKLİ YAP (Görünmeme sorununu çözer) */
    h1 {
        color: #C71585 !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        text-shadow: 2px 2px white;
    }
    h2, h3 {
        color: #6A1B9A !important;
        text-align: center;
    }
    p {
        color: #333333 !important;
    }

    /* İlerleme çubuğu */
    .stProgress > div > div > div > div {
        background-color: #00CC66;
        height: 20px;
        border-radius: 10px;
    }
    
    /* Buton tasarımı */
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 20px;
        font-size: 20px;
        padding: 10px 24px;
        border: 2px solid white;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: 0.3s;
        width: 100%;
    }
    
    /* --- RADYO BUTONLARI (TELEFON İÇİN DÜZELTME) --- */
    /* Kutunun kendisi */
    .stRadio div[role='radiogroup'] > label {
        background-color: rgba(255,255,255,0.95) !important; /* Arka planı daha opak yaptık */
        padding: 15px !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        border: 2px solid #ddd !important;
        display: block !important;
        cursor: pointer !important;
    }
    
    /* Şıkların yazı rengini ZORLA KOYU YAP */
    .stRadio div[role='radiogroup'] label p {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #4B0082 !important;
    }
    
    /* Seçilen şıkkın kenarını renklendir */
    .stRadio div[role='radiogroup'] > label:hover {
        background-color: #e6e6fa !important;
        border-color: #9370db !important;
    }
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
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/477/477163.png", width=120)
st.sidebar.title("Menü 🍭")
st.sidebar.info("Hadi Roza, Her Bölümü Tamamla!") 
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
st.sidebar.write("Hedef: 100 Puan! 🎯")

if st.sidebar.button("Tüm Puanları Sıfırla 🔄"):
    st.session_state.score_math = 0
    st.session_state.score_eng = 0
    st.session_state.score_zit = 0
    st.rerun()

# İlerleme Çubuğu
progress_val = min(current_score, 100) 
st.write(f"**{game_name} Hedefi: %{progress_val}**")
st.progress(progress_val / 100)

# ========================================================
# 🏆 100 PUAN KUTLAMASI
# ========================================================
if current_score >= 100:
    ses_cal("kazandi")
    st.balloons()
    st.snow()
    
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 30px; border-radius: 20px; text-align: center; border: 5px solid orange;">
        <h1 style='font-size: 80px;'>🏆</h1>
        <h1 style='color: #d32f2f; font-size: 40px !important;'>TEBRİKLER ROZA!</h1>
        <h2 style='color: #333 !important;'>{game_name} BÖLÜMÜNÜ BİTİRDİN! 🌟</h2>
        <p style='font-size: 20px; color: black !important;'>Harikasın! Şimdi menüden başka bir oyuna geçebilirsin.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/l4JySAWfMaY7w88sU/giphy.gif", use_container_width=True)
    
    st.write("")
    if st.button(f"{game_name} Puanını Sıfırla ve Oyna 🔄"):
        st.session_state[score_key] = 0
        st.rerun()
    st.stop()

# ========================================================
# 1. OYUN: ÇARPIM CANAVARI
# ========================================================
if page == "🧮 Çarpım Canavarı":
    st.title("🧮 Çarpım Canavarı") 
    st.markdown("<h3 style='text-align: center;'>Soruyu bil, çubuğu doldur! 🚀</h3>", unsafe_allow_html=True)

    n1 = st.session_state.math_q['n1']
    n2 = st.session_state.math_q['n2']
    correct_answer = n1 * n2

    st.markdown(f"""
    <div style="background-color: white; padding: 15px; border-radius: 20px; border: 3px dashed #FF4B4B; text-align:center;">
        <h1 style='color: #FF4B4B !important; font-size: 50px; margin:0;'>{n1} x {n2} = ?</h1>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    if 'math_options' not in st.session_state:
        opts = [correct_answer]
        while len(opts) < 3:
            wrong = random.randint(max(1, correct_answer - 10), correct_answer + 10)
            if wrong != correct_answer and wrong not in opts:
                opts.append(wrong)
        random.shuffle(opts)
        st.session_state.math_options = opts

    user_ans = st.radio("", st.session_state.math_options, index=None, key="math_radio")

    st.write("")
    if st.button("Kontrol Et ✅", key="btn_math"):
        if user_ans is None:
            st.warning("Lütfen bir şık seç Roza! 👆")
        elif user_ans == correct_answer:
            ses_cal("dogru")
            st.markdown("<h1 style='text-align: center; color: #28a745 !important; font-size: 35px;'>🌟 HARİKASIN KIZIM ROZA! 🌟</h1>", unsafe_allow_html=True)
            st.session_state.score_math += 10
            time.sleep(1.5)
            st.session_state.math_q = {'n1': random.randint(1, 10), 'n2': random.randint(1, 10)}
            if 'math_options' in st.session_state: del st.session_state.math_options
            st.rerun()
        else:
            ses_cal("yanlis")
            st.markdown("<h1 style='text-align: center; color: #FF4B4B !important; font-size: 35px;'>🐢 Yapma Roza!! 🐢</h1>", unsafe_allow_html=True)

# ========================================================
# 2. OYUN: İNGİLİZCE KARTLARI
# ========================================================
elif page == "🇬🇧 İngilizce Kartları":
    st.title("🇬🇧 İngilizce Kartları")
    st.markdown("<h3 style='text-align: center;'>Kelimeleri öğren, kupayı kazan! 🏆</h3>", unsafe_allow_html=True)

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
    correct_tr = current_word['tr']

    st.markdown(f"""
    <div style="background-color: #E0F7FA; padding: 15px; border-radius: 20px; border: 3px solid #00BCD4; text-align:center;">
        <h3 style='color: #006064 !important; margin:0;'>Bu kelime ne demek?</h3>
        <h1 style='color: #0097A7 !important; font-size: 50px; margin-top:5px;'>{current_word['eng']}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    if 'eng_options' not in st.session_state:
        opts = [correct_tr]
        tum_turkce = [w['tr'] for w in words]
        while len(opts) < 3:
            yanlis = random.choice(tum_turkce)
            if yanlis != correct_tr and yanlis not in opts:
                opts.append(yanlis)
        random.shuffle(opts)
        st.session_state.eng_options = opts

    cevap = st.radio("", st.session_state.eng_options, index=None, key="eng_radio")

    st.write("")
    if st.button("Cevabı Gönder 🚀", key="btn_eng"):
        if cevap is None:
            st.warning("Bir cevap seçmelisin! 👆")
        elif cevap == correct_tr:
            ses_cal("dogru")
            st.markdown("<h1 style='text-align: center; color: #28a745 !important; font-size: 35px;'>🌟 HARİKASIN KIZIM ROZA! 🌟</h1>", unsafe_allow_html=True)
            st.session_state.score_eng += 10
            time.sleep(1.5)
            st.session_state.eng_index += 1
            if 'eng_options' in st.session_state: del st.session_state.eng_options
            st.rerun()
        else:
            ses_cal("yanlis")
            st.markdown("<h1 style='text-align: center; color: #FF4B4B !important; font-size: 35px;'>🐢 Yapma Roza!! 🐢</h1>", unsafe_allow_html=True)

# ========================================================
# 3. OYUN: ZIT ANLAMLAR
# ========================================================
elif page == "🌗 Zıt Anlamlar":
    st.title("🌗 Zıt Anlamlar")
    st.markdown("<h3 style='text-align: center;'>Tersini bul, hedefi 12'den vur! 🎯</h3>", unsafe_allow_html=True)

    zit_words = {
        "SİYAH ⚫": "BEYAZ", "UZUN 🦒": "KISA", "ZENGİN 💰": "FAKİR",
        "ACI 🌶️": "TATLI", "BÜYÜK 🐘": "KÜÇÜK", "AĞIR 🏋️": "HAFİF",
        "GECE 🌑": "GÜNDÜZ", "SICAK 🔥": "SOĞUK", "YAVAŞ 🐢": "HIZLI",
        "GÜZEL 🌸": "ÇİRKİN", "VAR ✅": "YOK", "AÇIK 🔓": "KAPALI",
        "TEMİZ ✨": "KİRLİ", "GENÇ 👶": "YAŞLI", "DOLU 🥛": "BOŞ",
        "İNCE 🧵": "KALIN", "ÖN ⏩": "ARKA", "İÇERİ 🏠": "DIŞARI",
        "YENİ ✨": "ESKİ", "SERT 🪨": "YUMUŞAK", "KOLAY 👍": "ZOR",
        "SABAH ☀️": "AKŞAM", "YAZ 🏖️": "KIŞ", "DOĞRU ✅": "YANLIŞ",
        "İYİ 😇": "KÖTÜ", "ISLAK 💧": "KURU", "YUKARI ⬆️": "AŞAĞI",
        "SAĞ ➡️": "SOL", "GÜLMEK 😂": "AĞLAMAK"
    }

    if st.session_state.zit_soru == "" or st.session_state.zit_soru not in zit_words:
        st.session_state.zit_soru = random.choice(list(zit_words.keys()))

    soru = st.session_state.zit_soru
    dogru_cevap = zit_words[soru]

    st.markdown(f"""
    <div style="background-color: #F3E5F5; padding: 15px; border-radius: 20px; border: 3px solid #9C27B0; text-align:center;">
        <h3 style='color: #6A1B9A !important; margin:0;'>Bu kelimenin zıttı nedir?</h3>
        <h1 style='color: #8E24AA !important; font-size: 50px; margin-top:5px;'>{soru}</h1>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    if 'zit_options' not in st.session_state:
        opts = [dogru_cevap]
        tum_cevaplar = list(zit_words.values())
        while len(opts) < 3:
            yanlis = random.choice(tum_cevaplar)
            if yanlis != dogru_cevap and yanlis not in opts:
                opts.append(yanlis)
        random.shuffle(opts)
        st.session_state.zit_options = opts

    cevap_zit = st.radio("", st.session_state.zit_options, index=None, key="zit_radio")

    st.write("")
    if st.button("Kontrol Et 🎯", key="btn_zit"):
        if cevap_zit is None:
            st.warning("Lütfen bir şık işaretle! 👆")
        elif cevap_zit == dogru_cevap:
            ses_cal("dogru")
            st.markdown("<h1 style='text-align: center; color: #28a745 !important; font-size: 35px;'>🌟 HARİKASIN KIZIM ROZA! 🌟</h1>", unsafe_allow_html=True)
            st.session_state.score_zit += 10
            time.sleep(1.5)
            st.session_state.zit_soru = random.choice(list(zit_words.keys()))
            if 'zit_options' in st.session_state: del st.session_state.zit_options
            st.rerun()
        else:
            ses_cal("yanlis")
            st.markdown("<h1 style='text-align: center; color: #FF4B4B !important; font-size: 35px;'>🐢 Yapma Roza!! 🐢</h1>", unsafe_allow_html=True)
