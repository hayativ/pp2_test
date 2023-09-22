x = int(input())
y = int(input())
z = int(input())
cnt = 0
if x == y == z:
    print(3)
elif x == y or x == z or y == z:
    print(2)
else:
    print(0)
