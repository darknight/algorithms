#!/usr/bin/env python3

import math
from typing import List
from collections import defaultdict

class Solution:

    def TLE1_smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        groups = []
        for (i, j) in pairs:
            groups.append({i, j})

        merged = []
        while len(groups) > 0:
            g = groups.pop(0)
            can_merge = False
            for i in range(len(groups)):
                if len(groups[i].intersection(g)) > 0:
                    groups[i] = groups[i].union(g)
                    can_merge = True
            if can_merge is False:
                merged.append(g)

        pick_from = {}
        for group in merged:
            for idx in group:
                pick_from[idx] = group

        chars = list(s)
        for pos in range(len(chars)):
            if pos not in pick_from:
                continue
            indices = list(pick_from[pos])
            for idx in indices:
                if idx <= pos:
                    continue
                if chars[idx] < chars[pos]:
                    chars[pos], chars[idx] = chars[idx], chars[pos]

        return "".join(chars)

    def TLE2_smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjoint = [-1] * len(s)

        def findRoot(disjoint, node):
            if disjoint[node] == -1:
                return node
            return findRoot(disjoint, disjoint[node])

        for (i, j) in pairs:
            i, j = min(i, j), max(i, j)
            root_i = findRoot(disjoint, i)
            root_j = findRoot(disjoint, j)
            if root_i != root_j:
                disjoint[root_j] = root_i

        root_map = defaultdict(int)
        root_set = defaultdict(set)
        for i in range(len(s)):
            root = findRoot(disjoint, i)
            root_map[i] = root
            root_set[root].add(i)

        chars = list(s)
        for pos in range(len(chars)):
            root = root_map[pos]
            r_set = root_set[root]
            for idx in r_set:
                if idx <= pos:
                    continue
                if chars[idx] < chars[pos]:
                    chars[pos], chars[idx] = chars[idx], chars[pos]

        return "".join(chars)

    def TLE3_smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        raw_sets = []
        for (i, j) in pairs:
            raw_sets.append({i, j})

        disjoint_sets = []
        while len(raw_sets) > 0:
            head = raw_sets.pop(0)
            merged = False
            for i in range(len(raw_sets)):
                if head.isdisjoint(raw_sets[i]):
                    continue
                else:
                    raw_sets[i] |= head
                    merged = True
            if merged is False:
                disjoint_sets.append(head)

        set_map = defaultdict(set)
        for dset in disjoint_sets:
            for pos in dset:
                set_map[pos] = dset

        chars = list(s)
        for pos in range(len(chars)):
            r_set = set_map[pos]
            for idx in r_set:
                if idx <= pos:
                    continue
                if chars[idx] < chars[pos]:
                    chars[pos], chars[idx] = chars[idx], chars[pos]

        return "".join(chars)

    # union-find solution
    def UF_smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjoint = [-1] * len(s)

        # TLE + stack overflow if without path compression
        def find(disjoint, node):
            if disjoint[node] == -1:
                return node
            disjoint[node] = find(disjoint, disjoint[node])
            return disjoint[node]

        def union(disjoint, i, j):
            root_i = find(disjoint, i)
            root_j = find(disjoint, j)
            if root_i != root_j:
                disjoint[root_j] = root_i

        for (i, j) in pairs:
            union(disjoint, i, j)

        # use root as key
        root_map = defaultdict(list)
        for i in range(len(s)):
            root = find(disjoint, i)
            if root != -1:
                root_map[root].append(i)
            else:
                root_map[i].append(i)

        chars = list(s)
        res = [''] * len(chars)
        for pos in range(len(chars)):
            if pos not in root_map:
                continue
            index_list = root_map[pos]
            char_list = [chars[i] for i in index_list]
            index_list.sort()
            char_list.sort()
            # print("index_list =>", index_list)
            # print("char_list =>", char_list)
            for k in range(len(index_list)):
                res[index_list[k]] = char_list[k]

        return "".join(res)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # TODO: see it as a graph and try
        pass


if __name__ == '__main__':
    assert Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2]]) == "bacd"
    assert Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]) == "abcd"
    assert Solution().smallestStringWithSwaps("cba", [[0,1],[1,2]]) == "abc"

    # so tricky, `maximum recursion depth exceeded in comparison`
    assert Solution().smallestStringWithSwaps("qdwyt", [[2,3],[3,2],[0,1],[4,0],[3,2]]) == "dqwyt"