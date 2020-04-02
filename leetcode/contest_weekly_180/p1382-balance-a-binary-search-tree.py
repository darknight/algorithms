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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        self.in_order(root, vals)

        if len(vals) <= 2:
            return root
        mid = len(vals) // 2
        new_root = TreeNode(vals[mid])
        self.new_bst(new_root, vals[:mid], left=True)
        self.new_bst(new_root, vals[mid+1:], left=False)

        return new_root

    def in_order(self, node: TreeNode, vals: List[int]):
        if node is None:
            return
        self.in_order(node.left, vals)
        vals.append(node.val)
        self.in_order(node.right, vals)

    def new_bst(self, parent: TreeNode, nums: List[int], left: bool):
        size = len(nums)
        if size == 0:
            return
        elif size == 1:
            node = TreeNode(nums[0])
            if left is True:
                parent.left = node
            else:
                parent.right = node
        else:
            mid = size // 2
            node = TreeNode(nums[mid])
            if left is True:
                parent.left = node
            else:
                parent.right = node
            self.new_bst(node, nums[:mid], left=True)
            self.new_bst(node, nums[mid+1:], left=False)

    # TODO: a better solution
    # https://leetcode.com/problems/balance-a-binary-search-tree/discuss/539686/JavaC%2B%2B-Sorted-Array-to-BST-O(N)-Clean-code

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    node = Solution().balanceBST(root)
    print(node.val)
