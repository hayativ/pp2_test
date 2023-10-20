'''def squares(x,y):
    while x<=y:
        yield x*x
        x+=1
'''

n = int(input())
result = [x*x for x in range(1, n + 1)]
print(result)
'''for i in squares(1, n):
    print(i)
'''