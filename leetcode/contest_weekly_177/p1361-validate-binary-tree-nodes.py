#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited_nodes = [0] * n
        visited_left = [0] * n
        visited_right = [0] * n

        def preorder(root: int):
            visited_nodes[root] += 1
            left = leftChild[root]
            if left != -1 and visited_left[root] == 0:
                visited_left[root] = 1
                preorder(left)
            right = rightChild[root]
            if right != -1 and visited_right[root] == 0:
                visited_right[root] = 1
                preorder(right)

        preorder(0)

        for i in range(n):
            if visited_nodes[i] != 1:
                return False
            if leftChild[i] > -1 and visited_left[i] == 0:
                return False
            if rightChild[i] > -1 and visited_right[i] == 0:
                return False

        return True




if __name__ == '__main__':
    assert Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]) is True
    assert Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]) is False
    assert Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]) is False
    assert Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]) is False

    assert Solution().validateBinaryTreeNodes(4,[1, 2, 0, -1],[-1, -1, -1, -1]) is False
