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
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        length = n // 2
        left = range(-1, length - 1, -1)
        right = range(1, length + 1)
        if n % 2 == 1:
            return list(left) + [0] + list(right)
        else:
            return list(left) + list(right)


if __name__ == '__main__':
    pass
