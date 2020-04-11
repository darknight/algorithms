#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def WA_checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        delta_x = -x_center
        delta_y = -y_center

        x_center = 0
        y_center = 0

        x1 += delta_x
        y1 += delta_y
        x2 += delta_x
        y2 += delta_y

        if x1 > radius or x2 < -radius or y1 > radius or y2 < -radius:
            return False

        if -radius <= x1 <= radius:
            y = math.sqrt(radius * radius - x1 * x1)
            if y2 < -y or y1 > y:
                return False
            return True
        elif -radius <= x2 <= radius:
            y = math.sqrt(radius * radius - x2 * x2)
            if y2 < -y or y1 > y:
                return False
            return True

        return True

    def AC_checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        delta_x = -x_center
        delta_y = -y_center

        x_center = 0
        y_center = 0

        x1 += delta_x
        y1 += delta_y
        x2 += delta_x
        y2 += delta_y

        # exclude disjoint cases
        if x1 > radius or x2 < -radius or y1 > radius or y2 < -radius:
            return False

        # take care of edge cases
        if (x1 == radius or x2 == -radius) and y1 <= 0 <= y2:
            return True
        if (y1 == radius or y2 == -radius) and x1 <= 0 <= x2:
            return True

        # other cases
        if x1 >= 0:
            y = math.sqrt(radius * radius - x1 * x1)
            if y2 < -y or y1 > y:
                return False
            else:
                return True
        elif x2 < 0:
            y = math.sqrt(radius * radius - x2 * x2)
            if y2 < -y or y1 > y:
                return False
            else:
                return True

        return True


    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        refer to
        https://leetcode.com/problems/circle-and-rectangle-overlapping/discuss/563463/C%2B%2B-with-simple-explanation

        a nice explanation
        https://yal.cc/rectangle-circle-intersection-test/
        """
        delta_x = -x_center
        delta_y = -y_center

        x1 += delta_x
        y1 += delta_y
        x2 += delta_x
        y2 += delta_y

        min_x = 0
        if x1 * x2 > 0:
            min_x = min(x1*x1, x2*x2)
        min_y = 0
        if y1 * y2 > 0:
            min_y = min(y1*y1, y2*y2)

        return min_x + min_y <= radius * radius




if __name__ == '__main__':
    assert Solution().checkOverlap(1, 0, 0, 1, -1, 3, 1) is True

    assert Solution().checkOverlap(2, 8, 6, 5, 1, 10, 4) is True

    assert Solution().checkOverlap(4, 102, 50, 0, 0, 100, 100) is True
