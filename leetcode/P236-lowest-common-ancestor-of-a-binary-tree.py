# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #TODO: slow & improve
        if root is None:
            return None

        plist = []
        qlist = []
        def _dfs(root, p, q, path):
            if root is None:
                return
            path.append(root)
            if root is p:
                plist.append(path[:])
            if root is q:
                qlist.append(path[:])
            _dfs(root.left, p, q, path)
            _dfs(root.right, p, q, path)
            path.pop()

        _dfs(root, p, q, [])
        res = None
        max_len = 0
        for path1 in plist:
            for path2 in qlist:
                length = min(len(path1), len(path2))
                tmp_res = None
                tmp_len = 0
                for i in range(length):
                    if path1[i] is path2[i]:
                        tmp_res = path1[i]
                        tmp_len = i + 1
                if tmp_len > max_len:
                    res = tmp_res
        return res

if __name__ == '__main__':
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n2.left = n7
    n2.right = n4
    n1.left = n0
    n1.right = n8
    print Solution().lowestCommonAncestor(n3, n5, n1).val
    print Solution().lowestCommonAncestor(n3, n5, n4).val
    print Solution().lowestCommonAncestor(n3, n5, n0).val
