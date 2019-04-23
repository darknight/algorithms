#!/bin/python3

import os
import sys

# it's not (a * t * 0.5 + b * t * 0.5) % 1000000007
# it is exponential
def solve(a, b, t):
    return pow(int(a * 0.5 + b * 0.5), t, 1000000007)

if __name__ == '__main__':
    assert solve(2, 4, 1) == 3
    assert solve(98, 26, 818638958430279427) == 627473951
    assert solve(72, 82, 408362795258198340) == 988869683