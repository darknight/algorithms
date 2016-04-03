cin = []
while True:
    try:
        data = [int(x) for x in raw_input().split()]
        cin.append(data)
    except EOFError:
        break
tmp = []
for i in range(3):
    for j in range(3):
        if cin[i][j] != 0:
            tmp.append((i, j))
#print tmp
n = 0
base = [[8,1,6],[3,5,7],[4,9,2]]
res = ''
for k in range(8):
    if k % 2 == 0:
        base[0], base[2] = base[2], base[0]
    else:
        base[0][1], base[1][0] = base[1][0], base[0][1]
        base[0][2], base[2][0] = base[2][0], base[0][2]
        base[1][2], base[2][1] = base[2][1], base[1][2]
    #print base
    found = True
    for (i, j) in tmp:
        if cin[i][j] != base[i][j]:
            found = False
            break
    #print found
    if found:
        n += 1
        for i in range(3):
            if i > 0:
                res += '\n'
            res += ' '.join(str(base[i][j]) for j in range(3))
if n == 1:
    print res
else:
    print 'Too Many'
