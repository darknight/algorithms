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
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        group = []
        size = len(S)
        part = ''
        for i in range(size-1, -1, -1):
            ch = S[i].upper()
            if ch == '-':
                continue
            if len(part) == K:
                group.insert(0, part)
                part = ''
            part = ch + part

        if len(part) > 0:
            group.insert(0, part)

        return '-'.join(group)


if __name__ == '__main__':
    pass
