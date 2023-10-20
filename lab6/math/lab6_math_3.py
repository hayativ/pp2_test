from math import tan, pi
sides = int(input())
length = float(input())
result = sides * (length ** 2) // (4 * tan(pi/sides))
print(result)
