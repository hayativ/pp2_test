with open('lab8_row.txt','r') as f1, open('lab8_copy.txt','w') as f2:  
    for line in f1:  
             f2.write(line)