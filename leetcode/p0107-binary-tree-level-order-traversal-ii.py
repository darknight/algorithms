#!/usr/bin/env python3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        results = []
        queue = [root, None]
        while len(queue) > 0:
            level = []
            node = queue.pop(0)
            if node is None:
                continue
            while node is not None:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node = queue.pop(0)
            queue.append(None)
            results.append(level)
        results.reverse()
        return results

if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print(Solution().levelOrder(n1))
