# 02 - Arrays with Python and NumPy

Master arrays: traversal, insertion, deletion, searching, reversing, rotating, duplicates, merging, 2D arrays, and then the same ideas with NumPy. Files 01-07 use plain Python lists only; files 08-10 (the NumPy files) need NumPy.

## Table of Contents
- [A. Topic Introduction](#a-topic-introduction)
- [B. Core Concepts](#b-core-concepts)
- [C. How It Works](#c-how-it-works)
- [D. Time and Space Complexity](#d-time-and-space-complexity)
- [E. Problems for Practice](#e-problems-for-practice)
- [F. Installation Requirements](#f-installation-requirements)
- [G. How to Run the Files](#g-how-to-run-the-files)
- [H. Revision Notes](#h-revision-notes)

---

## A. Topic Introduction

**What it is.** An array is a collection of items stored one after another in memory and reached by a numeric index. In Python the everyday array is the `list`. NumPy adds a true fixed-type array (`ndarray`) built for fast numeric work.

**Why it matters in DSA.** Arrays are the most common data structure. Most other structures (stacks, queues, heaps, hash tables) are built on top of them, and a large share of interview questions are array questions: two pointers, searching, sliding windows, rotations.

**Where it is used.** Rows returned from a database query, CSV data, image pixels, game boards, spreadsheet grids, machine learning data, sales figures and reports.

**Everyday analogy.** A row of numbered lockers. If you know the locker number you open it instantly. Inserting a new locker in the middle means every locker after it must shift one place.

PHP link: a Python list used by position is like a PHP indexed array (`$items[2]`); NumPy is closer to a typed matrix library.

---

## B. Core Concepts

| Term | Meaning |
|------|---------|
| Index | Position of an element, starting at 0. |
| Length | Number of elements, `len(items)`. |
| Traversal | Visiting every element once. |
| Shifting | Moving elements to make or close a gap. |
| Two pointers | Two indexes that move through the array (from both ends or one behind the other). |
| In place | Changing the original array without a second array. |
| 2D array | An array of rows: `matrix[row][column]`. |
| `ndarray` | NumPy array: all elements share one type and are stored contiguously. |
| View vs copy | A NumPy slice shares memory with the original (view); `.copy()` makes an independent array. |
| Vectorised operation | One NumPy expression applied to all elements, no Python loop. |
| Broadcasting | NumPy stretches a smaller array (such as a scalar or a row) across a bigger one. |

```text
index:    0    1    2    3    4    5
        +----+----+----+----+----+----+
values: | 12 | 45 |  7 | 45 |  3 | 29 |
        +----+----+----+----+----+----+
negative: -6   -5   -4   -3   -2   -1
```

```text
2D array (3 rows x 4 columns)
          col0 col1 col2 col3
   row0 [  1    2    3    4 ]
   row1 [  5    6    7    8 ]
   row2 [  9   10   11   12 ]
element (1, 2) is 7  ->  matrix[1][2]
```

**Standard Python and NumPy are kept separate:** files 01-07 never import NumPy; files 08, 09 and 10 import it only inside the part that needs it (file 09 also contains a pure Python half).

---

## C. How It Works

**Insert 25 at index 2 into `[10, 20, 30, 40, 50]` (shift right, from the end)**

```text
start:        [10, 20, 30, 40, 50]
make room:    [10, 20, 30, 40, 50, __]
shift 50:     [10, 20, 30, 40, 50, 50]
shift 40:     [10, 20, 30, 40, 40, 50]
shift 30:     [10, 20, 30, 30, 40, 50]
write 25:     [10, 20, 25, 30, 40, 50]      3 shifts
```

Shifting must go right to left; going left to right would overwrite values you still need.

**Reverse with two pointers: `[1, 2, 3, 4]`**

```text
left=0 right=3  swap -> [4, 2, 3, 1]
left=1 right=2  swap -> [4, 3, 2, 1]
left=2 right=1  stop (crossed)
```

**Rotate right by 3 with three reversals: `[1..7]`**

| Step | Result |
|------|--------|
| reverse all | `[7, 6, 5, 4, 3, 2, 1]` |
| reverse first 3 | `[5, 6, 7, 4, 3, 2, 1]` |
| reverse last 4 | `[5, 6, 7, 1, 2, 3, 4]` |

**Binary search on a sorted array** looks at the middle and throws away half each time, which is why it needs only about `log2(n)` steps.

**NumPy slice is a view**

```text
values = [10 20 30 40 50 60]
view = values[1:3]      # shares memory
view[0] = 999
values -> [10 999 30 40 50 60]     (original changed!)
```

---

## D. Time and Space Complexity

| Operation | Python list | Notes |
|-----------|-------------|-------|
| Read / write by index | O(1) | direct address |
| Traverse | O(n) | |
| Append at end | O(1) amortised | |
| Insert / delete at front or middle | O(n) | shifting |
| Linear search | O(n) | any order |
| Binary search | O(log n) | sorted only |
| Reverse in place | O(n) time, O(1) space | two pointers |
| Rotate (three reversals) | O(n) time, O(1) space | |
| Remove duplicates, sorted, in place | O(n) time, O(1) space | slow and fast pointer |
| Merge two sorted arrays | O(n + m) time, O(n + m) space | |
| Matrix traversal | O(rows * cols) | |

NumPy: element access O(1); slicing O(1) (a view); arithmetic, `sum`, `mean`, `max`, boolean filtering O(n); `np.sort` O(n log n). NumPy is faster in practice because the loops run in compiled C, not because the Big O is different.

---

## E. Problems for Practice

| No | Title | Difficulty | Concept | Python File |
|----|-------|------------|---------|-------------|
| 1 | Array Traversal | Easy | Forward, backward, every k-th, two ends | `01_array_traversal.py` |
| 2 | Find Maximum, Minimum and Second Largest | Easy | Running-best pattern | `02_find_maximum.py` |
| 3 | Insert and Delete by Index | Easy | Manual shifting | `03_insert_and_delete.py` |
| 4 | Linear and Binary Search | Easy | Searching, sorted data | `04_linear_and_binary_search.py` |
| 5 | Reverse an Array | Easy | Two pointers, swap | `05_reverse_array.py` |
| 6 | Rotate an Array by K Positions | Medium | Three-reversal trick, `k % n` | `06_rotate_array.py` |
| 7 | Remove Duplicates and Merge Sorted Arrays | Medium | Slow/fast pointers, merging | `07_duplicates_and_merge.py` |
| 8 | NumPy Basics | Easy | Creating, indexing, slicing, views (NumPy) | `08_numpy_basics.py` |
| 9 | Two-Dimensional Arrays | Medium | Matrices with lists and NumPy | `09_two_dimensional_arrays.py` |
| 10 | NumPy Array Operations | Medium | Vectorising, broadcasting, statistics (NumPy) | `10_numpy_array_operations.py` |

### Problem 1 - Array Traversal (`01_array_traversal.py`)
**Statement.** Given a list of integers, produce its elements forward, backward, as `"index -> value"` text, every k-th element, and alternating from both ends (first, last, second, second-last, ...).

**Example.**
```text
numbers = [4, 8, 15, 16, 23, 42]
backward: [42, 23, 16, 15, 8, 4]
every 2nd: [4, 15, 23]
both ends: [4, 42, 8, 23, 15, 16]
```
**Constraints / edge cases.** Empty list; single element; odd length (middle visited once).

**Hints.**
- `range` accepts a start, stop and step (negative steps go backward).
- For both ends keep a left index and a right index and move them toward each other.
- When the indexes meet, add that element only once.

### Problem 2 - Find Maximum, Minimum and Second Largest (`02_find_maximum.py`)
**Statement.** Without `max()` or `min()`, return the largest and smallest value with their indexes, and the second largest distinct value.

**Example.**
```text
numbers = [12, 45, 7, 45, 3, 29]
maximum (value, index): (45, 1)    minimum: (3, 4)    second largest: 29
```
**Constraints / edge cases.** Empty list gives `None`; one element has no second largest; all equal means no second distinct value; negatives must work; with duplicates keep the first index.

**Hints.**
- Start from the first element, not from 0.
- Use a strict comparison to keep the first index.
- For the second largest keep two variables and decide carefully what happens on equality with the largest.

### Problem 3 - Insert and Delete by Index (`03_insert_and_delete.py`)
**Statement.** Write `insert_at(items, index, value)` and `delete_at(items, index)` by shifting elements manually (no `list.insert` or `list.pop(index)` doing the work). Report how many elements were shifted.

**Example.**
```text
[10, 20, 30, 40, 50] insert 25 at index 2 -> [10, 20, 25, 30, 40, 50], shifts = 3
insert at the end -> shifts = 0
delete index 0 from [5, 10, ...] -> shifts = 7
```
**Constraints / edge cases.** Index equal to length is a valid insert; empty list; out-of-range index must be rejected; negative index rejected.

**Hints.**
- Insert: grow the list, then copy elements one step right starting from the last one.
- Delete: copy elements one step left, then drop the final duplicate slot.
- Direction of copying matters; draw a 5-element example first.

### Problem 4 - Linear and Binary Search (`04_linear_and_binary_search.py`)
**Statement.** Return the index of a target or `-1`. Implement linear search and binary search and count comparisons for each.

**Example.**
```text
numbers = [3, 8, 12, 19, 25, 31, 47, 52, 60, 74]
target 47: linear (6, 7), binary (6, 4)
target 50: linear (-1, 10), binary (-1, 4)
```
**Constraints / edge cases.** Empty list; target below first or above last; duplicates (binary search returns any match); input must be sorted for binary search.

**Hints.**
- Binary search keeps a low and a high bound and checks the middle.
- Decide which bound moves when the middle value is smaller than the target.
- Loop while `low <= high`.

### Problem 5 - Reverse an Array (`05_reverse_array.py`)
**Statement.** Reverse a list in place (no `reverse()`, `reversed()` or `[::-1]`) and also return a reversed copy without touching the original.

**Example.**
```text
[1, 2, 3, 4, 5, 6] -> [6, 5, 4, 3, 2, 1]   swaps = 3
[50, 40, 30, 20, 10] for odd length input [10, 20, 30, 40, 50]
```
**Constraints / edge cases.** Empty, single element, odd length, palindrome.

**Hints.**
- Two indexes at the ends, swap, move inward.
- Stop when they meet or cross.
- The copy version can walk from the last index to the first.

### Problem 6 - Rotate an Array by K Positions (`06_rotate_array.py`)
**Statement.** Rotate a list to the right by `k` in place; also support left rotation.

**Example.**
```text
[1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]
k = 10 acts like k = 3;  k = -1 rotates left by one
```
**Constraints / edge cases.** Empty list (avoid modulo by zero); `k = 0` or multiple of `n`; `k > n`; negative `k`.

**Hints.**
- Reduce `k` first with the modulo operator.
- Reversing the whole list moves the last `k` items to the front, but backward.
- Reverse the two blocks separately to fix their order.

### Problem 7 - Remove Duplicates and Merge Sorted Arrays (`07_duplicates_and_merge.py`)
**Statement.** (a) Remove duplicates from a sorted list in place and return the new length. (b) Merge two sorted lists. (c) Return the values that appear more than once in any list.

**Example.**
```text
[1, 1, 2, 2, 2, 3, 5, 5] -> [1, 2, 3, 5], length 4
merge [1, 4, 7] and [2, 3, 9, 10] -> [1, 2, 3, 4, 7, 9, 10]
```
**Constraints / edge cases.** Empty lists; all elements equal; one list much longer; (a) and (b) need sorted input.

**Hints.**
- Keep a write position and a read position; copy only when the read value differs from the last kept one.
- Merging: compare the two fronts, take the smaller, then append what is left.
- A set remembers values already seen.

### Problem 8 - NumPy Basics (`08_numpy_basics.py`) - requires NumPy
**Statement.** Create arrays with several constructors, print shape/dtype/size, then index, slice, use negative indexes, boolean masks, and demonstrate that a slice is a view while `.copy()` is independent.

**Example.**
```text
values = np.array([10, 20, 30, 40, 50, 60])
values[1:4] -> [20 30 40]       values[::-1] -> [60 50 40 30 20 10]
values[values > 25] -> [30 40 50 60]
```
**Constraints / edge cases.** Out-of-range index raises `IndexError`; mixing ints and floats gives a float array; forgetting `.copy()` modifies the original.

**Hints.**
- Use `zeros`, `ones`, `arange` and `linspace` for creation.
- Slicing syntax is `[start:stop:step]`, same as lists.
- A comparison such as `values > 25` gives a boolean array you can index with.

### Problem 9 - Two-Dimensional Arrays (`09_two_dimensional_arrays.py`) - NumPy for the second half
**Statement.** For a 3 x 4 matrix compute row sums, column sums, transpose and the main-diagonal sum, first with nested lists, then with NumPy, and check both agree. Also show the shared-row bug of `[[0] * 3] * 2`.

**Example.**
```text
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
row sums: [10, 26, 42]     column sums: [15, 18, 21, 24]
diagonal sum: 18           pure Python equals NumPy: True
```
**Constraints / edge cases.** Empty matrix; non-square matrices (diagonal stops at the shorter side); ragged rows are invalid.

**Hints.**
- Element `(r, c)` sits at `matrix[r][c]`.
- Transpose swaps the roles of row and column index.
- NumPy uses the `axis` argument to choose rows or columns.

### Problem 10 - NumPy Array Operations (`10_numpy_array_operations.py`) - requires NumPy
**Statement.** Given daily sales, apply a 10 percent discount, find total, average, max/min with their day, count days above average, sort, cumulative totals, add arrays, broadcast a row over a matrix, and verify against a plain loop.

**Example.**
```text
sales = [120 340  90 560 210 430  75]
total: 1825 | average: 260.71    maximum: 560 on day index 3
days above average: [340 560 430]
```
**Constraints / edge cases.** Empty array: sum is fine but max raises `ValueError`; integer arrays become float after multiplying by 0.9; broadcasting needs compatible shapes.

**Hints.**
- Arithmetic on the whole array needs no loop.
- `argmax` returns a position, not a value.
- A boolean mask built from `sales > average` filters the array.

---

## F. Installation Requirements

| Item | Requirement |
|------|-------------|
| Python version | Python 3.8 or newer |
| Standard library only | Files `01` to `07` (nothing to install) |
| Third-party package | NumPy, needed only for `08_numpy_basics.py`, `09_two_dimensional_arrays.py` (its NumPy half) and `10_numpy_array_operations.py` |

**Installing NumPy** (one time):

```bash
python -m pip install numpy
```

On Linux/macOS use `python3 -m pip install numpy`. On Windows, if `python` is not recognised, use `py -m pip install numpy`. Verify with:

```bash
python -c "import numpy; print(numpy.__version__)"
```

NumPy is optional for the whole topic: you can solve problems 1-7 with no extra installation. If NumPy is missing, files 08 and 10 stop with an `ImportError` telling you to install it. File 09 needs it for the NumPy half.

Why `python -m pip` and not just `pip`? It guarantees that NumPy is installed for the same Python you use to run the scripts.

---

## G. How to Run the Files

1. Open a terminal (Windows: `cmd`, PowerShell or the VS Code terminal; Linux/macOS: Terminal).
2. Verify Python:
   ```bash
   python --version      # Windows (or: py --version)
   python3 --version     # Linux / macOS
   ```
3. Go to the folder and run a file.

**Windows**
```bash
cd Python-DSA-Practice\02-Arrays-Numpy-and-Python
python 01_array_traversal.py
python -m pip install numpy
python 08_numpy_basics.py
```
(`py 01_array_traversal.py` also works.)

**Linux / macOS**
```bash
cd Python-DSA-Practice/02-Arrays-Numpy-and-Python
python3 01_array_traversal.py
python3 -m pip install numpy
python3 08_numpy_basics.py
```

---

## H. Revision Notes

**Key concepts**
- Index access is O(1); insert or delete in the middle is O(n) because of shifting.
- Two pointers solve reversing, palindromes, merging, de-duplication and many search tasks in O(n) with O(1) space.
- Binary search needs sorted data and gives O(log n).
- Rotation: `k % n`, then three reversals.
- NumPy: same indexing as lists, vectorised math, slices are views, broadcasting stretches smaller shapes.

**Common mistakes**
- Off-by-one errors with `len(items)` versus last index `len(items) - 1`.
- Shifting in the wrong direction and overwriting data.
- Forgetting `k % n` (or `n = 0`) when rotating.
- Building a matrix with `[[0] * c] * r` (all rows are the same list).
- Modifying a NumPy slice and not realising the original changes.
- Calling binary search on unsorted data.

**Interview tips**
- Ask: is the array sorted? can it contain duplicates or negatives? can it be empty?
- Mention the in-place O(1)-space option after giving a simple solution.
- For "second largest" explain how you handle duplicates.
- Know when a hash set trades O(n) space for O(n) time.
- Be able to say why NumPy is faster: typed contiguous memory and loops in C.
