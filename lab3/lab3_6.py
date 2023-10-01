list = [int(x) for x in input().split()]
index =  0
max = list[0]
for i in range (len(list)):
    if list[i] > max:
        max = list[i]
        index = i
print(max, index)