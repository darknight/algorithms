#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):

        def toBST(start, stop):
            if start > stop:
                return None
            mid = (start + stop) / 2
            root = TreeNode(num[mid])
            root.left = toBST(start, mid - 1)
            root.right = toBST(mid + 1, stop)
            return root

        return toBST(0, len(num) - 1)

if __name__ == '__main__':
    root = Solution().sortedArrayToBST([1,2,3,4,5])
    print(root.val == 3)
    print(root.left.val == 1)
    print(root.left.right.val == 2)
    print(root.right.val == 4)
    print(root.right.right.val == 5)
