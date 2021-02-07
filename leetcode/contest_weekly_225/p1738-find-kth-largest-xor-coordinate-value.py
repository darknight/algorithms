#!/usr/bin/env python3

import math, itertools, functools, heapq, re
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        xors = [[0] * (N + 1) for _ in range(M + 1)]
        vals = []
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                xors[i][j] = xors[i - 1][j] ^ xors[i][j - 1] ^ xors[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                vals.append(xors[i][j])

        vals.sort(reverse=True)
        return vals[k - 1]


if __name__ == '__main__':
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 1))
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 2))
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 3))
    print(Solution().kthLargestValue([[5, 2], [1, 6]], 4))
