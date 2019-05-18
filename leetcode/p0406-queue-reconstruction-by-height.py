#!/usr/bin/env python3

class Solution(object):
    from typing import List

    # from 3rd
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for ppl in people:
            res.insert(ppl[1], ppl)
        return res


if __name__ == '__main__':
    assert Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]