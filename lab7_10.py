import re
def my_func(string):
    result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', result).lower()
with open('row.txt', 'r') as fp:
       text_list = fp.readlines()
for i in text_list:
       print(my_func(i))