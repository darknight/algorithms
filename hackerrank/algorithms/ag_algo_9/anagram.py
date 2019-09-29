#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 != 0:
        return -1
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]

    s1_cnt = [0] * 26
    s2_cnt = [0] * 26

    for c in s1:
        s1_cnt[ord(c) - ord('a')] += 1
    for c in s2:
        s2_cnt[ord(c) - ord('a')] += 1

    for i in range(26):
        s1_cnt[i] -= s2_cnt[i]

    res = 0
    for i in range(26):
        res += max(s1_cnt[i], 0)

    return res

if __name__ == '__main__':
    assert anagram('aaabbb') == 3
    assert anagram('ab') == 1
    assert anagram('abc') == -1
    assert anagram('mnop') == 2
    assert anagram('xyyx') == 0
    assert anagram('xaxbbbxx') == 1
