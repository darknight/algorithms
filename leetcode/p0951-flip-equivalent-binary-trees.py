#!/usr/bin/env python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    from typing import List
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            print("return %s", root1 == root2)
            return root1 == root2
        # test root
        if root1.val != root2.val:
            print("return false root1 = %s, root2 = %s" % (root1.val, root2.val))
            return False
        print("root1 = %s, root2 = %s" % (root1.val, root2.val))
        # decide if swap left & right
        if root1.left is None and root2.left is not None:
            print("cond1")
            root1.left, root1.right = root1.right, root1.left
        elif root1.right is None and root2.right is not None:
            print("cond2")
            root1.left, root1.right = root1.right, root1.left
        elif root1.left is not None and root2.right is not None and root1.left.val == root2.right.val:
            print("cond3")
            root1.left, root1.right = root1.right, root1.left
        elif root1.right is not None and root2.left is not None and root1.right.val == root2.left.val:
            print("cond4")
            root1.left, root1.right = root1.right, root1.left

        left = self.flipEquiv(root1.left, root2.left)
        right = self.flipEquiv(root1.right, root2.right)

        return left and right

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n7
    n5.right = n8
    n3.left = n6

    m1 = TreeNode(1)
    m2 = TreeNode(2)
    m3 = TreeNode(3)
    m4 = TreeNode(4)
    m5 = TreeNode(5)
    m6 = TreeNode(6)
    m7 = TreeNode(7)
    m8 = TreeNode(8)
    m1.left = m3
    m1.right = m2
    m3.right = m6
    m2.left = m4
    m2.right = m5
    m5.left = m8
    m5.right = m7

    assert Solution().flipEquiv(n1, m1) is True
