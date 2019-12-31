#!/usr/bin/env python3

import re
import math
import itertools
from collections import defaultdict
from typing import List
from typing import Set
try:
    from _tree import *
except ImportError:
    pass

try:
    from _list import *
except ImportError:
    pass

try:
    from _uitl import *
except ImportError:
    pass


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            no_dot = re.sub("\.+", "", local)
            no_plus = re.sub("\+\w+", "", no_dot)
            unique.add(no_plus+'@'+domain)

        return len(unique)

if __name__ == '__main__':
    pass
