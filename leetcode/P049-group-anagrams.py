class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #TODO: slow & improve
        length = len(strs)
        if length == 0:
            return [[]]
        if length == 1:
            return [strs]
        tmp = {}
        for s in strs:
            sign = [0] * 26
            for c in s:
                offset = ord(c) - ord('a')
                sign[offset] += 1
            key = []
            for i, val in enumerate(sign):
                if val > 0:
                    key.append(chr(ord('a')+i)+str(val))
            key = ''.join(key)
            #print key
            if key in tmp:
                tmp[key].append(s)
            else:
                tmp[key] = [s]
        res = []
        for k, v in tmp.items():
            if len(v) > 1:
                v.sort()
            res.append(v)
        return res

if __name__ == '__main__':
    #print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print Solution().groupAnagrams(["ron","huh","gay","tow","moe","tie","who","ion","rep","bob","gte","lee","jay","may","wyo","bay","woe","lip","tit","apt","doe","hot","dis","fop","low","bop","apt","dun","ben","paw","ere","bad","ill","fla","mop","tut","sol","peg","pop","les"])
