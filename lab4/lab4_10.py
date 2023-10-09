N, K = [int(x) for x in input().split()]
days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
ordinary_days = set(days)
for i in range(K):
    a, b = [int(x) for x in input().split()]
    max = (N - a) // b + 1
    ordinary_days -= {a + b*i for i in range(max)}
print(len(days) - len(ordinary_days))