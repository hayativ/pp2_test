import os
def my_func(str):
    if os.path.exists(str):
        if os.path.isfile(str):
            if os.access(str, os.R_OK | os.W_OK):
                os.remove(str)
                print("File has been deleted")
            else:
                print("No access to delete file")
        else:
            print("Path doesn't point to a regular file")
    else:
        print("File doesn't exist")

path = input()
my_func(path)