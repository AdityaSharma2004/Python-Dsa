"""
Problem title:
    Build a Graph with an Adjacency List

Problem statement:
    Given the number of vertices n (labelled 0..n-1) and a list of undirected
    edges, build an adjacency list (a dictionary mapping each vertex to the
    list of its neighbours). Then print each vertex's neighbours and degree.

What it teaches:
    - The most common graph representation used in interviews.
    - How an undirected edge is stored twice (once for each endpoint).
    - Degree of a vertex = number of neighbours.
    - Laravel analogy: think of a table of "friendships" where each user row
      lists the ids of related users.

Input example:
    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

Expected output:
    0 -> [1, 2] (degree 2)
    1 -> [0, 3] (degree 2)
    2 -> [0, 3] (degree 2)
    3 -> [1, 2, 4] (degree 3)
    4 -> [3] (degree 1)
    Empty graph: {}
    Isolated vertices: {0: [], 1: [], 2: []}
    Error: edge (0, 5) uses an unknown vertex

Approach:
    Create a dict with an empty list for every vertex, then for every edge
    (u, v) append v to u's list and u to v's list.

Step-by-step logic:
    1. Start with {0: [], 1: [], 2: [], 3: [], 4: []}.
    2. Edge (0, 1): 0 -> [1], 1 -> [0].
    3. Edge (0, 2): 0 -> [1, 2], 2 -> [0].
    4. Continue for every edge.
    5. Degree of a vertex is the length of its list.

Why it works:
    The list of a vertex contains exactly the vertices directly connected to
    it, so "who are my neighbours?" is answered in O(degree) time.

Time complexity:
    O(V + E) to build (V vertices created, E edges added, two appends each).

Space complexity:
    O(V + E) - every edge is stored twice.

Edge cases:
    - A vertex with no edges still appears with an empty list.
    - Self-loop (u, u) is stored once in this implementation.
    - Edges that mention a vertex outside 0..n-1 are rejected with ValueError.
    - n = 0 gives an empty graph.

Alternative approach:
    An adjacency matrix (see 02_adjacency_matrix.py) answers "is there an
    edge u-v?" in O(1) but needs O(V^2) space.
"""


def build_adjacency_list(vertex_count, edges):
    """Return a dict {vertex: [neighbours]} for an undirected graph."""
    graph = {vertex: [] for vertex in range(vertex_count)}
    for u, v in edges:
        if u not in graph or v not in graph:
            raise ValueError("edge (%s, %s) uses an unknown vertex" % (u, v))
        graph[u].append(v)
        if u != v:  # a self-loop must not be added twice
            graph[v].append(u)
    return graph


def degree(graph, vertex):
    """Number of neighbours of a vertex."""
    return len(graph[vertex])


def print_graph(graph):
    """Print every vertex with its neighbours and degree."""
    for vertex in graph:
        print("%d -> %s (degree %d)" % (vertex, graph[vertex], degree(graph, vertex)))


def main():
    vertex_count = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    graph = build_adjacency_list(vertex_count, edges)
    print_graph(graph)

    # Edge cases
    print("Empty graph:", build_adjacency_list(0, []))
    print("Isolated vertices:", build_adjacency_list(3, []))
    try:
        build_adjacency_list(2, [(0, 5)])
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
