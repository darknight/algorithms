# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):

        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            if root.left:
                return 1 + self.minDepth(root.left)
            if root.right:
                return 1 + self.minDepth(root.right)

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[2]
    x[1].left = x[3]
    x[1].right = x[4]
    x[3].left = x[5]
    x[3].right = x[6]
    root = x[0]

    print Solution().minDepth(root)
