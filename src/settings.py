import json


def load_language(language: str):
    with open(f'translation/{language}.json', 'r') as file:
        return json.load(file)
