import matplotlib.pyplot as plt
import numpy as np

# Generate random n-dimensional data
n = 2  # Number of dimensions
data = np.random.rand(100, n)

# Visualize using Scatter plot
plt.scatter(data[:, 0], data[:, 1])
plt.title('Scatter Plot of Random n-dimensional Data')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()

# Implement Hill Climbing Algorithm (dummy example)
def hill_climbing():
    current_solution = np.random.rand(n)  # Initialize random solution
    best_solution = current_solution.copy()

    # Hill climbing logic (dummy: random walk)
    for _ in range(100):
        new_solution = current_solution + 0.01 * np.random.randn(n)
        if objective_function(new_solution) > objective_function(best_solution):
            best_solution = new_solution
        current_solution = new_solution

    return best_solution

def objective_function(solution):
    return np.sum(solution ** 2)  # Example objective function

# Example usage of hill climbing
best_solution = hill_climbing()
print(f'Best solution found: {best_solution}')
