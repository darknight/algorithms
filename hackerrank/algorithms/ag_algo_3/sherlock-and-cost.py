#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set
from collections import defaultdict, Counter


def WA_cost(B: List[int]):
    """
    take 1 for odd index, and take B[i] for even index
    take 1 for even index, and take B[i] for odd index
    """
    size = len(B)
    if size == 1:
        return 0
    take_odd = 0
    take_even = 0
    for i in range(1, size):
        if i % 2 == 0:
            take_odd += abs(B[i] - 1)
        else:
            take_odd += abs(1 - B[i - 1])

    for i in range(1, size):
        if i % 2 == 1:
            take_even += abs(B[i] - 1)
        else:
            take_even += abs(1 - B[i - 1])

    print(take_odd, take_even)
    return max(take_even, take_odd)


def cost(B: List[int]):
    """
    idea is from discussion
    prove that A[i] is either equal to 1 or B[i]
    then define:
    dp[i][0] means the max sum of A[0~i] when A[i]=1
    dp[i][1] means the max sum of A[0~i] when A[i]=B[i]
    """
    size = len(B)
    dp = [[0] * size, [0] * size]
    for i in range(1, size):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + abs(1 - B[i - 1]))
        dp[1][i] = max(dp[1][i - 1] + abs(B[i] - B[i - 1]), dp[0][i - 1] + abs(1 - B[i]))

    # print(dp)
    return max(dp[0][-1], dp[1][-1])


if __name__ == '__main__':
    # input = "43 36 62 20 71 56 27 48 66 94 14 39 4 47 19 20 14 94 95 42 84 3 49 33 51 41 1 60 80 33 47 96 39 32 4 96 17 72"
    # input.split(' ')
    # ints = [int(x) for x in input.split(" ")]
    # print(cost(ints))

    assert cost([100, 2, 100, 2, 100]) == 396
    assert cost([3, 15, 4, 12, 10]) == 50
    assert cost([4, 7, 9]) == 12
