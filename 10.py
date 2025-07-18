# PCA
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
X = load_iris().data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title("PCA")
plt.show()
# LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
y = load_iris().target
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y)
plt.title("LDA")
plt.show()