#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs
        """
        res = [0]

        def dfs(curr: TreeNode, prev_max: int):
            if curr is None:
                return

            curr_max = prev_max
            if curr.val >= prev_max:
                res[0] += 1
                curr_max = curr.val

            if curr.left is not None:
                dfs(curr.left, curr_max)
            if curr.right is not None:
                dfs(curr.right, curr_max)

        dfs(root, root.val)
        return res[0]


if __name__ == '__main__':
    pass
