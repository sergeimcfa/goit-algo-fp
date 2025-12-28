import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Черга пріоритетів (бінарна купа) зберігає пари (відстань, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за вже знайдену, пропускаємо
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Створення графа (у вигляді словника)
graph_dict = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виклик алгоритму
start_node = 'A'
shortest_paths = dijkstra(graph_dict, start_node)

print(f"Найкоротші шляхи від вершини {start_node}: {shortest_paths}")

# Візуалізація графа (додатково, для перевірки)
G = nx.Graph()
for node, neighbors in graph_dict.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф для алгоритму Дейкстри")
plt.show()
