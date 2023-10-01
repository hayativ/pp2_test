N, K = [int(x) for x in input().split()]
result = []
for i in range(N):
    result.append('I')
for i in range(K):
    l1, r1 = [int(x) for x in input().split()]
    for j in range(l1 - 1, r1):
        result[j] = '.'
for i in range (len(result)):
    print(result[i], end = '')