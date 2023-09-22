x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx1 = abs(x2 - x1)
dy1 = abs(y2 - y1)
slon = dx1 == dy1
if slon == True:
    print("YES")
else:
    print("NO")