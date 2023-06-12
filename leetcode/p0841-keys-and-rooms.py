#!/usr/bin/env python3

import math, itertools, functools, heapq
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms[0]) == 0:
            return False

        visited = set([])
        unlocked = {0}
        while len(unlocked) != 0:
            keys = set([])
            for room in unlocked:
                if room in visited:
                    continue
                visited.add(room)
                for key in rooms[room]:
                    keys.add(key)
            unlocked = keys

        return len(visited) == len(rooms)


if __name__ == '__main__':
    pass
