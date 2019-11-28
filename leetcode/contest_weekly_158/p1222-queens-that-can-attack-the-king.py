#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        M = 8
        N = 8
        matrix = []
        for i in range(M):
            matrix.append([0] * N)

        for q in queens:
            i, j = q[0], q[1]
            matrix[i][j] = 1

        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        res = []
        for dir in directions:
            curr_i, curr_j = king[0], king[1]
            dx, dy = dir[0], dir[1]
            while True:
                curr_i += dx
                curr_j += dy
                if curr_i < 0 or curr_i >= M or curr_j < 0 or curr_j >= N:
                    break
                if matrix[curr_i][curr_j] == 1:
                    res.append([curr_i, curr_j])
                    break
        res.sort()
        # print(res)
        return res

if __name__ == '__main__':
    assert Solution().queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],
                                          [0,0]) == [[0,1],[1,0],[3,3]]
    assert Solution().queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]],
                                          [3,3]) == [[2,2],[3,4],[4,4]]
    assert Solution().queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]],
                                          [3,4]) == [[1,4],[1,6],[2,3],[3,7],[4,3],[4,5],[5,4]]
