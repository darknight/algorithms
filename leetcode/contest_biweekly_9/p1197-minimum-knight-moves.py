#!/usr/bin/env python3

from typing import List
class Solution:
    def _minKnightMoves(self, x: int, y: int) -> int:

        visit = {}
        dist = {(0, 0): 0}
        queue = [(0, 0)]

        x = abs(x)
        y = abs(y)

        def bfs(queue: list, visit: dict, dist: dict):
            curr_dist = x * x + y * y
            while len(queue) > 0:
                a, b = queue.pop(0)
                visit[(a, b)] = 1
                if a == x and b == y:
                    return
                delta = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
                for (dx, dy) in delta:
                    pa, pb = a + dx, b + dy
                    if (pa, pb) in visit:
                        continue
                    if abs(pa) + abs(pb) > 300:
                        continue
                    d = (pa - x) * (pa - x) + (pb - y) * (pb - y)
                    # truncate
                    # too random, make less sense
                    if d >= curr_dist and d > 5:
                        continue
                    curr_dist = d
                    queue.append((pa, pb))
                    dist[(pa, pb)] = dist[(a, b)] + 1

        bfs(queue, visit, dist)
        return dist[(x, y)]


    def minKnightMoves(self, x: int, y: int) -> int:
        # delta = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        dist = {(0, 0): 0}
        queue = [(0, 0)]

        x = abs(x)
        y = abs(y)
        # This is the truncate, since x y is abs value
        delta = [(2, 1), (2, -1), (1, 2), (-1, 2)]

        def bfs(queue: list, dist: dict):
            while len(queue) > 0:
                a, b = queue.pop(0)
                if a == x and b == y:
                    return
                for (dx, dy) in delta:
                    pa, pb = a + dx, b + dy
                    if (pa, pb) in dist:
                        continue
                    if abs(pa) + abs(pb) > 300:
                        continue
                    queue.append((pa, pb))
                    dist[(pa, pb)] = dist[(a, b)] + 1

        bfs(queue, dist)
        return dist[(x, y)]


if __name__ == '__main__':
    assert Solution().minKnightMoves(2, 1) == 1
    assert Solution().minKnightMoves(5, 5) == 4
    assert Solution().minKnightMoves(2, 112) == 56
    assert Solution().minKnightMoves(217, 47) == 110
    assert Solution().minKnightMoves(-99, 142) == 81