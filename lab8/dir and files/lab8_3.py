import os
def my_func(str):
    if os.path.exists(str):
        print("Path exists")
        filename = os.path.basename(str)
        dir_portion = os.path.dirname(str)

        print(f"Filename: {filename}")
        print(f"Directory portion: {dir_portion}")
    else:
        print("Path doesn't exist")

path = input()
my_func(path)