import pandas as pd

def load_symptom_data(path):
    data = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split("\t")
            data.append({
                "symptom": parts[0],
                "genes": parts[1:]
            })

    return pd.DataFrame(data)


def map_symptom_to_proteins(df, valid_nodes):
    symptom_map = {}

    for sym, group in df.groupby("symptom"):
        genes = set(sum(group["genes"].tolist(), []))
        overlap = genes & valid_nodes

        if len(overlap) >= 10:
            symptom_map[sym] = overlap

    return symptom_map
