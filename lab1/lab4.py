n = int(input())
hours = n // 60 % 24
minutes = n % 60 

print(hours // 10, hours % 10, ":", minutes // 10, minutes % 10, sep= "")