import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Visualize n-dimensional data using heatmap
def visualize_heatmap():
    data = np.random.rand(10, 5)
    sns.heatmap(data, annot=True, cmap="YlGnBu")
    plt.title("Heatmap of Synthetic 5D Data")
    plt.xlabel("Features")
    plt.ylabel("Samples")
    plt.show()

# Min-Max algorithm implementation

import math

# Min-Max algorithm implementation
def minmax(depth, node_index, is_max, values, max_depth):
    if depth == max_depth:
        return values[node_index]
    left = minmax(depth+1, node_index*2, not is_max, values, max_depth)
    right = minmax(depth+1, node_index*2+1, not is_max, values, max_depth)
    return max(left, right) if is_max else min(left, right)

# Main execution
if __name__ == "__main__":
    # User input
    n = int(input("Enter number of leaf nodes (power of 2): "))
    values = list(map(int, input(f"Enter {n} leaf node values separated by space: ").split()))

    # Depth = log2(n)
    max_depth = int(math.log2(n))

    result = minmax(0, 0, True, values, max_depth)
    print(f"✅ Optimal value from Min-Max: {result}")


values = [1, 2, 3, 4, 5, 6, 7, 8]
max_depth = 3

