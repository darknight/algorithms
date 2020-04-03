from collections import defaultdict

def solve(df, ds, raw):
    if len(raw) == 1 or len(raw) == 2:
        return 0
    real_first = set()
    real_second = set()
    may_fake = []
    for first, second in raw:
        if df[first] == 1 or ds[second] == 1:
            real_first.add(first)
            real_second.add(second)
        else:
            may_fake.append((first, second))
    res = 0
    i = 0
    while i < len(may_fake):
        (f, s) = may_fake[i]
        # this is not true
        # e.g (BJ, CY) <=> (BJ, OU) (FM, CY)
        # the real set is not stable
        # it is influenced by the order of input
        if f not in real_first and s not in real_second:
            real_first.add(f)
            real_second.add(s)
            may_fake.pop(i)
        else:
            i += 1
    while may_fake:
        f, s = may_fake.pop(0)
        if f in real_first and s in real_second:
            res += 1
        else:
            real_first.add(f)
            real_second.add(s)
    return res


def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        df = defaultdict(int)
        ds = defaultdict(int)
        raw = []
        for j in range(N):
            first, second = input().split()
            raw.append((first, second))
            df[first] += 1
            ds[second] += 1
        res = solve(df, ds, raw)
        print('Case #%d: %d' % (int(i), res))

if __name__ == '__main__':
    main()