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
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = [0]
        self.dfs(root, 0, 0, res)
        self.dfs(root, 1, 0, res)

        return res[0] - 1

    def dfs(self, node: TreeNode, next_dir: int, cnt: int, res: List):
        if node is None:
            res[0] = max(res[0], cnt)
            return
        if next_dir == 0:
            self.dfs(node.left, 1, cnt+1, res)
            self.dfs(node.left, 0, 0, res)
        else:
            self.dfs(node.right, 0, cnt+1, res)
            self.dfs(node.right, 1, 0, res)



if __name__ == '__main__':
    pass
