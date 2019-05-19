#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        h = len(letters) - 1
        while l <= h:
            m = l + (h - l) // 2
            if target >= letters[m]:
                l = m + 1
            else:
                h = m - 1
        if l >= len(letters) or h < 0:
            return letters[0]
        else:
            return letters[l]



if __name__ == '__main__':
    assert Solution().nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "g") == "j"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "k") == "c"
