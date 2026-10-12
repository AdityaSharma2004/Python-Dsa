# 19 - Fractional Knapsack

## A. Topic Introduction

**What it is.** You have a bag that holds at most `capacity` weight and a set of items, each with a weight and a value. In the *fractional* version you may take any fraction of an item (half the item gives half its value). The goal is the maximum total value that fits in the bag.

**Why it matters in DSA.** It is the textbook example of a greedy algorithm that is provably optimal. It also sits next to the 0/1 knapsack (where items cannot be split), which needs Dynamic Programming. Knowing why one is greedy and the other is not is a classic interview question.

**Where it is used.**
- Budget or resource allocation where resources are divisible (money, bandwidth, CPU time, liquid or bulk goods).
- Choosing what to load onto a truck, pick from a warehouse, or cut from raw material.
- Teaching the exchange argument for greedy proofs.

**Everyday analogy.** You are at a spice market with a bag that takes 50 kg. Saffron is worth far more per gram than rice. You fill the bag with saffron first, then the next most valuable spice, and so on, and if the last sack does not fully fit you scoop only part of it.

---

## B. Core Concepts

| Term | Meaning |
|------|---------|
| Capacity | Maximum weight the bag can hold. |
| Value density (ratio) | `value / weight`: how much value each unit of weight brings. |
| Fraction taken | A number from 0 to 1 saying how much of an item is used. |
| Greedy rule | Take items in decreasing order of value density. |
| Divisible items | Items can be split; this is what makes greedy optimal. |

**Picture of the bag (capacity 50)**

```
Items: A(w=10,v=60) ratio 6   B(w=20,v=100) ratio 5   C(w=30,v=120) ratio 4

Bag:  |AAAAAAAAAA|BBBBBBBBBBBBBBBBBBBB|CCCCCCCCCCCCCCCCCCCC          |
       10 units     20 units            20 of C's 30 units (2/3)
Value: 60      +   100        +   120 * 2/3 = 80     = 240
```

**Why only one item is ever fractional.** Items are taken in ratio order. Once one does not fit whole, you take what remains and the bag is full, so there is at most one partial item.

**Sorting key matters.** Ordering by value alone or by weight alone can fail (see problem 7). Only the ratio is always correct.

---

## C. How It Works

Input: weights `[10, 20, 30]`, values `[60, 100, 120]`, capacity `50`.

1. Ratios: A = 6, B = 5, C = 4. Sorted order: A, B, C.
2. Fill the bag:

| Step | Item | Remaining capacity before | Taken | Remaining after | Gain | Running total |
|------|------|---------------------------|-------|-----------------|------|---------------|
| 1 | A | 50 | 10 (whole) | 40 | 60 | 60 |
| 2 | B | 40 | 20 (whole) | 20 | 100 | 160 |
| 3 | C | 20 | 20 of 30 (2/3) | 0 | 80 | 240 |

Answer: **240**.

**Comparison with 0/1 knapsack on the same input.** Whole items only: best is B + C = 220 (the ratio greedy would take A and B for just 160). So fractional (240) is always at least as good as 0/1 (220).

**Why greedy is optimal (exchange argument).** If a better answer used some weight of a low-ratio item while a higher-ratio item still had unused weight, swapping the two would raise the total. So any optimal answer can be rearranged to look exactly like the greedy fill.

Laravel analogy: it is like `orderByDesc('value / weight')` and then looping over the rows, subtracting from a remaining-capacity variable until it hits zero.

---

## D. Time and Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort by ratio, then fill (merge/quick sort) | O(n log n) | O(n) | Standard answer |
| Sort by ratio with insertion/selection sort | O(n^2) | O(n) | What several files here use, since they hand-write simple sorts |
| Max-heap by ratio | O(n + k log n) | O(n) | `k` = items actually examined; worst case O(n log n) |
| Greedy loop alone | O(n) | O(1) extra | After items are ordered |
| 0/1 knapsack DP | O(n * capacity) | O(capacity) | For comparison |
| Brute force over all orders | O(n! * n) | O(n) | Only for verification on tiny inputs |

---

## E. Problems for Practice

| No | Title | Difficulty | Concept | Filename |
|----|-------|------------|---------|----------|
| 1 | Basic Fractional Knapsack | Easy | Ratio sort and greedy fill | `01_basic_fractional_knapsack.py` |
| 2 | Value-to-Weight Ratio Table | Easy | Computing and ranking ratios | `02_value_to_weight_ratio_table.py` |
| 3 | Trace the Greedy Fill | Easy | Step-by-step state table | `03_trace_greedy_steps.py` |
| 4 | Fractions Taken Report | Easy | Keeping original indexes | `04_fractions_taken_report.py` |
| 5 | Edge Cases | Easy | Validation, zero weights, empty input | `05_edge_cases.py` |
| 6 | Exact Answers with Fraction | Medium | Exact arithmetic, no float error | `06_exact_answers_with_fraction.py` |
| 7 | Wrong Greedy Criteria | Medium | Counterexamples to other rules | `07_wrong_greedy_criteria.py` |
| 8 | Compare with 0/1 Knapsack | Medium | Fractional vs 0/1 vs unbounded | `08_compare_with_01_knapsack.py` |
| 9 | Heap-based Fractional Knapsack | Medium | Max-heap instead of full sort | `09_heap_based_fractional_knapsack.py` |
| 10 | Verify Greedy Optimality | Medium | Brute-force testing of a greedy | `10_verify_greedy_optimality.py` |

---

### Problem 1 - Basic Fractional Knapsack
**Statement.** Given `n` items with weights and values and a capacity, find the maximum total value when any fraction of an item may be taken.

**Example.**
```
weights = [10, 20, 30], values = [60, 100, 120], capacity = 50 -> 240.0
capacity 0   -> 0.0
capacity 100 -> 280.0
```
**Constraints / edge cases.** Capacity 0 gives 0. Capacity above the total weight means take everything. Equal ratios can be taken in any order.

**Hints.**
- Which single number per item tells you how "worth it" a kilogram of that item is?
- Order items by that number, best first (write your own simple sort).
- For each item: if it fits whole, take it all; otherwise take only the part that fits and stop.
- How much value does a fraction `f` of an item give?

---

### Problem 2 - Value-to-Weight Ratio Table
**Statement.** For a list of named items, compute each item's value per unit weight and print a table ranked best to worst. Also report the highest-value item and the best-ratio item.

**Example.**
```
saffron (2, 300), pepper (10, 50), cardamom (5, 100), salt (20, 20), rice (50, 400)
Ranking: saffron 150.00, cardamom 20.00, rice 8.00, pepper 5.00, salt 1.00
highest value item: rice | best ratio item: saffron
```
**Constraints / edge cases.** Tied ratios (earlier item keeps the better rank). A heavy item with a large value can still rank low. A single item.

**Hints.**
- Rank without a built-in sort: repeatedly find the best item you have not ranked yet.
- Use a "used" marker per item so you do not rank an item twice.
- Notice that the highest-value item and the best-ratio item are different. Why?

---

### Problem 3 - Trace the Greedy Fill
**Statement.** Solve fractional knapsack and print a table with one row per item: weight, ratio, amount taken, capacity left, value gained, running total, and a note (whole item, fraction, or skipped).

**Example.**
```
capacity 50: A takes 10 (whole), B takes 20 (whole), C takes 20 of 30 (fraction) -> 240.0
capacity 30: A takes 10, B takes 20, C skipped (bag fills exactly) -> 160.0
```
**Constraints / edge cases.** Bag exactly full after a whole item (no fraction at all). Items after the bag is full are shown as skipped. Capacity 0 skips everything.

**Hints.**
- Decide three cases per item: capacity left is 0, item fits whole, item only partly fits.
- Amount taken is the smaller of the item's weight and the remaining capacity.
- Value gained is ratio times amount taken.
- Print after each decision, not only at the end.

---

### Problem 4 - Fractions Taken Report
**Statement.** Return the maximum value plus a list with the fraction (0 to 1) taken of every item in its ORIGINAL position. Print only the items that were taken.

**Example.**
```
weights = [5, 10, 15], values = [10, 30, 20], capacity = 15
fractions = [1.0, 1.0, 0.0], total value 40.0, weight used 15.0 of 15
```
**Constraints / edge cases.** Items never reached stay at 0.0. At most one fractional item. Capacity 0 gives all zeros.

**Hints.**
- Sorting scrambles positions. What can you sort instead of the items themselves so the original position is not lost?
- Prepare a result list of zeros, then write each fraction into the slot of the original index.
- Verify your answer: total of (fraction * weight) must not exceed capacity, and total value must match.

---

### Problem 5 - Edge Cases
**Statement.** Make the function safe for empty item lists, capacity 0, negative capacity, capacity larger than everything, zero-weight items, tied ratios, mismatched list lengths and negative weights/values.

**Example.**
```
weights = [0, 4, 6], values = [7, 8, 9], capacity = 5 -> 16.5
mismatched lengths -> ValueError
negative weight    -> ValueError
```
**Constraints / edge cases.** Division by zero when weight is 0. Decide what a zero-weight item with a positive value means (free value). Decide when to raise an error and when to return 0.

**Hints.**
- Validate inputs before computing any ratio.
- A zero-weight item costs no capacity. What should you do with its value?
- After removing zero-weight items, can any remaining weight be 0?
- Return 0 early when the capacity is 0 or negative.

---

### Problem 6 - Exact Answers with Fraction
**Statement.** Solve fractional knapsack with exact rational numbers so results like 2/3 are not rounded. Return the total value and each fraction taken as exact values.

**Example.**
```
weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
exact total 240, fractions 1, 1, 2/3
weights = [3, 7], values = [1, 1], capacity = 5 -> total 9/7, fractions 1 and 2/7
```
**Constraints / edge cases.** Totals that are whole numbers print without a decimal. Capacity 0. Equal ratios must be recognised as equal.

**Hints.**
- Look at the standard library module `fractions` and its `Fraction` class.
- Build every ratio and every fraction taken as a `Fraction`, not a float.
- Compare ratios using those exact values, so ties are detected correctly.
- Compare the output with a plain-float run to see the rounding difference (for example `0.1 + 0.2`).

---

### Problem 7 - Wrong Greedy Criteria
**Statement.** Implement the greedy fill with three ordering rules (highest ratio, lowest weight, highest value) and show on the same inputs that only the ratio rule is always optimal.

**Example.**
```
weights [1, 10], values [1, 100], capacity 10:
  by ratio 100.00, by weight 91.00 (worse), by value 100.00
weights [10, 1, 1], values [20, 15, 15], capacity 10:
  by ratio 46.00, by weight 46.00, by value 20.00 (worse)
```
**Constraints / edge cases.** A wrong rule may agree with the right one on some inputs (that proves nothing). Ties between rules.

**Hints.**
- Write one fill routine that takes items in any order given to it, then change only the ordering.
- Give each rule a "score" where a bigger score is better. For "lowest weight", what score makes small weights look big?
- Hunt for counterexamples with 2 or 3 items where a heavy item has a big value but poor value per kilo.

---

### Problem 8 - Compare with 0/1 Knapsack
**Statement.** For the same items and capacity compute: the fractional optimum, the 0/1 optimum (DP), what ratio-greedy gives if items cannot be split, and the unbounded knapsack optimum (unlimited copies of each item).

**Example.**
```
weights = [10, 20, 30], values = [60, 100, 120], capacity = 50
Fractional 240.0 | 0/1 DP 220 | Ratio-greedy whole items 160 | Unbounded 300
```
**Constraints / edge cases.** Capacity 0 gives 0 everywhere. An item heavier than the capacity is skipped in 0/1 and unbounded. When splitting makes no difference, all answers agree.

**Hints.**
- Fractional is always at least the 0/1 answer. Why does extra freedom never hurt?
- For 0/1, use a one-dimensional table indexed by capacity. Which direction should you loop over capacity so an item is used at most once?
- For unbounded, reverse that direction. What does that allow?
- Greedy on whole items: take an item only if it fits entirely, otherwise skip it.

---

### Problem 9 - Heap-based Fractional Knapsack
**Statement.** Solve fractional knapsack without sorting every item. Build a max-heap by ratio and repeatedly extract the best item until the bag is full. Report how many items were examined.

**Example.**
```
weights = [10, 20, 30, 5, 15], values = [60, 100, 120, 50, 45]
capacity 40 -> value 230.00, items examined 4 of 5
capacity 5  -> value 50.00,  items examined 1 of 5
capacity 200 -> value 375.00, items examined 5 of 5
```
**Constraints / edge cases.** Capacity 0 pops nothing. The heap may become empty before the bag is full (take everything). Equal ratios are decided by index.

**Hints.**
- Python's `heapq` is a MIN-heap. How can you make the highest ratio come out first?
- Store tuples that include the original index so you can report fractions in input order.
- Build the heap in one go rather than pushing items one by one. What is the cost?
- Stop as soon as the capacity reaches zero. When does that make it faster than a full sort?

---

### Problem 10 - Verify Greedy Optimality
**Statement.** Test the greedy algorithm on many seeded random inputs against two references: the best result over EVERY possible item order (brute force), and the 0/1 DP answer, which must never exceed the fractional one.

**Example.**
```
300 random cases (seed 42), 1-6 items, weights 1-10, values 1-50, capacity 1-25
greedy == best over all orders : True for every case
fractional >= 0/1 knapsack     : True for every case
```
**Constraints / edge cases.** Ties in ratio make several orders optimal but totals still match. Capacity greater than total weight. A single item. Floats need a small tolerance when compared.

**Hints.**
- Why does "the best result over all orders" equal the true optimum? Think: any optimal solution is a fill in some order.
- Generate permutations yourself with recursive backtracking (choose an item, recurse, undo).
- Keep n small (6 or fewer), since the work grows like n!.
- Seed the random generator so a failing case can be reproduced.
- Compare floating-point totals using an absolute difference, not `==`.

---

## F. Installation Requirements

- **Python version:** 3.8 or newer.
- **Packages:** none to install. Only the standard library is used (`heapq` in problem 9, `fractions` in problem 6, `random` in problem 10).
- **NumPy:** not required for this topic.
- **Extra installation:** not necessary.

---

## G. How to Run the Files

1. Open a terminal (Windows: Command Prompt or PowerShell; macOS/Linux: Terminal).
2. Check Python is installed:
   ```bash
   python --version      # Windows
   python3 --version     # Linux / macOS
   ```
   On Windows, if `python` is not recognised, try `py --version` and use `py` instead of `python` below.
3. Move to the topic folder and run a file:

**Windows**
```bash
cd Python-DSA-Practice\19-Fractional-Knapsack
python 01_basic_fractional_knapsack.py
:: or
py 01_basic_fractional_knapsack.py
```

**Linux / macOS**
```bash
cd Python-DSA-Practice/19-Fractional-Knapsack
python3 01_basic_fractional_knapsack.py
```

Every file is a standalone program that imports nothing from its sibling files.

---

## H. Revision Notes

**Key concepts**
- Fractional knapsack is solved by taking items in decreasing `value / weight` order, then a fraction of the last one.
- It is optimal because of divisibility (exchange argument). 0/1 knapsack lacks that and needs DP.
- Fractional answer >= 0/1 answer >= ratio-greedy on whole items.
- At most one item is partly taken.
- Cost: sorting dominates (O(n log n) with a good sort); the fill is O(n). A heap helps when only a few items fit.

**Common mistakes**
- Sorting by value or by weight instead of by ratio.
- Dividing by zero for zero-weight items.
- Losing the original item order after sorting (keep indexes).
- Using the greedy rule on the 0/1 version and expecting an optimal answer.
- Comparing floats with `==`; use exact `Fraction` or a tolerance.
- Forgetting to stop after taking a fraction (the bag is then full).

**Interview tips**
- First ask: can items be split? If yes, greedy by ratio; if no, DP.
- Quote the exchange argument in a sentence.
- Know the 240 vs 220 vs 160 example for `[10,20,30]`, `[60,100,120]`, capacity 50. It shows exactly why 0/1 differs.
- Mention the heap alternative and its `O(n + k log n)` cost.
