# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flatten2(root):
            if root is None:
                return None
            if root.left is None and root.right is None:
                return root
            left_leaf = _flatten2(root.left)
            right_leaf = _flatten2(root.right)
            if root.left is None:
                return right_leaf
            elif root.right is None:
                root.right = root.left
                root.left = None
                return left_leaf
            else:
                right_node = root.right
                root.right = root.left
                root.left = None
                left_leaf.right = right_node
                return right_leaf

        _flatten2(root)

    def v1flatten(self, root):
        '''
        idea: return the leaf node after each merge
        Time Limit Exceeded
        '''
        def _flatten2(root):
            if root is None:
                return None
            if root and root.left is None and root.right is None:
                return root
            left_leaf = _flatten2(root.left)
            right_leaf = _flatten2(root.right)
            if root.left is None:
                return right_leaf
            if root.right is None:
                root.right = root.left
                return left_leaf
            right_node = root.right
            root.right = root.left
            left_leaf.right = right_node
            while right_node.right:
                right_node = right_node.right
            return right_node

        _flatten2(root)

    def v2flatten(self, root):
        '''
        Time Limit Exceeded
        '''
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is None:
            return
        if root.right is None:
            root.right = root.left
            return
        node = root.left
        while node.right:
            node = node.right
        right = root.right
        root.right = root.left
        node.right = right

    def v3flatten(self, root):
        '''
        idea: find preorder list, then chain them all
        Time Limit Exceeded
        '''
        nodes = []
        def _preorder_traversal(node):
            if node is None:
                return
            nodes.append(node)
            _preorder_traversal(node.left)
            _preorder_traversal(node.right)
        _preorder_traversal(root)
        i = 0
        while i < len(nodes) - 1:
            nodes[i].right = nodes[i+1]
            i += 1

    def v4flatten(self, root):
        '''
        try not to find the most right leaf node, but still
        Time Limit Exceeded
        '''
        current_node = None
        stack = []
        if root is None:
            return
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        stack.append((root,))
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            if type(node) is tuple:
                node = node[0]
                if current_node is not None:
                    current_node.right = node
                current_node = node
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append((node,))

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[0].left =  x[1]
    x[0].right = x[4]
    x[1].left = x[2]
    x[1].right = x[3]
    x[4].right = x[5]
    x[4].left = x[6]
    root = x[0]

    Solution().flatten(root)

    while root:
        print root.val
        root = root.right

