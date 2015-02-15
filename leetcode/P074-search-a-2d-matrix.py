class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        last = len(matrix[0]) - 1
        start = 0
        stop = len(matrix) - 1
        row = -1
        while start <= stop:
            mid = (start + stop) / 2
            if matrix[mid][last] > target:
                stop = mid - 1
            elif matrix[mid][last] < target:
                start = mid + 1
            else:
                return True
        if stop >= 0 and matrix[stop][last] > target:
            row = stop
        elif start < len(matrix) and matrix[start][last] > target:
            row = start
        else:
            return False
        #print 'start: %d, stop: %d' % (start, stop)
        #print 'search row: %d' % row
        start = 0
        stop = last
        while start <= stop:
            mid = (start + stop) / 2
            if matrix[row][mid] > target:
                stop = mid - 1
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                return True
        return False

if __name__ == '__main__':
    m = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,50]
        ]
    print Solution().searchMatrix(m, 3) == True
    print Solution().searchMatrix(m, 8) == False
    print Solution().searchMatrix(m, 16) == True
    print Solution().searchMatrix(m, 17) == False
    print Solution().searchMatrix(m, 30) == True
    print Solution().searchMatrix(m, 55) == False

    m = [[1,3]]
    print Solution().searchMatrix(m, 2) == False
    print Solution().searchMatrix(m, 1) == True
    print Solution().searchMatrix(m, 4) == False
