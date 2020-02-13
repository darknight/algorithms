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
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 1:
                num -= 1
            else:
                num = num // 2
            steps += 1
        return steps



if __name__ == '__main__':
    pass
