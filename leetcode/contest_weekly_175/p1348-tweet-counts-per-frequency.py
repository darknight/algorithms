#!/usr/bin/env python3

import math, itertools, functools
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class TweetCounts:

    def __init__(self):
        self.store = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.store[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:
            delta = 86400

        times = self.store[tweetName]
        times.sort()
        size = len(times)

        res = []
        i = 0
        cnt = (endTime - startTime) // delta + 1
        for k in range(cnt):
            start = startTime + delta * k
            end = min(start + delta, endTime+1)
            curr = 0
            while i < size and times[i] < start:
                i += 1
            while i < size and times[i] < end:
                curr += 1
                i += 1
            res.append(curr)

        return res


if __name__ == '__main__':
    pass
