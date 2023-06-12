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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        level = 0
        res = 0
        max_val = -math.inf

        while len(queue) > 0:
            level += 1
            children = []
            level_sum = 0
            for node in queue:
                level_sum += node.val
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            if level_sum > max_val:
                max_val = level_sum
                res = level
            queue = children

        return res


if __name__ == '__main__':
    pass
