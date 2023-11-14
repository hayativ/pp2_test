import string
letters = string.ascii_uppercase
for letter in letters:
    with open(letter+".txt",'w') as file:
        file.write("")