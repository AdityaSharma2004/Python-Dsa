# 18 - Greedy Algorithm

## A. Topic Introduction

**What it is.** A greedy algorithm builds a solution one step at a time. At every step it takes the option that looks best *right now* and never goes back to change that decision.

**Why it matters in DSA.** Greedy solutions are usually short and fast (often O(n log n) or O(n)). The difficult part is not the code. It is deciding *which* local choice is safe and being able to argue why it is. Interviewers love greedy problems because a wrong "obvious" rule is easy to write and easy to break with a counterexample.

**Where it is used in real life.**
- Giving change at a shop counter (largest note first).
- Scheduling meetings or exam halls, and assigning platforms at a railway station.
- Compression (Huffman coding) and network routing (Dijkstra, Prim, Kruskal).
- Job scheduling in operating systems and task queues.

**Everyday analogy.** You are packing for a train and must catch as many connecting trains as possible. At each station you board the train that *arrives earliest* instead of weighing every future plan. If that rule is provably safe, you have a greedy algorithm. If it is not, you need Dynamic Programming.

---

## B. Core Concepts

| Term | Meaning |
|------|---------|
| Greedy choice | The locally best option picked at each step. |
| Greedy-choice property | Some globally optimal solution contains the greedy choice. |
| Optimal substructure | After the choice, what remains is a smaller problem of the same kind. |
| Exchange argument | Proof technique: take any optimal answer and swap its first choice for the greedy one without making it worse. |
| Counterexample | A small input on which a proposed greedy rule gives a non-optimal answer. Finding one kills the rule. |

**The greedy template**

```
sort or prepare the candidates by a "best first" rule
answer = empty
for each candidate in that order:
    if it is still allowed (fits, does not overlap, ...):
        take it and update the state
return answer
```

**Choosing the rule matters (interval example)**

```
time ->  0    2    4    6    8
A:       [-----------------------]      (0..100 long meeting)
B:       [--]                           (1..2)
C:            [--]                      (3..4)

earliest START   -> picks A  -> 1 meeting
earliest FINISH  -> picks B, C -> 2 meetings   (correct rule)
```

**Greedy vs Dynamic Programming**

```
Greedy : commit to one choice, move on.          Fast, but only valid with the greedy-choice property.
DP     : try all choices, remember sub-answers.  Slower, always valid when substructure holds.
```

---

## C. How It Works

Dry run of **Activity Selection** (pick maximum non-overlapping meetings), sorted by finish time:

Meetings: (1,4) (3,5) (0,6) (5,7) (3,9) (5,9) (6,10) (8,11) (8,12) (2,14) (12,16)

| Meeting | last_finish before | start >= last_finish? | Action | last_finish after |
|---------|--------------------|-----------------------|--------|-------------------|
| (1,4)   | -                  | first one             | take   | 4  |
| (3,5)   | 4                  | 3 >= 4 no             | skip   | 4  |
| (0,6)   | 4                  | 0 >= 4 no             | skip   | 4  |
| (5,7)   | 4                  | 5 >= 4 yes            | take   | 7  |
| (3,9)   | 7                  | no                    | skip   | 7  |
| (5,9)   | 7                  | no                    | skip   | 7  |
| (6,10)  | 7                  | no                    | skip   | 7  |
| (8,11)  | 7                  | 8 >= 7 yes            | take   | 11 |
| (8,12)  | 11                 | no                    | skip   | 11 |
| (2,14)  | 11                 | no                    | skip   | 11 |
| (12,16) | 11                 | 12 >= 11 yes          | take   | 16 |

Result: 4 meetings. Think of it in Laravel terms: it is like ordering a query by `finish` and then walking the rows once with a running "last finish" variable, the way you would use `->orderBy('finish')->each(...)`.

**How to prove a greedy rule (the mental checklist)**
1. State the rule in one sentence.
2. Try to break it with tiny inputs (2 to 4 items, and zero/equal values).
3. If it survives, argue by exchange: "any optimal answer can be rewritten to start with my choice."

---

## D. Time and Space Complexity

| Problem | Time | Space | Dominant cost |
|---------|------|-------|---------------|
| Coin change (greedy) | O(d log d) | O(d) | sorting denominations |
| Assign cookies | O(n log n + m log m) | O(n + m) | two sorts |
| Activity selection | O(n log n) | O(n) | sort by finish |
| Jump game | O(n) | O(1) | single scan |
| Stock II | O(n) | O(1) | single scan |
| Minimum platforms | O(n log n) | O(n) | two sorts |
| Job sequencing | O(n log n + n*D) | O(n + D) | sort + slot search (D = max deadline) |
| Gas station | O(n) | O(1) | single scan |
| Non-overlapping intervals | O(n log n) | O(n) | sort by end |
| Optimal merge patterns | O(n log n) | O(n) | min-heap operations |

Rule of thumb: if the greedy rule needs an order, expect O(n log n) from sorting; if it only needs a running value, expect O(n).

---

## E. Problems for Practice

| No | Title | Difficulty | Concept | Filename |
|----|-------|------------|---------|----------|
| 1 | Minimum Coins (Indian Denominations) | Easy | Largest-first greedy and its counterexample | `01_coin_change_indian.py` |
| 2 | Assign Cookies | Easy | Sort both sides, two pointers | `02_assign_cookies.py` |
| 3 | Activity Selection | Easy | Earliest finish time rule | `03_activity_selection.py` |
| 4 | Jump Game | Easy | Track farthest reachable index | `04_jump_game.py` |
| 5 | Best Time to Buy and Sell Stock II | Easy | Collect every upward step | `05_best_time_to_buy_sell_stock_ii.py` |
| 6 | Minimum Railway Platforms | Medium | Two sorted lists swept together | `06_minimum_platforms.py` |
| 7 | Job Sequencing with Deadlines | Medium | Profit-first with latest free slot | `07_job_sequencing_with_deadlines.py` |
| 8 | Gas Station (Circular Tour) | Medium | Running tank with reset | `08_gas_station.py` |
| 9 | Non-overlapping Intervals | Medium | Reuse activity selection (removals) | `09_non_overlapping_intervals.py` |
| 10 | Optimal Merge Patterns | Medium | Min-heap, merge two smallest | `10_optimal_merge_patterns.py` |

---

### Problem 1 - Minimum Coins (Indian Denominations)
**Statement.** Given a list of denominations and an amount, return the fewest coins/notes that add up to the amount by always taking the largest denomination that still fits. Also show that this rule fails for an arbitrary system such as `[1, 3, 4]`.

**Example.**
```
denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1], amount = 289
Output: [200, 50, 20, 10, 5, 2, 2]  -> 7 coins

denominations = [1, 3, 4], amount = 6
Greedy gives [4, 1, 1] (3 coins), but the true optimum is 3 + 3 (2 coins)
```
**Constraints / edge cases.** Amount 0 returns an empty list. An amount that cannot be formed (coins `[5, 10]`, amount 3) returns `None`. A negative amount is an error.

**Hints.**
- Order the denominations from largest to smallest first.
- For each denomination, how many fit into what is left? One division with remainder answers that.
- What should you do if you finish all denominations and still have a remainder?
- To prove the rule wrong for `[1, 3, 4]`, write a tiny slow checker that tries all combinations (a table of best answers for every smaller amount).

---

### Problem 2 - Assign Cookies
**Statement.** Child `i` has greed `g[i]` (minimum cookie size that satisfies them). Cookie `j` has size `s[j]`. Each cookie goes to at most one child and each child gets at most one cookie. Return the maximum number of satisfied children.

**Example.**
```
greed = [1, 2, 3], cookies = [1, 1]   -> 1
greed = [1, 2],    cookies = [1, 2, 3] -> 2
```
**Constraints / edge cases.** No children or no cookies gives 0. All cookies too small gives 0. Extra cookies are simply unused.

**Hints.**
- Which child is easiest to satisfy? Which cookie is the cheapest way to do it?
- Sort both lists ascending (write your own sort).
- Walk through the cookies once and keep a pointer to the first unsatisfied child.
- When a cookie is too small for the current child, it is too small for every greedier child too.

---

### Problem 3 - Activity Selection
**Statement.** Given meetings as `(start, finish)` pairs and one room, choose the maximum number of meetings that do not overlap. A meeting may begin exactly when another ends.

**Example.**
```
[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
Chosen: [(1,4),(5,7),(8,11),(12,16)] -> 4
```
**Constraints / edge cases.** Empty list gives nothing. Touching meetings (end 5, start 5) are allowed. Identical meetings: only one can be chosen.

**Hints.**
- Test three candidate rules (earliest start, shortest duration, earliest finish) on a 2-to-3 meeting input. Only one survives.
- After sorting by the winning key, you only need to remember one number: the finish time of the last chosen meeting.
- Decide carefully between `>` and `>=` when comparing start with that number.

---

### Problem 4 - Jump Game
**Statement.** `nums[i]` is the maximum jump length from index `i`. Starting at index 0, decide whether the last index is reachable.

**Example.**
```
[2, 3, 1, 1, 4] -> True
[3, 2, 1, 0, 4] -> False
```
**Constraints / edge cases.** A single element is already at the end. `[0]` is True but `[0, 1]` is False. A zero in the middle is harmless if an earlier jump passes over it. Empty input is False in this solution.

**Hints.**
- Do not explore paths. Keep a single number: the farthest index you could possibly reach so far.
- Every index up to that number is reachable, so scanning left to right is enough.
- When can you declare failure? When the index you are standing on is beyond your farthest reach.
- You can stop early once the farthest reach touches the last index.

---

### Problem 5 - Best Time to Buy and Sell Stock II
**Statement.** `prices[i]` is the price on day `i`. You may buy and sell as many times as you like but hold at most one share at a time. Return the maximum profit.

**Example.**
```
[7, 1, 5, 3, 6, 4] -> 7   (buy 1 sell 5, buy 3 sell 6)
[1, 2, 3, 4, 5]    -> 4
[7, 6, 4, 3, 1]    -> 0
```
**Constraints / edge cases.** Empty list or one price gives 0. Strictly falling prices give 0. Strictly rising prices give last minus first. Equal prices give 0.

**Hints.**
- A long climb from low to high equals the sum of its day-to-day climbs.
- Look only at the difference between today and yesterday. When is it worth keeping?
- Do you need to remember the buy day to compute the profit? (No.)

---

### Problem 6 - Minimum Railway Platforms
**Statement.** Given arrival and departure times of trains (24-hour style, 930 = 9:30), find the minimum number of platforms so that no train waits. A train arriving exactly when another departs needs its own platform.

**Example.**
```
arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
```
**Constraints / edge cases.** Empty input gives 0. Arrival equal to a departure counts both trains at once. All overlapping trains give `n`.

**Hints.**
- The question is really "what is the maximum number of trains present at the same moment?"
- Does the pairing of a train's arrival with its own departure matter for that count? Not really, so the two lists can be sorted separately.
- Use two pointers: if the next event is an arrival, one more platform is in use; otherwise one is freed.
- For ties, decide which event is processed first, and justify it from the statement.

---

### Problem 7 - Job Sequencing with Deadlines
**Statement.** Each job takes one unit of time, has a deadline (latest slot, slots start at 1) and a profit earned only if finished by the deadline. Schedule jobs to maximise total profit.

**Example.**
```
jobs (name, deadline, profit) = [("a",2,100),("b",1,19),("c",2,27),("d",1,25),("e",3,15)]
Slot 1: c, Slot 2: a, Slot 3: e   -> total profit 142
```
**Constraints / edge cases.** Deadlines may exceed the number of jobs (use slots up to the maximum deadline). Empty list gives profit 0. Equal profits keep input order.

**Hints.**
- Consider jobs from the most profitable down. Is skipping a high-profit job ever better than fitting it?
- Where should a chosen job go: as early as possible or as late as possible? Think about whom you want to leave room for.
- Use an array with one entry per time slot and scan downward from the job's deadline.
- For a faster version, look up "union-find for latest free slot" or "min-heap on profits".

---

### Problem 8 - Gas Station (Circular Tour)
**Statement.** `gas[i]` is the fuel gained at station `i`; `cost[i]` is the fuel needed to reach the next station. Starting with an empty tank, return the index of the station from which you can complete the full circle, or -1.

**Example.**
```
gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2] -> 3
gas = [2, 3, 4],       cost = [3, 4, 3]       -> -1
```
**Constraints / edge cases.** If total gas is less than total cost the answer is -1. A single station works when `gas >= cost`.

**Hints.**
- Define `diff[i] = gas[i] - cost[i]` and keep a running tank.
- If the tank goes negative at station `i`, can any station between the start and `i` be a better start? Argue why not.
- Keep a second running total across the whole circle. What does its sign tell you about existence of an answer?
- Aim for one pass instead of trying every start.

---

### Problem 9 - Non-overlapping Intervals
**Statement.** Given intervals `[start, end]`, return the minimum number of intervals to remove so the rest do not overlap. Intervals that only touch at an endpoint do not overlap.

**Example.**
```
[[1,2],[2,3],[3,4],[1,3]] -> 1
[[1,2],[1,2],[1,2]]       -> 2
```
**Constraints / edge cases.** Empty list gives 0. Identical intervals: all but one are removed. Touching intervals are not overlaps.

**Hints.**
- Minimum removals = total intervals minus the maximum you can keep. Does the second quantity look familiar?
- Sort by END time, not start time.
- Walk once with a variable for the end of the last kept interval and count the ones you must drop.

---

### Problem 10 - Optimal Merge Patterns
**Statement.** You have files of given sizes. Merging two files of sizes `a` and `b` costs `a + b` and produces one file of size `a + b`. Merge everything into one file at minimum total cost.

**Example.**
```
sizes = [20, 30, 10, 5, 30]
Merges: 5+10=15, 15+20=35, 30+30=60, 35+60=95  -> total cost 205
```
**Constraints / edge cases.** Zero or one file costs 0. Two files cost their sum. Equal sizes are fine.

**Hints.**
- A file merged early is counted again in every later merge above it. So who should be merged first, the small or the large?
- You need "give me the two smallest right now" repeatedly. Which data structure does that cheaply? (Python: the `heapq` module.)
- After each merge, the new file goes back into the structure.
- This same pattern builds Huffman codes.

---

## F. Installation Requirements

- **Python version:** 3.8 or newer.
- **Packages:** none to install. Everything uses the Python standard library only (for example `heapq` in problem 10 is part of the standard library).
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
   On Windows, if `python` is not found, try `py --version` and use `py` in place of `python` below.
3. Go to the topic folder and run a file:

**Windows**
```bash
cd Python-DSA-Practice\18-Greedy-Algorithm
python 01_coin_change_indian.py
:: or
py 01_coin_change_indian.py
```

**Linux / macOS**
```bash
cd Python-DSA-Practice/18-Greedy-Algorithm
python3 01_coin_change_indian.py
```

Each file is a standalone program: it imports nothing from its sibling files and needs no input files.

---

## H. Revision Notes

**Key concepts**
- Greedy = pick the best local option, never undo. Correct only if it has the greedy-choice property.
- Interval problems: sort by END time. Resource counting problems: sort starts and ends separately. Value-based problems: sort by profit or ratio.
- Running-variable greedy (jump game, stock II, gas station) needs no sort and runs in O(n).
- A min-heap is the greedy engine when you repeatedly need the current smallest item (merge patterns, Huffman).
- Exchange argument is the standard proof.

**Common mistakes**
- Using `>` instead of `>=` when intervals may touch (or the reverse when touching means overlap).
- Sorting intervals by start time when the rule needs end time.
- Assuming largest-coin-first works for every coin system (it does not: `[1, 3, 4]`).
- Forgetting empty input, a single element, or the "impossible" case (`None` or -1).
- Placing a job in the earliest slot instead of the latest free slot.

**Interview tips**
- Say the greedy rule out loud, then offer a quick counterexample test before coding.
- Mention the exchange argument in one sentence; it shows you understand why it works.
- If greedy fails on a counterexample, pivot to DP and say so.
- State complexity: sort cost plus scan cost.
