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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        self.preorder(root1, res1)
        self.preorder(root2, res2)

        size1 = len(res1)
        size2 = len(res2)
        res = []
        i = 0
        j = 0
        while i < size1 and j < size2:
            if res1[i] < res2[j]:
                res.append(res1[i])
                i += 1
            elif res1[i] > res2[j]:
                res.append(res2[j])
                j += 1
            else:
                res.append(res1[i])
                res.append(res2[j])
                i += 1
                j += 1

        while i < size1:
            res.append(res1[i])
            i += 1

        while j < size2:
            res.append(res2[j])
            j += 1

        return res

    def preorder(self, root: TreeNode, res: List[int]):
        if root is None:
            return
        self.preorder(root.left, res)
        res.append(root.val)
        self.preorder(root.right, res)


if __name__ == '__main__':
    pass
