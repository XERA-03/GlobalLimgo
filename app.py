import streamlit as st
from model.translator import Translator

st.set_page_config(page_title="🌍 Global Text Translator", layout="centered")
st.markdown("## 🌐 GlobaLingo — Real-Time Universal Translator")

st.markdown("Translate between 100+ verified languages using AI 🤖")

# Language code mappings
languages = {
    "English": "en",
    "French": "fr",
    "Hindi": "hi",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh",
    "Tamil": "ta",
    "Bengali": "bn",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Portuguese": "pt",
    "Turkish": "tr",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Swahili": "sw"
}

with st.sidebar:
    st.header("🌍 Language Settings")
    src_lang = st.selectbox("Select Source Language", list(languages.keys()), index=0)
    tgt_lang = st.selectbox("Select Target Language", list(languages.keys()), index=1)

src = languages[src_lang]
tgt = languages[tgt_lang]

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📝 {src_lang} Input")
    input_text = st.text_area("Type or paste your text here", height=200)

with col2:
    st.subheader(f"📄 {tgt_lang} Output")
    output_placeholder = st.empty()  # Placeholder to show translation later

# Button centered below
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("🔁 Translate"):
    if src == tgt:
        st.warning("⚠️ Source and target languages cannot be the same.")
    elif not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating... ⏳"):
            translator = Translator(src, tgt)
            result = translator.translate(input_text)
        output_placeholder.success(result)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Powered by Meta AI's M2M100 via Hugging Face 🤗")
