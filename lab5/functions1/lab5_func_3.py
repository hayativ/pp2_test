def solve(numheads, numlegs):
    #heads = r + ch 
    #legs = 4r + 2ch
    rabbits = (numlegs - 2 *numheads)//2
    chicken = numheads - rabbits
    print(rabbits, chicken)
# numheads = 35
# numlegs = 94
numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)