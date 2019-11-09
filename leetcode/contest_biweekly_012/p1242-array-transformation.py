#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        size = len(arr)
        if size <= 2:
            return arr

        changed = True
        while changed is True:
            changed = False
            tmp = [0] * size
            tmp[0] = arr[0]
            tmp[-1] = arr[-1]
            for i in range(1, size-1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    tmp[i] = arr[i] + 1
                    changed = True
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    tmp[i] = arr[i] - 1
                    changed = True
                else:
                    tmp[i] = arr[i]
            arr = tmp

        return arr

if __name__ == '__main__':
    assert Solution().transformArray([6,2,3,4]) == [6,3,3,4]
    assert Solution().transformArray([1,6,3,4,3,5]) == [1,4,4,4,4,5]
    assert Solution().transformArray([1,2,3,4,5]) == [1,2,3,4,5]
