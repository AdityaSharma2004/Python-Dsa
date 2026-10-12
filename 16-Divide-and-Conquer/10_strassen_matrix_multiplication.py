"""
Problem Title: Strassen Matrix Multiplication

Problem Statement:
    Multiply two n x n matrices (n a power of two) with Strassen's divide and
    conquer algorithm, using 7 recursive block multiplications instead of 8.

What It Teaches:
    - Block (sub-matrix) decomposition.
    - Reducing the number of recursive calls with algebra: T(n) = 7T(n/2) +
      O(n^2) -> O(n^2.807).
    - Matrix helper functions (add, subtract, split, join).

Input Example:
    A = [[1, 2], [3, 4]]       B = [[5, 6], [7, 8]]
    plus a 4 x 4 case

Expected Output:
    2x2 result: [[19, 22], [43, 50]]
    [5, 6, 7, 10]
    [13, 14, 15, 30]
    [21, 22, 23, 50]
    [29, 30, 31, 70]
    Strassen matches classic multiplication.
    3x3 -> matrices must be square, equal size, power of two

Approach:
    Split each matrix into four quadrants (A11, A12, A21, A22 ...). Compute
    the seven products M1..M7 and assemble the result quadrants from sums and
    differences of them.

Step-by-Step Logic:
    1. Base case: 1 x 1 matrices -> multiply the numbers.
    2. Split A and B into quadrants of size n/2.
    3. M1 = (A11 + A22)(B11 + B22)   M2 = (A21 + A22) B11
       M3 = A11 (B12 - B22)          M4 = A22 (B21 - B11)
       M5 = (A11 + A12) B22          M6 = (A21 - A11)(B11 + B12)
       M7 = (A12 - A22)(B21 + B22)
    4. C11 = M1 + M4 - M5 + M7     C12 = M3 + M5
       C21 = M2 + M4               C22 = M1 - M2 + M3 + M6
    5. Join the four quadrants.

Why It Works:
    Each C block equals the usual block formula (for example C12 = A11 B12 +
    A12 B22) after substituting the M expressions; the algebra cancels the
    extra terms. We verify against the ordinary triple-loop product.

Time Complexity:
    O(n^log2(7)) ~ O(n^2.807) multiplications (standard method is O(n^3)).
    For tiny matrices the overhead makes Strassen slower in practice.
Space Complexity:
    O(n^2) for the temporary sub-matrices.

Edge Cases:
    1 x 1 matrices, non-power-of-two sizes (we reject them; padding with zeros
    is the usual fix), identity and zero matrices, negative entries.

Alternative Approach:
    Classic triple loop, O(n^3), included as the verification reference.
"""


def add(a, b):
    """Element-wise a + b."""
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def subtract(a, b):
    """Element-wise a - b."""
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def split(matrix):
    """Return the four quadrants of a square matrix with even size."""
    half = len(matrix) // 2
    top_left = [row[:half] for row in matrix[:half]]
    top_right = [row[half:] for row in matrix[:half]]
    bottom_left = [row[:half] for row in matrix[half:]]
    bottom_right = [row[half:] for row in matrix[half:]]
    return top_left, top_right, bottom_left, bottom_right


def join(c11, c12, c21, c22):
    """Glue four quadrants back into one matrix."""
    top = [c11[i] + c12[i] for i in range(len(c11))]
    bottom = [c21[i] + c22[i] for i in range(len(c21))]
    return top + bottom


def strassen(a, b):
    """Multiply square matrices whose size is a power of two."""
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    m1 = strassen(add(a11, a22), add(b11, b22))
    m2 = strassen(add(a21, a22), b11)
    m3 = strassen(a11, subtract(b12, b22))
    m4 = strassen(a22, subtract(b21, b11))
    m5 = strassen(add(a11, a12), b22)
    m6 = strassen(subtract(a21, a11), add(b11, b12))
    m7 = strassen(subtract(a12, a22), add(b21, b22))
    c11 = add(subtract(add(m1, m4), m5), m7)
    c12 = add(m3, m5)
    c21 = add(m2, m4)
    c22 = add(add(subtract(m1, m2), m3), m6)
    return join(c11, c12, c21, c22)


def classic_multiply(a, b):
    """Standard O(n^3) multiplication for verification."""
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def is_power_of_two(n):
    """True for 1, 2, 4, 8 ..."""
    return n > 0 and (n & (n - 1)) == 0


def multiply(a, b):
    """Validate sizes, then call strassen."""
    if len(a) != len(b) or not is_power_of_two(len(a)):
        raise ValueError("matrices must be square, equal size, power of two")
    return strassen(a, b)


def main():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print("2x2 result:", multiply(a, b))
    assert multiply(a, b) == classic_multiply(a, b)
    a4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    b4 = [[1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, 3], [1, 1, 1, -1]]
    result = multiply(a4, b4)
    for row in result:
        print(row)
    assert result == classic_multiply(a4, b4)
    print("Strassen matches classic multiplication.")
    try:
        multiply([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    except ValueError as error:
        print("3x3 ->", error)


if __name__ == "__main__":
    main()
