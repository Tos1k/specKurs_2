import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited, path)

    return path

def visualize_graph(graph, path):
    G = nx.Graph()
    G.add_nodes_from(graph.keys())
    for key, values in graph.items():
        for value in values:
            G.add_edge(key, value)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')

    # Вывод пройденного пути в консоль
    print("DFS traversal path:", "->".join(path))

    plt.show()

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E', 'G']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E']),
             'G': set(['B'])
             }

    start_node = 'C'

    # Обход в глубину
    path = dfs(graph, start_node)

    # Визуализация графа и вывод пройденного пути
    visualize_graph(graph, path)
