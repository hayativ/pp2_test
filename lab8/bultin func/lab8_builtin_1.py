import math
def my_func(lst):
    result = math.prod(lst)
    return result
lst = [int(x) for x in input().split()]
answer = my_func(lst)
print(answer)