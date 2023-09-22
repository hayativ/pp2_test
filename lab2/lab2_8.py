x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
d1 = (x1 == (x2 - 1) and y1 == (y2 - 1))
d2 = (x2 == (x1 - 1) and y1 == (y2 - 1))
d3 = (x1 == (x2 - 1) and y2 == (y1 - 1))
d4 = (x2 == (x1 - 1) and y2 == y1 - 1)
g1 = (x1 == (x2 - 1) and y1 == y2)
g2 = (x2 == (x1 - 1) and y1 == y2)
v1 = (x1 == x2 and y1 == y2 - 1)
v2 = (x1 == x2 and y2 == y1 - 1)
korol = g1 or g2 or v1 or v2 or d1 or d2 or d3 or d4
if korol == True:
    print("YES")
else:
    print("NO")