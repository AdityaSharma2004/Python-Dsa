"""
Problem title:
    Detect a Cycle in an Undirected Graph

Problem statement:
    Given an undirected graph (adjacency list), return True if it contains a
    cycle, otherwise False. The graph may be disconnected.

What it teaches:
    - DFS with a "parent" argument to ignore the edge we just came through.
    - A cycle is found when we meet an already visited vertex that is not our
      parent.
    - Handling disconnected graphs by starting a DFS from every component.

Input example:
    tree  = {0: [1, 2], 1: [0], 2: [0]}          -> no cycle
    cycle = {0: [1, 2], 1: [0, 2], 2: [0, 1]}    -> cycle 0-1-2

Expected output:
    Tree has cycle: False
    Triangle has cycle: True
    Cycle only in second component: True
    Self-loop: True
    Empty graph: False
    Path graph: False

Approach:
    DFS from each unvisited vertex, passing along the vertex we came from.
    If a neighbour is visited and is not the parent, a back edge exists.

Step-by-step logic:
    1. For each unvisited vertex, call dfs(vertex, parent=None).
    2. In dfs: mark visited. For each neighbour:
       - not visited: recurse; if that returns True, return True.
       - visited and neighbour != parent: cycle found.
    3. If every call returns False, there is no cycle.

Why it works:
    In an undirected tree, the only visited neighbour of a vertex is its
    parent. Any other visited neighbour gives a second route between two
    vertices, which is exactly a cycle.

Time complexity:
    O(V + E).

Space complexity:
    O(V) for visited and recursion depth.

Edge cases:
    - Disconnected graph where only one component has a cycle.
    - Self-loop (v in graph[v]) is a cycle.
    - Parallel edges (the same edge listed twice) form a cycle of length 2;
      this simple version treats them as the "parent" edge and would miss
      them, so inputs are assumed to be simple graphs.
    - Empty graph: no cycle.

Alternative approach:
    Union-Find: process edges; if both endpoints already share a root, the
    edge closes a cycle.
"""


def has_cycle(graph):
    """Return True if the undirected graph contains a cycle."""
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, vertex):
                    return True
            elif neighbour != parent:
                return True  # visited and not where we came from: back edge
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False


def main():
    tree = {0: [1, 2], 1: [0], 2: [0]}
    triangle = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Tree has cycle:", has_cycle(tree))
    print("Triangle has cycle:", has_cycle(triangle))

    # Edge cases
    mixed = {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]}
    print("Cycle only in second component:", has_cycle(mixed))
    print("Self-loop:", has_cycle({0: [0]}))
    print("Empty graph:", has_cycle({}))
    print("Path graph:", has_cycle({0: [1], 1: [0, 2], 2: [1]}))


if __name__ == "__main__":
    main()
