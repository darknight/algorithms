#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #TODO: too slow, improve...
        res = []
        if root is None:
            return ''
        
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node is None:
                res.append('x')
            else:
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        vals = data.split(',')
        root = TreeNode(vals.pop(0))
        stack = [root]
        while stack:
            if len(vals) == 0:
                break
            node = stack.pop(0)
            left_val = vals.pop(0)
            if left_val != 'x':
                left = TreeNode(left_val)
                node.left = left
                stack.append(left)
            right_val = vals.pop(0)
            if right_val != 'x':
                right = TreeNode(right_val)
                node.right = right
                stack.append(right)
        return root 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    nodes = [TreeNode(i+1) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]
    codec = Codec()
    s = codec.serialize(nodes[0])
    print(s)
    r = codec.deserialize(s)
    def _preorder(node):
        if node:
            print(node.val)
            print('left')
            _preorder(node.left)
            print('right')
            _preorder(node.right)
    _preorder(r)
