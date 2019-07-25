#!/usr/bin/env python3

from collections import defaultdict

class Solution(object):
    from typing import List

    # TLE
    def _checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars = set(s1)
        count_dict = defaultdict(int)
        for c in s1:
            count_dict[c] += 1
        count_sorted = sorted(count_dict.items())

        tmp_dict = defaultdict(int)
        step = len(s1)
        i = 0
        while i < len(s2) - step + 1:
            skip = False
            tmp_dict.clear()
            for j in range(i, i + step):
                if s2[j] not in chars:
                    skip = True
                    break
                tmp_dict[s2[j]] += 1
            if skip is True:
                i = j + 1
                continue
            if len(tmp_dict) < len(count_dict):
                i += 1
                continue
            if count_sorted == sorted(tmp_dict.items()):
                return True
            i += 1
        return False

    # TLE - sliding window
    def _checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True

        chars = set(s1)
        s1_sorted = sorted(s1)

        candidates = []
        step = len(s1)
        i = 0
        j = 0
        while i < len(s2) - step + 1:
            if s2[i] not in chars:
                i += 1
                continue
            skip = False
            for j in range(i, i + step):
                if s2[j] not in chars:
                    skip = True
                    break
            if skip is True:
                i = j + 1
                continue
            candidates.append(sorted(s2[i:j+1]))
            j = i + step
            while j < len(s2) and s2[j] in chars:
                candidates.append(sorted(s2[j-step+1:j+1]))
                j += 1
            i = j + 1

        return s1_sorted in candidates

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True

        chars = set(s1)
        s1_arr = [0] * 128
        for c in s1:
            s1_arr[ord(c)] += 1

        arr = [0] * 128
        step = len(s1)
        i = 0
        j = 0
        while i < len(s2) - step + 1:
            if s2[i] not in chars:
                i += 1
                j += 1
                continue
            while j < len(s2):
                if s2[j] not in chars:
                    break
                arr[ord(s2[j])] += 1
                if arr[ord(s2[j])] > s1_arr[ord(s2[j])]:
                    break
                j += 1
            if j - i == step:
                return True
            if s2[j] not in chars:  # break 1
                arr = [0] * 128
                i = j + 1
                j = i
                continue
            while s2[i] != s2[j]:  # break 2
                arr[ord(s2[i])] -= 1
                i += 1
            arr[ord(s2[i])] -= 1
            i += 1
            j += 1
        return False

if __name__ == '__main__':
    # assert Solution().checkInclusion("ab", "eidbaooo") is True
    # assert Solution().checkInclusion("ab", "eidboaoo") is False
    # assert Solution().checkInclusion("adc", "dcda") is True
    # assert Solution().checkInclusion("r", "pilmtnzraxj") is True
    assert Solution().checkInclusion("ky", "ainwkckifykxlribaypk") is True