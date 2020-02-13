#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6
        hour_angle = minutes / 60 * 30 + (30 * hour) % 360
        angle = abs(min_angle - hour_angle)
        if angle > 180:
            return 360 - angle
        return angle


if __name__ == '__main__':
    print(Solution().angleClock(12, 30))
    print(Solution().angleClock(3, 30))
    print(Solution().angleClock(3, 15))
    print(Solution().angleClock(4, 50))
    print(Solution().angleClock(12, 0))
