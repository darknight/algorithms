T = int(raw_input().strip())
for t in range(T):
    N = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    #print arr
    new_arr = sorted(arr)
    for item in new_arr[:-3]:
        idx = arr.index(item)
        #print idx
        if idx % 2 != 0:
            arr.remove(item)
            temp = arr.pop(0)
            arr.insert(1, temp)
        else:
            arr.remove(item)
        #print arr
    assert(len(arr) == 3)
    a, b, c = arr
    #print a, b, c
    if a < b < c or b > a > c or a > c > b:
        print 'YES'
    else:
        print 'NO'