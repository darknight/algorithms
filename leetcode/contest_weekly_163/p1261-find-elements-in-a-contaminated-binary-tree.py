#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class FindElements:

    def __init__(self, root: TreeNode):
        vals = []
        self.recover(root, 0, vals)
        vals.sort()
        self.root = root
        self.vals = vals

    def recover(self, node: TreeNode, value: int, vals: List[int]):
        if node is None:
            return
        node.val = value
        vals.append(value)
        self.recover(node.left, 2 * value + 1, vals)
        self.recover(node.right, 2 * value + 2, vals)

    def find(self, target: int) -> bool:
        try:
            self.vals.index(target)
            return True
        except:
            return False


if __name__ == '__main__':
    pass
