#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    if len(arr) <= 1:
        return 0
    n = len(arr)
    left2right = 0
    right2left = 0
    for i in range(n):
        left2right += arr[i][i]
        right2left += arr[i][n-(i+1)]

    return abs(left2right - right2left)

if __name__ == '__main__':
    pass
