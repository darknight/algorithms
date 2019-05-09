#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[0])
        prev_s, prev_e = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            curr_s, curr_e = intervals[i]
            if curr_s == prev_s:
                prev_e = min(prev_e, curr_e)
                res += 1
            elif curr_s < prev_e:
                if curr_e <= prev_e:
                    prev_s, prev_e = curr_s, curr_e
                res += 1
            else:
                prev_s, prev_e = curr_s, curr_e

        return res

    # TODO: sort by end
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        pass

if __name__ == '__main__':
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0