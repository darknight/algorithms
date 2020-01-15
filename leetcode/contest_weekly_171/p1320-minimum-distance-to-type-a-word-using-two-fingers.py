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
    def _minimumDistance(self, word: str) -> int:
        coord = []
        for w in word:
            offset = ord(w) - ord('A')
            row = offset // 6
            col = offset - row * 6
            coord.append((row, col))
        size = len(coord)
        res = math.inf
        for i in range(size - 1):
            for j in range(i + 1, size):
                tmp = [0]
                marked = [0] * size
                marked[i] = 1
                marked[j] = 1
                self.dfs(i, j, coord, marked, size, tmp)
                res = min(res, tmp[0])

        return res

    # TODO: finish dfs solution
    def dfs(self, idx1, idx2, coord, marked, size, tmp):
        pass

    def minimumDistance(self, word: str) -> int:
        """
        https://www.youtube.com/watch?v=GRRDl3HxQAI
        """
        size = len(word)
        dp = []
        for _ in range(size + 1):
            t = []
            for _ in range(27):
                t.append([0] * 27)
            dp.append(t)

        # TLE if calculate distance in a separate util method
        cost = []
        for i in range(26):
            cost.append([0] * 26)
            for j in range(26):
                x1 = i // 6
                y1 = i % 6
                x2 = j // 6
                y2 = j % 6
                cost[i][j] = abs(x1-x2) + abs(y1-y2)
            cost[i].append(0)
        cost.append([0] * 27)

        for pos in range(size-1, -1, -1):
            to = ord(word[pos]) - ord('A')
            for i in range(27):
                for j in range(27):
                    dp[pos][i][j] = min(
                        dp[pos + 1][to][j] + cost[i][to],
                        dp[pos + 1][i][to] + cost[j][to]
                    )
            pos -= 1

        return dp[0][26][26]


if __name__ == '__main__':
    assert Solution().minimumDistance("CAKE") == 3
    assert Solution().minimumDistance("HAPPY") == 6
    assert Solution().minimumDistance("NEW") == 3
    assert Solution().minimumDistance("YEAR") == 7
    assert Solution().minimumDistance("GSALRVPVEYXICXWTWIZTXHAEGXSVANEEPRBQKHVFOKVOHUUXIVWGDLPILRSJGJRMCFMDSUDQEWOENIXRGYZFXCIOKMQBLMXXMREYWWRSEUBJTOQYSNGOGMCDRMDQVOXUFBGHHDTMNCRGQGGPCGDQETGRSQUTNTMUIVZPUUTZALLYZGWUBGOGQVGAEHOPCTIUJMKXXVWJVCTDPLTTUCHENHAPJEQULXVEDQKKVXCLZGGJQWNUXXMMBEOCJUVEQGTPLESES")
