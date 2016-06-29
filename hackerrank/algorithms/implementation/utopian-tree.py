T = int(raw_input().strip())

for _ in xrange(T):
    N = int(raw_input().strip())
    height = 1
    while N >= 2:
        height *= 2
        height += 1
        N -= 2
    if N == 1:
        height *= 2
    print height
