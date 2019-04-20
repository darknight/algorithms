#!/usr/bin/env python3

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #TODO: too slow, improve!
        preorder = preorder.split(',')
        length = len(preorder)
        if length < 3:
            if length == 1 and preorder[0] == '#':
                return True
            return False

        start = 0
        while preorder:
            end = len(preorder)
            try:
                i = preorder.index('#', start, end)
            except:
                break
            if i == 0 or i == len(preorder)-1:
                break
            next = preorder[i+1]
            if next == '#':
                preorder = preorder[:i-1] + ['#'] + preorder[i+2:]
                start = 0
            else:
                start = i+1

        if len(preorder) == 1 and preorder[0] == '#':
            return True
        return False

if __name__ == '__main__':
    #print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    #print(Solution().isValidSerialization("1,#"))
    #print(Solution().isValidSerialization("9,#,#,1"))
    #print(Solution().isValidSerialization("1"))
    #print(Solution().isValidSerialization("9,#,92,#,#"))
    #print(Solution().isValidSerialization("91,13,14,#,#,10"))
    print(Solution().isValidSerialization("#") == True)
