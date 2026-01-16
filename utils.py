import streamlit as st

# --- SES ÇALMA FONKSİYONU ---
def ses_cal(durum):
    """
    Ses dosyalarını oynatır.
    durum: 'kazandi', 'dogru' veya 'yanlis'
    """
    if durum == "kazandi":
        sound_url = "https://www.soundjay.com/human/sounds/applause-2.mp3"
    elif durum == "dogru":
        sound_url = "https://www.soundjay.com/human/sounds/applause-01.mp3"
    else:
        sound_url = "https://www.soundjay.com/misc/sounds/fail-buzzer-01.mp3"
    
    st.markdown(f"""<audio autoplay="true"><source src="{sound_url}" type="audio/mp3"></audio>""", unsafe_allow_html=True)

# --- CSS TASARIMI YÜKLEME ---
def css_yukle():
    st.markdown("""
        <style>
        .stApp {
            background-color: #ffe4e1;
            background-image: linear-gradient(180deg, #fff0f5 0%, #ffe4e1 100%);
        }
        h1, h2, h3, h4, p, span, div, label {
            color: #333333 !important;
        }
        [data-testid="stSidebar"] {
            background-color: #fff0f5;
            border-right: 3px solid #ff69b4;
        }
        [data-testid="stSidebar"] * {
            color: #333333 !important;
        }
        .stButton button {
            background-color: white !important;
            border: 2px solid #FF4B4B !important;
            color: #FF4B4B !important;
            font-size: 24px !important;
            font-weight: bold !important;
            border-radius: 12px !important;
            padding: 15px !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }
        .stButton button:active {
            transform: scale(0.98);
        }
        .question-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            border: 3px dashed #FF4B4B;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
        }
        #MainMenu, footer, {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
