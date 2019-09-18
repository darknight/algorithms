#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the quickestWayUp function below.
def _quickestWayUp(ladders, snakes):
    """
    idea: dfs of direct graph
    TLE
    """
    m = [[0] * 101 for _ in range(101)]
    visit = [[0] * 101 for _ in range(101)]
    for i in range(1, 101):
        for j in range(1, 7):
            if i + j <= 100:
                m[i][i + j] = 1

    for (x, y) in ladders:
        m[x][y] = 1
        for j in range(1, 7):
            if x + j <= 100:
                m[x][x + j] = 0

    for (x, y) in snakes:
        m[x][y] = 1
        for j in range(1, 7):
            if x + j <= 100:
                m[x][x + j] = 0

    reachable = [m[i][100] for i in range(1, 101)]
    if any(reachable) is False:
        return -1

    def dfs(m, visit, curr_x, path, res):
        if len(path) >= res[0]:
            return
        if curr_x == 100:
            res[0] = min(res[0], len(path))
            return
        for j in range(1, 101):
            if m[curr_x][j] == 0:
                continue
            if visit[curr_x][j] != 2:
                visit[curr_x][j] = 2
                if (curr_x, j) not in snakes and (curr_x, j) not in ladders:
                    path.append((curr_x, j))
                dfs(m, visit, j, path, res)
                if (curr_x, j) not in snakes and (curr_x, j) not in ladders:
                    path.pop()
                visit[curr_x][j] = 1

    path = []
    res = [math.inf]
    dfs(m, visit, 1, path, res)
    return res[0]

def quickestWayUp(ladders, snakes):
    """
    classic bfs for unweighted shortest path
    """
    m = [[0] * 101 for _ in range(101)]
    for i in range(1, 101):
        for delta in range(1, 7):
            if i + delta <= 100:
                m[i][i + delta] = 1
    for (x, y) in ladders:
        m[x][y] = 1
        for delta in range(1, 7):
            if x + delta <= 100:
                m[x][x + delta] = 0
            if x - delta >= 1:
                m[x - delta][y] = 1
    for (x, y) in snakes:
        m[x][y] = 1
        for delta in range(1, 7):
            if x + delta <= 100:
                m[x][x + delta] = 0
            if x - delta >= 1:
                m[x - delta][y] = 1

    dist = [-1 for _ in range(101)]
    dist[1] = 0
    queue = [1]

    while len(queue) != 0:
        v = queue.pop(0)
        for w in range(1, 101):
            if m[v][w] == 1 and dist[w] == -1:
                dist[w] = dist[v] + 1
                queue.append(w)

    return dist[100]


if __name__ == '__main__':
    assert quickestWayUp(
        [(32, 62), (42, 68), (12, 98)],
        [(95, 13), (97, 25), (93, 37), (79, 27), (75, 19), (49, 47), (67, 17)]
    ) == 3
    assert quickestWayUp(
        [(8, 52), (6, 80), (26, 42), (2, 72)],
        [(51, 19), (39, 11), (37, 29), (81, 3), (59, 5), (79, 23), (53, 7), (43, 33), (77, 21)]
    ) == 5
    assert quickestWayUp(
        [(3, 90)],
        [(99, 10), (97, 20), (98, 30), (96, 40), (95, 50), (94, 60), (93, 70)]
    ) == -1
    assert quickestWayUp(
        [(3, 54), (37, 100)],
        [(56, 33)]
    ) == 3
