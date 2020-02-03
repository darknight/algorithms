#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def WA_maxProduct(self, root: TreeNode) -> int:
        nums = []
        self.inorder(root, nums)

        size = len(nums)
        prefix_incl = [0] * size
        prefix_incl[0] = nums[0]
        for i in range(1, size):
            prefix_incl[i] = prefix_incl[i-1] + nums[i]
        suffix_incl = [0] * size
        suffix_incl[-1] = nums[-1]
        for j in range(size-2, -1, -1):
            suffix_incl[j] = suffix_incl[j+1] + nums[j]

        res = 1
        for i in range(size - 1):
            product = prefix_incl[i] * suffix_incl[i+1]
            res = max(res, product)

        return res % (10**9+7)

    def inorder(self, root: TreeNode, nums: List[int]):
        if root is None:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

    def TLE_maxProduct(self, root: TreeNode) -> int:
        res = [0]
        self.search(root, res)
        return res[0] % (10 ** 9 + 7)

    def search(self, root: TreeNode, res: List[int]):
        if root is None:
            return
        left = self.subtree(root.left)
        right = self.subtree(root.right)
        res[0] = max(res[0], (left + root.val) * right, (right + root.val) * left)
        if root.left is not None:
            root.left.val += right + root.val
            self.search(root.left, res)
        if root.right is not None:
            root.right.val += left + root.val
            self.search(root.right, res)

    @functools.lru_cache(None)           # TLE
    def subtree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.subtree(root.left)   # RecursionError: maximum recursion depth exceeded
        right = self.subtree(root.right) # RecursionError: maximum recursion depth exceeded
        return left + right + root.val

    def maxProduct(self, root: TreeNode) -> int:
        """
        refer to this smart solution
        https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/496700/Python3-a-concise-recursive-solution
        """
        sums = []
        def subtree(root: TreeNode) -> int:
            if root is None:
                return 0
            left = subtree(root.left)
            right = subtree(root.right)
            val = left + right + root.val
            sums.append(val)
            return val

        total = subtree(root)
        res = [v * (total - v) for v in sums]
        return max(res) % (10**9+7)

if __name__ == '__main__':
    pass
