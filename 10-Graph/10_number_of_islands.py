"""
Problem title:
    Number of Islands (Grid as a Graph)

Problem statement:
    Given a 2D grid of '1' (land) and '0' (water), count the islands. An
    island is a group of land cells connected horizontally or vertically.

What it teaches:
    - Seeing a grid as an implicit graph: each cell is a vertex, its 4
      neighbours are the edges.
    - Connected components on a grid with BFS/DFS flood fill.
    - Bounds checking and marking visited cells in place.

Input example:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1

Expected output:
    Islands: 3
    Grid unchanged: ['1', '1', '0', '0', '0']
    Empty grid: 0
    All water: 0
    All land: 1
    Diagonal only: 2
    Single land cell: 1

Approach:
    Scan every cell. When an unvisited land cell is found, count one island
    and flood-fill all connected land with BFS.

Step-by-step logic:
    1. Work on a copy of the grid so the input is not destroyed.
    2. For each cell (r, c) holding '1': islands += 1, then BFS.
    3. In BFS, pop a cell, look at up/down/left/right; if inside the grid
       and '1', mark it '0' (visited) and enqueue it.
    4. Return islands.

Why it works:
    Flood fill erases an entire island once discovered, so each island is
    counted exactly once.

Time complexity:
    O(R * C): every cell is visited a constant number of times.

Space complexity:
    O(R * C) for the grid copy plus O(min(R, C)) to O(R * C) for the queue.

Edge cases:
    - Empty grid or empty rows: 0 islands.
    - All water: 0. All land: 1.
    - Diagonal cells are NOT connected.
    - Single-cell grids.

Alternative approach:
    DFS flood fill or Union-Find over cells.
"""

from collections import deque


def count_islands(grid):
    """Return the number of islands in the grid (list of lists of '0'/'1')."""
    if not grid or not grid[0]:
        return 0
    work = [list(row) for row in grid]  # copy so we can mark cells visited
    rows = len(work)
    cols = len(work[0])
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if work[r][c] == "1":
                islands += 1
                flood_fill(work, r, c, rows, cols)
    return islands


def flood_fill(work, start_row, start_col, rows, cols):
    """Turn every land cell connected to the start into water."""
    work[start_row][start_col] = "0"
    queue = deque([(start_row, start_col)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and work[nr][nc] == "1":
                work[nr][nc] = "0"
                queue.append((nr, nc))


def to_grid(lines):
    """Convert strings like '11000' to a list of character lists."""
    return [list(line) for line in lines]


def main():
    grid = to_grid(["11000", "11000", "00100", "00011"])
    print("Islands:", count_islands(grid))
    print("Grid unchanged:", grid[0])

    # Edge cases
    print("Empty grid:", count_islands([]))
    print("All water:", count_islands(to_grid(["000", "000"])))
    print("All land:", count_islands(to_grid(["111", "111"])))
    print("Diagonal only:", count_islands(to_grid(["10", "01"])))
    print("Single land cell:", count_islands(to_grid(["1"])))


if __name__ == "__main__":
    main()
