def unique(list):
    unique_list = []
    for l in list :
        if l not in unique_list:
            unique_list.append(l)
    return unique_list
list = [int(x) for x in input().split()]
print(unique(list))
