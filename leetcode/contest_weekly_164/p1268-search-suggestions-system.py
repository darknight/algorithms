#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        wlen = len(searchWord)

        res = []

        for n in range(1, wlen+1):
            prefix = searchWord[:n]
            i = 0
            tmp = []
            while i < len(products):
                pre = products[i][:n]
                if pre != prefix:
                    products.pop(i)
                    continue
                tmp.append(products[i])
                i += 1
            tmp.sort()
            res.append(tmp[:3])

        for _ in range(wlen - len(res)):
            res.append(res[-1])
        print(res)
        return res



if __name__ == '__main__':
    assert Solution().suggestedProducts(
        products = ["mobile","mouse","moneypot","monitor","mousepad"],
        searchWord = "mouse")
    assert Solution().suggestedProducts(products = ["havana"], searchWord = "havana")
    assert Solution().suggestedProducts(
        products = ["bags","baggage","banner","box","cloths"],
        searchWord = "bags")
    assert Solution().suggestedProducts(products = ["havana"], searchWord = "tatiana")
