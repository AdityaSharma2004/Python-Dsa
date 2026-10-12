"""
Problem Title: Longest Common Subsequence (LCS)

Problem Statement:
    Given two strings, find the length of their longest common subsequence (characters
    that appear in both in the same order, not necessarily next to each other) and
    return one such subsequence.

What It Teaches:
    - A 2-D DP table over two sequences.
    - Match / mismatch transitions.
    - Reconstructing the answer by walking back through the table.

Input Example:
    a = "ABCBDAB", b = "BDCABA"

Expected Output:
    a = ABCBDAB, b = BDCABA
    LCS length: 4
    One LCS: BCBA
    Valid in both: True
    LCS('', 'ABC') = 0 ''
    LCS('ABC', 'ABC') = 3 'ABC'
    LCS('ABC', 'XYZ') = 0 ''
    LCS('AGGTAB', 'GXTXAYB') = 4 'GTAB'

Approach:
    dp[i][j] = LCS length of the first i characters of a and first j of b.
    If a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1.
    Otherwise: dp[i][j] = larger of dp[i-1][j] and dp[i][j-1].

Step-by-Step Logic:
    1. Row 0 and column 0 are 0 (an empty string has no common part).
    2. Fill row by row using the rule above.
    3. dp[len(a)][len(b)] is the length.
    4. Backtrack from the bottom-right: on a match take the character and go
       diagonally; otherwise move towards the larger neighbour.

Why It Works:
    If the last characters match, some optimal answer uses them both. If they do
    not, at least one of them is unused, so we drop one and keep the better result.

Time Complexity:
    O(m * n) for strings of length m and n.
Space Complexity:
    O(m * n) for the table (O(min(m, n)) if only the length is needed).

Edge Cases:
    Empty strings, identical strings, no common characters, one string inside
    the other, repeated characters.

Alternative Approach:
    Memoised recursion (same complexity), or exponential brute force over subsequences.
"""


def lcs_table(a, b):
    """Return the DP table of LCS lengths."""
    rows, cols = len(a), len(b)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp


def lcs_string(a, b, dp):
    """Backtrack through dp to rebuild one longest common subsequence."""
    i, j = len(a), len(b)
    letters = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            letters.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    letters.reverse()
    return "".join(letters)


def is_subsequence(small, big):
    """Check that `small` appears inside `big` in order (used for verification)."""
    position = 0
    for char in big:
        if position < len(small) and char == small[position]:
            position += 1
    return position == len(small)


def main():
    a, b = "ABCBDAB", "BDCABA"
    dp = lcs_table(a, b)
    answer = lcs_string(a, b, dp)
    print(f"a = {a}, b = {b}")
    print("LCS length:", dp[-1][-1])
    print("One LCS:", answer)
    print("Valid in both:", is_subsequence(answer, a) and is_subsequence(answer, b))
    for first, second in [("", "ABC"), ("ABC", "ABC"), ("ABC", "XYZ"), ("AGGTAB", "GXTXAYB")]:
        table = lcs_table(first, second)
        print(f"LCS({first!r}, {second!r}) = {table[-1][-1]} {lcs_string(first, second, table)!r}")


if __name__ == "__main__":
    main()
