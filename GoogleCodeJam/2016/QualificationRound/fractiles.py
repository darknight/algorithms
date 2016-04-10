def solve(K, C, S):
    res = []
    if K == 1:
        return ['1']
    if C == 1:
        if S == K:
            res = [str(i) for i in xrange(1, K+1)]
    else:
        if S >= K-1:
            res = [str(i) for i in xrange(2, K+1)]
    return res

def main():
    T = int(raw_input())
    for t in range(1, T+1):
        raw = raw_input().split()
        K, C, S = int(raw[0]), int(raw[1]), int(raw[2])
        if K == S:
            res = [str(i) for i in xrange(1, K+1)]
            print 'Case #%d: %s' % (t, ' '.join(res))
        else:
            res = solve(K, C, S)
            if not res:
                print 'Case #%d: IMPOSSIBLE' % t
            else:
                print 'Case #%d: %s' % (t, ' '.join(res))

if __name__ == '__main__':
    main()
