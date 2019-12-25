#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = [0]
        self.in_order(root, L, R, res)
        return res[0]

    def in_order(self, root: TreeNode, L: int, R: int, res: List[int]):
        if root is None:
            return
        if root.val < L and root.right is None:
            return
        if root.val > R and root.left is None:
            return
        if L <= root.val <= R:
            res[0] += root.val
        self.in_order(root.left, L, R, res)
        self.in_order(root.right, L, R, res)

if __name__ == '__main__':
    assert Solution().rangeSumBST()
