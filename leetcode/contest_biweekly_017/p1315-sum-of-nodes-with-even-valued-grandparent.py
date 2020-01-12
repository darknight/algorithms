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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, None, None, res)
        return sum(res)

    def dfs(self, curr: TreeNode, father: TreeNode, grand: TreeNode, res: List[int]):
        if curr is None:
            return
        if grand is not None and grand.val % 2 == 0:
            res.append(curr.val)
        self.dfs(curr.left, curr, father, res)
        self.dfs(curr.right, curr, father, res)


if __name__ == '__main__':
    pass
