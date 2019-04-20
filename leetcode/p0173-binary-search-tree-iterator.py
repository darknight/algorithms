# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        node = self.root
        while node:
            self.stack.append(node)
            node = node.left


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0


    # @return an integer, the next smallest number
    def next(self):
        val = None
        if self.hasNext():
            node = self.stack.pop()
            val = node.val
            temp = node.right
            while temp:
                self.stack.append(temp)
                temp = temp.left
        return val
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    x = [TreeNode(i) for i in range(7)]
    x[1].left =  x[0]
    x[1].right = x[4]
    x[4].left = x[2]
    x[2].right = x[3]
    x[5].left = x[1]
    x[5].right = x[6]
    root = x[5]

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())

    print v


    root = TreeNode(10)

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())

    print v


