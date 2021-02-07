#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple

try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:

    # TODO: use Counter
    def minCharacters(self, a: str, b: str) -> int:
        cnt_a = [0] * 26
        cnt_b = [0] * 26
        most_a, a_idx, most_b, b_idx = 0, 0, 0, 0
        for ch in a:
            idx = ord(ch) - ord('a')
            cnt_a[idx] += 1
            if cnt_a[idx] > most_a:
                most_a = cnt_a[idx]
                a_idx = idx
        for ch in b:
            idx = ord(ch) - ord('a')
            cnt_b[idx] += 1
            if cnt_b[idx] > most_b:
                most_b = cnt_b[idx]
                b_idx = idx

        # condition 1 & 2
        move1 = math.inf
        move2 = math.inf
        for i in range(25, 0, -1):
            move1 = min(move1, sum(cnt_a[i:] + cnt_b[:i]))
            move2 = min(move2, sum(cnt_b[i:] + cnt_a[:i]))

        # condition 3
        move3 = 0
        if a_idx == b_idx:
            move3 = len(a) - most_a + len(b) - most_b
        else:
            move3 = min(len(a) - most_a + len(b) - cnt_b[a_idx], len(b) - most_b + len(a) - cnt_a[b_idx])

        return min(move1, move2, move3)


if __name__ == '__main__':
    print(Solution().minCharacters("aba", "caa"))
    print(Solution().minCharacters("dabadd", "cda"))
    print(Solution().minCharacters("aaaaa", "eeeee"))
    print(Solution().minCharacters("abcde", "cdefg"))
    print(Solution().minCharacters("sssswxyz", "ssss"))

