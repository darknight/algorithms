# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []

        def _dfs(node, partsum, path):
            if node is None:
                return
            #print node.val, path
            if node.left is None and node.right is None:
                if node.val + partsum == sum:
                    path.append(node.val)
                    res.append(path[:])
                    path.pop()
            path.append(node.val)
            _dfs(node.left, partsum+node.val, path)
            _dfs(node.right, partsum+node.val, path)
            x = path.pop()

        _dfs(root, 0, [])
        return res

if __name__ == '__main__':
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t11 = TreeNode(11)
    t13 = TreeNode(13)
    t5.left = t4
    t5.right = t8
    t4.left = t11
    t11.left = t7
    t11.right = t2
    t8.left = t13
    t8.right = t9
    t_2 = TreeNode(-2)
    t_3 = TreeNode(-3)
    t_2.right = t_3
    print Solution().pathSum(t_2, -5)
