import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self): #Конструктор класса
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity): #u - начальная вершина,v - конечная вершина,пропускная способность - capacity
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Обратное ребро сначала имеет нулевую пропускную способность

    def ford_fulkerson(self, source, sink):
        parent = {}

        def bfs():
            visited = set()
            queue = [source]
            visited.add(source)

            while queue:
                u = queue.pop(0)

                for v, capacity in self.graph[u].items():
                    if v not in visited and capacity > 0:
                        queue.append(v)
                        visited.add(v)
                        parent[v] = u

            return sink in visited

        max_flow = 0

        while bfs():
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def visualize_graph(self, title="Граф"):
        G = nx.DiGraph()

        for u, neighbors in self.graph.items():
            for v, capacity in neighbors.items():
                if capacity > 0:
                    G.add_edge(u, v, capacity=capacity, weight=capacity)

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): f"{d['capacity']}/{self.graph[v][u]}" for u, v, d in G.edges(data=True)}
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(title)

# Пример использования с визуализацией
g = Graph()
g.add_edge('source', 'A', 5)
g.add_edge('source', 'B', 3)
g.add_edge('A', 'C', 1)
g.add_edge('A', 'D', 3)
g.add_edge('B', 'C', 4)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'sink', 4)
g.add_edge('D', 'sink', 6)

source = 'source'
sink = 'sink'

# Визуализация графа до выполнения алгоритма
g.visualize_graph("Граф до выполнения алгоритма")

max_flow = g.ford_fulkerson(source, sink)
print(f"Максимальный поток из {source} в {sink}: {max_flow}")

# Открываем новое окно для визуализации графа после выполнения алгоритма
plt.figure()
g.visualize_graph("Граф после выполнения алгоритма")

plt.show()  # Покажем оба графика в отдельных окнах
