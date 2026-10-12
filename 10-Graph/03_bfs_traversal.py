"""
Problem title:
    Breadth-First Search (BFS) Traversal

Problem statement:
    Given an adjacency list and a start vertex, return the vertices in the
    order BFS visits them (level by level, nearest vertices first).

What it teaches:
    - Using a queue to explore a graph layer by layer.
    - Why a visited set is needed (graphs can contain cycles).
    - Level-order thinking, the base for shortest paths in unweighted graphs.

Input example:
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    start = 0

Expected output:
    BFS from 0: [0, 1, 2, 3, 4, 5]
    BFS from 3: [3, 1, 0, 4, 2, 5]
    Single vertex: [7]
    Triangle (cycle): [0, 1, 2]
    Disconnected, from 0: [0, 1]
    Error: start vertex 99 is not in the graph

Approach:
    Keep a queue of vertices waiting to be explored. Mark a vertex visited
    when it is enqueued, so it is never queued twice.

Step-by-step logic:
    1. Put start in the queue and in the visited set.
    2. Remove the front vertex, append it to the result.
    3. For each neighbour not yet visited: mark it, enqueue it.
    4. Repeat until the queue is empty.

Why it works:
    A queue is first-in-first-out, so all vertices at distance d are
    processed before any vertex at distance d + 1.

Time complexity:
    O(V + E): each vertex is dequeued once and each edge is inspected
    once (twice in an undirected graph).

Space complexity:
    O(V) for the queue, visited set and result.

Edge cases:
    - A start vertex with no neighbours returns just [start].
    - Disconnected vertices are never reached.
    - Cycles are safe thanks to the visited set.
    - A start vertex not in the graph raises ValueError.

Alternative approach:
    DFS (04_dfs_traversal.py) visits in a different order using a stack.
"""

from collections import deque


def bfs(graph, start):
    """Return the list of vertices in BFS order from start."""
    if start not in graph:
        raise ValueError("start vertex %s is not in the graph" % start)
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)  # mark on enqueue to avoid duplicates
                queue.append(neighbour)
    return order


def main():
    graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    print("BFS from 0:", bfs(graph, 0))
    print("BFS from 3:", bfs(graph, 3))

    # Edge cases
    print("Single vertex:", bfs({7: []}, 7))
    cyclic = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Triangle (cycle):", bfs(cyclic, 0))
    disconnected = {0: [1], 1: [0], 2: []}
    print("Disconnected, from 0:", bfs(disconnected, 0))
    try:
        bfs(graph, 99)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
