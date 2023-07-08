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


class SolutionTLE:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        for i in range(len(self.arr)-2, -1, -1):
            if self.arr[i+1] < self.arr[i]:
                self.arr[i+1], self.arr[i] = self.arr[i], self.arr[i+1]

    def findMedian(self) -> float:
        i = len(self.arr) // 2
        if len(self.arr) % 2 == 0:
            return (self.arr[i] + self.arr[i-1]) / 2
        else:
            return self.arr[i]


class Solution:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right_min, num)
        while len(self.left_max) < len(self.right_min):
            right = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -right)
        while len(self.left_max) > 0 and len(self.right_min) > 0 and -self.left_max[0] > self.right_min[0]:
            left = -heapq.heappop(self.left_max)
            right = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -right)
            heapq.heappush(self.right_min, left)

    def findMedian(self) -> float:
        size = len(self.left_max) + len(self.right_min)
        if size % 2 == 0:
            left = -self.left_max[0]
            right = self.right_min[0]
            return (left + right) / 2
        else:
            return -self.left_max[0]


class Solution_official_3_Heap:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max, -num)
        left = -heapq.heappop(self.left_max)
        heapq.heappush(self.right_min, left)
        if len(self.left_max) < len(self.right_min):
            right = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -right)

    def findMedian(self) -> float:
        size = len(self.left_max) + len(self.right_min)
        if size % 2 == 0:
            return (-self.left_max[0] + self.right_min[0]) / 2
        else:
            return -self.left_max[0]


class Solution_Official_1_Sort:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()

        size = len(self.data)
        if size % 2 == 0:
            return (self.data[size//2]+self.data[size//2-1]) / 2
        return self.data[size//2]


class Solution_Official_2_Insert:

    def __init__(self):
        self.data = []

    def addNum_TLE(self, num: int) -> None:
        self.data.append(num)
        size = len(self.data)
        if size == 1:
            return
        i = 0
        j = size - 2
        while i <= j:
            k = (i + j) // 2
            if self.data[k] <= num:
                i = k + 1
            elif self.data[k] > num:
                j = k - 1
        k = size - 1
        while k > i:
            self.data[k] = self.data[k - 1]
            k -= 1
        self.data[i] = num

    def addNum(self, num: int) -> None:
        size = len(self.data)
        if size == 0:
            self.data.append(num)
            return
        i = 0
        j = size - 1
        while i <= j:
            k = (i + j) // 2
            if self.data[k] <= num:
                i = k + 1
            elif self.data[k] > num:
                j = k - 1
        self.data.insert(i, num)  # FIXME: this is faster than move element by hand, which is TLE


    def findMedian(self) -> float:
        size = len(self.data)
        if size % 2 == 0:
            return (self.data[size//2]+self.data[size//2-1]) / 2
        return self.data[size//2]

# TODO
class Solution_Multiset:
    pass

# TODO
class Solution_AVL:
    pass

# TODO
class Solution_Other_Ideas:
    pass

if __name__ == '__main__':
    arr = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]
    # arr = [1, 2]
    # arr = [1, 2, 3]
    s = Solution()
    for num in arr:
        s.addNum(num)
        print(s.findMedian())
