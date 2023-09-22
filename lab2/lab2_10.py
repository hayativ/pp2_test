x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ladya = x1 == x2 or y1 == y2
dx1 = abs(x2 - x1)
dy1 = abs(y2 - y1)
slon = dx1 == dy1
ferz = (ladya == True) or (slon == True)
if ferz == True:
    print("YES")
else:
    print("NO")