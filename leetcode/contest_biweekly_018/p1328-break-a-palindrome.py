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
    def breakPalindrome(self, palindrome: str) -> str:
        size = len(palindrome)
        if size == 1:
            return ""
        res = []
        chars = list(palindrome)
        for i in range(size):
            origin = chars[i]
            base = ord('a')
            for offset in range(26):
                ch = chr(base + offset)
                if ch == origin:
                    continue
                chars[i] = ch
                if self.is_palidrome(chars) is False:
                    res.append("".join(chars))
                    chars[i] = origin
                    break
                chars[i] = origin

        res.sort()
        if len(res) > 0:
            return res[0]
        return ""

    def is_palidrome(self, target: List[str]) -> bool:
        i = 0
        j = len(target) - 1
        while i < j:
            if target[i] != target[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    pass
