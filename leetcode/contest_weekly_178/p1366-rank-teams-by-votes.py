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
    def rankTeams(self, votes: List[str]) -> str:
        T = len(votes[0])
        stat = {}
        for vote in votes:
            for i in range(len(vote)):
                if vote[i] not in stat:
                    stat[vote[i]] = [0] * T
                stat[vote[i]][i] += 1

        cand = []
        for ch, rank in stat.items():
            rank.append(-ord(ch))
            cand.append(rank)
        cand.sort(reverse=True)

        res = ""
        for tmp in cand:
            res = res + chr(-tmp[-1])

        return res





if __name__ == '__main__':
    assert Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]) == "ACB"
    assert Solution().rankTeams(["WXYZ","XYZW"]) == "XWYZ"
    assert Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]) == "ZMNAGUEDSJYLBOPHRQICWFXTVK"
    assert Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]) == "ABC"
    assert Solution().rankTeams(["M","M","M","M"]) == "M"
