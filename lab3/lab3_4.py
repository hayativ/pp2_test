list = [int(x) for x in input().split()]
list2 = []
for i in range (1, len(list)):
    if list[i-1] * list[i] > 0:
        print(list[i-1], list[i])
        break