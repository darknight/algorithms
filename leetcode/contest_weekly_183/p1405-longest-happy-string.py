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
    def WA_longestDiverseString(self, a: int, b: int, c: int) -> str:
        seq = []
        x, y, z = 0, 0, 0
        t = max(a, b, c)
        if t == a:
            if b >= c:
                seq = ['a', 'b', 'c']
                x, y, z = a, b, c
            else:
                seq = ['a', 'c', 'b']
                x, y, z = a, c, b
        elif t == b:
            if a >= c:
                seq = ['b', 'a', 'c']
                x, y, z = b, a, c
            else:
                seq = ['b', 'c', 'a']
                x, y, z = b, c, a
        else:
            if a >= b:
                seq = ['c', 'a', 'b']
                x, y, z = c, a, b
            else:
                seq = ['c', 'b', 'a']
                x, y, z = c, b, a

        res = ''
        while x > 0:
            if x > 1:
                res += seq[0] + seq[0]
                x -= 2
                if y > 0:
                    res += seq[1]
                    y -= 1
                    continue
                elif z > 0:
                    res += seq[2]
                    z -= 1
                    continue
                else:
                    break
            else:
                res += seq[0]
                x -= 1

        if z > y:
            y, z = z, y
            seq[1], seq[2] = seq[2], seq[1]

        # put last char back to avoid `???`
        if y > 0 and seq[1] == res[-1]:
            res = res[:-1]
            y += 1

        while y > 0:
            if y > 1:
                res += seq[1] + seq[1]
                y -= 2
                if z > 0:
                    res += seq[2]
                    z -= 1
                    continue
                else:
                    break
            else:
                res += seq[1]
                y -= 1

        if z > 0:
            res += seq[2]

        return res

    def WA_2_longestDiverseString(self, a: int, b: int, c: int) -> str:
        seq = []
        x, y, z = 0, 0, 0
        t = max(a, b, c)
        if t == a:
            if b >= c:
                seq = ['a', 'b', 'c']
                x, y, z = a, b, c
            else:
                seq = ['a', 'c', 'b']
                x, y, z = a, c, b
        elif t == b:
            if a >= c:
                seq = ['b', 'a', 'c']
                x, y, z = b, a, c
            else:
                seq = ['b', 'c', 'a']
                x, y, z = b, c, a
        else:
            if a >= b:
                seq = ['c', 'a', 'b']
                x, y, z = c, a, b
            else:
                seq = ['c', 'b', 'a']
                x, y, z = c, b, a

        res = []
        while x > 0 and y > 0 and z > 0:
            res.append(seq[0])
            res.append(seq[1])
            res.append(seq[2])
            x -= 1
            y -= 1
            z -= 1

        while x > 0 and y > 0:
            res.append(seq[0])
            res.append(seq[1])
            x -= 1
            y -= 1

        if x > 0:
            tmp = []
            for i in range(len(res) - 1):
                if x == 0:
                    break
                if res[i] == seq[0]:
                    tmp.append(res[i])
                    tmp.append(seq[0])
                    x -= 1
                elif res[i] != seq[0] and res[i + 1] != seq[0]:
                    tmp.append(res[i])
                    tmp.append(seq[0])
                    x -= 1
                    if x > 0:
                        tmp.append(seq[0])
                        x -= 1
                else:
                    tmp.append(res[i])
            res = tmp

        return ''.join(res)

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        refer to
        https://leetcode.com/problems/longest-happy-string/discuss/564277/C%2B%2BJava-a-greater-b-greater-c
        """
        return self.generate(a, b, c, 'a', 'b', 'c')

    def generate(self, lg: int, md: int, sm: int, lgchr: str, mdchr: str, smchr: str) -> str:
        if lg < md:
            return self.generate(md, lg, sm, mdchr, lgchr, smchr)
        if md < sm:
            return self.generate(lg, sm, md, lgchr, smchr, mdchr)
        if md == 0:
            return lgchr * min(2, lg)
        # num_lg = min(2, lg)
        # num_md = 0
        # if lg - 2 >= md:
        #     num_md = 1
        # newstr = lgchr * num_lg + mdchr * num_md
        # return newstr + self.generate(lg-num_lg, md-num_md, sm, lgchr, mdchr, smchr)

        # here, we always have a >= b >= c and b >= 1
        # more understandable
        if lg - 2 >= md - 1:
            return lgchr * 2 + mdchr + self.generate(lg - 2, md - 1, sm, lgchr, mdchr, smchr)
        else:
            k = min(2, lg)
            return lgchr * k + self.generate(lg-k, md, sm, lgchr, mdchr, smchr)


if __name__ == '__main__':
    # print(Solution().longestDiverseString(1, 1, 7))
    # print(Solution().longestDiverseString(2, 2, 1))
    # print(Solution().longestDiverseString(7, 1, 0))
    # print(Solution().longestDiverseString(2, 7, 10))
    print(Solution().longestDiverseString(10, 7, 2))
    # print(Solution().longestDiverseString(1, 0, 3))
    # print(Solution().longestDiverseString(0, 9, 12))
