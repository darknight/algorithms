# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        queue = [root, None]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if queue[0] is None:
                res.append(node.val)
                queue.append(None)
        return res

if __name__ == '__main__':
    nodes = [TreeNode(i+1) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[3]
    print Solution().rightSideView(nodes[0])
