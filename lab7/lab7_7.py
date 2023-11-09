import re
def my_func(string):
    return ''.join(x.capitalize() or '_' for x in string.split('_'))
with open('row.txt', 'r') as fp:
       text_list = fp.readlines()
for i in text_list:
       print(my_func(i))