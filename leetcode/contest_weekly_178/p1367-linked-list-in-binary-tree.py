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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return self.loop(head, root)

    def loop(self, head: ListNode, root: TreeNode):
        if root is None:
            return False
        if head.val == root.val:
            if self.dfs(head, root) is True:
                return True
        return self.loop(head, root.left) or self.loop(head, root.right)

    def dfs(self, curr: ListNode, root: TreeNode):
        if curr is None:
            return True
        if root is None:
            return False
        if curr.val != root.val:
            return False
        return self.dfs(curr.next, root.left) or self.dfs(curr.next, root.right)

if __name__ == '__main__':
    pass
