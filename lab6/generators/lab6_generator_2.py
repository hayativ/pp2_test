'''def even(n):
    a=1
    while a<n:
        yield a+1 
        a+=2
'''

n = int(input())
result = [x for x in range(n) if x % 2 == 0]
print(result)
'''for i in even(n):
    print(i)
'''