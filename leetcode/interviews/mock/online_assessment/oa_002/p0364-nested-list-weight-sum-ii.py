#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_dep = [0]
        self.find_max_dep(1, nestedList, max_dep)

        return self.traverse(1, max_dep[0], nestedList)

    def find_max_dep(self, dep: int, nestedList: List[NestedInteger], max_dep: List[int]):
        max_dep[0] = max(max_dep[0], dep)
        for nested in nestedList:
            if nested.isInteger() is False:
                self.find_max_dep(dep+1, nested.getList(), max_dep)

    def traverse(self, dep: int, max_dep: int, nestedList: List[NestedInteger]) -> int:
        res = 0
        for nested in nestedList:
            if nested.isInteger():
                res += (max_dep - dep + 1) * nested.getInteger()
            else:
                res += self.traverse(dep+1, max_dep, nested.getList())

        return res

if __name__ == '__main__':
    assert Solution().depthSumInverse([[1,1],2,[1,1]]) == 8
    assert Solution().depthSumInverse([1,[4,[6]]]) == 8
    assert Solution().depthSumInverse([]) == 8
    assert Solution().depthSumInverse([1,2,3]) == 6
