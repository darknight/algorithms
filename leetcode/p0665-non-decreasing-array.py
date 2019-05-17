#!/usr/bin/env python3


class Solution(object):

    from typing import List

    def _checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                    case1 = True
                    for j in range(i+1, len(nums) - 1):
                        if nums[j] > nums[j + 1]:
                            case1 = False
                            break
                    return case1
                elif i + 1 == len(nums) - 1:
                    return True
                elif i + 1 < len(nums) - 1 and nums[i + 2] >= nums[i]:
                    case2 = True
                    for j in range(i+2, len(nums) - 1):
                        if nums[j] > nums[j + 1]:
                            case2 = False
                            break
                    return case2
                else:
                    return False
        return True

    # TODO
    def checkPossibility(self, nums: List[int]) -> bool:
        pass

if __name__ == '__main__':
    # assert Solution().checkPossibility([4,2,3]) is True
    # assert Solution().checkPossibility([4,2,1]) is False
    # assert Solution().checkPossibility([3,4,2,3]) is False
    # assert Solution().checkPossibility([1,2,4,5,3]) is True
    assert Solution().checkPossibility([2,3,1,5,4]) is False
