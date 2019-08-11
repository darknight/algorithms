#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        if a1 >= x2 or a2 <= x1:
            return False
        if b1 >= y2 or b2 <= y1:
            return False
        # if rec2 wraps rec1 or rec1 wraps rec2, it's considered as overlap
        # if a1 < x1 and a2 > x2 and b1 < y1 and b2 > y2:
        #     return False
        # if a1 < x1 and a2 < x2 and b1 > y1 and b2 < y2:
        #     return False
        return True

if __name__ == '__main__':
    # assert Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3]) is True
    # assert Solution().isRectangleOverlap([0,0,1,1],[1,0,2,1]) is False
    assert Solution().isRectangleOverlap([229,-132,833,333],[-244,-577,837,804]) is True