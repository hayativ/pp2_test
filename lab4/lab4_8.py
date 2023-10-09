n = int(input())
set = set(range(1, n + 1))
result = set
while True:
    question = input()
    if question == 'HELP':
        break
    question = {int(x) for x in question.split()}
    if len(result & question) > len(result) / 2:
        print('YES')
        result &= question
        #resut = {r for r in result if r in question}
    else:
        print('NO')
        result &= set - question
        
for i in result:
    print(i, end = ' ')