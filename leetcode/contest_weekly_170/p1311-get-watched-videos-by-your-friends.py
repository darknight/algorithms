#!/usr/bin/env python3

import math, itertools
from collections import defaultdict, Counter
from typing import List, Set
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        marked = [0] * len(friends)
        nodes = self.bfs(friends, marked, id, level)
        cnt = defaultdict(int)
        for v in nodes:
            for video in watchedVideos[v]:
                cnt[video] += 1

        items = list(cnt.items())
        items.sort(key=lambda x: (x[1], x[0]))

        res = [k for (k, v) in items]
        return res

    def bfs(self, table: List[List[int]], marked: List[int], id: int, level: int) -> List[int]:
        queue = [id]
        marked[id] = 1
        while level > 0:
            tmp = []
            for u in queue:
                for v in table[u]:
                    if marked[v] != 1:
                        tmp.append(v)
                        # forgot to update marked array, WA here
                        marked[v] = 1
            queue = tmp
            level -= 1
        return queue


if __name__ == '__main__':
    print(Solution().watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))
    print(Solution().watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))
