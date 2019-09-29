#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def solve(a, b, c):
    def output(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return '%d/%d' % (numerator // gcd, denominator // gcd)

    if a + b <= c:
        return '1/1'
    if a < c and b < c and a + b > c:
        return output(2 * a * c + 2 * b * c - a * a - b * b - c * c, 2 * a * b)
    if a >= c and b >= c:
        return output(c * c, 2 * a * b)
    if (a >= c and b < c) or (a < c and b >= c):
        x = min(a, b)
        y = max(a, b)
        return output(2 * c - x, 2 * y)

if __name__ == '__main__':
    assert solve(1,1,1) == '1/2'
    assert solve(1,1,2) == '1/1'
    assert solve(1,1,3) == '1/1'
