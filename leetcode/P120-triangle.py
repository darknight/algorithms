class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # TODO: review knapsack problem
        m = len(triangle)
        if m == 0:
            return 0
        if m == 1:
            return min(triangle[0])
        max_n = len(triangle[-1])
        res = [float('inf')] * (max_n + 1)
        res[1] = triangle[0][0]
        for i in xrange(1, m):
            n = len(triangle[i])
            for j in xrange(n, 0, -1):
                res[j] = min(res[j-1], res[j]) + triangle[i][j-1]
        return min(res)

if __name__ == '__main__':
    triangle = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print Solution().minimumTotal(triangle)
