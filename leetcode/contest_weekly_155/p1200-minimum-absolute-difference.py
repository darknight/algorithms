#!/usr/bin/env python3

import math
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffs = [arr[i]-arr[i-1] for i in range(1, len(arr))]
        min_diff = min(diffs)
        res = []
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])
        return res

if __name__ == '__main__':
    assert Solution().minimumAbsDifference([4,2,1,3]) == [[1,2],[2,3],[3,4]]
    assert Solution().minimumAbsDifference([1,3,6,10,15]) == [[1,3]]
    assert Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]