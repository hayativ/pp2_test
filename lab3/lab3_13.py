list = [int(x) for x in input().split()]
cnt = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            cnt += 1
print(cnt)