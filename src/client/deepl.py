import os
import time

import deepl
import requests
from dotenv import load_dotenv

load_dotenv()

auth_key = os.getenv("DEEPL_AUTH_KEY", None)
translator = deepl.Translator(auth_key)


def translate(text: str, **kwargs) -> str:
    """
    Translate a text using the DeepL API
    :param text: a string representing the text to translate
    :param kwargs: additional parameters like formality and target_lang
    :return: a string representing the translated text
    """
    formality = kwargs.get("formality", "default")
    target_lang = kwargs.get("target_lang", "EN-US")

    try:
        result = translator.translate_text(
            text=text,
            target_lang=target_lang,
            formality=formality
        )

        for letter in result.text:
            time.sleep(0.01)  # Simulate a delay
            yield letter
    except Exception as e:
        raise e


def get_characters_remaining() -> int:
    """
    Get the number of characters remaining in the DeepL API
    :return: an int representing the number of characters remaining
    """
    res = requests.get(
        url="https://api-free.deepl.com/v2/usage",
        headers={"Authorization": f"DeepL-Auth-Key {auth_key}"},
        timeout=15
    )
    if res.status_code == 200:
        return res.json()["character_limit"] - res.json()["character_count"]

    return 0
