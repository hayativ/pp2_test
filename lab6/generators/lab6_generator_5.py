def generator(x, y):
    while y<=x:
        yield x
        x-=1

n = int(input())
for i in generator(n, 0):
    print(i)