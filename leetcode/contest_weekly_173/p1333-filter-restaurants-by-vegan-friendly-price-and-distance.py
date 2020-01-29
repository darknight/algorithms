#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        candidate = []
        for rest in restaurants:
            id, rating, vegan, price, dist = rest
            if veganFriendly == 1 and vegan == 0:
                continue
            if price > maxPrice:
                continue
            if dist > maxDistance:
                continue
            candidate.append(rest)
        candidate.sort(key=lambda x: (-x[1], -x[0]))

        return [c[0] for c in candidate]



if __name__ == '__main__':
    pass
