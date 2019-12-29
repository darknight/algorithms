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
    def AC_deepestLeavesSum(self, root: TreeNode) -> int:
        res = [0]
        self.level_order([root], res)

        return res[0]

    def level_order(self, roots: List[TreeNode], res: List[int]):
        next_level = []
        curr_sum = 0
        for root in roots:
            curr_sum += root.val
            if root.left is not None:
                next_level.append(root.left)
            if root.right is not None:
                next_level.append(root.right)

        if len(next_level) == 0:
            res[0] = curr_sum
            return
        else:
            self.level_order(next_level, res)

    # TODO: iterative solution
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/deepest-leaves-sum/discuss/463239/Python-Level-Traversal
        """
        pass

if __name__ == '__main__':
    pass
