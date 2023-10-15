import random
res = False
cnt = 0
x = random.randint(1, 20)
print("Hello! What is your name?")
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
while(res == False):
    cnt += 1
    number = int(input())
    if number < x:
        print("Your guess is too low.\nTake a guess.")
    elif number > x:
        print("Your guess is too high.\nTake a guess.")
    else:
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        res = True