#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    res = 0
    for c in s:
        if c.isupper():
            res += 1
    return res + 1

if __name__ == '__main__':
    assert camelcase("saveChangesInTheEditor") == 5
    assert camelcase("oneTwoThree") == 3
