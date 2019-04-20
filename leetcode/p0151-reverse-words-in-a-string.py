class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split()
        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    print Solution().reverseWords("the sky is blue")