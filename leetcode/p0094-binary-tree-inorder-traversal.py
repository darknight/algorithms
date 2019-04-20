# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root.right)
        stack.append(root.val)
        stack.append(root.left)
        while len(stack) > 0:
            x = stack.pop()
            if isinstance(x, int):
                res.append(x)
            elif isinstance(x, TreeNode) and x is not None:
                stack.append(x.right)
                stack.append(x.val)
                stack.append(x.left)
        return res

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    print Solution().inorderTraversal(node1)
