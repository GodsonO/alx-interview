#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.
    """
    if not boxes or type(boxes) is not list:
        return False

    box_opened = [0]
    for n in box_opened:
        for key in boxes[n]:
            if key not in box_opened and key < len(boxes):
                box_opened.append(key)

    if len(box_opened) == len(boxes):
        return True

    return False
