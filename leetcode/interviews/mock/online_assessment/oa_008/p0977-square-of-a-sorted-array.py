#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A


if __name__ == '__main__':
    pass
