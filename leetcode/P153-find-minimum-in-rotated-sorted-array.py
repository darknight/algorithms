class Solution:
    # @param num, a list of integer
    # @return an integer
    def _findMin(self, num):
        '''
        passed
        '''
        return min(num)

    def _findMin(self, num):
        '''
        passed
        '''
        if len(num) == 0:
            return
        ret = num[0]
        for x in num:
            if x < ret:
                ret = x
                break
        return ret

    def findMin(self, num):
        '''
        Tag: Binary Search
        '''
        # TODO
        pass

if __name__ == '__main__':
    print Solution().findMin([4,5,6,7,0,1,2])
