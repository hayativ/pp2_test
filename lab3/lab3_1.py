list = [int(x) for x in input().split()]
list2 = []
for i in range (len(list)):
    if i % 2 == 0:
        list2.append(list[i])
for i in range (len(list2)):
    print(list2[i], end = ' ')