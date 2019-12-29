#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        if size == 1:
            return [-1]

        curr = arr[-1]
        arr[-1] = -1
        for i in range(size - 2, -1, -1):
            tmp = arr[i]
            arr[i] = curr
            curr = max(curr, tmp)

        return arr


if __name__ == '__main__':
    pass
