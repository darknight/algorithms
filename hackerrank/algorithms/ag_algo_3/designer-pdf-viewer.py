#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Set
from collections import defaultdict, Counter

def designerPdfViewer(h: List[int], word: str):
    height = 0
    for w in word:
        idx = ord(w) - ord('a')
        height = max(height, h[idx])

    return height * len(word)

if __name__ == '__main__':
    pass
