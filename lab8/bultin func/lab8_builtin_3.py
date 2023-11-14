def my_func(str):
    str = str.lower()
    str = ''.join(s for s in str if s.isalnum())
    return str == ''.join(reversed(str))
str = input()
print(my_func(str))