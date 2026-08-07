import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_list):
    """
    Перетворює список/масив бінарної купи у дерево об'єктів Node.
    """
    if not heap_list:
        return None

    # Створюємо вузол Node для кожного елемента списку
    nodes = [Node(val) for val in heap_list]

    # Зв'язуємо батьківські вузли з дочірніми за індексами бінарної купи
    n = len(heap_list)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    # Повертаємо корінь дерева (перший елемент масиву)
    return nodes[0]

if __name__ == '__main__':
    # Припустимо, що у нас є бінарна купа у вигляді списку
    heap_list = [1, 3, 5, 7, 9, 2]
    
    heapq.heapify(heap_list)
    print(type(heap_list))
    print(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Візуалізація дерева бінарної купи
    draw_tree(heap_tree_root)