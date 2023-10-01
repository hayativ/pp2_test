N = 8
list1 = []
list2 = []
for i in range(N):
    x, y = [int(k) for k in input().split()]
    list1.append(x)
    list2.append(y)
flag = True
for i in range(N):
    for j in range(i + 1, N):
        if list1[i] == list1[j] or list2[i] == list2[j] or abs(list1[i] - list1[j]) == abs(list2[i] - list2[j]):
            flag = False
if flag: print('NO')
else: print('YES')
