r"""
Problem: Undo and Redo in a Text Editor

Problem statement:
    Simulate a tiny text editor with type, undo and redo commands. Undo must
    reverse the most recent change; redo re-applies an undone change unless
    a new edit was made after the undo.

What it teaches:
    Using two stacks to model history, a pattern behind real undo systems.

Input example:
    type "Hello", type " World", undo, undo, redo, type "!", redo

Expected output:
    type 'Hello'   -> 'Hello'
    type ' World'  -> 'Hello World'
    undo           -> 'Hello'
    undo           -> ''
    redo           -> 'Hello'
    type '!'       -> 'Hello!'
    redo           -> nothing to redo, text 'Hello!'
    undo           -> 'Hello'

Approach:
    Keep an undo stack of typed fragments and a redo stack of undone ones.

Step-by-step logic:
    1. type(s): append s to the text, push s on the undo stack, clear the
    redo stack (history branches).
    2. undo(): pop the last fragment, remove it from the end of the text and
    push it on the redo stack.
    3. redo(): pop from the redo stack, re-append it and push it on undo.
    4. Report when a stack is empty instead of failing.

Why it works:
    The latest edit is always the one to undo first (LIFO), and the redo
    stack stores undone edits in reverse so they replay in the correct order.

Time complexity:
    O(k) per operation where k is the fragment length (O(1) stack work).

Space complexity:
    O(total typed characters) for the two stacks.

Edge cases:
    Undo on empty history, redo with nothing undone, redo after a new edit
    (must be cleared), repeated undo until empty.

Alternative approach:
    Store full snapshots of the text on each step; simpler but uses far more
    memory (command pattern stores only the change).
"""


class Editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_text(self, fragment):
        self.text += fragment
        self.undo_stack.append(fragment)
        self.redo_stack.clear()  # a new edit invalidates the redo history
        return True

    def undo(self):
        if not self.undo_stack:
            return False
        fragment = self.undo_stack.pop()
        self.text = self.text[:len(self.text) - len(fragment)]
        self.redo_stack.append(fragment)
        return True

    def redo(self):
        if not self.redo_stack:
            return False
        fragment = self.redo_stack.pop()
        self.text += fragment
        self.undo_stack.append(fragment)
        return True


def main():
    editor = Editor()
    commands = [("type", "Hello"), ("type", " World"), ("undo", None),
                ("undo", None), ("redo", None), ("type", "!"),
                ("redo", None), ("undo", None)]
    for name, argument in commands:
        if name == "type":
            editor.type_text(argument)
            label = "type %r" % argument
        elif name == "undo":
            editor.undo()
            label = "undo"
        else:
            changed = editor.redo()
            label = "redo"
            if not changed:
                print("%-14s -> nothing to redo, text %r" % (label, editor.text))
                continue
        print("%-14s -> %r" % (label, editor.text))


if __name__ == "__main__":
    main()
