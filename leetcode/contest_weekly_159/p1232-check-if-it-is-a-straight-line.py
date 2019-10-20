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
    def AC_checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        if dx == 0:
            for i in range(1, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True

        tan = dy / dx

        for i in range(1, len(coordinates)):
            dx2 = coordinates[i][0] - coordinates[i-1][0]
            dy2 = coordinates[i][1] - coordinates[i-1][1]
            if dx2 == 0: # WA once to forget dx2 could be `0`
                return False

            tan2 = dy2 / dx2
            if abs(tan - tan2) > 0.0001:
                return False

        return True

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        for i in range(1, len(coordinates)):
            dx2 = coordinates[i][0] - coordinates[i-1][0]
            dy2 = coordinates[i][1] - coordinates[i-1][1]

            if dy * dx2 != dy2 * dx:
                return False

        return True



if __name__ == '__main__':
    assert Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) is True
    assert Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) is False

    assert Solution().checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]) is True