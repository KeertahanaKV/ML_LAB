from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns

# Load data
X = load_iris().data

# Apply K-Means clustering
labels = KMeans(n_clusters=3, random_state=0).fit_predict(X)

# Reduce dimensions for 2D plot
X_pca = PCA(n_components=2).fit_transform(X)

# Plot clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()


# Calculate and plot the confusion matrix
# the X-axis in the plot is for the predicted class and the Y-axis is for the true class. 
conf_matrix = confusion_matrix(labels, y)
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d')
plt.xlabel('Predicted Class')
plt.ylabel('True Class')
plt.title('Confusion Matrix')
plt.show()

print("The accuracy is: ", accuracy_score(labels,y))  
