r"""
Problem title: NumPy Array Operations - Vectorising, Broadcasting and Statistics

Problem statement:
    Given the daily sales of a shop, apply a 10 percent discount, find totals,
    average, maximum and its day, count days above the average, and compare the
    NumPy approach with an explicit Python loop.

What it teaches:
    Vectorised operations (work on the whole array without a Python loop),
    broadcasting (scalar with array, row with matrix), aggregate functions and
    boolean filtering. (Requires NumPy: python -m pip install numpy)

Input example:
    sales = np.array([120, 340, 90, 560, 210, 430, 75])

Expected output:
    sales: [120 340  90 560 210 430  75]
    with 10% discount: [108.  306.   81.  504.  189.  387.   67.5]
    total: 1825 | average: 260.71
    maximum: 560 on day index 3
    minimum: 75 on day index 6
    days above average: [340 560 430]
    sorted: [ 75  90 120 210 340 430 560]
    cumulative: [ 120  460  550 1110 1320 1750 1825]
    element-wise sales + sales: [ 240  680  180 1120  420  860  150]
    broadcasting matrix + row: [[11, 22, 33], [14, 25, 36]]
    column means: [2.5, 3.5, 4.5]
    loop total equals NumPy total: True
    empty sum: 0.0 | empty days above average: []
    empty.max() -> ValueError

Approach:
    Use array arithmetic (sales * 0.9), aggregate methods (sum, mean, max,
    argmax), a boolean mask for filtering and np.sort for ordering.

Step-by-step logic:
    1. discounted = sales * 0.9 - applied to every element at once.
    2. total = sales.sum(); average = sales.mean().
    3. best_day = sales.argmax() - the INDEX of the maximum.
    4. above = sales[sales > average] - boolean filtering.
    5. Broadcasting: matrix + row adds the row to every matrix row.
    6. Verify against a hand-written Python loop.

Why it works:
    NumPy runs these loops in compiled C over contiguous typed memory, so the
    Python interpreter is not involved for each element.

Time complexity:
    O(n) for arithmetic, sum, mean, max, argmax and filtering; O(n log n) for
    np.sort.

Space complexity:
    O(n) for each new result array; aggregates (sum, mean) need O(1).

Edge cases:
    - Empty array: sum is 0 but max/argmax raise ValueError.
    - Integer array times 0.9 becomes float.
    - Broadcasting needs compatible shapes (3 columns with a length-3 row only).
    - Integer division and overflow depend on the dtype.

Alternative approach:
    The same results with plain Python loops or list comprehensions - correct
    but slower on large data (see the loop check at the end).
"""

try:
    import numpy as np
except ImportError:
    raise SystemExit("NumPy is required: python -m pip install numpy")


def apply_discount(sales, percent):
    """Return a new array with the discount applied to every element."""
    return sales * (1 - percent / 100)


def loop_total(sales):
    """Plain Python loop version of the total, used to verify NumPy."""
    total = 0
    for value in sales:
        total += int(value)
    return total


def days_above_average(sales):
    if sales.size == 0:
        return sales
    return sales[sales > sales.mean()]


def main():
    sales = np.array([120, 340, 90, 560, 210, 430, 75])
    print("sales:", sales)
    print("with 10% discount:", apply_discount(sales, 10))
    print("total:", sales.sum(), "| average:", round(float(sales.mean()), 2))
    print("maximum:", sales.max(), "on day index", sales.argmax())
    print("minimum:", sales.min(), "on day index", sales.argmin())
    print("days above average:", days_above_average(sales))
    print("sorted:", np.sort(sales))
    print("cumulative:", sales.cumsum())
    print("element-wise sales + sales:", sales + sales)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    row = np.array([10, 20, 30])
    print("broadcasting matrix + row:", (matrix + row).tolist())
    print("column means:", matrix.mean(axis=0).tolist())

    print("loop total equals NumPy total:", loop_total(sales) == int(sales.sum()))
    empty = np.array([])
    print("empty sum:", empty.sum(), "| empty days above average:", days_above_average(empty))
    try:
        empty.max()
    except ValueError as error:
        print("empty.max() -> ValueError")


if __name__ == "__main__":
    main()
