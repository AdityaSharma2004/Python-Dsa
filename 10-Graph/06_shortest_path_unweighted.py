"""
Problem title:
    Shortest Path in an Unweighted Graph

Problem statement:
    Given an undirected, unweighted graph, a source and a destination, return
    the minimum number of edges between them and one shortest path. Return
    (-1, None) if the destination cannot be reached.

What it teaches:
    - Why BFS finds shortest paths when every edge costs the same.
    - Storing distance and parent for each vertex.
    - Path reconstruction by walking parents backwards.

Input example:
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3], 5: []}
    (0, 4) and (0, 5)

Expected output:
    0 -> 4: distance=3 path=[0, 1, 3, 4]
    0 -> 0: distance=0 path=[0]
    0 -> 5: distance=-1 path=None
    4 -> 1: distance=2 path=[4, 3, 1]
    Error: source or destination is not in the graph

Approach:
    BFS from the source. The first time a vertex is discovered, the number of
    steps taken is its shortest distance.

Step-by-step logic:
    1. distance[source] = 0, parent[source] = None, queue = [source].
    2. Pop a vertex u. For each unseen neighbour v:
       distance[v] = distance[u] + 1, parent[v] = u, enqueue v.
    3. Stop early when the destination is discovered.
    4. Rebuild the path from destination back to source via parent.

Why it works:
    BFS processes vertices in non-decreasing distance order, so the first
    discovery of a vertex uses the fewest possible edges.

Time complexity:
    O(V + E).

Space complexity:
    O(V).

Edge cases:
    - source == destination: distance 0, path [source].
    - Unreachable destination: (-1, None).
    - Several shortest paths may exist; any one is acceptable.
    - Unknown vertices raise ValueError.
    - This does NOT work for weighted edges (use Dijkstra there).

Alternative approach:
    Run BFS from the destination too (bidirectional BFS) to cut the explored
    area on big graphs.
"""

from collections import deque


def shortest_path(graph, source, destination):
    """Return (distance, path) using BFS."""
    if source not in graph or destination not in graph:
        raise ValueError("source or destination is not in the graph")
    distance = {source: 0}
    parent = {source: None}
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            break
        for neighbour in graph[vertex]:
            if neighbour not in distance:
                distance[neighbour] = distance[vertex] + 1
                parent[neighbour] = vertex
                queue.append(neighbour)
    if destination not in distance:
        return -1, None
    return distance[destination], rebuild_path(parent, destination)


def rebuild_path(parent, destination):
    """Walk parent links back to the source and return the forward path."""
    backwards = []
    current = destination
    while current is not None:
        backwards.append(current)
        current = parent[current]
    path = []
    for index in range(len(backwards) - 1, -1, -1):
        path.append(backwards[index])
    return path


def main():
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3], 5: []}
    for source, destination in [(0, 4), (0, 0), (0, 5), (4, 1)]:
        distance, path = shortest_path(graph, source, destination)
        print("%d -> %d: distance=%d path=%s" % (source, destination, distance, path))
    try:
        shortest_path(graph, 0, 99)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
