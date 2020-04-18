#!/usr/bin/env python3

import math, itertools, functools, heapq, re
from collections import defaultdict, Counter
from typing import List, Set, Dict, Tuple
try:
    from _tree import *
    from _list import *
    from _util import *
except ImportError:
    pass


class Solution:
    def entityParser(self, text: str) -> str:
        text = re.sub(r"&quot;", r'"', text)
        text = re.sub(r"&apos;", r"'", text)
        text = re.sub(r"&amp;", r"&", text)
        text = re.sub(r"&gt;", r">", text)
        text = re.sub(r"&lt;", r"<", text)
        text = re.sub(r"&frasl;", r"/", text)
        return text


if __name__ == '__main__':
    pass
