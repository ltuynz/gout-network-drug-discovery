import pandas as pd

def merge_herb_gout(herb_df, gout_df):
    df = pd.merge(
        herb_df,
        gout_df,
        on="Gene Symbol",
        how="inner"
    )
    return df
