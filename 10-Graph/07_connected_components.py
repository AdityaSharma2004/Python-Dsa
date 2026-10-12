"""
Problem title:
    Count and List Connected Components

Problem statement:
    Given an undirected graph with n vertices (0..n-1) and an edge list,
    return the number of connected components and the vertices in each one.

What it teaches:
    - Using traversal as a "flood fill" over separate islands of vertices.
    - Outer loop over all vertices + inner traversal pattern.
    - Isolated vertices count as their own component.

Input example:
    n = 7, edges = [(0, 1), (1, 2), (3, 4)]
    (vertices 5 and 6 are isolated)

Expected output:
    Component count: 4
    Component 1: [0, 1, 2]
    Component 2: [3, 4]
    Component 3: [5]
    Component 4: [6]
    No vertices: 0
    No edges (4 vertices): 4
    Fully connected: 1

Approach:
    Build the adjacency list. For each vertex not yet visited, start a BFS
    from it; everything that BFS reaches belongs to one component.

Step-by-step logic:
    1. visited = empty set, components = [].
    2. For v in 0..n-1: if v is unvisited, run BFS collecting a list.
    3. Append that list to components.
    4. The answer is len(components).

Why it works:
    A BFS from v reaches exactly the vertices connected to v. Any vertex left
    unvisited must lie in a different component.

Time complexity:
    O(V + E): each vertex and edge is processed once overall.

Space complexity:
    O(V + E) for the adjacency list, O(V) for visited.

Edge cases:
    - n = 0 gives 0 components.
    - No edges: every vertex is its own component (n components).
    - Fully connected graph: exactly 1 component.
    - Invalid edge endpoints raise ValueError.

Alternative approach:
    Union-Find (disjoint set union) counts components in near O(E) time and
    supports adding edges online.
"""

from collections import deque


def build_graph(vertex_count, edges):
    graph = {vertex: [] for vertex in range(vertex_count)}
    for u, v in edges:
        if u not in graph or v not in graph:
            raise ValueError("edge (%s, %s) uses an unknown vertex" % (u, v))
        graph[u].append(v)
        graph[v].append(u)
    return graph


def collect_component(graph, start, visited):
    """BFS from start, marking vertices visited; return the component."""
    visited.add(start)
    queue = deque([start])
    component = []
    while queue:
        vertex = queue.popleft()
        component.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return component


def connected_components(vertex_count, edges):
    """Return a list of components (each a list of vertices)."""
    graph = build_graph(vertex_count, edges)
    visited = set()
    components = []
    for vertex in range(vertex_count):
        if vertex not in visited:
            components.append(collect_component(graph, vertex, visited))
    return components


def main():
    components = connected_components(7, [(0, 1), (1, 2), (3, 4)])
    print("Component count:", len(components))
    for number, component in enumerate(components, start=1):
        print("Component %d: %s" % (number, component))

    # Edge cases
    print("No vertices:", len(connected_components(0, [])))
    print("No edges (4 vertices):", len(connected_components(4, [])))
    print("Fully connected:", len(connected_components(3, [(0, 1), (1, 2), (0, 2)])))


if __name__ == "__main__":
    main()
