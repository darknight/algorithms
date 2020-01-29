#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        if size == 1:
            return 1
        if self.is_palindrome(s):
            return 1
        return 2

    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    pass
