#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    B.sort()
    Y = [k-a for a in A]
    Y.sort()
    # Y <= B
    for (i, y) in enumerate(Y):
        if y > B[i]:
            return "NO"
    return "YES"



if __name__ == '__main__':
    assert twoArrays(10, [2,1,3], [7,8,9]) == "YES"
    assert twoArrays(5, [1,2,2,1], [3,3,3,4]) == "NO"