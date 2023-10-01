list = [int(x) for x in input().split()]
index_min = 0
index_max = 0
for i in range(1, len(list)):
    if list[i] > list[index_max]:
        index_max = i
    if list[i] < list[index_min]:
        index_min = i
list[index_min], list[index_max] = list[index_max], list[index_min]
for i in range (len(list)):
    print(list[i], end = ' ')