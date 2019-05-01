#!/usr/bin/env python3

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                break
        return [i+1, j+1]

if __name__ == '__main__':
    assert Solution().twoSum([2,7,11,15], 9) == [1,2]