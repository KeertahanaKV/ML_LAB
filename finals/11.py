import numpy as np

def step_function(x):                   # Step activation function    
    return np.where(x >= 0, 1, 0)

class Perceptron:                       # Perceptron model
    def __init__(self, input_size, lr=0.1, epochs=1000):
        self.weights = np.zeros((input_size, 1))
        self.bias = 0
        self.lr = lr
        self.epochs = epochs

    def train(self, X, y):               # Training the perceptron
        for _ in range(self.epochs):
            for inputs, label in zip(X, y):
                inputs = inputs.reshape(-1, 1)
                output = step_function(np.dot(inputs.T, self.weights) + self.bias)
                error = label - output
                self.weights += self.lr * error * inputs
                self.bias += self.lr * error

    def predict(self, X):                  # Predict function
        return step_function(np.dot(X, self.weights) + self.bias)

# ---------------- Main Program ---------------- #

# Training data for AND
X_and = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([[0],[0],[0],[1]])

# Training data for OR
X_or = np.array([[0,0],[0,1],[1,0],[1,1]])
y_or = np.array([[0],[1],[1],[1]])

# Train perceptron for AND
p_and = Perceptron(2)
p_and.train(X_and, y_and)
print("AND Function Predictions:")
print(p_and.predict(X_and))

# Train perceptron for OR
p_or = Perceptron(2)
p_or.train(X_or, y_or)
print("\nOR Function Predictions:")
print(p_or.predict(X_or))

# Testing specific inputs
print("\nAND(1,1) =", p_and.predict(np.array([[1,1]])))
print("OR(0,1)  =", p_or.predict(np.array([[0,1]])))
