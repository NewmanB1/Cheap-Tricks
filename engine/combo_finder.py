import networkx as nx

def find_loops(graph):

    combos = []

    for cycle in nx.simple_cycles(graph.to_directed()):
        if len(cycle) <= 4:
            combos.append(cycle)

    return combos
