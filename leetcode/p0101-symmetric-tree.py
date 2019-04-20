#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):

        def _mirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    res1 = _mirror(node1.left, node2.right)
                    res2 = _mirror(node1.right, node2.left)
                    return res1 and res2
            return False

        if root is None:
            return True
        if root.left is None and root.right is not None:
            return False
        elif root.right is None and root.left is not None:
            return False
        else:
            res = _mirror(root.left, root.right)
            return res

    # TODO: solve it iteratively
    def isSymmetric2(self, root):
        pass

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(3)
    n6 = TreeNode(4)
    #n7 = TreeNode(4)
    n7 = TreeNode(8)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n6
    n3.left = n7
    n3.right = n5

    print(Solution().isSymmetric(n1))

