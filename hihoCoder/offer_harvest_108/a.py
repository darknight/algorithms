discount = {}
ml = []

while True:
    try:
        raw = raw_input()
        if len(raw) == 0:
            break
        N, C = raw.split()
        N, C = int(N), int(C)
        for _ in range(N):
            A, B = raw_input().split()
            A, B = int(A), int(B)
            discount[A] = B
            ml.append(A)
    except EOFError:
        break

# print ml
# print discount

if C >= ml[-1]:
    print discount[ml[-1]]
else:
    idx = 0
    while C >= ml[idx]:
        idx += 1
    X = discount[ml[idx-1]]
    Y = ml[idx] - C
    Z = discount[ml[idx]]
    print "%d %d %d" % (X, Y, Z)
