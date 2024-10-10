#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Each box is numbered sequentially from 0 to n - 1 and may contain keys to
    other boxes. A key with the same number as a box opens that box.

    Args:
    boxes (List[List[int]]): A list of lists where each inner list represents
                             a box and contains the keys (as integers) found
                             in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.

    Note:
    - The first box (boxes[0]) is always unlocked.
    - All keys are assumed to be positive integers.
    - There can be keys that do not have corresponding boxes.

    Examples:
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True
    >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
    True
    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    """
    n = len(boxes)
    unlocked = set([0])  # First box is always unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
