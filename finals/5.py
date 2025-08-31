import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------- PART 1: Box Plot for n-Dimensional Data --------
def plot_nd_box():
    data = pd.DataFrame(np.random.randn(100, 5), columns=[f"F{i}" for i in range(1, 6)])
    sns.boxplot(data=data)
    plt.title("Box Plot of 5D Data")
    plt.xlabel("Features")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

# -------- PART 2: Alpha-Beta Pruning --------
def alpha_beta(depth, idx, is_max, vals, alpha, beta, max_depth):
    if depth == max_depth:
        return vals[idx]
    if is_max:
        for i in range(2):
            alpha = max(alpha, alpha_beta(depth+1, idx*2+i, False, vals, alpha, beta, max_depth))
            if beta <= alpha:
                break
        return alpha
    else:
        for i in range(2):
            beta = min(beta, alpha_beta(depth+1, idx*2+i, True, vals, alpha, beta, max_depth))
            if beta <= alpha:
                break
        return beta

# -------- MAIN --------
if __name__ == "__main__":
    print("📊 Box-Plot for n-Dimensional Data:")
    plot_nd_box()

    print("\n♟ Alpha-Beta Pruning Result:")
    n = int(input("Enter number of leaf nodes (power of 2, e.g., 8): "))
    leaf_values = list(map(int, input(f"Enter {n} leaf node values separated by space: ").split()))

    max_depth = int(np.log2(n))  # calculate tree depth
    result = alpha_beta(0, 0, True, leaf_values, float('-inf'), float('inf'), max_depth)
    print(f"✅ Optimal Value: {result}")
