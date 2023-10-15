import math
def prime (lst):
    result = lst
    for i in range(2, max(lst) // 2 + 1):
        result = filter(lambda x: x == i or x % i, result)
    return list(result)
lst = [int(x) for x in input().split()]
print(prime(lst))