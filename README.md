# Python DSA Practice

A beginner-friendly practice repository: **19 topics × 10 solved problems = 190 standalone Python programs**, each topic with its own README that explains the concept and lets you re-attempt every problem before reading the solution.

## Learning objectives
- Understand core data structures and algorithms by reading small, fully working programs.
- Re-solve the same problems on your own for revision and interview preparation.
- Learn to state time and space complexity for every solution.

## Prerequisites and setup
- **Python 3.8 or newer** (developed and tested with Python 3.13).
- Everything uses the **standard library only**, except the NumPy examples in `02-Arrays-Numpy-and-Python`.

```bash
python --version          # Windows may need: py --version ; Linux/macOS: python3 --version
python -m pip install numpy   # only needed for the NumPy files in topic 02
# or: python -m pip install -r requirements.txt
```

## Table of contents
1. [Time Complexity](01-Time-Complexity/README.md) — 10 problems
2. [Arrays Numpy and Python](02-Arrays-Numpy-and-Python/README.md) — 10 problems
3. [Singly Linked List](03-Singly-Linked-List/README.md) — 10 problems
4. [Doubly and Circular Linked List](04-Doubly-and-Circular-Linked-List/README.md) — 10 problems
5. [Stack](05-Stack/README.md) — 10 problems
6. [Queue and Deque](06-Queue-and-Deque/README.md) — 10 problems
7. [Circular Queue](07-Circular-Queue/README.md) — 10 problems
8. [Recursion](08-Recursion/README.md) — 10 problems
9. [Tree](09-Tree/README.md) — 10 problems
10. [Graph](10-Graph/README.md) — 10 problems
11. [Bubble Sort](11-Bubble-Sort/README.md) — 10 problems
12. [Selection Sort](12-Selection-Sort/README.md) — 10 problems
13. [Insertion Sort](13-Insertion-Sort/README.md) — 10 problems
14. [Merge Sort](14-Merge-Sort/README.md) — 10 problems
15. [Quick Sort](15-Quick-Sort/README.md) — 10 problems
16. [Divide and Conquer](16-Divide-and-Conquer/README.md) — 10 problems
17. [Dynamic Programming](17-Dynamic-Programming/README.md) — 10 problems
18. [Greedy Algorithm](18-Greedy-Algorithm/README.md) — 10 problems
19. [Fractional Knapsack](19-Fractional-Knapsack/README.md) — 10 problems

## Folder structure
```text
Python-DSA-Practice/
├── README.md
├── requirements.txt
├── 01-Time-Complexity/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 02-Arrays-Numpy-and-Python/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 03-Singly-Linked-List/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 04-Doubly-and-Circular-Linked-List/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 05-Stack/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 06-Queue-and-Deque/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 07-Circular-Queue/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 08-Recursion/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 09-Tree/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 10-Graph/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 11-Bubble-Sort/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 12-Selection-Sort/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 13-Insertion-Sort/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 14-Merge-Sort/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 15-Quick-Sort/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 16-Divide-and-Conquer/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 17-Dynamic-Programming/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 18-Greedy-Algorithm/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
├── 19-Fractional-Knapsack/
│   ├── README.md
│   └── 01_… to 10_….py (10 files)
```

## Naming convention
- Topic folders: `NN-Topic-Name` in suggested learning order.
- Problem files: `01_…py` to `10_…py`, easy to medium within each topic.
- Every problem file is a **standalone program**: no imports from other files, no external files or APIs. Open it, run it.

## How to run one problem
```bash
cd Python-DSA-Practice/05-Stack
python 01_stack_implementation.py      # Windows (or: py 01_stack_implementation.py)
python3 01_stack_implementation.py     # Linux / macOS
```

## Suggested study workflow
1. Read the topic README.
2. Understand the problem statement and examples.
3. Attempt the problem independently.
4. Test with normal and edge-case inputs.
5. Open the provided solution only after attempting it.
6. Compare approaches and time/space complexity.
7. Reimplement the solution from memory a few days later.

## Avoiding spoilers while practising
- Work from the topic README, not the `.py` files.
- Copy the folder to `my-attempts/` and write your solutions there.
- Or in your editor, collapse/hide `*.py` in the file explorer until you have tried the problem.
- Each `.py` starts with a long docstring (approach + logic). Scroll past it only after your attempt.

## Suggested learning order
Follow the numbering: 01 Time Complexity → 02 Arrays → 03–04 Linked Lists → 05–07 Stack/Queues → 08 Recursion → 09 Tree → 10 Graph → 11–15 Sorting → 16 Divide and Conquer → 17 Dynamic Programming → 18 Greedy → 19 Fractional Knapsack.

## Troubleshooting
| Problem | Fix |
|---|---|
| `python` is not recognised (Windows) | Use `py` instead, or reinstall Python and tick *Add Python to PATH*. |
| `python` opens Python 2 or nothing (Linux/macOS) | Use `python3`. |
| `No module named numpy` | `python -m pip install numpy` (only topic 02 NumPy files need it). |
| `pip` not found | Use `python -m pip ...` (or `py -m pip ...`). |
| `externally-managed-environment` (Linux) | Create a venv: `python3 -m venv .venv && source .venv/bin/activate`, then install. |
| Wrong Python used for pip | Always run `python -m pip` with the same interpreter you run scripts with. |
