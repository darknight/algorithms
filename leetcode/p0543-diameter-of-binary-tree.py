#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def WA_diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        based on the proof of contradiction:
        the longest path must contain longest p which is from root to leaf

        failed case: [0,0,0,0,null,null,0,null,null,null,0]
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        res = 0
        paths = [[root.val]]
        path = []
        self.dfs(root, path, paths)
        paths.sort(key=lambda x: len(x), reverse=True)
        for i in range(1, len(paths)):
            p = paths[0]
            q = paths[i]
            j = 0
            # no one says the numbers are unique
            while j < len(p) and j < len(q) and p[j] == q[j]:
                j += 1
            res = max(res, len(p[j:]) + len(q[j:]) + 1 - 1)

        return res


    def dfs(self, node: TreeNode, path: List[int], paths: List[List[int]]):
        if node is None:
            return
        if node.left is None and node.right is None: # leaf
            path.append(node.val)
            paths.append(path.copy())
            path.pop()
            return

        path.append(node.val)
        self.dfs(node.left, path, paths)
        self.dfs(node.right, path, paths)
        path.pop()

    def AC_diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        for any given node x:
        longest path which x is root = max_height(x.left) + max_height(h.right)

        height vs depth: https://stackoverflow.com/questions/2603692/what-is-the-difference-between-tree-depth-and-height
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0

        res = [0]
        self.max_depth(root, 0, res)

        return res[0]

    def max_depth(self, node, curr: int, res: List[int]) -> int:
        if node is None:
            return curr - 1

        left_d = self.max_depth(node.left, curr + 1, res)
        right_d = self.max_depth(node.right, curr + 1, res)

        res[0] = max(res[0], left_d - curr + right_d - curr)

        return max(left_d, right_d)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        refer to
        https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python
        """
        if root is None:
            return 0

        res = [0]
        self.max_height(root, res)

        return res[0]

    def max_height(self, node: TreeNode, res: List[int]):
        """
        not strictly max height, just use recursive to tag each node!!
        """
        if node is None:
            return 0
        left = self.max_height(node.left, res)
        right = self.max_height(node.right, res)
        res[0] = max(res[0], left + right)

        return max(left, right) + 1

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    assert Solution().diameterOfBinaryTree(n1) == 3

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2
    assert Solution().diameterOfBinaryTree(n1) == 1
