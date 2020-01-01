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
    def numTilePossibilities(self, tiles: str) -> int:
        chars = list(tiles)
        size = len(chars)
        if size == 1:
            return 1
        res = set()
        for n in range(1, size + 1):
            candidates = []
            self.combination(0, n, chars, size, [], candidates)
            print(candidates)
            for cand in candidates:
                sz = len(cand)
                results = set()
                self.perm(0, cand, sz, results)
                print(results)
                res.update(results)

        return len(res)


    def combination(self, curr: int, N: int, chars: List[str], size: int, tmp: List[str], candidates: List[List[str]]):
        if len(tmp) == N:
            candidates.append(tmp.copy())
            return
        if curr >= size:
            return
        for j in range(curr, size):
            tmp.append(chars[j])
            self.combination(j+1, N, chars, size, tmp, candidates)
            tmp.pop()


    def perm(self, curr: int, chars: List[str], size: int, res: Set[str]):
        if curr == size:
            s = ''.join(chars)
            res.add(s)
            return
        for i in range(curr, size):
            chars[curr], chars[i] = chars[i], chars[curr]
            self.perm(curr+1, chars, size, res)
            chars[curr], chars[i] = chars[i], chars[curr]


if __name__ == '__main__':
    assert Solution().numTilePossibilities("AB") == 4
    assert Solution().numTilePossibilities("AAB") == 8
    assert Solution().numTilePossibilities("AAABBC") == 188
