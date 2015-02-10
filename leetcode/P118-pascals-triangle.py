class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return result

        def _oneRow(n):
            if n == 2:
                result.append([1,1])
                return [1,1]
            res = _oneRow(n-1)
            i = 0
            j = 1
            thisRow = [1]
            while j < len(res):
                thisRow.append(res[i] + res[j])
                i += 1
                j += 1
            thisRow.append(1)
            result.append(thisRow)
            return thisRow

        row = _oneRow(numRows)
        return result

if __name__ == '__main__':
    print Solution().generate(1)
    print Solution().generate(2)
    print Solution().generate(3)
    print Solution().generate(4)
    print Solution().generate(5)
    print Solution().generate(6)
