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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        while len(queue) > 0:
            next_level = []
            total = 0
            cnt = len(queue)
            while len(queue) > 0:
                node = queue.pop(0)
                total += node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            res.append(total/cnt)
            queue = next_level

        return res


if __name__ == '__main__':
    pass
