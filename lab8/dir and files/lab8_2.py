import os
def my_func(str):
    if os.path.exists(str):
        print("Path exists")
        readability = os.access(str, os.R_OK)
        writability = os.access(str, os.W_OK)
        executability = os.access(str, os.X_OK)
        print(f"Readability: {'Yes' if readability else 'No'}")
        print(f"Writability: {'Yes' if writability else 'No'}")
        print(f"Executability: {'Yes' if executability else 'No'}")
    else:
        print("Path doesn't exist")

path = input()
my_func(path)