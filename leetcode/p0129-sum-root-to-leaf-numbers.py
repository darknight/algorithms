# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        numbers = []
        number = []

        def _findNumber(root):
            if root is None:
                return
            number.append(root.val)
            if root.left is None and root.right is None:#leaf
                num = 0
                for i, x in enumerate(number):
                    num = num * 10 + x
                numbers.append(num)
            _findNumber(root.left)
            _findNumber(root.right)
            number.pop()

        _findNumber(root)
        return sum(numbers)

if __name__ == '__main__':
    n1 = TreeNode(4)
    n2 = TreeNode(9)
    n3 = TreeNode(0)
    n4 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.right = n4

    print Solution().sumNumbers(n1)
