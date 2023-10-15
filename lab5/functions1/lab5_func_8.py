def spy_game(list):
    flag1 = False
    flag2 = False
    for i in list:
        if flag2 == True:
            if i == 7:
                return True
            else: flag2, flag1 = False, False
        if flag1 == True:
            if i == 0:
                flag2 = True
            else: flag1 = False
        if i == 0:
            flag1 = True
    return False
list = [int(x) for x in input().split()]
print(spy_game(list))