def my_func(result):
    result = all(result)
    return result
lst = []
while True:
    x = int(input())
    if x > 1:
        break
    lst.append(x)
result = tuple(lst)
print(my_func(result))