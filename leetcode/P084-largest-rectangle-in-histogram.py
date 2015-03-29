class Solution:
    # @param height, a list of integer
    # @return an integer

    #Memory Limit Exceeded
    def _largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        largest = max(height)
        matrix = [height]
        length = len(height)
        for row in range(1, length):
            matrix.append([0] * length)
        for row in range(1, length):
            for col in range(length - row):
                matrix[row][col] = min(matrix[row-1][col], matrix[row-1][col+1])
                largest = max(matrix[row][col] * (row + 1), largest)
        return largest

    #Time Limit Exceeded
    def _largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        largest = max(height)
        length = len(height)
        for row in range(1, length):
            for col in range(length - row):
                height[col] = min(height[col], height[col+1])
                largest = max(height[col] * (row + 1), largest)
            print height
        return largest

    #Memory Limit Exceeded
    def _largestRectangleArea(self, height):
        def _divide_conquer(histo):
            if len(histo) == 1:
                return histo[0]
            if len(histo) == 0:
                return 0
            curr_min = min(histo)
            curr_idx = histo.index(curr_min)
            left = _divide_conquer(histo[:curr_idx])
            right = _divide_conquer(histo[curr_idx+1:])
            curr = curr_min * len(histo)
            return max(left, right, curr)

        if len(height) == 0:
            return 0
        largest = self._divide_conquer(height)
        return largest

    #Time Limit Exceeded
    def _largestRectangleArea(self, height):
        #TODO: use Segment Tree, see
        #http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
        def _divide_conquer(height, start, stop):
            if start == stop:
                return height[start]
            if start > stop:
                return 0

            curr_min = height[start]
            curr_idx = start
            i = start + 1
            while i < stop:
                if curr_min > height[i]:
                    curr_min = height[i]
                    curr_idx = i
                i += 1

            left = _divide_conquer(height, start, curr_idx - 1)
            right = _divide_conquer(height, curr_idx + 1, stop)
            curr = curr_min * (stop - start + 1)

            return max(left, right, curr)

        if len(height) == 0:
            return 0
        largest = _divide_conquer(height, 0, len(height) - 1)
        return largest

    #Accepted
    def largestRectangleArea(self, height):
        '''
        Reference:
        http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
        '''
        if len(height) == 0:
            return 0

        largest = 0
        height.append(0)
        stack = []
        i = 0
        while i < len(height):
            if len(stack) == 0 or height[stack[-1]] < height[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if len(stack) == 0 else i - stack[-1] - 1
                largest = max(largest, height[top] * width)

        return largest

print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([2,1,3,2,1,3])

