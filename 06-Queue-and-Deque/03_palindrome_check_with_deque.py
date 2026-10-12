r"""
Problem: Palindrome Check Using a Deque

Problem statement:
    Decide whether a string is a palindrome, ignoring case, spaces and
    punctuation, by comparing characters taken from both ends of a deque.

What it teaches:
    Why a double-ended queue is ideal for problems that compare the front
    with the back.

Input example:
    "racecar", "A man, a plan, a canal: Panama", "hello", "abba", "", "x"

Expected output:
    'racecar' -> palindrome
    'A man, a plan, a canal: Panama' -> palindrome
    'hello' -> not a palindrome
    'abba' -> palindrome
    '' -> palindrome
    'x' -> palindrome

Approach:
    Load the cleaned characters into a deque; repeatedly pop one from the
    left and one from the right and compare them.

Step-by-step logic:
    1. Keep only letters and digits, converted to lowercase.
    2. Put them in a deque.
    3. While more than one character remains: popleft and pop, and if they
    differ return False.
    4. If the loop ends, every pair matched, so return True.

Why it works:
    A palindrome reads the same in both directions, so the first character
    must equal the last, the second the second-last, and so on; a deque
    removes each end in O(1).

Time complexity:
    O(n).

Space complexity:
    O(n) for the deque.

Edge cases:
    Empty string, single character, odd and even length, mixed case,
    punctuation, strings of only punctuation.

Alternative approach:
    Two indexes moving inwards (O(1) extra space after cleaning) or
    comparing with the reversed string.
"""

from collections import deque


def clean(text):
    return [char.lower() for char in text if char.isalnum()]


def is_palindrome(text):
    chars = deque(clean(text))
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


def main():
    samples = ["racecar", "A man, a plan, a canal: Panama", "hello", "abba", "", "x"]
    for text in samples:
        verdict = "palindrome" if is_palindrome(text) else "not a palindrome"
        print("%r -> %s" % (text, verdict))


if __name__ == "__main__":
    main()
