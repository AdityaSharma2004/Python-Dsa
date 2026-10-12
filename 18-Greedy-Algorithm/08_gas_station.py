"""
Problem title:
    Gas Station (Circular Tour)

Problem statement:
    There are n gas stations on a circular route. gas[i] is the fuel you get
    at station i and cost[i] is the fuel needed to drive from station i to the
    next one. Starting with an empty tank, return the index of the station
    from which you can complete the full circle, or -1 if impossible.

What it teaches:
    * Greedy reset: if a start fails, no station before the failure point
      can be a valid start either.
    * One pass instead of trying every start (O(n^2)).

Input example:
    gas  = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

Expected output:
    gas=[1, 2, 3, 4, 5] cost=[3, 4, 5, 1, 2] -> start=3 (simulated ok: True)
    gas=[2, 3, 4] cost=[3, 4, 3] -> start=-1 (simulated ok: n/a)
    gas=[5] cost=[4] -> start=0 (simulated ok: True)
    gas=[5] cost=[6] -> start=-1 (simulated ok: n/a)
    gas=[3, 1, 1] cost=[1, 2, 2] -> start=0 (simulated ok: True)

Approach:
    Track the running tank. When it drops below zero at station i, restart the
    candidate at i + 1. Also track total (gas - cost); if it is negative,
    answer -1.

Step-by-step logic:
    1. total = 0, tank = 0, start = 0.
    2. For each i: diff = gas[i] - cost[i]; total += diff; tank += diff.
    3. If tank < 0: start = i + 1, tank = 0.
    4. After the loop: return start if total >= 0 else -1.

Why it works:
    If we start at s and first fail at station i, every station between s and
    i also fails: they would arrive at i with even less fuel than s did
    (s arrived at each of them with a non-negative tank). So the next
    candidate is i + 1. If total fuel >= total cost, a valid start must exist
    and it is the last candidate.

Time complexity:
    O(n).

Space complexity:
    O(1).

Edge cases:
    * total gas < total cost -> -1.
    * Single station: valid if gas >= cost.
    * Answer is unique when it exists (problem guarantee in the classic
      version); this code returns the first valid candidate found.

Alternative approach:
    Brute force: try every start and simulate the loop - O(n^2).
"""


def can_complete_circuit(gas, cost):
    """Return the starting station index, or -1 if the tour is impossible."""
    if len(gas) != len(cost):
        raise ValueError("gas and cost must have the same length")
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:  # cannot reach station i + 1 from the current start
            start = i + 1
            tank = 0
    if total < 0 or len(gas) == 0:
        return -1
    return start


def simulate(gas, cost, start):
    """Verification helper: really drive the loop from `start`."""
    n = len(gas)
    tank = 0
    for step in range(n):
        i = (start + step) % n
        tank += gas[i] - cost[i]
        if tank < 0:
            return False
    return True


def main():
    tests = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        ([2, 3, 4], [3, 4, 3]),
        ([5], [4]),
        ([5], [6]),
        ([3, 1, 1], [1, 2, 2]),
    ]
    for gas, cost in tests:
        start = can_complete_circuit(gas, cost)
        check = simulate(gas, cost, start) if start != -1 else "n/a"
        print(f"gas={gas} cost={cost} -> start={start} (simulated ok: {check})")


if __name__ == "__main__":
    main()
