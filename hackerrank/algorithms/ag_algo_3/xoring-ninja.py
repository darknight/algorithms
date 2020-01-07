#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set
from collections import defaultdict, Counter

def xoringNinja(arr: List[int]):
    """
    n is 10^5, so can not permute, since it's exponential
    refer to
    https://cscodingnote.wordpress.com/2015/12/27/xoring-ninja/
    https://www.quora.com/What-is-the-algorithm-of-this-Hacker-Rank-question
    """
    val = 0
    for num in arr:
        val = val | num
    res = 2 ** (len(arr) - 1) * val
    return res % 1000000007

if __name__ == '__main__':
    pass
