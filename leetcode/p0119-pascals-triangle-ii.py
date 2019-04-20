class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        lastLevel = [None] * (rowIndex + 1)
        lastLevel[0] = lastLevel[1] = 1
        for index in range(2, rowIndex+1):
            j = index - 1
            i = index - 2
            while i >= 0:
                lastLevel[j] = lastLevel[j] + lastLevel[i]
                j -= 1
                i -= 1
            lastLevel[0] = 1
            lastLevel[index] = 1
        return lastLevel

if __name__ == '__main__':
    print Solution().getRow(2)
    print Solution().getRow(3)
    print Solution().getRow(5)
