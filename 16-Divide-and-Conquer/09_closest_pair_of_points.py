"""
Problem Title: Closest Pair of Points

Problem Statement:
    Given points in the plane, find the pair with the smallest Euclidean
    distance. Use divide and conquer rather than checking all pairs.

What It Teaches:
    - Splitting space (not just arrays) by a vertical line.
    - The "strip" combine step: only points within distance d of the line and
      only a few neighbours (by y) need checking.
    - Comparing against the O(n^2) brute force.

Input Example:
    [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

Expected Output:
    Points: [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    Closest pair: (2, 3) and (3, 4), distance = 1.4142
    Brute force distance = 1.4142 (matches)
    With duplicates: (1, 1) and (1, 1), distance = 0.0000
    40 pseudo-random points: divide & conquer matches brute force

Approach:
    Sort by x once. Split at the median x. Find the closest pair in each half
    (distance d = smaller of the two). Then check pairs that straddle the
    dividing line, using only points within d of it, ordered by y.

Step-by-Step Logic:
    1. Sort points by x (insertion sort written by hand, stable and simple).
    2. If at most 3 points, use brute force.
    3. mid = n // 2; recurse on left and right halves; d = best of both.
    4. Collect strip points with |x - mid_x| < d and order them by y.
    5. For each strip point compare with following strip points while the y
       difference is < d (at most a handful of checks).
    6. Return the best of d and the strip result.

Why It Works:
    A pair closer than d that straddles the line must lie in the strip, and in
    a d x 2d box only a constant number of points can coexist, so the inner
    loop is O(1) per point.

Time Complexity:
    O(n log n) in the textbook version with presorted y; this teaching version
    re-orders the strip each call using an O(k^2) insertion sort on the strip
    only, so its worst case is O(n^2) but it is typically close to O(n log n).
Space Complexity:
    O(n) for the sorted copies and strip lists.

Edge Cases:
    Fewer than 2 points (error), duplicate points (distance 0), points sharing
    the same x, collinear points.

Alternative Approach:
    Brute force checks all n(n-1)/2 pairs: O(n^2), included for verification.
"""


def distance(p, q):
    """Euclidean distance between two points."""
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5


def insertion_sort_by(points, axis):
    """Return a copy of points ordered by the given coordinate index."""
    result = list(points)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j][axis] > current[axis]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def brute_force(points):
    """Return (distance, pair) by checking every pair."""
    best = (float("inf"), None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < best[0]:
                best = (d, (points[i], points[j]))
    return best


def closest_recursive(points_by_x):
    """points_by_x must already be ordered by x."""
    if len(points_by_x) <= 3:
        return brute_force(points_by_x)
    mid = len(points_by_x) // 2
    mid_x = points_by_x[mid][0]
    left_best = closest_recursive(points_by_x[:mid])
    right_best = closest_recursive(points_by_x[mid:])
    best = left_best if left_best[0] <= right_best[0] else right_best
    strip = [p for p in points_by_x if abs(p[0] - mid_x) < best[0]]
    strip = insertion_sort_by(strip, 1)  # order by y
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < best[0]:
            d = distance(strip[i], strip[j])
            if d < best[0]:
                best = (d, (strip[i], strip[j]))
            j += 1
    return best


def closest_pair(points):
    """Public entry point."""
    if len(points) < 2:
        raise ValueError("need at least two points")
    return closest_recursive(insertion_sort_by(points, 0))


def main():
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Points:", points)
    dist, pair = closest_pair(points)
    print(f"Closest pair: {pair[0]} and {pair[1]}, distance = {dist:.4f}")
    brute_dist, _ = brute_force(points)
    assert abs(dist - brute_dist) < 1e-9
    print(f"Brute force distance = {brute_dist:.4f} (matches)")
    duplicate_points = [(1, 1), (4, 5), (1, 1), (9, 9)]
    dist, pair = closest_pair(duplicate_points)
    print(f"With duplicates: {pair[0]} and {pair[1]}, distance = {dist:.4f}")
    # deterministic larger test against brute force
    state = 12345
    grid = []
    for _ in range(40):
        state = (state * 1103515245 + 12345) % 2147483648
        x = state % 100
        state = (state * 1103515245 + 12345) % 2147483648
        y = state % 100
        grid.append((x, y))
    assert abs(closest_pair(grid)[0] - brute_force(grid)[0]) < 1e-9
    print("40 pseudo-random points: divide & conquer matches brute force")


if __name__ == "__main__":
    main()
