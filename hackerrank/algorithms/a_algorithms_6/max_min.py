#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    res = int(pow(10, 9))
    for i in range(len(arr) - k + 1):
        res = min(res, arr[i + k - 1] - arr[i])
    return res


if __name__ == '__main__':
    # assert maxMin(3, [10,100,300,200,1000,20,30]) == 20
    # assert maxMin(4, [1,2,3,4,10,20,30,40,100,200]) == 3
    # assert maxMin(2, [1,2,1,2,1]) == 0
    # WA
    assert maxMin(3, [100,200,300,350,400,401,402]) == 2