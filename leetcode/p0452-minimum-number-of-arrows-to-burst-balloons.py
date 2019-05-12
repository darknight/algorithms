#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        res = 1
        points.sort(key=lambda x: x[1])
        prev_s, prev_e = points[0]
        for curr_s, curr_e in points[1:]:
            if curr_s <= prev_e:
                continue
            else:
                res += 1
                prev_s, prev_e = curr_s, curr_e
        return res

if __name__ == '__main__':
    assert Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]) == 2
    assert Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2