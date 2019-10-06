#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except:
    pass

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        def in_order(root: TreeNode, accu: Set[int]):
            if root is None:
                return
            in_order(root.left, accu)
            accu.add(root.val)
            in_order(root.right, accu)

        set1 = set()
        in_order(root1, set1)

        set2 = set()
        in_order(root2, set2)

        for num in set1:
            if target - num in set2:
                return True

        return False


if __name__ == '__main__':
    root1 = construct_tree([2,1,4])
    root2 = construct_tree([1,0,3])
    assert Solution().twoSumBSTs(root1, root2, 5) is True

    root1 = construct_tree([0,-10,10])
    root2 = construct_tree([5,1,7,0,2])
    assert Solution().twoSumBSTs(root1, root2, 18) is False