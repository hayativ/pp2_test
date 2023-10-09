set = {int(x) for x in input().split()}
set2 = {int(x1) for x1 in input().split()}
set3 = {x for x in set if x in set2}
print(*sorted(set3))