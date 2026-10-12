r"""
Problem title: Two-Dimensional Arrays (Matrices) - Python Lists and NumPy

Problem statement:
    For a 3 x 4 matrix compute row sums, column sums, the transpose and the
    main-diagonal sum - first with nested Python lists, then with NumPy - and
    check that both give the same answers.

What it teaches:
    A 2D array is an array of rows. Row-major traversal uses two nested loops;
    NumPy does the same work with the axis argument. Also teaches the common
    bug of building a matrix with [[0] * cols] * rows (shared rows).

Input example:
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]

Expected output:
    matrix: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    row sums: [10, 26, 42]
    column sums: [15, 18, 21, 24]
    transpose: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    diagonal sum: 18
    NumPy shape: (3, 4)
    NumPy row sums: [10, 26, 42]
    NumPy column sums: [15, 18, 21, 24]
    NumPy transpose: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    NumPy diagonal sum: 18
    pure Python equals NumPy: True
    correct matrix: [[7, 0, 0], [0, 0, 0]]
    shared-row bug: [[7, 0, 0], [7, 0, 0]]
    empty matrix: [] [] []

Approach:
    Pure Python: nested loops with row and column indices.
    NumPy: arr.sum(axis=1), arr.sum(axis=0), arr.T, arr.trace().

Step-by-step logic:
    1. Row sum: for each row add all its columns.
    2. Column sum: for each column index add matrix[row][column] over all rows.
    3. Transpose: new[col][row] = old[row][col] (rows become columns).
    4. Diagonal: add matrix[i][i] for i up to the smaller dimension.
    5. Compare with NumPy results.

Why it works:
    Element (r, c) is stored at row r, position c, so two indices reach any
    element in O(1); visiting all r * c elements costs O(r * c).

Time complexity:
    O(rows * cols) for row sums, column sums and transpose; O(min(rows, cols))
    for the diagonal.

Space complexity:
    O(rows + cols) for the sum lists, O(rows * cols) for the transpose.

Edge cases:
    - Empty matrix [] (no rows) and rows with zero columns.
    - Non-square matrices: the diagonal stops at the shorter side.
    - Ragged rows (different lengths) are not valid matrices.
    - [[0] * 3] * 2 makes two names for the SAME row - build rows in a loop.

Alternative approach:
    zip(*matrix) transposes in one line; NumPy is far faster for large data.
"""

try:
    import numpy as np
except ImportError:
    raise SystemExit("NumPy is required: python -m pip install numpy")


def row_sums(matrix):
    sums = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        sums.append(total)
    return sums


def column_sums(matrix):
    if len(matrix) == 0:
        return []
    sums = []
    for col in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
            total += matrix[row][col]
        sums.append(total)
    return sums


def transpose(matrix):
    if len(matrix) == 0:
        return []
    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])  # old (row, col) -> new (col, row)
        result.append(new_row)
    return result


def diagonal_sum(matrix):
    total = 0
    if len(matrix) == 0:
        return total
    steps = len(matrix)
    if len(matrix[0]) < steps:
        steps = len(matrix[0])
    for i in range(steps):
        total += matrix[i][i]
    return total


def create_matrix(rows, cols, fill=0):
    """Correct way: every row is its own list."""
    matrix = []
    for _ in range(rows):
        matrix.append([fill] * cols)
    return matrix


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print("matrix:", matrix)
    print("row sums:", row_sums(matrix))
    print("column sums:", column_sums(matrix))
    print("transpose:", transpose(matrix))
    print("diagonal sum:", diagonal_sum(matrix))

    arr = np.array(matrix)
    print("NumPy shape:", arr.shape)
    print("NumPy row sums:", arr.sum(axis=1).tolist())
    print("NumPy column sums:", arr.sum(axis=0).tolist())
    print("NumPy transpose:", arr.T.tolist())
    print("NumPy diagonal sum:", int(arr.trace()))
    same = (row_sums(matrix) == arr.sum(axis=1).tolist()
            and column_sums(matrix) == arr.sum(axis=0).tolist()
            and transpose(matrix) == arr.T.tolist())
    print("pure Python equals NumPy:", same)

    grid = create_matrix(2, 3)
    grid[0][0] = 7
    shared = [[0] * 3] * 2  # the classic bug: both rows are the same list
    shared[0][0] = 7
    print("correct matrix:", grid)
    print("shared-row bug:", shared)
    print("empty matrix:", row_sums([]), column_sums([]), transpose([]))


if __name__ == "__main__":
    main()
