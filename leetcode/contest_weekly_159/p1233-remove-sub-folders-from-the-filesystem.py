#!/usr/bin/env python3

import math
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass


class Solution:

    def sub_path(self, base: List[str], path: List[str]) -> bool:
        if len(base) > len(path):
            return False
        for i in range(len(base)):
            if base[i] != path[i]:
                return False
        return True

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if len(folder) == 1:
            return folder

        folder.sort()
        paths = []
        for fd in folder:
            path = []
            for p in fd.split("/"):
                if p == "":
                    continue
                path.append(p)
            paths.append(path)

        res = [paths[0]]
        i = 1
        while i < len(paths):
            base = res[-1]
            path = paths[i]
            if self.sub_path(base, path):
                i += 1
                continue
            res.append(path)
            i += 1

        res = ["/" + "/".join(item) for item in res]
        # print(res)
        return res


if __name__ == '__main__':
    Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    Solution().removeSubfolders(["/a","/a/b/c","/a/b/d"])
    Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])
