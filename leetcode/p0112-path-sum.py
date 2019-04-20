#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        # NOTE:
        #if root.val < sum: # WA for this case: {-2,#,-3} -5
        #if root.val != sum: # WA for this case: {1,-2,-3,1,3,-2,#,-1}, -1
        res1 = self.hasPathSum(root.left, sum-root.val)
        res2 = self.hasPathSum(root.right, sum-root.val)
        return res1 or res2

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    n4 = TreeNode(4)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node11 = TreeNode(11)
    node13 = TreeNode(13)

    node5.left = node4
    node5.right = node8
    node4.left = node11
    node8.left = node13
    node8.right = n4
    node11.left = node7
    node11.right = node2
    n4.right = node1

    print(Solution().hasPathSum(node5, 22))
