import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.stats import mannwhitneyu

def compute_auc(df):
    return roc_auc_score(df["indication"], -df["proximity_d"])


def mann_whitney(df):
    a = df[df["indication"] == 1]["proximity_d"]
    b = df[df["indication"] == 0]["proximity_d"]
    return mannwhitneyu(a, b, alternative="less")
