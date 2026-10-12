r"""
Problem: Shortest Path in a Grid Maze Using BFS

Problem statement:
    A grid contains open cells (0) and walls (1). Find the length of the
    shortest path from the top-left cell to the bottom-right cell moving up,
    down, left or right, and print one such path. Return -1 if none exists.

What it teaches:
    Breadth-first search with a queue: it explores cells in order of distance,
    so the first time the goal is reached is the shortest route.

Input example:
    0 0 0
    1 1 0
    0 0 0

Expected output:
    Maze 1: shortest path has 4 moves
    path: (0, 0) (0, 1) (0, 2) (1, 2) (2, 2)
    Maze 2: no path (-1)
    Maze 3: shortest path has 0 moves
    path: (0, 0)
    Maze 4: shortest path has 6 moves
    path: (0, 0) (1, 0) (2, 0) (3, 0) (3, 1) (3, 2) (3, 3)

Approach:
    BFS from the start. Each queue entry is a cell; a parent dictionary
    remembers how each cell was reached, which also marks it as visited.

Step-by-step logic:
    1. If the start or goal is a wall, return no path.
    2. Enqueue the start; parent[start] = None.
    3. Dequeue a cell; if it is the goal stop.
    4. For each of its 4 neighbours inside the grid, not a wall and not yet
    in parent: record the parent and enqueue it.
    5. Rebuild the path by following parents back from the goal, then
    reverse it with a stack (a plain list popped in order).

Why it works:
    The queue processes all cells at distance d before any at distance d + 1,
    so the first arrival at the goal uses the fewest moves.

Time complexity:
    O(rows * cols): each cell is enqueued at most once and has 4 neighbours.

Space complexity:
    O(rows * cols) for the queue and parent map.

Edge cases:
    Start equals goal (1x1 grid), blocked start or goal, no route, empty grid,
    long winding corridors.

Alternative approach:
    DFS finds a path but not necessarily the shortest one; Dijkstra or A*
    handle weighted grids.
"""

from collections import deque


def shortest_path(grid):
    if not grid or not grid[0]:
        return None
    rows, cols = len(grid), len(grid[0])
    start, goal = (0, 0), (rows - 1, cols - 1)
    if grid[0][0] == 1 or grid[goal[0]][goal[1]] == 1:
        return None
    parent = {start: None}
    queue = deque([start])
    while queue:
        cell = queue.popleft()
        if cell == goal:
            break
        row, col = cell
        for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nxt = (row + d_row, col + d_col)
            inside = 0 <= nxt[0] < rows and 0 <= nxt[1] < cols
            if inside and grid[nxt[0]][nxt[1]] == 0 and nxt not in parent:
                parent[nxt] = cell
                queue.append(nxt)
    if goal not in parent:
        return None
    path = []
    cell = goal
    while cell is not None:  # walk back from goal to start
        path.append(cell)
        cell = parent[cell]
    ordered = []
    while path:  # popping the stack gives start -> goal order
        ordered.append(path.pop())
    return ordered


def main():
    mazes = [
        [[0, 0, 0], [1, 1, 0], [0, 0, 0]],
        [[0, 1], [1, 0]],
        [[0]],
        [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    ]
    for number, grid in enumerate(mazes, start=1):
        path = shortest_path(grid)
        if path is None:
            print("Maze %d: no path (-1)" % number)
        else:
            print("Maze %d: shortest path has %d moves" % (number, len(path) - 1))
            print("path:", " ".join(str(cell) for cell in path))


if __name__ == "__main__":
    main()
