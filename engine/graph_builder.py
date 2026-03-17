import networkx as nx
from .card_parser import extract_mechanics

def build_graph(cards):

    G = nx.Graph()

    for card in cards:
        G.add_node(card["name"])

    for i, c1 in enumerate(cards):
        m1 = extract_mechanics(c1["text"])

        for c2 in cards[i+1:]:

            m2 = extract_mechanics(c2["text"])

            if set(m1) & set(m2):
                G.add_edge(c1["name"], c2["name"])

    return G
