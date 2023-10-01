list = [int(x) for x in input().split()]
X = int(input())
index = 0
while index < len(list) and list[index] >= X:
    index += 1
print(index + 1)