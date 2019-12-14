#!/usr/bin/env python3

import math
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


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        table = [[0,0,0],[0,0,0],[0,0,0]]
        size = len(moves)
        for k in range(0, size, 2):
            i, j = moves[k]
            table[i][j] = 1
        for k in range(1, size, 2):
            i, j = moves[k]
            table[i][j] = -1

        # check row
        for i in range(3):
            if sum(table[i]) == 3:
                return "A"
            if sum(table[i]) == -3:
                return "B"

        # check col
        for j in range(3):
            if table[0][j] + table[1][j] + table[2][j] == 3:
                return "A"
            if table[0][j] + table[1][j] + table[2][j] == -3:
                return "B"

        # check diagonal
        if table[0][0] + table[1][1] + table[2][2] == 3:
            return "A"
        if table[0][0] + table[1][1] + table[2][2] == -3:
            return "B"

        if table[0][2] + table[1][1] + table[2][0] == 3:
            return "A"
        if table[0][2] + table[1][1] + table[2][0] == -3:
            return "B"

        if size == 9:
            return "Draw"

        return "Pending"

if __name__ == '__main__':
    pass
