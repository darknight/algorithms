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

    def freqAlphabets(self, s: str) -> str:
        size = len(s)
        i = size - 1
        res = []
        while i >= 0:
            if s[i] == '#':
                ch = chr(ord('a') + int(s[i-2:i]) - 1)
                res.insert(0, ch)
                i -= 3
            else:
                ch = chr(ord('a') + int(s[i:i+1]) - 1)
                res.insert(0, ch)
                i -= 1

        return ''.join(res)


if __name__ == '__main__':
    print(Solution().freqAlphabets("10#11#12"))
    print(Solution().freqAlphabets("1326#"))
    print(Solution().freqAlphabets("25#"))
    print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
