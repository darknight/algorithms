#!/usr/bin/env python3

from collections import defaultdict
from typing import List


class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = defaultdict(int)
        for a in arr:
            count[a] += 1
        all_cnt = count.values()
        if len(all_cnt) == len(set(all_cnt)):
            return True
        return False


if __name__ == '__main__':
    assert Solution().uniqueOccurrences([1,2,2,1,1,3]) is True
    assert Solution().uniqueOccurrences([1,2]) is False
    assert Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) is True
