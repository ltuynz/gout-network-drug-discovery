import networkx as nx

def build_ppi_network(ppi_df):
    G = nx.Graph()
    G.add_edges_from(zip(ppi_df["proteinA"], ppi_df["proteinB"]))
    return G


def get_largest_component(G):
    components = list(nx.connected_components(G))
    return max(components, key=len)
