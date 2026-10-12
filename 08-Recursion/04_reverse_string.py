"""
Problem title:
    Reverse a String Recursively

Problem statement:
    Reverse the given string without slicing tricks like text[::-1] or
    reversed(). Use recursion (and also show an in-place two-pointer version
    on a list of characters).

What it teaches:
    Breaking a sequence into "first item + rest" and rebuilding on the way
    back; two-index recursion that works toward the middle.

Input example:
    text = "recursion"

Expected output:
    'recursion' -> 'noisrucer' | two-pointer: 'noisrucer'
    'ab' -> 'ba' | two-pointer: 'ba'
    'a' -> 'a' | two-pointer: 'a'
    '' -> '' | two-pointer: ''
    'hello world' -> 'dlrow olleh' | two-pointer: 'dlrow olleh'

Approach:
    reverse(text) = reverse(text[1:]) + text[0], base case: length <= 1.

Step-by-step logic:
    1. Empty or 1-character string is its own reverse (base case).
    2. Reverse everything except the first character.
    3. Append the first character at the end.
    Two-pointer variant: swap chars at left and right, then recurse on
    (left + 1, right - 1) until left >= right.

Why it works:
    The first character must end up last, and the remainder must be
    reversed - exactly what the formula does.

Time complexity:
    Slicing version: O(n^2) because each slice copies; two-pointer: O(n).

Space complexity:
    O(n) stack (slicing version also creates temporary strings).

Edge cases:
    Empty string, single character, spaces, even/odd lengths.

Alternative approach:
    Iterate from the end building a new string, or use a stack.
"""


def reverse_string(text):
    """Simple recursive reverse using slicing for the rest."""
    if len(text) <= 1:  # base case
        return text
    return reverse_string(text[1:]) + text[0]


def reverse_chars(chars, left, right):
    """Improved: reverse a list in place with two pointers."""
    if left >= right:  # pointers met or crossed
        return
    chars[left], chars[right] = chars[right], chars[left]
    reverse_chars(chars, left + 1, right - 1)


def reverse_string_two_pointer(text):
    chars = list(text)
    reverse_chars(chars, 0, len(chars) - 1)
    return "".join(chars)


def main():
    samples = ["recursion", "ab", "a", "", "hello world"]
    for text in samples:
        print(f"'{text}' -> '{reverse_string(text)}' | "
              f"two-pointer: '{reverse_string_two_pointer(text)}'")


if __name__ == "__main__":
    main()
