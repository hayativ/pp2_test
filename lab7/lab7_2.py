import re
def my_func(string):
        pattern = '^ab{2,3}$'
        if re.search(pattern, string):
               return 'Match'
        else:
              return('No match')
with open('row.txt', 'r') as fp:
       text_list = fp.readlines()
for i in text_list:
       print(my_func(i))