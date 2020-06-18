#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
import re


class Solution:

    def WA_add_parenthese(self, s: str, num: int) -> str:
        if s == '':
            return ''
        if num > 9:
            return s
        arr = re.split(r'({}+)'.format(num), s)
        for i in range(len(arr)):
            if arr[i] == '':
                continue
            if int(arr[i][0]) == num:
                arr[i] = '(' * num + arr[i] + ')' * num
            else:
                arr[i] = self.WA_add_parenthese(arr[i], num + 1)

        return ''.join(arr)


if __name__ == '__main__':
    sln = Solution()
    T = int(input())
    for i in range(1, T + 1):
        s = input().rstrip()
        res = sln.WA_add_parenthese(s, 0)
        print("Case #{}: {}".format(i, res))
