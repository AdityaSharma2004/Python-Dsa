r"""
Problem: Check Balanced Parentheses

Problem statement:
    Given a string containing (), [] and {} (and other characters), decide
    whether every opening bracket is closed by the correct bracket type in
    the correct order.

What it teaches:
    The classic stack pattern: remember unmatched openers, match them against
    closers in reverse order.

Input example:
    "{[()]}", "([)]", "((", ")(", "a(b)c", ""

Expected output:
    '{[()]}' -> balanced
    '([)]' -> NOT balanced
    '((' -> NOT balanced
    ')(' -> NOT balanced
    'a(b)c' -> balanced
    '' -> balanced

Approach:
    Scan left to right. Push openers. On a closer, the top of the stack must
    be its matching opener, otherwise the string is unbalanced.

Step-by-step logic:
    1. Build a map closer -> opener.
    2. For an opener push it.
    3. For a closer: if the stack is empty or the popped top is not the
    matching opener, return False.
    4. Ignore any other character.
    5. At the end the stack must be empty (no unmatched openers).

Why it works:
    The most recently opened bracket must be the first one closed, which is
    exactly LIFO order.

Time complexity:
    O(n).

Space complexity:
    O(n) in the worst case (all openers).

Edge cases:
    Empty string, only closers, only openers, wrong type ordering like ([)],
    closer appearing before any opener, non-bracket characters.

Alternative approach:
    For a single bracket type a counter is enough (O(1) space); repeatedly
    deleting "()", "[]", "{}" also works but is O(n^2).
"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    stack = []
    for char in text:
        if char in PAIRS.values():
            stack.append(char)
        elif char in PAIRS:
            if not stack or stack.pop() != PAIRS[char]:
                return False
    return len(stack) == 0


def main():
    for text in ("{[()]}", "([)]", "((", ")(", "a(b)c", ""):
        verdict = "balanced" if is_balanced(text) else "NOT balanced"
        print("%r -> %s" % (text, verdict))


if __name__ == "__main__":
    main()
