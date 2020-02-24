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
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        d1 = datetime.date.fromisoformat(date1)
        d2 = datetime.date.fromisoformat(date2)
        delta = d1 - d2
        return abs(delta.days)


    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        no cheating
        refer to
        https://leetcode.com/problems/number-of-days-between-two-dates/discuss/517605/Similar-to-day-of-the-year
        """
        pass


if __name__ == '__main__':
    pass
