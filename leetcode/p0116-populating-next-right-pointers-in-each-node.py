#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None or root.left is None or root.right is None:
            return
        if root.left and root.right:
            root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[2]
    x[1].left = x[3]
    x[1].right = x[4]
    x[2].left = x[5]
    x[2].right = x[6]
    p = x[0]
    
    Solution().connect(p)
    Solution().connect(None)

    print(p.left.next.val == 2)
    print(p.left.right.next.val == 5)
