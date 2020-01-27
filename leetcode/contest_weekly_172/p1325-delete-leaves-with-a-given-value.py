#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return root
        parent = TreeNode(0)
        parent.left = root
        self.delete(root, parent, target)
        return parent.left

    def delete(self, curr: TreeNode, parent: TreeNode, target: int):
        if curr is None:
            return
        self.delete(curr.left, curr, target)
        self.delete(curr.right, curr, target)
        if curr.left is None and curr.right is None and target == curr.val:
            if parent.left is curr:
                parent.left = None
            else:
                parent.right = None


if __name__ == '__main__':
    pass
