"""
Problem title:
    Depth-First Search (DFS) Traversal (Recursive and Iterative)

Problem statement:
    Given an adjacency list and a start vertex, return the vertices in DFS
    order: go as deep as possible along one path before backtracking.

What it teaches:
    - Recursion on graphs and the equivalent explicit stack.
    - Why neighbours must be pushed in reverse for the iterative version to
      match the recursive order.
    - Backtracking intuition used in cycle detection, components, etc.

Input example:
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    start = 0

Expected output:
    Recursive DFS: [0, 1, 3, 4, 2, 5]
    Iterative DFS: [0, 1, 3, 4, 2, 5]
    Same order? True
    Single vertex: [1]
    Triangle: [0, 1, 2]
    Long path visited: 5000

Approach:
    Recursive: visit a vertex, then recurse into each unvisited neighbour.
    Iterative: use a list as a stack; pop a vertex, visit it if new, push its
    neighbours in reverse order.

Step-by-step logic (recursive):
    1. Mark vertex visited and append to the result.
    2. For each neighbour: if not visited, call dfs on it.
    3. Returning from a call is the "backtrack".

Why it works:
    The call stack (or explicit stack) always holds the current path, so the
    most recently discovered vertex is explored first.

Time complexity:
    O(V + E) for both versions.

Space complexity:
    O(V): visited set plus recursion depth / stack (up to V in a path graph).

Edge cases:
    - Very deep graphs (thousands of vertices in a line) can overflow Python's
      recursion limit; the iterative version avoids that.
    - Cycles are handled by the visited set.
    - Unknown start vertex raises ValueError.

Alternative approach:
    BFS (03_bfs_traversal.py) uses a queue and explores by level.
"""


def dfs_recursive(graph, start):
    """Return DFS order using recursion."""
    if start not in graph:
        raise ValueError("start vertex %s is not in the graph" % start)
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def dfs_iterative(graph, start):
    """Return DFS order using an explicit stack (same order as recursive)."""
    if start not in graph:
        raise ValueError("start vertex %s is not in the graph" % start)
    visited = set()
    order = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        # Push in reverse so the first neighbour is popped first.
        for index in range(len(graph[vertex]) - 1, -1, -1):
            neighbour = graph[vertex][index]
            if neighbour not in visited:
                stack.append(neighbour)
    return order


def main():
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    print("Recursive DFS:", dfs_recursive(graph, 0))
    print("Iterative DFS:", dfs_iterative(graph, 0))
    print("Same order?", dfs_recursive(graph, 0) == dfs_iterative(graph, 0))

    # Edge cases
    print("Single vertex:", dfs_recursive({1: []}, 1))
    cyclic = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Triangle:", dfs_iterative(cyclic, 0))
    # Long path: iterative version copes with depth beyond the recursion limit
    long_path = {i: [j for j in (i - 1, i + 1) if 0 <= j < 5000] for i in range(5000)}
    print("Long path visited:", len(dfs_iterative(long_path, 0)))


if __name__ == "__main__":
    main()
