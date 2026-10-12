"""
Problem title:
    Topological Sort (Kahn's Algorithm) with Cycle Detection

Problem statement:
    Given a directed graph of tasks where an edge (a, b) means "a must be done
    before b", return an order in which all tasks can be done. If the graph
    contains a cycle, no order exists - return None.

What it teaches:
    - Directed graphs, in-degree, and dependency ordering.
    - Kahn's algorithm: repeatedly remove vertices with no incoming edges.
    - Detecting directed cycles: if not every vertex is output, a cycle exists.
    - Laravel analogy: ordering database migrations that depend on each other.

Input example:
    n = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

Expected output:
    Order: [4, 5, 2, 0, 3, 1]
    Cycle 0->1->2->0: None
    Empty graph: []
    No edges: [0, 1, 2]
    Chain: [0, 1, 2, 3]

Approach:
    Count each vertex's in-degree. Queue every vertex with in-degree 0. Pop
    one, add it to the order, and reduce the in-degree of its out-neighbours;
    queue those that reach 0.

Step-by-step logic:
    1. Build adjacency list (directed) and in-degree array.
    2. Queue = all vertices with in-degree 0 (in increasing label order).
    3. While the queue is not empty: pop u, append to order, for each v in
       graph[u] decrement in_degree[v]; if it becomes 0, enqueue v.
    4. If len(order) == n return order, else a cycle blocked some vertices.

Why it works:
    A vertex with no remaining prerequisites is safe to place next. In a
    cycle, every vertex has an unmet prerequisite so none ever reaches 0.

Time complexity:
    O(V + E).

Space complexity:
    O(V + E).

Edge cases:
    - Empty graph returns [].
    - Cycle (e.g. 0 -> 1 -> 0) returns None.
    - Several valid orders can exist; this code returns the one produced by
      processing the queue in FIFO order.
    - Invalid edge endpoints raise ValueError.

Alternative approach:
    DFS-based topological sort: output vertices in reverse finishing order.
"""

from collections import deque


def topological_sort(vertex_count, edges):
    """Return a valid ordering of vertices, or None if a cycle exists."""
    graph = {vertex: [] for vertex in range(vertex_count)}
    in_degree = [0] * vertex_count
    for u, v in edges:
        if u not in graph or v not in graph:
            raise ValueError("edge (%s, %s) uses an unknown vertex" % (u, v))
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for vertex in range(vertex_count):
        if in_degree[vertex] == 0:
            queue.append(vertex)

    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbour in graph[vertex]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) != vertex_count:
        return None  # some vertices were never freed: there is a cycle
    return order


def main():
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print("Order:", topological_sort(6, edges))
    print("Cycle 0->1->2->0:", topological_sort(3, [(0, 1), (1, 2), (2, 0)]))

    # Edge cases
    print("Empty graph:", topological_sort(0, []))
    print("No edges:", topological_sort(3, []))
    print("Chain:", topological_sort(4, [(0, 1), (1, 2), (2, 3)]))


if __name__ == "__main__":
    main()
