import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_iris

data = load_iris().data[:6]         # Load a subset of the Iris dataset (first 6 samples)

def proximity_matrix(data):         # Function to compute proximity matrix (Euclidean distance)
    n = len(data)
    return np.array([[np.linalg.norm(data[i] - data[j]) for j in range(n)] for i in range(n)])

def plot_dendrogram(data, method):      # Function to plot dendrogram with given linkage method
    dendrogram(linkage(data, method=method))
    plt.title(f'Dendrogram - {method} Linkage')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()

print("Proximity Matrix:\n", proximity_matrix(data))    # Main Execution: Proximity Matrix + Dendrograms
plot_dendrogram(data, 'single')
plot_dendrogram(data, 'complete')
