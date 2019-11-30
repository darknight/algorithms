#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        if num == 1:
            return "0"
        if num == 2:
            return "1"
        k = 2
        while num >= (2 ** k - 1):
            k += 1
        base = 2 ** (k - 1) - 1

        if num == base:
            return "0" * (k-1)

        real = num - base
        bits = []
        while real != 0:
            bits.append(real % 2)
            real = real >> 1
        while len(bits) < (k-1):
            bits.append(0)

        bits.reverse()
        res = "".join(["%s" % b for b in bits])
        return res


if __name__ == '__main__':
    # assert Solution().encode(3) == "00"
    assert Solution().encode(4) == "01"
    assert Solution().encode(5) == "10"
    assert Solution().encode(6) == "11"
    assert Solution().encode(7) == "000"
    assert Solution().encode(8) == "001"
    assert Solution().encode(9) == "010"
    assert Solution().encode(14) == "111"
    assert Solution().encode(15) == "0000"
    assert Solution().encode(16) == "0001"
    assert Solution().encode(22) == "0111"
    assert Solution().encode(23) == "1000"
    assert Solution().encode(107) == "101100"
