import numpy as np
import networkx as nx

# ---------- distance cache ----------
def build_distance_cache(G, nodes):
    cache = {}

    for node in nodes:
        lengths = nx.single_source_shortest_path_length(G, node)
        cache[node] = lengths

    return cache


# ---------- proximity d ----------
def compute_proximity_d(herb_targets, symptom_prots, dist_matrix, idx_map):
    t_idx = [idx_map[t] for t in herb_targets if t in idx_map]
    s_idx = [idx_map[s] for s in symptom_prots if s in idx_map]

    if not t_idx or not s_idx:
        return np.nan

    sub = dist_matrix[np.ix_(t_idx, s_idx)]
    return float(np.mean(np.min(sub, axis=1)))


# ---------- Sab ----------
def compute_sab(DAA, DBB, DAB):
    return DAB - (DAA + DBB) / 2
