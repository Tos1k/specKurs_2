import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v, weight):
        self.graph.add_edge(u, v, weight=weight)

    def prim_algorithm(self):
        mst = []
        min_heap = [(0, 0, None)]  # (вес ребра, вершина, предыдущая вершина)
        visited = set()

        while min_heap:
            weight, current_vertex, prev_vertex = heapq.heappop(min_heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            if prev_vertex is not None:
                mst.append((prev_vertex, current_vertex, weight))

            for neighbor, edge_weight in self.graph[current_vertex].items():
                heapq.heappush(min_heap, (edge_weight['weight'], neighbor, current_vertex))

        return mst

    def visualize_graph(self):
        plt.figure()  # Создаем новое окно для графа
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        plt.title("Исходный граф")
        plt.show(block=False)

    def visualize_mst(self, mst_result):
        plt.figure()  # Создаем новое окно для минимального остовного дерева
        mst_graph = nx.Graph()

        for edge in mst_result:
            u, v, weight = edge[0], edge[1], edge[2]
            mst_graph.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(mst_graph)
        labels = nx.get_edge_attributes(mst_graph, 'weight')

        nx.draw(mst_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
        nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=labels)

        plt.title("Минимальное остовное дерево")
        plt.show()

# Пример использования с визуализацией
g = Graph()
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
g.visualize_graph()

mst_result = g.prim_algorithm()
print("Минимальное остовное дерево:")
for edge in mst_result:
    print(f"Ребро: {edge[0]} - {edge[1]}, Вес: {edge[2]}")

g.visualize_mst(mst_result)

plt.show()
