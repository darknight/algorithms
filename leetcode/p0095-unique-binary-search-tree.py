# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #TODO: slow, improve it
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        def _subtree(i, j):
            if i > j:
                return [None]
            elif i == j:
                return [TreeNode(i+1)]
            else:
                k = i
                res = []
                while k <= j:
                    left_tree = _subtree(i, k-1)
                    right_tree = _subtree(k+1, j)
                    for left in left_tree:
                        for right in right_tree:
                            root = TreeNode(k+1)
                            root.left = left
                            root.right = right
                            res.append(root)
                    k += 1
                return res
        comb = _subtree(0, n-1)
        return comb

if __name__ == '__main__':
    for root in Solution().generateTrees(2):
        print '-----------'
        def _pp(node):
            if node is None:
                return
            print node.val
            print 'left', _pp(node.left)
            print 'right', _pp(node.right)
        _pp(root)

