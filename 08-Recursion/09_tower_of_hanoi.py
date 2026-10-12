"""
Problem title:
    Tower of Hanoi

Problem statement:
    Three pegs A, B, C. n disks of different sizes sit on A (smallest on
    top). Move all disks to C, one at a time, never placing a larger disk on
    a smaller one. Print the moves and count them.

What it teaches:
    Trusting recursion to solve a smaller identical problem, and a
    recurrence T(n) = 2T(n-1) + 1 that gives exponential growth.

Input example:
    n = 3

Expected output:
    Move 1: disk 1 from A to C
    Move 2: disk 2 from A to B
    Move 3: disk 1 from C to B
    Move 4: disk 3 from A to C
    Move 5: disk 1 from B to A
    Move 6: disk 2 from B to C
    Move 7: disk 1 from A to C
    Total moves: 7 (2^n - 1 = 7 )
    Final pegs: {'A': [], 'B': [], 'C': [3, 2, 1]}
    n=0: 0 moves
    n=1: 1 moves
    n=5: 31 moves
    n=10: 1023 moves

Approach:
    Move n-1 disks to the helper peg, move the largest disk, then move the
    n-1 disks from the helper onto it.

Step-by-step logic:
    1. n == 0: nothing to do (base case).
    2. hanoi(n-1, source, helper, target): clear the way.
    3. Move disk n from source to target.
    4. hanoi(n-1, helper, target, source): put the small tower back on top.

Why it works:
    The biggest disk can only move when all smaller disks sit on the helper
    peg. Smaller disks can always go on top of larger ones, so the rule holds.

Time complexity:
    O(2^n) - exactly 2^n - 1 moves.

Space complexity:
    O(n) recursion depth (plus the list of moves if stored).

Edge cases:
    n = 0 -> no moves; n = 1 -> a single move; large n grows very fast.

Alternative approach:
    An iterative solution using a stack, or the cyclic-move pattern for
    the smallest disk.
"""


def hanoi(n, source, target, helper, moves):
    """Append (disk, from, to) tuples to moves."""
    if n == 0:  # base case
        return
    hanoi(n - 1, source, helper, target, moves)
    moves.append((n, source, target))
    hanoi(n - 1, helper, target, source, moves)


def simulate(n, moves):
    """Replay moves on real pegs to prove that no rule is broken."""
    pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    for disk, source, target in moves:
        assert pegs[source] and pegs[source][-1] == disk, "wrong disk moved"
        assert not pegs[target] or pegs[target][-1] > disk, "bigger on smaller"
        pegs[source].pop()
        pegs[target].append(disk)
    return pegs


def main():
    n = 3
    moves = []
    hanoi(n, "A", "C", "B", moves)
    for number, (disk, source, target) in enumerate(moves, start=1):
        print(f"Move {number}: disk {disk} from {source} to {target}")
    print("Total moves:", len(moves), "(2^n - 1 =", 2 ** n - 1, ")")
    print("Final pegs:", simulate(n, moves))
    for size in (0, 1, 5, 10):
        all_moves = []
        hanoi(size, "A", "C", "B", all_moves)
        print(f"n={size}: {len(all_moves)} moves")


if __name__ == "__main__":
    main()
