import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from sklearn.metrics import roc_curve, auc

def plot_roc(df):
    fpr, tpr, _ = roc_curve(df["indication"], -df["proximity_d"])
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, label=f"AUC={roc_auc:.4f}")
    plt.plot([0,1],[0,1],'--')
    plt.legend()
    plt.show()


def plot_box(df):
    sns.boxplot(x="indication", y="proximity_d", data=df)
    plt.show()
