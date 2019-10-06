#!/usr/bin/env python3

from typing import List
from typing import Any


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_tree(data_list: List[Any]) -> TreeNode:
    if len(data_list) == 0:
        return None

    node = TreeNode(data_list.pop(0))
    queue = [node]
    while len(data_list) > 0:
        root = queue.pop(0)
        left_val = data_list.pop(0)
        if left_val is not None:
            root.left = TreeNode(left_val)
        try:
            right_val = data_list.pop(0)
            if right_val is not None:
                root.right = TreeNode(right_val)
        except:
            pass
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)

    return node


if __name__ == '__main__':
    root = construct_tree([10, 9, 8, 7, 6, None, 5, 4, 3, None, 2])
    assert root.val == 10

    assert root.left.val == 9
    assert root.right.val == 8

    assert root.left.left.val == 7
    assert root.left.right.val == 6

    assert root.right.left is None
    assert root.right.right.val == 5

    assert root.left.left.left.val == 4
    assert root.left.left.right.val == 3

    assert root.left.right.left is None
    assert root.left.right.right.val == 2

    root = construct_tree([1, 2, 3, 4, 5, 6, None, 7])
    assert root.val == 1

    assert root.left.val == 2
    assert root.right.val == 3

    assert root.left.left.val == 4
    assert root.left.right.val == 5

    assert root.right.left.val == 6
    assert root.right.right is None

    assert root.left.left.left.val == 7
