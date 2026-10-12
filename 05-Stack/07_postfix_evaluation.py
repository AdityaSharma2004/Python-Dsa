r"""
Problem: Evaluate a Postfix (Reverse Polish) Expression

Problem statement:
    Evaluate an expression written in postfix notation, where operators come
    after their operands, e.g. "2 3 4 * +" means 2 + 3 * 4. Support + - * /
    and report invalid expressions.

What it teaches:
    Using a stack of operands for expression evaluation, and why postfix
    needs no parentheses or precedence rules.

Input example:
    "2 3 4 * +", "5 1 2 + 4 * + 3 -", "10 2 /", "1 +", "4 0 /"

Expected output:
    '2 3 4 * +' = 14
    '5 1 2 + 4 * + 3 -' = 14
    '10 2 /' = 5.0
    '1 +' -> error: not enough operands
    '4 0 /' -> error: division by zero

Approach:
    Read tokens left to right. Numbers are pushed. An operator pops two
    operands, applies itself and pushes the result.

Step-by-step logic:
    1. Split the string on spaces.
    2. Number token: convert and push.
    3. Operator token: pop right operand first, then left operand (order
    matters for - and /), compute, push the result.
    4. After all tokens exactly one value must remain: the answer.

Why it works:
    When an operator appears its two operands are the two most recent
    unconsumed values, which are the top two stack items.

Time complexity:
    O(n) for n tokens.

Space complexity:
    O(n) for the operand stack.

Edge cases:
    Too few operands, leftover operands, division by zero, unknown token,
    empty expression, operand order for subtraction and division.

Alternative approach:
    Convert to a tree and evaluate recursively, or convert postfix back to
    infix. Stack evaluation is the simplest and fastest.
"""


def apply_operator(operator, left, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if right == 0:
        raise ZeroDivisionError("division by zero")
    return left / right


def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token in ("+", "-", "*", "/"):
            if len(stack) < 2:
                raise ValueError("not enough operands")
            right = stack.pop()  # right operand is on top
            left = stack.pop()
            stack.append(apply_operator(token, left, right))
        else:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError("unknown token " + token)
    if len(stack) != 1:
        raise ValueError("not enough operands" if not stack else "too many operands")
    return stack[0]


def main():
    expressions = ["2 3 4 * +", "5 1 2 + 4 * + 3 -", "10 2 /", "1 +", "4 0 /"]
    for expression in expressions:
        try:
            print("%r = %s" % (expression, evaluate_postfix(expression)))
        except (ValueError, ZeroDivisionError) as error:
            print("%r -> error: %s" % (expression, error))


if __name__ == "__main__":
    main()
