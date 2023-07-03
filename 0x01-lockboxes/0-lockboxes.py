#!/usr/bin/python3
"""
0. Lockboxes
"""
def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.
    """
    if not boxes:
        return False
    if not isinstance(boxes, list):
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False