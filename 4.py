# Heatmap
import seaborn as sns
data = np.random.rand(5, 5)
sns.heatmap(data, annot=True)
plt.show()

# Min-Max
def minmax(depth, idx, max_player, vals):
    if depth == 2: return vals[idx]
    if max_player:
        return max(minmax(depth+1, idx*2, False, vals),
                   minmax(depth+1, idx*2+1, False, vals))
    else:
        return min(minmax(depth+1, idx*2, True, vals),
                   minmax(depth+1, idx*2+1, True, vals))
print("Result:", minmax(0, 0, True, [3, 5, 6, 9]))