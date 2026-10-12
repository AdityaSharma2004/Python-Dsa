r"""
Problem: Convert Infix to Postfix (Shunting-Yard)

Problem statement:
    Convert an infix expression such as "a+b*c" into postfix notation
    "abc*+". Support + - * / ^ and parentheses; ^ is right-associative.

What it teaches:
    Operator precedence, associativity and the use of a stack to hold
    operators until their turn comes.

Input example:
    "a+b*c", "(a+b)*c", "a+b*c-d/e", "a^b^c", "((a+b))*(c-d)"

Expected output:
    a+b*c -> abc*+
    (a+b)*c -> ab+c*
    a+b*c-d/e -> abc*+de/-
    a^b^c -> abc^^
    ((a+b))*(c-d) -> ab+cd-*
    a+(b -> error: mismatched parentheses

Approach:
    Output operands immediately. Keep operators on a stack; before pushing a
    new operator pop operators of higher (or equal, for left-associative)
    precedence to the output.

Step-by-step logic:
    1. Operand (letter or digit): append to output.
    2. '(' : push. ')' : pop to output until '(' is found, then discard it.
    3. Operator: while the top has higher precedence, or equal precedence and
    the new operator is left-associative, pop it to output; then push the
    new operator.
    4. At the end pop every remaining operator to the output.

Why it works:
    The stack keeps pending operators in increasing precedence order, so an
    operator is emitted only after everything that binds tighter than it has
    been emitted.

Time complexity:
    O(n).

Space complexity:
    O(n).

Edge cases:
    Mismatched parentheses, nested parentheses, chained ^ (right
    associative), equal-precedence operators (left to right), single operand.

Alternative approach:
    Build an expression tree and print its post-order traversal.
"""

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(expression):
    output = []
    stack = []
    for char in expression:
        if char == " ":
            continue
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("mismatched parentheses")
            stack.pop()  # discard '('
        elif char in PRECEDENCE:
            while stack and stack[-1] != "(" and (
                PRECEDENCE[stack[-1]] > PRECEDENCE[char]
                or (PRECEDENCE[stack[-1]] == PRECEDENCE[char] and char != "^")
            ):
                output.append(stack.pop())
            stack.append(char)
        else:
            raise ValueError("unknown character " + char)
    while stack:
        top = stack.pop()
        if top == "(":
            raise ValueError("mismatched parentheses")
        output.append(top)
    return "".join(output)


def main():
    samples = ["a+b*c", "(a+b)*c", "a+b*c-d/e", "a^b^c", "((a+b))*(c-d)", "a+(b"]
    for expression in samples:
        try:
            print("%s -> %s" % (expression, infix_to_postfix(expression)))
        except ValueError as error:
            print("%s -> error: %s" % (expression, error))


if __name__ == "__main__":
    main()
