#!/usr/bin/env python3

class Solution(object):
    from typing import List
    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        max_n = (len(flowerbed) + 1) // 2
        if n > max_n:
            return False
        existed = []
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                existed.append(i)
        if len(existed) == 0:
            return n <= max_n
        else:
            curr_n = 0
            # head
            plot_num = existed[0] - 1
            curr_n += (plot_num + 1) // 2
            # tail
            plot_num = len(flowerbed) - 1 - existed[-1] - 1
            curr_n += (plot_num + 1) // 2
            # middle
            for i in range(len(existed) - 1):
                j = i + 1
                plot_num = existed[j] - 1 - existed[i] - 2
                curr_n += (plot_num + 1) // 2
            return n <= curr_n

    # TODO: from 3rd party
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pass

if __name__ == '__main__':
    assert Solution().canPlaceFlowers([1,0,0,0,0,1], 2) == False
    assert Solution().canPlaceFlowers([1,0,0,0,1], 1) == True
    assert Solution().canPlaceFlowers([1,0,0,0,1], 2) == False