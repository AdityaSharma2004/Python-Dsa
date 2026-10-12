r"""
Problem title: NumPy Basics - Creating, Indexing and Slicing Arrays

Problem statement:
    Create NumPy arrays in several ways, inspect their shape/dtype, and read or
    change elements using indexing, slicing, negative indices and boolean masks.

What it teaches:
    A NumPy array is a fixed-type, contiguous block of memory (a real "array"),
    unlike a Python list that stores references to objects. Slices are VIEWS,
    not copies. (Requires NumPy: python -m pip install numpy)

Input example:
    values = np.array([10, 20, 30, 40, 50, 60])

Expected output:
    values: [10 20 30 40 50 60]
    shape: (6,) | dtype: int64 | size: 6
    np.array([1, 2, 3]): [1 2 3]
    np.zeros(4): [0. 0. 0. 0.]
    np.ones(3, dtype=int): [1 1 1]
    np.arange(0, 10, 3): [0 3 6 9]
    np.linspace(0, 1, 5): [0.   0.25 0.5  0.75 1.  ]
    mixed ints+float: [1.  2.  3.5] dtype = float64
    values[0]: 10 | values[-1]: 60
    values[1:4]: [20 30 40]
    values[::2]: [10 30 50]
    values[::-1]: [60 50 40 30 20 10]
    mask (values > 25): [False False  True  True  True  True]
    selected: [30 40 50 60]
    after view[0] = 999 -> original: [ 10 999  30  40  50  60]
    independent copy unchanged: [20 30]
    values[10] -> IndexError: index 10 is out of bounds for axis 0 with size 6

Approach:
    Use np.array, np.zeros, np.ones, np.arange and np.linspace for creation and
    the usual [start:stop:step] syntax for access.

Step-by-step logic:
    1. Build arrays and print shape, dtype and size.
    2. Index with values[0], values[-1]; slice values[1:4], values[::2].
    3. Show that a slice shares memory: changing the slice changes the original.
    4. Use .copy() to get an independent array.
    5. Boolean mask: values[values > 25] keeps only matching elements.

Why it works:
    All elements have the same type and size, so element i is found by simple
    address arithmetic (start + i * item_size) - O(1) access.

Time complexity:
    Indexing O(1); slicing O(1) (a view); copy / boolean mask O(n).

Space complexity:
    Views O(1) extra; copy and mask results O(n).

Edge cases:
    - Index out of range raises IndexError (same as lists).
    - Mixed types are converted to one dtype (ints + float -> float).
    - Forgetting .copy() and accidentally modifying the original array.

Alternative approach:
    Plain Python lists (see files 01-07) work for the same tasks but are slower
    for numeric work and have no vectorised operations.
"""

try:
    import numpy as np
except ImportError:  # friendly message instead of a traceback
    raise SystemExit("NumPy is required: python -m pip install numpy")


def create_arrays():
    """Show common ways to create arrays."""
    print("np.array([1, 2, 3]):", np.array([1, 2, 3]))
    print("np.zeros(4):", np.zeros(4))
    print("np.ones(3, dtype=int):", np.ones(3, dtype=int))
    print("np.arange(0, 10, 3):", np.arange(0, 10, 3))
    print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))
    mixed = np.array([1, 2, 3.5])
    print("mixed ints+float:", mixed, "dtype =", mixed.dtype)


def inspect_array(values):
    print("shape:", values.shape, "| dtype:", values.dtype, "| size:", values.size)


def indexing_and_slicing(values):
    print("values[0]:", values[0], "| values[-1]:", values[-1])
    print("values[1:4]:", values[1:4])
    print("values[::2]:", values[::2])
    print("values[::-1]:", values[::-1])


def view_versus_copy(values):
    """A slice is a view; .copy() is independent."""
    view = values[1:3]
    independent = values[1:3].copy()
    view[0] = 999
    print("after view[0] = 999 -> original:", values)
    print("independent copy unchanged:", independent)


def boolean_mask(values):
    mask = values > 25
    print("mask (values > 25):", mask)
    print("selected:", values[mask])


def main():
    values = np.array([10, 20, 30, 40, 50, 60])
    print("values:", values)
    inspect_array(values)
    create_arrays()
    indexing_and_slicing(values)
    boolean_mask(values)
    view_versus_copy(values)
    try:
        print(values[10])
    except IndexError as error:
        print("values[10] -> IndexError:", error)


if __name__ == "__main__":
    main()
