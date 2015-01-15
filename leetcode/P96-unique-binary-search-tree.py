class Solution:
    # @return an integer
    def numTrees(self, n):
        res = [1, 1, 2, 5]
        if n <= 3:
            return res[n]
        for i in range(4, n+1):
            total = 0
            for j in range(i):
                total += res[j] * res[i-j-1]
            res.append(total)
        return res[-1]

print Solution().numTrees(4)
print Solution().numTrees(5)
print Solution().numTrees(6)
print Solution().numTrees(7)
