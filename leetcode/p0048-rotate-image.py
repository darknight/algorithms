#!/usr/bin/env python3

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if n <= 1:
            return matrix
        pivot = n / 2
        for i in range(pivot):
            for j in range(i, n - i - 1):
                curr_x = i
                curr_y = j
                temp = matrix[curr_x][curr_y]
                for _ in range(4):
                    next_x = curr_y
                    next_y = n - curr_x - 1
                    matrix[next_x][next_y], temp = temp, matrix[next_x][next_y]
                    curr_x = next_x
                    curr_y = next_y
        return matrix

if __name__ == '__main__':
    print(Solution().rotate([[1]]))
    print(Solution().rotate([[1,2],[3,4]]))
    print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

