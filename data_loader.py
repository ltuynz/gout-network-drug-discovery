import pandas as pd

def load_herb_data(path):
    return pd.read_csv(path)

def load_gout_targets(path):
    df = pd.read_csv(path)
    return df[df["Relevance score"] > 0.2]

def load_ppi(path):
    df = pd.read_csv(path, sep="\t")
    df.columns = ["proteinA", "proteinB", "db"]
    return df
