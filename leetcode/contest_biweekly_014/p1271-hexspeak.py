#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def toHexspeak(self, num: str) -> str:
        map = { 0: 'O', 1: 'I', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        n = int(num)
        hex = []
        while n != 0:
            if n % 16 not in map:
                return "ERROR"
            hex.append(map[n % 16])
            n = n // 16

        hex.reverse()
        return ''.join(hex)


if __name__ == '__main__':
    assert Solution().toHexspeak("257") == "IOI"
    assert Solution().toHexspeak("3") == "ERROR"
