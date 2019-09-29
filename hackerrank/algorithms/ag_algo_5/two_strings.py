#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    if s1_set.intersection(s2_set):
        return "YES"
    return "NO"

if __name__ == '__main__':
    assert twoStrings("hello", "world") == "YES"
    assert twoStrings("hi", "world") == "NO"