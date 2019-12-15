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
    from _uitl import *
except ImportError:
    pass


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        res = []
        chars = list(characters)
        tmp = [''] * combinationLength
        self.perm(0, tmp, 0, chars, res)

        self.res = res
        self.idx = 0

    def next(self) -> str:
        s = self.res[self.idx]
        self.idx += 1
        return s

    def hasNext(self) -> bool:
        return self.idx < len(self.res)

    def perm(self, accu_i: int, accu: List[str], pos: int, chars: List[str], res: List[str]):
        if accu_i == len(accu):
            res.append("".join(accu))
            return
        while pos < len(chars) - (len(accu) - accu_i) + 1:
            accu[accu_i] = chars[pos]
            self.perm(accu_i+1, accu, pos+1, chars, res)
            pos += 1

if __name__ == '__main__':
    com = CombinationIterator("abc", 2)
    com = CombinationIterator("abcd", 2)
    com = CombinationIterator("abcde", 1)
    com = CombinationIterator("abcde", 2)
    com = CombinationIterator("abcde", 3)
    com = CombinationIterator("abcde", 4)
    com = CombinationIterator("abcde", 5)
