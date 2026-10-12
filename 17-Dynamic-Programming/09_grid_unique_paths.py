"""
Problem Title: Unique Paths in a Grid (with Obstacles)

Problem Statement:
    A robot starts at the top-left cell of an m x n grid and may move only right
    or down. Count the paths to the bottom-right cell. Cells marked 1 are
    obstacles and cannot be entered. Also find the path with the minimum cost
    when each cell has a cost.

What It Teaches:
    - 2-D DP where each cell depends on its top and left neighbours.
    - Handling blocked cells.
    - The same table shape reused for counting (sum) and optimising (smaller).

Input Example:
    3 x 3 empty grid; grid with obstacle in the centre; cost grid
    [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

Expected Output:
    3x3 empty grid: 6
    7x3 empty grid: 28
    3x3 with centre obstacle: 2
    1x1 grid: 1
    Single row of 5: 1
    Blocked start: 0
    Wall across the middle: 0
    Minimum cost path total: 7

Approach:
    paths[r][c] = paths[r-1][c] + paths[r][c-1], and 0 if the cell is blocked.
    For the cost version: cost[r][c] = grid[r][c] + smaller of the top and left totals.

Step-by-Step Logic:
    1. If the start or end cell is blocked the answer is 0.
    2. paths[0][0] = 1. For the first row and column only one neighbour exists.
    3. Fill row by row; blocked cells stay 0.
    4. paths[m-1][n-1] is the answer.
    5. For costs use addition of the cell's own cost plus the cheaper neighbour.

Why It Works:
    Any path into a cell comes from the cell above or the cell to the left, and
    those two groups of paths never overlap.

Time Complexity:
    O(m * n).
Space Complexity:
    O(m * n) for the table (could be O(n) by keeping one row).

Edge Cases:
    1 x 1 grid, single row or column, blocked start or end, grid fully blocked
    in the middle.

Alternative Approach:
    Without obstacles the count is the binomial coefficient C(m+n-2, m-1).
"""


def count_paths(grid):
    """Count right/down paths; grid cells: 0 free, 1 obstacle."""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return 0
    paths = [[0] * cols for _ in range(rows)]
    paths[0][0] = 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                paths[r][c] = 0
            elif r > 0 or c > 0:
                from_top = paths[r - 1][c] if r > 0 else 0
                from_left = paths[r][c - 1] if c > 0 else 0
                paths[r][c] = from_top + from_left
    return paths[rows - 1][cols - 1]


def min_cost_path(cost):
    """Minimum total cost from top-left to bottom-right moving right/down."""
    rows, cols = len(cost), len(cost[0])
    total = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                total[r][c] = cost[r][c]
            elif r == 0:
                total[r][c] = total[r][c - 1] + cost[r][c]
            elif c == 0:
                total[r][c] = total[r - 1][c] + cost[r][c]
            else:
                better = total[r - 1][c] if total[r - 1][c] < total[r][c - 1] else total[r][c - 1]
                total[r][c] = better + cost[r][c]
    return total[rows - 1][cols - 1]


def empty_grid(rows, cols):
    """Build a rows x cols grid with no obstacles."""
    return [[0] * cols for _ in range(rows)]


def main():
    print("3x3 empty grid:", count_paths(empty_grid(3, 3)))
    print("7x3 empty grid:", count_paths(empty_grid(7, 3)))
    blocked = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print("3x3 with centre obstacle:", count_paths(blocked))
    print("1x1 grid:", count_paths([[0]]))
    print("Single row of 5:", count_paths(empty_grid(1, 5)))
    print("Blocked start:", count_paths([[1, 0], [0, 0]]))
    print("Wall across the middle:", count_paths([[0, 0], [1, 1], [0, 0]]))
    cost = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print("Minimum cost path total:", min_cost_path(cost))


if __name__ == "__main__":
    main()
