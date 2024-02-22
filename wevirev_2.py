import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([(start, None)])  # Используем кортеж для хранения пары (вершина, предыдущая вершина)
    visited.add(start)

    path = []

    while queue:
        current_node, prev_node = queue.popleft()
        path.append(current_node)

        for neighbor in graph[current_node] - visited:
            queue.append((neighbor, current_node))
            visited.add(neighbor)

    return path

def visualize_bfs(graph, start):
    G = nx.Graph()
    G.add_nodes_from(graph.keys())
    for key, values in graph.items():
        for value in values:
            G.add_edge(key, value)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

    # Вызываем bfs и выводим путь в консоль
    path = bfs(graph, start)
    print("BFS traversal path:")
    print(" -> ".join(path))

    plt.show()

if __name__ == "__main__":
    graph = {'A': set(['B', 'C', 'H']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F', 'G']),
             'D': set(['B']),
             'E': set(['B']),
             'F': set(['C']),
             'G': set(['C']),
             'H': set(['A','I','J']),
             'I': set(['H']),
             'J': set(['H']),
             }

    start_node = 'A'

    # Визуализация графа и вывод обхода в ширину с путем
    visualize_bfs(graph, start_node)
