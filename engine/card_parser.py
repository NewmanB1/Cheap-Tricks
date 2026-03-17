import json
import re

KEYWORDS = [
    "draw",
    "sacrifice",
    "create",
    "token",
    "mana",
    "graveyard",
    "cast",
    "life",
    "damage",
]

def load_cards(path):
    with open(path) as f:
        return json.load(f)

def extract_mechanics(text):
    text = text.lower()
    found = []

    for k in KEYWORDS:
        if re.search(k, text):
            found.append(k)

    return found
