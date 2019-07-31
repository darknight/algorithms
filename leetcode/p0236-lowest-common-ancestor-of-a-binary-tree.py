#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        idea:
        find ancestor list for both p and q
        """
        #TODO: slow & improve
        if root is None or p is None or q is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        def _dfs(root, target, path):
            path.append(root)
            if root.val == target.val:
                return True
            if root.left is not None:
                if _dfs(root.left, target, path) is True:
                    return True
            if root.right is not None:
                if _dfs(root.right, target, path) is True:
                    return True
            path.pop()
            return False

        plist = []
        qlist = []
        _dfs(root, p, plist)
        _dfs(root, q, qlist)

        i = 0
        while i < len(plist) and i < len(qlist) and plist[i].val == qlist[i].val:
            i += 1
        return plist[i-1]

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
    assert Solution().lowestCommonAncestor(n3, n5, n1).val == 3
    assert Solution().lowestCommonAncestor(n3, n5, n4).val == 5
    assert Solution().lowestCommonAncestor(n3, n5, n0).val == 3
