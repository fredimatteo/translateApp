import streamlit as st

from client import deepl
from settings import load_language

LANGUAGES = {
    "English": "en",
    "Italiano": "it"
}

translations = load_language(LANGUAGES["English"])

with st.sidebar:
    st.markdown(f"# {translations['sidebar_title']}")
    selected_language = st.selectbox(translations['select_app_language_title'], options=list(LANGUAGES.keys()))

    characters_remaining = deepl.get_characters_remaining()

    st.markdown(f"### Character remaining: {characters_remaining}")

translations = load_language(LANGUAGES[selected_language])
a = translations['sidebar_title']

st.title(translations['app_title'] + '  🧠 🌍 🚀')

prompt = st.chat_input(translations['chat_input_placeholder'])

formality_option = st.selectbox(
    translations['formality_title'],
    ("Default", "More", "Less")
)

target_lang = st.selectbox(
    translations['select_target_language_title'],
    ("EN-US", "EN-GB", "FR", "DE", "ES")
)


if prompt and prompt.strip():
    try:
        with st.spinner(f'{translations["spinner_text"]}...'):
            translation = deepl.translate(
                text=prompt,
                formality=formality_option.lower(),
                target_lang=target_lang
            )
            st.write(translation)
    except Exception as e:
        st.error(f"{translations['error_occurred']} {e}")
else:
    st.warning(translations['valid_prompt_required'])
