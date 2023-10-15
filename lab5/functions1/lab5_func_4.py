def filter_prime(x):
    if x == 1:
        return 0
    elif x == 2 or x == 3:
        return 1
    else:
        for i in range(2, x//2 + 1):
            if x % i == 0:
                return 0
            return 1
list = [int(x) for x in input().split()]
list = [x for x in list if filter_prime(x) == 1]
print(list)
