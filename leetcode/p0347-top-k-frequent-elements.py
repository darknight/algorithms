#!/usr/bin/env python3

from typing import List
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        bucket = []
        for _ in range(max(map.values()) + 1):
            bucket.append([])
        for (key, val) in map.items():
            bucket[val].append(key)
        res = []
        bucket.reverse()
        for vals in bucket:
            for val in vals:
                res.append(val)
                if len(res) == k:
                    return res

if __name__ == '__main__':
    assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    assert Solution().topKFrequent([1], 1) == [1]