#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)

        set4 = set1.intersection(set2)
        set5 = set4.intersection(set3)

        res = list(set5)
        res.sort()

        return res


if __name__ == '__main__':
    assert Solution().arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]) == [1,5]
    assert Solution().arraysIntersection([1,2,3,4,5], [1,2,5,7,9], []) == []