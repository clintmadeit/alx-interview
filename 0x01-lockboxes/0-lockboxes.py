#!/usr/bin/python3

""" Lockboxes """

def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)