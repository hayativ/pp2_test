list = [int(x) for x in input().split()]
list2 = []
for i in range (len(list)):
    if i == 0:
        continue
    elif list[i] > list[i-1]:
        list2.append(list[i])
for i in range (len(list2)):
    print(list2[i], end = ' ')