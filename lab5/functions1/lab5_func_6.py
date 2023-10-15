def reverse(str):
    str = str.split()
    str.reverse()
    return ' '.join(str)
str = input()
print(reverse(str))