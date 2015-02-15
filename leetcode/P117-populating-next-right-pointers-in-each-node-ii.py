# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        '''
        bad case:
        {1,2,3,4,#,#,5}
        {1,2,3,4,5,#,6,7,#,#,#,#,8}
        {2,1,3,0,7,9,1,2,#,1,0,#,#,8,8,#,#,#,#,7}
        '''
        # TODO: slow, see other's answer
        if root is None:
            return
        curr_node = root
        while curr_node:
            next_node = curr_node.next
            if curr_node.left is None and curr_node.right is None:
                curr_node = next_node
                continue
            if curr_node.left and curr_node.right:
                curr_node.left.next = curr_node.right
            node1 = curr_node.right or curr_node.left
            node2 = None
            while next_node:
                node2 = next_node.left or next_node.right
                if node2:
                    break
                next_node = next_node.next
            if node2:
                node1.next = node2
            curr_node = next_node
        while root and root.left is None and root.right is None:
            root = root.next
        if root:
            self.connect(root.left or root.right)

if __name__ == '__main__':
    x = [TreeNode(i) for i in range(14)]
    x[1].val = 2
    x[2].val = 1
    x[3].val = 3
    x[4].val = 0
    x[5].val = 7
    x[6].val = 9
    x[7].val = 1
    x[8].val = 2
    x[9].val = 1
    x[10].val = 0
    x[11].val = 8
    x[12].val = 8
    x[13].val = 7
    x[1].left =  x[2]
    x[1].right = x[3]
    x[2].left = x[4]
    x[2].right = x[5]
    x[3].left = x[6]
    x[3].right = x[7]
    x[4].left = x[8]
    x[5].left = x[9]
    x[5].right = x[10]
    x[7].left = x[11]
    x[7].right = x[12]
    x[10].left = x[13]
    p = x[1]
    
    Solution().connect(p)

    print x[10].next.val
