#!/usr/bin/python3
"""
This module contains a function to determine if all the boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist
         represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0 or boxes is None:
        return False

    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                if len(opened_boxes) == len(boxes):
                    return True
                new_keys.update(boxes[key])
        keys = new_keys

    return len(opened_boxes) == len(boxes)


def canUnlockAll_simple(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist
         represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked_boxes, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked_boxes = [0]
    for n in unlocked_boxes:
        for key in boxes[n]:
            print(f"checking key boxes[{key}] in unlocked_boxes")
            if key not in unlocked_boxes and key < len(boxes):
                print(f"adding key {key}")
                unlocked_boxes.append(key)
                if len(unlocked_boxes) == len(boxes):
                    return True
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
