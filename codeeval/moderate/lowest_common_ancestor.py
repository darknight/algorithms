import sys

class T(dict):
    def __init__(self, *args, **kwargs):
        super(T, self).__init__(*args, **kwargs)
        self.__dict__ = self

def get_ancestors(tree, node, queue):
    queue.append(tree.val)
    if tree.val == node:
        return True
    if tree.left is not None:
        find = get_ancestors(tree.left, node, queue)
        if find:
            return True
        else:
            queue.pop(-1)
    if tree.right is not None:
        find = get_ancestors(tree.right, node, queue)
        if find:
            return True
        else:
            queue.pop(-1)
    return False

if __name__ == '__main__':
    t1 = T(val='10', left=None, right=None)
    t2 = T(val='29', left=None, right=None)
    t3 = T(val='3', left=None, right=None)
    t4 = T(val='52', left=None, right=None)
    t5 = T(val='20', left=t1, right=t2)
    t6 = T(val='8', left=t3, right=t5)
    tree = T(val='30', left=t6, right=t4)
    #print tree

    test = open(sys.argv[1])
    for line in test:
        n1, n2 = line.strip().split(' ')
        n1_que, n2_que = [], []
        get_ancestors(tree, n1, n1_que) 
        get_ancestors(tree, n2, n2_que)
        #print n1_que, n2_que
        common = n1_que[0]
        for i in range(min(len(n1_que), len(n2_que))):
            if n1_que[i] != n2_que[i]:
                break
            else:
                common = n1_que[i]
        print common

