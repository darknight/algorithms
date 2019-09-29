#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(coordinates):
    all_x = [p[0] for p in coordinates]
    all_y = [p[1] for p in coordinates]
    x1, x2 = min(all_x), max(all_x)
    y1, y2 = min(all_y), max(all_y)
    for p in coordinates:
        if p[0] > x1 and p[0] < x2 and p[1] > y1 and p[1] < y2:
            return "NO"
    return "YES"

if __name__ == '__main__':
    assert solve([[0, 0], [0, 1], [1, 0]]) == "YES"
    assert solve([[0, 0], [0, 2], [2, 0], [1, 1]]) == "NO"