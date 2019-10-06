#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        low_n = len(str(low))
        high_n = len(str(high))

        def calc(arr: List[int]) -> int:
            res = 0
            for i in range(len(arr)):
                res += arr[i] * (10 ** i)
            return res

        def fill_arr(arr: List[int], i: int, n: int, res: Set[int]):
            if i == n:
                num = calc(arr)
                res.add(num)
                return
            if arr[i-1] == 0:
                arr[i] = 1
                fill_arr(arr, i+1, n, res)
            elif arr[i-1] == 9:
                arr[i] = 8
                fill_arr(arr, i + 1, n, res)
            else:
                arr[i] = arr[i-1] + 1
                fill_arr(arr, i + 1, n, res)
                arr[i] = arr[i-1] - 1
                fill_arr(arr, i + 1, n, res)

        tmp = set()
        for n in range(low_n, high_n + 1):
            arr = [0] * n
            for first in range(0, 10):
                arr[0] = first
                fill_arr(arr, 1, len(arr), tmp)

        res = list(tmp)
        res.sort()
        i = 0
        while res[i] < low:
            i += 1
        j = len(res) - 1
        while res[j] > high:
            j -= 1

        return res[i:j+1]



if __name__ == '__main__':
    assert Solution().countSteppingNumbers(0, 21) == [0,1,2,3,4,5,6,7,8,9,10,12,21]
