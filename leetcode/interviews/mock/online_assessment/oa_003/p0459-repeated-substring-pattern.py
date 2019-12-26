#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set

try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    # very slow...
    def AC_repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        # WA here: size % 2 != 1
        if size <= 1:
            return False
        for length in range(1, size // 2 + 1):
            if size % length != 0:
                continue
            segments = size // length
            all_equal = True
            for i in range(length):
                for j in range(segments):
                    if s[i + 0] != s[i + j * length]:
                        all_equal = False
                        break
                if all_equal is False:
                    break
            if all_equal is True:
                return True
        return False

    # clear than AC 1 but still very slow
    def AC_2_repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size <= 1:
            return False
        steps = [l for l in range(1, size//2+1) if size % l == 0]
        for step in steps:
            equal = True
            i = 0
            while i + step < size:
                if s[i] != s[i+step]:
                    equal = False
                    break
                i += 1
            if equal is True:
                return True
        return False

    # TODO: several ideas here....
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        """
        pass


if __name__ == '__main__':
    assert Solution().repeatedSubstringPattern("abab") is True
    assert Solution().repeatedSubstringPattern("aba") is False
    assert Solution().repeatedSubstringPattern("abcabcabcabc") is True
    assert Solution().repeatedSubstringPattern("ababab") is True
    assert Solution().repeatedSubstringPattern("babbabbabbabbab") is True
