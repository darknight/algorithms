# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None: #both are null
            return True
        elif p is not None and q is not None: #both are not null
            if p.val != q.val:
                return False
            same_left = self.isSameTree(p.left, q.left)
            same_right = self.isSameTree(p.right, q.right)
            return same_left and same_right
        else:# either p or q is null
            return False

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[2]
    x[1].left = x[3]
    x[1].right = x[4]
    x[2].right = x[5]
    x[5].left = x[6]
    p = x[0]

    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[2]
    x[1].left = x[3]
    x[1].right = x[4]
    x[2].right = x[5]
    x[5].left = x[6]
    q = x[0]
    #x[6].val = 1

    print Solution().isSameTree(p, q)

