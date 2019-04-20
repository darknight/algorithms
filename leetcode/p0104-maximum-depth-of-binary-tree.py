#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[2]
    x[1].left = x[3]
    x[1].right = x[4]
    x[2].right = x[5]
    x[5].left = x[6]
    root = x[0]

    print(Solution().maxDepth(root))
