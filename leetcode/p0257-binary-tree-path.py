#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []

        if root == None:
            return res

        def _dfs(root, path):
            path.append(str(root.val))
            if root.left:
                _dfs(root.left, path)
            if root.right:
                _dfs(root.right, path)
            if root.left is None and root.right is None:
                res.append('->'.join(path))
            path.pop()

        _dfs(root, [])
        return res

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.right = n5

    print(Solution().binaryTreePaths(n1))
