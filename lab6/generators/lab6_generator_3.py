n = int(input())
result = [x for x in range(n) if x % 3 == 0 or x % 4 == 0]
print(result)