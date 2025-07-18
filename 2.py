# 3D Surface Plot
from mpl_toolkits.mplot3d import Axes3D
x = y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()

# Best First Search
import heapq
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
heuristics = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
def bfs(start, goal):
    q = [(heuristics[start], start, [])]
    while q:
        _, node, path = heapq.heappop(q)
        if node == goal: return path + [node]
        for n in graph[node]:
            heapq.heappush(q, (heuristics[n], n, path + [node]))
print("Path:", bfs('A', 'D'))