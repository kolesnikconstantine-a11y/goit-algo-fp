import heapq

import matplotlib.pyplot as plt
import networkx as nx


def create_graph():
    """Create and return a weighted undirected graph."""
    graph = nx.Graph()

    edges = [
        ("A", "B", 4),
        ("A", "C", 20),
        ("B", "C", 10),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3),
        ("F", "G", 10),
    ]

    graph.add_weighted_edges_from(edges)

    return graph


def dijkstra(graph, start):
    """
    Find the shortest paths from the start vertex
    using Dijkstra's algorithm and a binary heap.

    Returns:
        dict: Information about the shortest distance and
              predecessor for every vertex.
    """

    # Initialize distances and predecessors
    shortest_paths = {
        vertex: {
            "distance": float("inf"),
            "predecessor": None,
        }
        for vertex in graph.nodes
    }

    shortest_paths[start]["distance"] = 0

    # Priority queue stores pairs: (distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the vertex with the smallest known distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip outdated entries in the priority queue
        if current_distance > shortest_paths[current_vertex]["distance"]:
            continue

        # Check all neighboring vertices
        for neighbor, edge_data in graph[current_vertex].items():
            weight = edge_data.get("weight", 1)
            new_distance = current_distance + weight

            # Relax the edge if a shorter path is found
            if new_distance < shortest_paths[neighbor]["distance"]:
                shortest_paths[neighbor]["distance"] = new_distance
                shortest_paths[neighbor]["predecessor"] = current_vertex

                # Add the updated distance to the priority queue
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor),
                )

    return shortest_paths


def reconstruct_path(shortest_paths, target):
    """Reconstruct the shortest path from the start vertex to the target."""
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = shortest_paths[current]["predecessor"]

    return path[::-1]


def print_shortest_paths(results, start):
    """Print the shortest distances from the start vertex."""
    print(f"Shortest distances from vertex '{start}':")

    for vertex, data in results.items():
        print(f"  To '{vertex}': {data['distance']}")


def visualize_graph(graph, shortest_path, start, target):
    """Visualize the graph and highlight the shortest path."""

    # Generate fixed node positions for reproducible results
    pos = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(10, 8))

    # Draw all nodes
    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=800,
        node_color="lightblue",
    )

    # Draw all graph edges
    nx.draw_networkx_edges(
        graph,
        pos,
        width=2,
        edge_color="gray",
        alpha=0.5,
    )

    # Convert the shortest path into a list of edges
    path_edges = list(zip(shortest_path, shortest_path[1:]))

    # Highlight the shortest path
    nx.draw_networkx_edges(
        graph,
        pos,
        edgelist=path_edges,
        width=4,
        edge_color="red",
    )

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels,
        font_size=12,
    )

    # Draw vertex labels
    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=16,
        font_weight="bold",
    )

    plt.title(
        f"Weighted Graph: Shortest Path from "
        f"{start} to {target}",
        fontsize=14,
    )

    plt.axis("off")
    plt.tight_layout()
    plt.show()


def main():
    """Run the Dijkstra algorithm and visualize the result."""

    start_node = "A"
    target_node = "G"

    # Create the graph
    graph = create_graph()

    # Find shortest paths
    results = dijkstra(graph, start_node)

    # Display shortest distances
    print_shortest_paths(results, start_node)

    # Reconstruct the shortest path to the target
    shortest_path = reconstruct_path(results, target_node)

    print(
        f"\nShortest path from '{start_node}' "
        f"to '{target_node}': "
        f"{' -> '.join(shortest_path)}"
    )

    # Display the graph
    visualize_graph(
        graph,
        shortest_path,
        start_node,
        target_node,
    )


if __name__ == "__main__":
    main()
