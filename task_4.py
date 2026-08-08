import heapq
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    """Represents a node in a binary tree."""

    def __init__(self, value, color="skyblue"):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())


def build_heap_tree(heap):
    """
    Convert a binary heap represented as a list into a tree of Node objects.

    Args:
        heap: List containing heap elements.

    Returns:
        The root Node of the binary heap tree.
    """
    if not heap:
        return None

    # Create a Node object for every heap element.
    nodes = [Node(value) for value in heap]

    # Connect parent nodes with their children.
    for index, node in enumerate(nodes):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            node.left = nodes[left_index]

        if right_index < len(nodes):
            node.right = nodes[right_index]

    return nodes[0]


def add_edges(graph, node, positions, x=0, y=0, level=1):
    """
    Recursively add tree nodes and edges to a NetworkX graph.

    Args:
        graph: NetworkX graph.
        node: Current tree node.
        positions: Dictionary containing node positions.
        x: Current horizontal position.
        y: Current vertical position.
        level: Current tree level.

    Returns:
        The updated NetworkX graph.
    """
    if node is None:
        return graph

    # Add the current node to the graph.
    graph.add_node(
        node.id,
        color=node.color,
        label=node.value
    )

    # Add the left child.
    if node.left:
        graph.add_edge(node.id, node.left.id)

        left_x = x - 1 / (2 ** level)
        positions[node.left.id] = (left_x, y - 1)

        add_edges(
            graph,
            node.left,
            positions,
            x=left_x,
            y=y - 1,
            level=level + 1
        )

    # Add the right child.
    if node.right:
        graph.add_edge(node.id, node.right.id)

        right_x = x + 1 / (2 ** level)
        positions[node.right.id] = (right_x, y - 1)

        add_edges(
            graph,
            node.right,
            positions,
            x=right_x,
            y=y - 1,
            level=level + 1
        )

    return graph


def draw_tree(root):
    """
    Visualize a binary tree using NetworkX and Matplotlib.

    Args:
        root: Root node of the tree.
    """
    if root is None:
        print("The tree is empty.")
        return

    graph = nx.DiGraph()
    positions = {root.id: (0, 0)}

    add_edges(graph, root, positions)

    # Get node colors and labels from graph attributes.
    colors = [
        data["color"]
        for _, data in graph.nodes(data=True)
    ]

    labels = {
        node_id: data["label"]
        for node_id, data in graph.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))

    nx.draw(
        graph,
        pos=positions,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_size=12
    )

    plt.title("Binary Heap Tree")
    plt.axis("off")
    plt.show()


def main():
    """Create, build, and visualize a binary heap tree."""

    # Create a list of values.
    heap = [1, 3, 5, 7, 9, 2]

    # Convert the list into a valid min-heap.
    heapq.heapify(heap)

    print("Heap:", heap)

    # Build a binary tree from the heap.
    root = build_heap_tree(heap)

    # Visualize the binary heap tree.
    draw_tree(root)


if __name__ == "__main__":
    main()