#!/usr/bin/python3
"""lockboxes module"""
from queue import Queue


def canUnlockAll(boxes):
    """return true if all boxes can open otherwise return False"""
    if len(boxes[0]) == 0:
        return False
    count = 0
    key_queue = []
    key_queue.extend(boxes[0])
    keys = set()
    keys.add(0)
    keys.update(boxes[0])
    boxesList = set()
    boxesList.update(list(range(0, len(boxes))))
    
    while len(key_queue) > 0 and  count <= len(boxesList):
        count += 1
        key = key_queue.pop(0)
        if key < len(boxesList):
            key_queue.extend(boxes[key])
            for k in boxes[key]:
                keys.update(boxes[key])
    if len(boxesList - keys) == 0:
        return True
    return False
        