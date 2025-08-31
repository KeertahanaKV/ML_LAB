import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

# ----------- Contour Plot -----------
def visualize_contour():
    x, y = np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    plt.contourf(X, Y, Z, 20, cmap='viridis')
    plt.colorbar()
    plt.title("Contour Plot of sin(x) * cos(y)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# ----------- A* Algorithm -----------
def a_star(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((0, start))
    g = {start: 0}
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [start] + path[::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                new_g = g[current] + 1

                if neighbor not in g or new_g < g[neighbor]:
                    g[neighbor] = new_g
                    f = new_g + abs(nx - goal[0]) + abs(ny - goal[1])  # f = g + h
                    open_set.put((f, neighbor))
                    came_from[neighbor] = current

    return None

# ----------- Run Program -----------
if __name__ == "__main__":
    visualize_contour()

    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    path = a_star((0, 0), (4, 4), grid)

    if path:
        print("Path Found:", path)
    else:
        print("No Path Found.")





#Write a program to implement the A* algorithm
import heapq

# ----------- INPUT FROM USER ------------
# Number of edges
n = int(input("Enter number of edges: "))

Graph_nodes = {}
for _ in range(n):
    u, v, w = input("Enter edge (format: from to cost): ").split()
    w = int(w)
    if u not in Graph_nodes:
        Graph_nodes[u] = []
    Graph_nodes[u].append((v, w))

# Heuristic values
H_dist = {}
m = int(input("Enter number of heuristic values: "))
for _ in range(m):
    node, h = input("Enter heuristic (format: node value): ").split()
    H_dist[node] = int(h)

start = input("Enter start node: ")
goal = input("Enter goal node: ")
# ----------------------------------------


def a_star(start, goal):
    open_heap = []
    heapq.heappush(open_heap, (H_dist[start], start))  # (f_score, node)

    g_cost = {start: 0}        # cost from start to node
    parent = {start: None}     # to reconstruct path
    closed_set = set()

    while open_heap:
        f_score, current = heapq.heappop(open_heap)  # best node so far

        if current in closed_set:
            continue
        closed_set.add(current)

        if current == goal:  # reached goal → build path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for (neighbor, step_cost) in Graph_nodes.get(current, []):
            new_cost = g_cost[current] + step_cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_score = new_cost + H_dist[neighbor]
                heapq.heappush(open_heap, (f_score, neighbor))
                parent[neighbor] = current

    return None


# Run
print("Path found:", a_star(start, goal))


Enter number of edges: 5
Enter edge (format: from to cost): A B 6
Enter edge (format: from to cost): A F 3
Enter edge (format: from to cost): B C 3
Enter edge (format: from to cost): B D 2
Enter edge (format: from to cost): C E 5

Enter number of heuristic values: 4
Enter heuristic (format: node value): A 10
Enter heuristic (format: node value): B 8
Enter heuristic (format: node value): C 5
Enter heuristic (format: node value): E 0

Enter start node: A
Enter goal node: E

