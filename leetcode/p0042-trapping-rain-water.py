#!/usr/bin/env python3

from typing import List


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def AC_trap(self, height):
        '''
        The tag showed [Array][Stack][Two Pointers], so if it can be
        solved by using stack, it should be solved by recursion.
        '''
        if len(height) < 3:
            return 0

        def _find_index_of_max_height(ht):
            max_height = max(ht)
            return ht.index(max_height)

        def _calculate_water(ht):
            if len(ht) < 3:
                return 0
            h = min(ht[0], ht[-1])
            area = h * (len(ht) - 2)
            for i in range(1, len(ht) - 1):
                area -= ht[i]
            return area

        def _trap(ht):
            if len(ht) < 3:
                return 0
            if ht[0] == ht[-1]:
                return _calculate_water(ht)
            if ht[0] > ht[-1]:
                index = _find_index_of_max_height(ht[1:]) + 1
                return _calculate_water(ht[:index + 1]) + _trap(ht[index:])
            else:
                index = _find_index_of_max_height(ht[:-1])
                return _calculate_water(ht[index:]) + _trap(ht[:index + 1])

        index = _find_index_of_max_height(height)
        return _trap(height[:index + 1]) + _trap(height[index:])

    def trap(self, height: List[int]) -> int:
        """
        two pointer
        refer to: https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution./185869
        """
        res = 0
        left = 0
        left_max = -1
        right = len(height) - 1
        right_max = -1
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res


if __name__ == '__main__':
    print(Solution().trap([2,5,1,3,1,2,1,7,7,6]))
    print(Solution().trap([2,5,1,2,3,4,7,7,6]))
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
