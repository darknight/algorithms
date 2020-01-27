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
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        """
        https://www.youtube.com/watch?v=G88X89Eo2C0
        """
        clips.sort(key=lambda x: x[0])
        size = len(clips)
        res = 0
        i = 0
        last_end = 0
        while last_end < T:
            curr_end = last_end
            while i < size and clips[i][0] <= last_end:
                curr_end = max(curr_end, clips[i][1])
                i += 1
            if curr_end == last_end:
                return -1
            res += 1
            last_end = curr_end

        return res


if __name__ == '__main__':
    pass
