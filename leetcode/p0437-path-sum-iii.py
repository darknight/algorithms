#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Any
try:
    from _tree import *
except:
    pass


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """TODO: slow"""

        if root is None:
            return 0

        def findPath(node: TreeNode, part_sum: int, accu: List[int]):
            if node is None:
                return
            if node.val == part_sum:
                accu[0] += 1
            findPath(node.left, part_sum - node.val, accu)
            findPath(node.right, part_sum - node.val, accu)

        res = [0]
        queue = [root]

        while len(queue) > 0:
            node = queue.pop(0)
            findPath(node, sum, res)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return res[0]



if __name__ == '__main__':
    root = construct_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    assert Solution().pathSum(root, 8) == 3
    root = construct_tree([1,-2,-3,1,3,-2,None,-1])
    assert Solution().pathSum(root, -1) == 4
