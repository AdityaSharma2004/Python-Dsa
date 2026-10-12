r"""
Problem: Reverse a String (and Each Word) Using a Stack

Problem statement:
    Reverse a whole string using a stack. Then reverse only the letters of
    each word while keeping the word order.

What it teaches:
    How LIFO order naturally reverses a sequence: what goes in first comes
    out last.

Input example:
    "hello", "Data Structures", ""

Expected output:
    Original      : hello
    Reversed      : olleh
    Words reversed: olleh

    Original      : Data Structures
    Reversed      : serutcurtS ataD
    Words reversed: ataD serutcurtS

    Original      :
    Reversed      :
    Words reversed:

Approach:
    Push every character on a stack, then pop them all into a result list.
    For word-wise reversal, flush the stack whenever a space is met.

Step-by-step logic:
    1. Create an empty stack (a list used at one end).
    2. Push each character in order.
    3. Pop until empty, appending each popped character to the output.
    4. For word reversal: on a space, pop everything pushed so far, then add
    the space; flush once more at the end of the string.

Why it works:
    The last character pushed is the first popped, so the output order is the
    exact opposite of the input order.

Time complexity:
    O(n) - each character is pushed once and popped once.

Space complexity:
    O(n) for the stack and the output.

Edge cases:
    Empty string, single character, multiple consecutive spaces, leading or
    trailing spaces, palindromes.

Alternative approach:
    Two pointers swapping from both ends of a list of characters, which needs
    only O(1) extra space besides the list itself.
"""


def reverse_string(text):
    stack = []
    for char in text:
        stack.append(char)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result)


def reverse_each_word(text):
    stack = []
    result = []
    for char in text:
        if char == " ":
            while stack:  # flush the current word reversed
                result.append(stack.pop())
            result.append(" ")
        else:
            stack.append(char)
    while stack:  # flush the last word
        result.append(stack.pop())
    return "".join(result)


def main():
    for text in ("hello", "Data Structures", ""):
        print("Original      :", text)
        print("Reversed      :", reverse_string(text))
        print("Words reversed:", reverse_each_word(text))
        print()


if __name__ == "__main__":
    main()
