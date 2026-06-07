def build_herb_targets(df, valid_nodes):
    herb_map = {}

    for uid, group in df.groupby("tcm_id"):
        targets = set(group["entrez_id"].astype(str))
        targets = targets & valid_nodes

        if len(targets) > 0:
            herb_map[uid] = targets

    return herb_map
