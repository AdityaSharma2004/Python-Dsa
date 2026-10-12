"""
Problem title:
    Palindrome Check Using Recursion

Problem statement:
    Check whether a string reads the same forwards and backwards. Ignore
    case, spaces and punctuation (only letters and digits count).

What it teaches:
    Recursion with two indices moving inward, skipping unwanted characters,
    and returning early (short-circuit) on a mismatch.

Input example:
    text = "A man, a plan, a canal: Panama"

Expected output:
    'A man, a plan, a canal: Panama' -> True (loop: True)
    'racecar' -> True (loop: True)
    'hello' -> False (loop: False)
    '' -> True (loop: True)
    'a' -> True (loop: True)
    'No 'x' in Nixon' -> True (loop: True)
    '!!' -> True (loop: True)

Approach:
    Compare the outer characters; if equal, recurse on the inner part.

Step-by-step logic:
    1. left = 0, right = len - 1.
    2. If left >= right: everything matched -> True (base case).
    3. If text[left] is not alphanumeric, move left forward and recurse.
    4. If text[right] is not alphanumeric, move right back and recurse.
    5. If the lowercase characters differ -> False, else recurse inward.

Why it works:
    A string is a palindrome only if its first and last (relevant)
    characters match and the middle part is also a palindrome.

Time complexity:
    O(n) - each character is looked at once.

Space complexity:
    O(n) recursion stack in the worst case.

Edge cases:
    Empty string (True), single char, only punctuation, mixed case.

Alternative approach:
    Build a cleaned string and compare with its reverse, or use a loop with
    two pointers (O(1) space).
"""


def is_palindrome(text, left=0, right=None):
    """Recursive palindrome check using two indices."""
    if right is None:
        right = len(text) - 1
    if left >= right:  # base case
        return True
    if not text[left].isalnum():  # skip junk on the left
        return is_palindrome(text, left + 1, right)
    if not text[right].isalnum():  # skip junk on the right
        return is_palindrome(text, left, right - 1)
    if text[left].lower() != text[right].lower():
        return False
    return is_palindrome(text, left + 1, right - 1)


def is_palindrome_loop(text):
    """Iterative two-pointer version (O(1) space) for comparison."""
    left, right = 0, len(text) - 1
    while left < right:
        if not text[left].isalnum():
            left += 1
        elif not text[right].isalnum():
            right -= 1
        elif text[left].lower() != text[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def main():
    samples = ["A man, a plan, a canal: Panama", "racecar", "hello",
               "", "a", "No 'x' in Nixon", "!!"]
    for text in samples:
        print(f"'{text}' -> {is_palindrome(text)} "
              f"(loop: {is_palindrome_loop(text)})")


if __name__ == "__main__":
    main()
