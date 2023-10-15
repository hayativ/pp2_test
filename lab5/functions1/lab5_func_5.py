import itertools
def my_function(str):
    return itertools.permutations(str)
str = input()
str2 = my_function(str)
for t in str2:
    print(t)