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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, res: List[int]):
            if root is None:
                return
            if root.left is None and root.right is None:
                res.append(root.val)
                return
            dfs(root.left, res)
            dfs(root.right, res)

        res1 = []
        res2 = []
        dfs(root1, res1)
        dfs(root2, res2)

        return res1 == res2


if __name__ == '__main__':
    pass
