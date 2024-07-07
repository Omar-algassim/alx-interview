#!/usr/bin/python3
"""lockboxes module"""
from queue import Queue


def canUnlockAll(boxes):
    """return true if all boxes can open otherwise return False"""
    if len(boxes[0]) == 0:
        return False
    keys = [0]
    q = Queue()
    q.put(boxes[0])
    while not q.empty():
        box = q.get()
        for key in box:
            if key not in keys and key < len(boxes):
                q.put(boxes[key])
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False