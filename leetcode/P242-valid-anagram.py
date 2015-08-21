class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #TODO: do not user library
        from collections import Counter

        return Counter(s) == Counter(t)

if __name__ == '__main__':
    print Solution().isAnagram('anagram', 'nagaram')
