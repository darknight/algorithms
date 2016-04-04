# TODO: Time Limit Exceeded, try to rewrite using c#
while True:
    try:
        N, Q = raw_input().split()
        N, Q = int(N), int(Q)
        P = [int(i) for i in raw_input().split()]
    except EOFError:
        break

P.insert(0, -1)

def insert(q, i, v):
    '''
    q: queue of length k
    i: index, 1 <= i <= k
    v: value
    '''
    q[i] = v
    j = i / 2
    while i > 1 and q[i] > q[j]:
        q[i], q[j] = q[j], q[i]
        i = j
        j = i / 2

def delete_max(q, k):
    '''
    q: queue of length k
    k: queue length
    '''
    res = q[1]
    q[1] = q[k]
    n = k - 1
    i = 1
    j = 2 * i
    while j <= n:
        if j+1 <= n and q[j+1] > q[j]:
            j += 1
        if q[i] >= q[j]:
            break
        q[i], q[j] = q[j], q[i]
        i = j
        j = 2 * i
    return res

min_k = N + 1
low = 1
high = N
q = [0] * (N+1)

while low <= high:
    k = (low + high) / 2
    for i in range(1, k+1):
        insert(q, i, P[i])
    sp = 0
    n = 0
    for j in range(k+1, N+1):
        if sp > Q:
            break
        v = delete_max(q, k) 
        n += 1
        sp += v * n
        insert(q, k, P[j])
    for j in range(k):
        if sp > Q:
            break
        v = delete_max(q, k-j)
        n += 1
        sp += v * n
    if sp <= Q:
        min_k = min(min_k, k)
        high = k-1
    else:
        low = k+1

if min_k <= N:
    print min_k
else:
    print -1
