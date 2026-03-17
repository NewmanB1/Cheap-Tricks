from collections import defaultdict
from .card_parser import extract_mechanics

def build_mechanic_index(cards):

    index = defaultdict(list)

    for card in cards:
        mechanics = extract_mechanics(card["text"])

        for m in mechanics:
            index[m].append(card["name"])

    return index
