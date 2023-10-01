list = [int(x) for x in input().split()]
cnt = 0
tmp = list[0]
for i in range (len(list)):
    if list[i] == tmp:continue
    else:
        tmp = list[i]
        cnt+=1
print(cnt + 1)