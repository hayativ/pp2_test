list = [int(x) for x in input().split()]
list2 = []
for i in range(len(list)):
    for j in range(len(list)):
        if i != j and list[i] == list[j]:
            break
    else:
        list2.append(list[i])
for i in range (len(list2)):
    print(list2[i], end = ' ')