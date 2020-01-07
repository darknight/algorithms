#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set
from collections import defaultdict


def bigSorting(unsorted: List[str]):
    size_map = defaultdict(list)
    for integer in unsorted:
        size_map[len(integer)].append(integer)
    res = []
    keys = sorted(size_map.keys())
    for key in keys:
        vals = size_map[key]
        res.extend(sorted(vals))

    return res


if __name__ == '__main__':
    print(bigSorting([
        "31415926535897932384626433832795",
        "1",
        "3",
        "10",
        "3",
        "5"
    ]))
    print(bigSorting([
        "1",
        "2",
        "100",
        "12303479849857341718340192371",
        "3084193741082937",
        "3084193741082938",
        "111",
        "200"
    ]))
