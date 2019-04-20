class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        '''
        basic thinking: http://www.cnblogs.com/wei-li/p/SingleNumberII.html
        refer to: https://oj.leetcode.com/discuss/21113/c-o-n-complex-solution-easy-to-understand
        another method: http://blog.csdn.net/morewindows/article/details/12684497
        related questions: http://www.cnblogs.com/luxiaoxun/archive/2012/09/08/2676610.html
        '''
        oneNum = 0
        twoNum = 0
        threeNum = 0
        for a in A:
            threeNum = twoNum & a
            twoNum = twoNum | oneNum & a
            oneNum = oneNum | a

            twoNum = twoNum & (~threeNum)
            oneNum = oneNum & (~threeNum)
        return oneNum

if __name__ == '__main__':
    print Solution().singleNumber([1,2,3,4,3,2,1,1,2,3])
