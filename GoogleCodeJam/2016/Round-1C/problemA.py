def solve(total, data):
    res = []
    while data:
        data.sort(key=lambda x: x[1], reverse=True)
        party_num = len(data)
        #print data
        if party_num >= 2:
            p1, n1 = data[0]
            p2, n2 = data[1]
            if n1 - n2 >= 1:
                res.append(p1*2)
                n1 -= 2
            else:
                res.append(p1+p2)
                n1 -= 1
                n2 -= 1
            if n1 == 0:
                data.pop(0)
            else:
                data[0][1] = n1
            if n2 == 0:
                data.pop(0)
            else:
                data[1][1] = n2
        else:
            p1, n1 = data[0]
            assert(n1 == 1)
            p1, n1 = data[0]
            res.append(p1)
            n1 -= 1
            data.pop(0)

    # so, AB C is invalid, because C is dominated,
    # that's why I've got 3 WAs, holy crap...
    # you should swap the last two items
    if len(res[-1]) == 1:
        res[-1], res[-2] = res[-2], res[-1]

    return ' '.join(res)

def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        raw = input().split()
        data = []
        total = 0
        for j in range(N):
            party = int(raw[j])
            total += party
            data.append([chr(ord('A')+j), party])
        res = solve(total, data)
        print('Case #%d: %s' % (int(i), res))

if __name__ == '__main__':
    main()