from collections import defaultdict
from itertools import combinations

def solve(df, ds, raw):
    if len(raw) == 1 or len(raw) == 2:
        return 0
    res = len(raw)
    for i in range(2, len(raw)+1):
        subsets = combinations(raw, i)
        found = False
        for sub in subsets:
            fset = set([f for (f, s) in sub])
            sset = set([s for (f, s) in sub])
            if df == fset and ds == sset:
                res = min(res, i)
                found = True
                break
        if found:
            break
    return len(raw) - res

def main():
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        df = set()
        ds = set()
        raw = []
        for j in range(N):
            first, second = raw_input().split()
            raw.append((first, second))
            df.add(first)
            ds.add(second)
        res = solve(df, ds, raw)
        print 'Case #%d: %d' % (int(i), res)

if __name__ == '__main__':
    main()