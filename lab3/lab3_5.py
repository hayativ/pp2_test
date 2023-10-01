list = [int(x) for x in input().split()]
cnt = 0
for i in range (1, len(list) - 1):
    if list[i] > list[i-1] and list[i] > list[i + 1]:
        cnt += 1
print(cnt)