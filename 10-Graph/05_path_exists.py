"""
Problem title:
    Does a Path Exist Between Two Vertices?

Problem statement:
    Given an undirected graph (adjacency list), a source and a destination,
    return True if you can travel from source to destination along edges,
    and also return one such path when it exists.

What it teaches:
    - Path finding with DFS and a parent/path record.
    - Reachability: the most basic graph question.
    - Reconstructing a path by remembering how each vertex was reached.

Input example:
    graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: [5], 5: [4]}
    (0, 3) and (0, 5)

Expected output:
    0 -> 3: exists=True path=[0, 1, 3]
    0 -> 5: exists=False path=None
    2 -> 2: exists=True path=[2]
    3 -> 2: exists=True path=[3, 1, 0, 2]
    Error: source or destination is not in the graph

Approach:
    Run an iterative DFS from the source, storing parent[v] = the vertex we
    came from. If the destination is reached, walk the parents backwards.

Step-by-step logic:
    1. If source == destination the path is [source].
    2. Push source on a stack, parent[source] = None.
    3. Pop a vertex; for each unseen neighbour set its parent and push it.
    4. If destination gets a parent, rebuild the path by following parents
       from destination back to source, then flip the list.

Why it works:
    Every vertex reachable from the source is eventually discovered, and its
    parent chain is a valid walk back to the source.

Time complexity:
    O(V + E).

Space complexity:
    O(V) for the parent map and stack.

Edge cases:
    - source == destination is trivially reachable.
    - Different components: no path (returns None).
    - Unknown vertices raise ValueError.
    - The path found by DFS is valid but not necessarily the shortest
      (use BFS for that, see 06_shortest_path_unweighted.py).

Alternative approach:
    BFS gives the same reachability answer and also the shortest path.
"""


def find_path(graph, source, destination):
    """Return one path as a list of vertices, or None if unreachable."""
    if source not in graph or destination not in graph:
        raise ValueError("source or destination is not in the graph")
    if source == destination:
        return [source]
    parent = {source: None}
    stack = [source]
    while stack:
        vertex = stack.pop()
        for neighbour in graph[vertex]:
            if neighbour not in parent:
                parent[neighbour] = vertex
                if neighbour == destination:
                    return build_path(parent, destination)
                stack.append(neighbour)
    return None


def build_path(parent, destination):
    """Follow parent links from destination back to the source."""
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parent[current]
    # Reverse manually: the list was built destination -> source.
    left, right = 0, len(path) - 1
    while left < right:
        path[left], path[right] = path[right], path[left]
        left += 1
        right -= 1
    return path


def path_exists(graph, source, destination):
    """True when destination is reachable from source."""
    return find_path(graph, source, destination) is not None


def main():
    graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: [5], 5: [4]}
    for source, destination in [(0, 3), (0, 5), (2, 2), (3, 2)]:
        path = find_path(graph, source, destination)
        print("%d -> %d: exists=%s path=%s" % (
            source, destination, path_exists(graph, source, destination), path))
    try:
        find_path(graph, 0, 42)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
