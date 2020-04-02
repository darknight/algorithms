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


class UndergroundSystem:

    def __init__(self):
        self.cin = defaultdict(set)
        self.cout = defaultdict(set)
        self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cin[stationName].add(id)
        self.time[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.cout[stationName].add(id)
        self.time[id].append((stationName, t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ids = self.cin[startStation].intersection(self.cout[endStation])
        cnt = 0
        total = 0
        for id in ids:
            for i in range(0, len(self.time[id]), 2):
                start, t1 = self.time[id][i]
                end, t2 = self.time[id][i+1]
                if start != startStation or end != endStation:
                    continue
                cnt += 1
                total += t2 - t1

        return total / cnt


if __name__ == '__main__':
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    undergroundSystem.getAverageTime("Paradise", "Cambridge")
    undergroundSystem.getAverageTime("Leyton", "Waterloo")
    undergroundSystem.checkIn(10, "Leyton", 24)
    undergroundSystem.getAverageTime("Leyton", "Waterloo")
    undergroundSystem.checkOut(10, "Waterloo", 38)
    undergroundSystem.getAverageTime("Leyton", "Waterloo")

