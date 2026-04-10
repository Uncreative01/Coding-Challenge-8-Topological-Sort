
from collections import deque

def topological_sort(graph):
    # Step 1: Compute in-degrees
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Step 2: Initialize queue with nodes having 0 in-degree
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    # Step 3: Process the queue
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(topo_order) != len(graph):
        raise ValueError("Graph contains a cycle, topological sort not possible")

    return topo_order


# ---- TEST GRAPH ----
# Directed Acyclic Graph (DAG)
test_graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}


# ---- FUNCTION CALL ----
if __name__ == "__main__":
    result = topological_sort(test_graph)
    print("Topological Sort Order:", result)

# within a Kahn's Algorithm ¯\_(ツ)_/¯
