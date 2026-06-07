from data_loader import *
from preprocessing import *
from network_builder import *
from symptom_module import *
from herb_module import *
from proximity import *
from statistics import *
import config

def main():

    # 1. Load data
    herb = load_herb_data(config.HERB_PATH)
    gout = load_gout_targets(config.GOUT_TARGET_PATH)
    ppi = load_ppi(config.PPI_PATH)

    # 2. Build network
    G = build_ppi_network(ppi)
    largest_cc = get_largest_component(G)
    G = G.subgraph(largest_cc).copy()

    # 3. Load symptom
    symptom_df = load_symptom_data(config.SYMPTOM_PATH)
    symptom_map = map_symptom_to_proteins(symptom_df, set(G.nodes()))

    # 4. Build herb
    herb_map = build_herb_targets(herb, set(G.nodes()))

    print("Pipeline ready")
    print(len(symptom_map), len(herb_map))

if __name__ == "__main__":
    main()
