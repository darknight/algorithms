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
    def lengthLongestPath(self, input: str) -> int:
        """
        refer to
        https://leetcode.com/problems/longest-absolute-file-path/discuss/421102/Python-HashMap-explanation-(EnglishChinese)-Time-Complexity
        """
        res = 0
        prefix = {0: 0}
        for path in input.splitlines():
            name = path.lstrip('\t')
            depth = len(path) - len(name)
            if '.' in name:
                res = max(res, prefix[depth] + len(name))
            else:
                prefix[depth + 1] = prefix[depth] + len(name) + 1

        return res

    # TODO: use stack
    def lengthLongestPath(self, input: str) -> int:
        """
        refer to
        https://leetcode.com/problems/longest-absolute-file-path/discuss/86615/9-lines-4ms-Java-solution
        """
        pass

if __name__ == '__main__':
    pass
