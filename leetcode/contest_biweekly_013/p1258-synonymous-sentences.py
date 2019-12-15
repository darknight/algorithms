#!/usr/bin/env python3

import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:
    def WA_generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """
        WA on:
        [["v", "yr"]],
        "v v v v yZ"
        """
        words = text.split()
        idxlist = []
        wordlist = []

        for (i, w) in enumerate(words):
            s = set()
            for synonym in synonyms:
                if w == synonym[0] or w == synonym[1]:
                    s.add(synonym[0])
                    s.add(synonym[1])
            if len(s) == 0:
                continue
            self.drain(synonyms, s)
            idxlist.append(i)
            wordlist.append(s)

        res = []
        self.replace(0, idxlist, wordlist, words, res)

        return res

    def replace(self, i, idxlist, wordlist, words: List[str], res: List[str]):
        if i == len(idxlist):
            res.append(" ".join(words))
            return
        idx = idxlist[i]
        ws = sorted(wordlist[i])
        for w in sorted(ws):
            words[idx] = w
            self.replace(i+1, idxlist, wordlist, words, res)

    def drain(self, synonyms: List[List[str]], s: set):
        while True:
            found = -1
            for j in range(len(synonyms)):
                syn0, syn1 = synonyms[j]
                if syn0 in s or syn1 in s:
                    s.add(syn0)
                    s.add(syn1)
                    found = j
                    break
            if found == -1:
                break
            else:
                synonyms.pop(found)

    def union(self, p: str, q: str, uf: dict):
        root1 = self.find(p, uf)
        root2 = self.find(q, uf)
        if root1 == root2:
            return
        uf[root1] = root2

    def find(self, p: str, uf: dict) -> str:
        if p not in uf:
            uf[p] = p
        while p != uf[p]:
            p = uf[p]
        return p

    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """
        refer to
        https://leetcode.com/problems/synonymous-sentences/discuss/430489/python-union-find
        """
        uf = {}
        words = text.split()
        for w in words:
            uf[w] = w
        for syn in synonyms:
            p, q = syn[0], syn[1]
            self.union(p, q, uf)

        roots = defaultdict(list)
        for k in uf.keys():
            r = self.find(k, uf)
            roots[r].append(k)

        # forgot to sort, contribute WA
        for k in roots.keys():
            roots[k].sort()

        all_items = []
        for w in words:
            r = self.find(w, uf)
            all_items.append(roots[r])

        item_list = itertools.product(*all_items)
        res = []
        for items in item_list:
            res.append(" ".join(items))

        return res


    # TODO
    def DFS_generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        pass

    # TODO
    def BFS_generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        pass

if __name__ == '__main__':
    Solution().generateSentences(
        synonyms=[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
        text="I am happy today but was sad yesterday"
    )

    Solution().generateSentences(
        [["happy", "joy"], ["cheerful", "glad"]],
        "I am happy today but was sad yesterday"
    )

    Solution().generateSentences(
        [["a", "b"], ["c", "d"], ["e", "f"]],
        "a c e"
    )

    Solution().generateSentences(
        [["v", "yr"]],
        "v v v v yZ"
    )