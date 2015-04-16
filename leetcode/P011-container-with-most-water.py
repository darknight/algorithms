class Solution:
    # @return an integer
    def _maxArea(self, height):
        '''
        Time Limit Exceeded
        '''
        length = len(height)
        if length < 2:
            return 0
        max_area = 0
        for i in range(length - 1):
            for j in range(i+1, length):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area

    def _maxArea(self, height):
        '''
        Time Limit Exceeded
        '''
        length = len(height)
        if length < 2:
            return 0
        max_area = 0
        for step in range(1, length):
            maxh = 0
            for i in range(length - step):
                j = i + step
                maxh = max(maxh, min(height[i], height[j]))
            max_area = max(max_area, maxh * step)
        return max_area

    def _maxArea(self, height):
        '''
        Time Limit Exceeded
        '''
        length = len(height)
        if length < 2:
            return 0
        max_area = 0
        for i in range(length - 1):
            hj = height[length - 1]
            area = min(height[i], hj) * (length - 1 - i)
            for j in range(length - 1, i, -1):
                if height[j] > hj:
                    hj = height[j]
                    area = min(height[i], hj) * (j - i)
                    max_area = max(max_area, area)
        return max_area

    def maxArea(self, height):
        '''
        refer to: http://www.cnblogs.com/TenosDoIt/p/3812880.html
        '''
        length = len(height)
        if length < 2:
            return 0
        max_area = 0
        i = 0
        j = length - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    print Solution().maxArea([1, 4, 3, 1, 5])
