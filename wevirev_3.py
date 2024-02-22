import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, target=None):
    # Инициализация
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0
    visited = set()

    # Создание графа networkx
    G = nx.Graph(graph)

    # Для визуализации
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)

    while len(visited) < len(graph):
        # Выбор вершины с наименьшим расстоянием
        current_vertex = min(
            (vertex for vertex in graph if vertex not in visited),
            key=lambda vertex: distance[vertex]
        )

        # Помечаем вершину как посещенную
        visited.add(current_vertex)

        # Обновляем расстояния до соседних вершин
        for neighbor, weight in graph[current_vertex].items():
            new_distance = distance[current_vertex] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

                # Для визуализации: подсветка ребра
                nx.draw_networkx_edges(G, pos, edgelist=[(current_vertex, neighbor)],
                                       edge_color='k', width=2)

        # Для визуализации: подсветка вершины
        nx.draw_networkx_nodes(G, pos, nodelist=[current_vertex],
                               node_color='w', edgecolors='k',  node_size=500, linewidths=2)

    # Добавляем веса рёбер
    edge_labels = {(current_vertex, neighbor): str(weight) for current_vertex, neighbors in graph.items() for neighbor, weight in neighbors.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')

    plt.show()

    return distance

# Пример создания графа с 6 вершинами
graph = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 5, 'E': 6},
    'C': {'A': 4, 'B': 1, 'D': 1, 'E': 7},
    'D': {'A': 3, 'B': 5, 'C': 1, 'E': 8},
    'E': {'B': 6, 'C': 7, 'D': 8, 'F': 9},
    'F': {'E': 9}
}



start_vertex = 'A'
result = dijkstra(graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}: {result}")
