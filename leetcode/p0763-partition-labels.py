#!/usr/bin/env python3

class Solution(object):
    from typing import List

    # slow
    def _partitionLabels(self, S: str) -> List[int]:
        res = []
        i = 0
        while i < len(S):
            j = len(S) - 1
            while i < j and S[i] != S[j]:
                j -= 1
            if i == j:
                res.append(1)
                i += 1
            else:
                interval = set(S[i:j])
                end = j
                k = len(S) - 1
                while k > end:
                    if S[k] in interval:
                        interval = set(S[i:k+1])
                        end = k
                        k = len(S) - 1
                    else:
                        k -= 1
                res.append(end - i + 1)
                i = end + 1
        return res

    # TODO
    def partitionLabels(self, S: str) -> List[int]:
        pass


if __name__ == '__main__':
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]
    assert Solution().partitionLabels("defegde") == [7]
    assert Solution().partitionLabels("defegxe") == [1,6]
    assert Solution().partitionLabels("defegdz") == [6,1]
    assert Solution().partitionLabels("qiejxqfnqceocmy") == [13,1,1]