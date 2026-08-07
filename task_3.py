import heapq
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=20)
G.add_edge("B", "C", weight=10)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "F", weight=3)
G.add_edge("F", "G", weight=10) 

# Реалізація алгоритму Дейкстри з використанням бінарної купи
def dijkstra(graph, start):
    # Ініціалізація: відстані до всіх вершин нескінченні, до початкової - 0
    # Зберігаємо також попередника для кожної вершини, щоб відновити шлях
    shortest_paths = {vertex: {'distance': float('infinity'), 'predecessor': None} for vertex in graph.nodes()}
    shortest_paths[start]['distance'] = 0
    
    # Пріоритетна черга (міні-купа), зберігає пари (відстань, вершина)
    # heapify працює на основі першого елемента кортежу (відстані)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # 1. Вибираємо вершину з найменшою поточною відстанню (використовуючи купу)
        # Вилучаємо елемент з вершини купи за O(log N)
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдена відстань вже більша за відому найкоротшу, пропускаємо
        # Це оптимізація для випадків, коли вершина була додана до купи кілька разів
        if current_distance > shortest_paths[current_vertex]['distance']:
            continue
            
        # 2. Оглядаємо всіх сусідів поточної вершини
        # Для networkx графа, graph[current_vertex].items() повертає (сусід, атрибути_ребра)
        for neighbor, edge_attributes in graph[current_vertex].items():
            weight = edge_attributes.get('weight', 1) # якщо ваги немає, вважаємо її 1
            distance = current_distance + weight
            
            # 3. Релаксація ребра: якщо новий шлях коротший, оновлюємо дані
            if distance < shortest_paths[neighbor]['distance']:
                shortest_paths[neighbor]['distance'] = distance
                shortest_paths[neighbor]['predecessor'] = current_vertex
                
                # Додаємо оновлену відстань до сусідньої вершини в купу за O(log N)
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return shortest_paths

# Допоміжна функція для відновлення шляху
def reconstruct_path(shortest_paths_dict, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = shortest_paths_dict[current]['predecessor']
    return path[::-1] # повертаємо перевернутий список

#  Використання алгоритму Дейкстри
start_node = "A"
target_node = "G" 

results = dijkstra(G, start_node)

print(f"Найкоротші відстані від вершини '{start_node}':")
for node, data in results.items():
    print(f"  До '{node}': {data['distance']}")

# Відновимо найкоротший шлях до конкретної цільової вершини
shortest_path_to_target = reconstruct_path(results, target_node)
print(f"\nНайкоротший шлях від '{start_node}' до '{target_node}': {' -> '.join(shortest_path_to_target)}")

#  Візуалізація графа
pos = nx.spring_layout(G, seed=42)  # Фіксуємо розташування для відтворюваності

plt.figure(figsize=(10, 8)) # Розмір вікна

# Малюємо всі вузли
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue')

# Малюємо всі ребра (сірим кольором)
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', alpha=0.5)

# Створення списку ребер, які входять до найкоротшого шляху
path_edges = []
if len(shortest_path_to_target) > 1:
    path_edges = list(zip(shortest_path_to_target, shortest_path_to_target[1:]))

# Виділяємо червоним ребра найкоротшого шляху
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4, edge_color='red')

# Етикетки для ребер (ваги)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Етикетки для вузлів (назви вершин)
nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif", font_weight='bold')

plt.title(f"Ваговий граф. Найкоротший шлях від {start_node} до {target_node} виділено червоним.", fontsize=14)
plt.axis("off") # Вимикаємо осі
plt.tight_layout()
plt.show()