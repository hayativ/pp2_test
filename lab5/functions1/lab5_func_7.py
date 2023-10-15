def has_33(list):
    flag = False
    for i in list:
        if flag == True:
            if i == 3:
                return True
            else: flag = False
        if i == 3:
            flag = True
    return False
list = [int(x) for x in input().split()]
print(has_33(list))