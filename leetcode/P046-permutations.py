class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) <= 1:
            return [num]
        results = []

        def _permute(start, stop):
            if start == stop:
                results.append(num[:])
                return
            for i in range(start, stop+1):
                num[i], num[start] = num[start], num[i]
                _permute(start+1, stop)
                num[i], num[start] = num[start], num[i]

        _permute(0, len(num)-1)
        return results

if __name__ == '__main__':
    print Solution().permute([1,2,3])
