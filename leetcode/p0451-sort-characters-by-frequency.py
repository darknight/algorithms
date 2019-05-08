#!/usr/bin/env python3

from typing import List

class Solution(object):
    def _frequencySort(self, s: str) -> str:
        from collections import defaultdict
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        tuples = sorted(map.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for (c, freq) in tuples:
            res = res + c * freq
        return res

    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        map = defaultdict(int)
        for c in s:
            map[c] += 1
        bucket = []
        for _ in range(len(s) + 1):
            bucket.append([])
        for (c, freq) in map.items():
            bucket[freq].append(c)
        res = ''
        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                res += c * i

        return res

if __name__ == '__main__':
    assert Solution().frequencySort('tree') in ['eert', 'eetr']
    assert Solution().frequencySort('cccaaa') in ['cccaaa', 'aaaccc']
    assert Solution().frequencySort('Aabb') in ['bbAa', 'bbaA']