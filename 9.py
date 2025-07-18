from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

X = load_iris().data[:6]
for method in ['single', 'complete']:
    Z = linkage(X, method=method)
    dendrogram(Z)
    plt.title(method + " linkage")
    plt.show()
