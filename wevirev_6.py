import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u

        return sink in visited

    def dfs(self, u, sink, path_flow, visited):
        if u == sink:
            return path_flow

        for v, capacity in self.graph[u].items():
            if v not in visited and capacity > 0:
                visited.add(v)
                min_capacity = min(path_flow, capacity)
                flow = self.dfs(v, sink, min_capacity, visited)

                if flow > 0:
                    self.graph[u][v] -= flow
                    self.graph[v][u] += flow
                    return flow

        return 0

    def dinic_algorithm(self, source, sink):
        max_flow = 0

        plt.ion()  # Включаем интерактивный режим для обновления графа в том же окне

        # Шаг 0: Исходный граф
        self.visualize_graph(source, sink, 0)

        step = 1
        while True:
            parent = [-1] * len(self.graph)
            if not self.bfs(source, sink, parent):
                break

            path_flow = float('inf')

            while path_flow > 0:
                visited = set([source])
                path_flow = self.dfs(source, sink, float('inf'), visited)
                max_flow += path_flow

                # Визуализация после каждого блокирующего потока
                self.visualize_graph(source, sink, step)
                step += 1

        plt.ioff()  # Выключаем интерактивный режим
        plt.show()  # Отображаем окно с финальным графом

        return max_flow

    def visualize_graph(self, source, sink, step):
        plt.figure(step)
        plt.clf()

        G = nx.DiGraph()

        for u, neighbors in self.graph.items():
            for v, capacity in neighbors.items():
                if capacity > 0:
                    G.add_edge(u, v, capacity=capacity, weight=capacity)

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): f"{d['capacity']}/{self.graph[v][u]}" for u, v, d in G.edges(data=True)}
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"Шаг {step}: Граф с максимальным потоком из {source} в {sink}")
        plt.pause(0.5)  # Пауза перед следующим шагом

# Пример использования
g = Graph()
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 2)

source = 0
sink = 4

max_flow = g.dinic_algorithm(source, sink)
print(f"Максимальный поток из {source} в {sink}: {max_flow}")
