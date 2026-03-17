from engine.card_parser import load_cards
from engine.graph_builder import build_graph
from engine.basin_search import build_mechanic_index
from engine.combo_finder import find_loops

cards = load_cards("data/cards.json")

print("Loaded cards:", len(cards))

graph = build_graph(cards)

basins = build_mechanic_index(cards)

print("\nMechanic basins:")
for k, v in basins.items():
    print(k, "->", v)

combos = find_loops(graph)

print("\nPossible combos:")
for c in combos:
    print(" -> ".join(c))
