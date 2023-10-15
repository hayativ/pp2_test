def isPalindrom(str):
    res = True
    for i in range(len(str)):
        if str[i] != str[len(str) - i - 1]:
            res = False
    return res
str = input()
str = str.lower().replace(" ", "")
if isPalindrom(str):
    print("YES")
else:
    print("NO")