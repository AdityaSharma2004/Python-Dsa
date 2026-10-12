r"""
Problem title: Insert and Delete in an Array by Index

Problem statement:
    Implement insert_at(items, index, value) and delete_at(items, index) by hand
    - shifting elements yourself instead of calling list.insert() or list.pop().
    Return the new length and count how many elements were shifted.

What it teaches:
    Arrays are contiguous, so adding or removing in the middle forces the
    elements after that position to move. This is why array insertion is O(n).

Input example:
    items = [10, 20, 30, 40, 50]
    insert 25 at index 2  -> [10, 20, 25, 30, 40, 50]
    delete index 0        -> [20, 25, 30, 40, 50]

Expected output:
    start: [10, 20, 30, 40, 50]
    insert 25 at index 2: [10, 20, 25, 30, 40, 50] shifts = 3
    insert 60 at the end: [10, 20, 25, 30, 40, 50, 60] shifts = 0
    insert 5 at the front: [5, 10, 20, 25, 30, 40, 50, 60] shifts = 7
    delete index 0 (removed 5 ): [10, 20, 25, 30, 40, 50, 60] shifts = 7
    delete last (removed 60 ): [10, 20, 25, 30, 40, 50] shifts = 0
    insert into empty: [99]
    delete from empty -> index out of range
    insert at index 5 of 2 items -> index out of range

Approach:
    Insert: grow the list by one slot, shift elements right (from the end back
    to the index), then place the value.
    Delete: shift elements left over the removed slot, then shrink the list.

Step-by-step logic:
    1. Validate the index (0..len for insert, 0..len-1 for delete).
    2. Insert: append a placeholder, then for position from last down to
       index+1 copy items[position-1] into items[position].
    3. Write the new value at index.
    4. Delete: for position from index to len-2 copy items[position+1] into
       items[position].
    5. Remove the last (now duplicate) slot with pop().

Why it works:
    Moving elements in the right direction (right-to-left for insert,
    left-to-right for delete) never overwrites a value that still needs copying.

Time complexity:
    O(n) worst case (insert/delete at the front shifts every element);
    O(1) at the end of the list.

Space complexity:
    O(1) extra - the list is modified in place.

Edge cases:
    - Insert at index len(items) behaves like append (0 shifts).
    - Insert into an empty list at index 0.
    - Delete from an empty list or an out-of-range index -> IndexError.
    - Negative indices are rejected here to keep the logic explicit.

Alternative approach:
    list.insert(i, x) and list.pop(i) do the same shifting in C, still O(n).
    If you only add/remove at the ends, collections.deque gives O(1).
"""


def insert_at(items, index, value):
    """Insert value at index by shifting. Return the number of shifts."""
    if index < 0 or index > len(items):
        raise IndexError("index out of range")
    items.append(None)  # make room for one more element
    shifts = 0
    for position in range(len(items) - 1, index, -1):
        items[position] = items[position - 1]  # move right, starting at the end
        shifts += 1
    items[index] = value
    return shifts


def delete_at(items, index):
    """Delete the element at index by shifting. Return (removed value, shifts)."""
    if index < 0 or index >= len(items):
        raise IndexError("index out of range")
    removed = items[index]
    shifts = 0
    for position in range(index, len(items) - 1):
        items[position] = items[position + 1]  # move left over the gap
        shifts += 1
    items.pop()  # drop the leftover last slot
    return removed, shifts


def main():
    items = [10, 20, 30, 40, 50]
    print("start:", items)
    shifts = insert_at(items, 2, 25)
    print("insert 25 at index 2:", items, "shifts =", shifts)
    shifts = insert_at(items, len(items), 60)
    print("insert 60 at the end:", items, "shifts =", shifts)
    shifts = insert_at(items, 0, 5)
    print("insert 5 at the front:", items, "shifts =", shifts)
    removed, shifts = delete_at(items, 0)
    print("delete index 0 (removed", removed, "):", items, "shifts =", shifts)
    removed, shifts = delete_at(items, len(items) - 1)
    print("delete last (removed", removed, "):", items, "shifts =", shifts)

    empty = []
    insert_at(empty, 0, 99)
    print("insert into empty:", empty)
    try:
        delete_at([], 0)
    except IndexError as error:
        print("delete from empty ->", error)
    try:
        insert_at([1, 2], 5, 9)
    except IndexError as error:
        print("insert at index 5 of 2 items ->", error)


if __name__ == "__main__":
    main()
