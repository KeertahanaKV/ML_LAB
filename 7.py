import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

glass = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', header=None)
X = glass.iloc[:, 1:-1]
y = glass.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

for m in ['euclidean', 'manhattan']:
    knn = KNeighborsClassifier(n_neighbors=3, metric=m)
    knn.fit(X_train, y_train)
    print(f"{m} acc:", knn.score(X_test, y_test))
