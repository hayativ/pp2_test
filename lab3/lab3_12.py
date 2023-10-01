list = [int(x) for x in input().split()]
k, C = [int(y) for y in input().split()]
list.append(0)
for i in range(len(list) - 1, k, -1):
    list[i] = list[i - 1]
list[k] = C
for i in range (len(list)):
    print(list[i], end = ' ')