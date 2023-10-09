list = [{input() for j in range(int(input()))} for i in range(int(input()))]
result1, result2 = set.intersection(*list), set.union(*list)
print(len(result1), *sorted(result1), sep='\n')
print(len(result2), *sorted(result2), sep='\n')