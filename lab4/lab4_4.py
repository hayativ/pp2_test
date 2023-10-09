list = [int(x) for x in input().split()]
set = set()
for l in list:
    if l in set:
        print('YES')
    else:
        print('NO')
        set.add(l)