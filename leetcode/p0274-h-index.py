class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        citations.sort(reverse=True)
        res = 0
        for i, val in enumerate(citations):
            if val >= i+1:
                res = i+1
            else:
                break
        return res

if __name__ == '__main__':
    print Solution().hIndex([0])
    print Solution().hIndex([1])
    print Solution().hIndex([8])
    print Solution().hIndex([3, 0, 6, 1, 5])
    print Solution().hIndex([10, 8, 5, 4, 3])
    print Solution().hIndex([10, 8, 5, 3, 3])
