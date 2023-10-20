def squares(a,b):
    while a<=b:
        yield a*a
        a+=1

a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)