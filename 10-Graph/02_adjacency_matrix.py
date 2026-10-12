"""
Problem title:
    Build a Graph with an Adjacency Matrix

Problem statement:
    Given n vertices and a list of undirected edges, build an n x n adjacency
    matrix where matrix[u][v] = 1 if an edge joins u and v, else 0. Provide
    helper functions to check an edge and to list the neighbours of a vertex.

What it teaches:
    - Matrix representation of a graph and when it is better than a list.
    - Symmetry of the matrix for undirected graphs.
    - Space/time trade-off: O(1) edge lookup but O(V^2) memory.

Input example:
    n = 4
    edges = [(0, 1), (0, 2), (2, 3)]

Expected output:
       0 1 2 3
    0: 0 1 1 0
    1: 1 0 0 0
    2: 1 0 0 1
    3: 0 0 1 0
    Edge 0-1? True
    Edge 1-3? False
    Neighbours of 2: [0, 3]
    Empty matrix: []
    Error: edge (0, 9) uses an unknown vertex

Approach:
    Create an n x n grid of zeros. For each edge (u, v) set both
    matrix[u][v] and matrix[v][u] to 1.

Step-by-step logic:
    1. Make n rows of n zeros (build each row separately so rows are not
       shared references).
    2. For every edge set the two symmetric cells to 1.
    3. has_edge(u, v) is just a cell lookup.
    4. neighbours(u) scans row u and collects the columns holding 1.

Why it works:
    Row u, column v answers the question "is v adjacent to u?" directly.

Time complexity:
    Build: O(V^2) to create the matrix + O(E) to fill it.
    has_edge: O(1). neighbours: O(V).

Space complexity:
    O(V^2) regardless of how many edges exist.

Edge cases:
    - n = 0 gives an empty matrix.
    - Invalid vertex numbers raise ValueError.
    - Duplicate edges just set the same cell again (no change).
    - Dense graphs suit a matrix; sparse graphs waste space.

Alternative approach:
    Adjacency list (01_adjacency_list.py): O(V + E) space, O(degree) lookup.
"""


def build_adjacency_matrix(vertex_count, edges):
    """Return a list of lists matrix for an undirected graph."""
    # Build each row separately: [[0] * n] * n would share one row object.
    matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    for u, v in edges:
        if not (0 <= u < vertex_count and 0 <= v < vertex_count):
            raise ValueError("edge (%s, %s) uses an unknown vertex" % (u, v))
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


def has_edge(matrix, u, v):
    """O(1) edge check."""
    return matrix[u][v] == 1


def neighbours(matrix, u):
    """Scan row u and return the vertices adjacent to u."""
    return [v for v in range(len(matrix)) if matrix[u][v] == 1]


def print_matrix(matrix):
    """Print the matrix with a header row."""
    size = len(matrix)
    print("   " + " ".join(str(i) for i in range(size)))
    for u in range(size):
        print("%d: %s" % (u, " ".join(str(cell) for cell in matrix[u])))


def main():
    edges = [(0, 1), (0, 2), (2, 3)]
    matrix = build_adjacency_matrix(4, edges)
    print_matrix(matrix)
    print("Edge 0-1?", has_edge(matrix, 0, 1))
    print("Edge 1-3?", has_edge(matrix, 1, 3))
    print("Neighbours of 2:", neighbours(matrix, 2))

    # Edge cases
    print("Empty matrix:", build_adjacency_matrix(0, []))
    try:
        build_adjacency_matrix(2, [(0, 9)])
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
