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
    def isBalanced(self, root):
        '''
        refer to: http://feilong.me/2012/06/interesting-python-closures
        '''
        # balanced = True # Wrong! inner method will override this
        balanced = [True]

        # NOTE: balanced should be a container
        # Python 3.x use nonlocal keyword
        def depth(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1

            # NOTE: return more quickly for following case:
            # {0,1,#,2,#,3,#,4,#,5,#,6,#,7,#,8,#,9,#,0,#,...}
            if node.left is None and node.right is not None:
                if any((node.right.left, node.right.right)):
                    balanced[0] = False
                    return 2
            if node.left is not None and node.right is None:
                if any((node.left.left, node.left.right)):
                    balanced[0] = False
                    return 2

            d1 = depth(node.left)
            d2 = depth(node.right)
            if abs(d1-d2) > 1:
                balanced[0] = False
            return max(d1, d2) + 1

        depth(root)
        return balanced[0]

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    #node1.left = node2
    #node1.right = node3
    #node2.left = node4
    #node2.right = node5
    #node4.left = node6
    #node5.right = node7
    node1.left = node2
    node2.left = node3
    node3.left = node4

    print(Solution().isBalanced(node1))

