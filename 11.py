import numpy as np
X = np.array([[0,0],[0,1],[1,0],[1,1]])
def train(y_target):
    w = np.zeros(2)
    b = 0
    for _ in range(10):
        for x, y in zip(X, y_target):
            y_pred = int(np.dot(x, w) + b > 0)
            w += (y - y_pred) * x
            b += (y - y_pred)
    return w, b
# AND
w, b = train([0,0,0,1])
print("AND:", [int(np.dot(x, w)+b > 0) for x in X])
# OR
w, b = train([0,1,1,1])
print("OR:", [int(np.dot(x, w)+b > 0) for x in X])
