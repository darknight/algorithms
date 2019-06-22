#!/usr/bin/env python3

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return
        self.prefix = [nums[0]]
        for num in nums[1:]:
            self.prefix.append(num + self.prefix[-1])

    def sumRange(self, i: int, j: int) -> int:
        assert i >= 0
        if i == 0:
            return self.prefix[j]
        return self.prefix[j] - self.prefix[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    array = NumArray([-2, 0, 3, -5, 2, -1])
    assert array.sumRange(0, 2) == 1
    assert array.sumRange(2, 5) == -1
    assert array.sumRange(0, 5) == -3