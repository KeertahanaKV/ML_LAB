import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA as SklearnPCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

X = load_iris().data                   # Load the Iris dataset
y = load_iris().target

pca = SklearnPCA(n_components=2)       # PCA Implementation
X_pca = pca.fit_transform(X)

print("PCA -> Shape of Data:", X.shape)
print("PCA -> Shape of transformed Data:", X_pca.shape)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="jet")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset")
plt.show()

lda = LinearDiscriminantAnalysis(n_components=2)      # LDA Implementation
X_lda = lda.fit_transform(X, y)

print("LDA -> Shape of Data:", X.shape)
print("LDA -> Shape of transformed Data:", X_lda.shape)

plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap="jet")
plt.xlabel("Linear Discriminant 1")
plt.ylabel("Linear Discriminant 2")
plt.title("LDA of Iris Dataset")
plt.show()
