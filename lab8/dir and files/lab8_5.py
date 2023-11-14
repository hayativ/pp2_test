lst = [int(x) for x in input().split()]
with open('lab8_row.txt', 'w') as f:
    for l in lst:
        f.write(f"{l}\n")