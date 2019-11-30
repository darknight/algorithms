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
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        num = 1
        idx = {}
        mapping = {}
        for region in regions:
            for reg in region:
                if reg not in idx:
                    idx[reg] = num
                    mapping[num] = reg
                    num += 1

        # print(idx)
        # print(mapping)
        arr = [0] * num

        for region in regions:
            root = idx[region[0]]
            for child in region[1:]:
                arr[idx[child]] = root

        # print(arr)
        r1 = idx[region1]
        r2 = idx[region2]

        path1 = [r1]
        path2 = [r2]

        while arr[r1] != 0:
            path1.append(arr[r1])
            r1 = arr[r1]

        while arr[r2] != 0:
            path2.append(arr[r2])
            r2 = arr[r2]

        path1.reverse()
        path2.reverse()

        # print(path1)
        # print(path2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                common = path1[i-1]
                return mapping[common]
            i += 1

        if i == len(path1):
            return mapping[path1[-1]]
        else:
            return mapping[path2[-1]]


if __name__ == '__main__':
    assert Solution().findSmallestRegion(regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York") == "North America"

    assert Solution().findSmallestRegion(
        [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]]
        ,"Canada"
        ,"Quebec") == "Canada"
