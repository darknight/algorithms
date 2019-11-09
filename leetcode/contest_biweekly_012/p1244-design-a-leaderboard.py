#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Leaderboard:

    def __init__(self):
        self.map = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.map:
            self.map[playerId] = score
        else:
            self.map[playerId] += score

    def top(self, K: int) -> int:
        vals = list(self.map.values())
        vals.sort(reverse=True)
        return sum(vals[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.map:
            del self.map[playerId]


if __name__ == '__main__':
    leaderboard = Leaderboard()
    leaderboard.addScore(1, 73)
    leaderboard.addScore(2, 56)
    leaderboard.addScore(3, 39)
    leaderboard.addScore(4, 51)
    leaderboard.addScore(5, 4)
    assert leaderboard.top(1) == 73
    leaderboard.reset(1)
    leaderboard.reset(2)
    leaderboard.addScore(2, 51)
    assert leaderboard.top(1) == 51

    b = Leaderboard()
    b.addScore(1,13)
    b.addScore(2,93)
    b.addScore(3,84)
    b.addScore(4,6)
    b.addScore(5,89)
    b.addScore(6,31)
    b.addScore(7,7)
    b.addScore(8,1)
    b.addScore(9,98)
    b.addScore(10,42)
    assert b.top(5) == 406
    b.reset(1)
    b.reset(2)
    b.addScore(3,76)
    b.addScore(4,68)
    assert b.top(1) == 160
