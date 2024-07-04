#!/usr/bin/env python
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
    arr = boxes[0]
    opened_boxes = [0]
    for box in arr:
        if box not in opened_boxes:
            opened_boxes.append(box)
            open_box(box, boxes, opened_boxes)
    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False


def open_box(box, boxes, opened_boxes):
    """
    Recursively opens a box and adds its keys to the list of opened boxes.

    Args:
        box (int): The index of the box to open.
        boxes (list of list of int): A list of lists where each sublist
         represents a box and contains keys to other boxes.
        opened_boxes (list of int): A list of indices of boxes that have
         been opened.
    """
    arr = boxes[box]
    for i in arr:
        if i not in opened_boxes:
            opened_boxes.append(i)
            open_box(i, boxes, opened_boxes)
