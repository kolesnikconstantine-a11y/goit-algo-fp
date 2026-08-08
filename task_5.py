import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id,
            color=node.color,
            label=node.val
        )

        if node.left:
            graph.add_edge(node.id, node.left.id)

            left_x = x - 1 / (2 ** layer)
            pos[node.left.id] = (left_x, y - 1)

            add_edges(
                graph,
                node.left,
                pos,
                x=left_x,
                y=y - 1,
                layer=layer + 1
            )

        if node.right:
            graph.add_edge(node.id, node.right.id)

            right_x = x + 1 / (2 ** layer)
            pos[node.right.id] = (right_x, y - 1)

            add_edges(
                graph,
                node.right,
                pos,
                x=right_x,
                y=y - 1,
                layer=layer + 1
            )

    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}

    tree = add_edges(tree, tree_root, pos)

    node_colors = [
        colors.get(node, "#87CEFA")
        for node in tree.nodes()
    ]

    labels = {
        node_id: data["label"]
        for node_id, data in tree.nodes(data=True)
    }

    plt.figure(figsize=(10, 6))

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
        font_weight="bold"
    )

    plt.show()


def build_heap_tree(heap, index=0):
    """
    Build a binary tree from a heap represented as a list.

    For a node at index i:
        left child  = 2 * i + 1
        right child = 2 * i + 2
    """

    if index >= len(heap):
        return None

    node = Node(heap[index])

    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)

    return node


def generate_color(step, total_steps):
    """
    Generate a color from dark blue to light blue.

    step = current visit number
    total_steps = total number of nodes
    """

    # Base light blue color: #87CEFA
    base_color = [135, 206, 250]

    if total_steps <= 1:
        darken_factor = 0
    else:
        # First node is the darkest,
        # last node is the lightest.
        darken_factor = 0.6 * (1 - step / (total_steps - 1))

    new_color = [
        int(channel * (1 - darken_factor))
        for channel in base_color
    ]

    return f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"


def dfs_visualize(root, total_steps):
    """
    Depth-First Search (DFS).

    Uses a stack to explore nodes as deep as possible before backtracking.
    """

    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()

        if node is None or node.id in visited:
            continue

        # Mark node as visited
        visited.add(node.id)

        # Assign a unique color according to visit order
        colors[node.id] = generate_color(step, total_steps)
        step += 1

        # Add right child first so that
        # the left child is processed first.
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return colors


def bfs_visualize(root, total_steps):
    """
    Breadth-First Search (BFS).
    Uses a queue to explore nodes level by level.
    """

    visited = set()
    queue = deque([root])
    colors = {}
    step = 0

    while queue:
        node = queue.popleft()

        if node is None or node.id in visited:
            continue

        # Mark node as visited
        visited.add(node.id)

        # Assign a unique color according to visit order
        colors[node.id] = generate_color(step, total_steps)
        step += 1

        # Add children to the queue
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return colors


def count_nodes(node):
    if node is None:
        return 0

    return (
        1
        + count_nodes(node.left)
        + count_nodes(node.right)
    )


if __name__ == "__main__":
    # Initial heap data
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]

    # Convert the list into a min-heap
    heapq.heapify(heap_list)

    print("Heap:", heap_list)

    # Build a binary tree from the heap
    heap_tree_root = build_heap_tree(heap_list)

    # Count the number of nodes
    total_steps = count_nodes(heap_tree_root)

    # DFS visualization
    print("DFS traversal:")
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # BFS visualization
    print("BFS traversal:")
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)
