from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = load_iris().data
model = KMeans(n_clusters=3, n_init=10)
model.fit(X)
plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
plt.show()
