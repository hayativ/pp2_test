n = int(input())
set = set(range(1, n + 1))
result = set
while True:
    question = input()
    if question == 'HELP':
        break
    question = {int(x) for x in question.split()}
    answer = input()
    if answer == 'YES':
        result &= question
    else:
        result &= set - question
for i in result:
    print(i, end = ' ')