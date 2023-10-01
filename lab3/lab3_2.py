list = [int(x) for x in input().split()]
list2 = [x for x in list if x % 2 == 0]
for i in range (len(list2)):
    print(list2[i], end = ' ')