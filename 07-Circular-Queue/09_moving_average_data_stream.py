"""
Problem title:
    Moving Average from a Data Stream

Problem statement:
    Numbers arrive one by one. After each number, report the average of the
    last "window" numbers (or of all numbers so far, if fewer have arrived).
    Memory must stay O(window), no matter how long the stream is.

What it teaches:
    - A circular buffer as a sliding window.
    - Keeping a running total instead of re-adding the window every time.
    - Subtracting the value that leaves the window.

Input example:
    window = 3; stream = 1, 10, 3, 5, 8, 2

Expected output:
    value  1 -> average 1.0000 | slots [1, 0, 0]
    value 10 -> average 5.5000 | slots [1, 10, 0]
    value  3 -> average 4.6667 | slots [1, 10, 3]
    value  5 -> average 6.0000 | slots [5, 10, 3]
    value  8 -> average 5.3333 | slots [5, 8, 3]
    value  2 -> average 5.0000 | slots [5, 8, 2]
    window 1: [4.0, 9.0, -2.0]

Approach:
    A circular array of "window" slots and a running total. When the array is
    full, the slot about to be overwritten holds the value leaving the window,
    so subtract it from the total before storing the new value.

Step-by-step logic:
    1. position = count % window (the slot to write next).
    2. If count >= window, total -= slots[position] (the outgoing value).
    3. slots[position] = new value; total += new value; count += 1.
    4. Number of values in the window = count if count < window else window.
    5. average = total / that number.

Why it works:
    The slot at (count % window) always holds the oldest value in the window,
    which is exactly the one that must leave when a new value arrives.

Time complexity:
    O(1) per number.

Space complexity:
    O(window).

Edge cases:
    - Fewer numbers than the window size (average over what we have).
    - Window of 1 (average equals the latest value).
    - Negative numbers and floats.

Alternative approach:
    Re-add the last "window" values every time: O(window) per number, simpler
    but slower for big windows.
"""


class MovingAverage:
    def __init__(self, window):
        if window < 1:
            raise ValueError("window must be at least 1")
        self.window = window
        self.slots = [0] * window
        self.count = 0  # how many numbers have arrived in total
        self.total = 0

    def next(self, value):
        """Add value to the stream and return the current moving average."""
        position = self.count % self.window  # circular write position
        if self.count >= self.window:
            self.total -= self.slots[position]  # oldest value leaves
        self.slots[position] = value
        self.total += value
        self.count += 1
        in_window = self.count if self.count < self.window else self.window
        return self.total / in_window


def main():
    stream = [1, 10, 3, 5, 8, 2]
    average = MovingAverage(3)
    for value in stream:
        result = average.next(value)
        print("value {:>2} -> average {:.4f} | slots {}".format(
            value, result, average.slots))

    single = MovingAverage(1)
    print("window 1:", [single.next(value) for value in (4, 9, -2)])


if __name__ == "__main__":
    main()
