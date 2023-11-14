import os
path = input()
print("Directories: ")
print([dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))])
print("Files and all directories: ")
print([file_dir for file_dir in os.listdir(path)])
print("Files: ")
print([file for file in os.listdir(path) if not os.path.isdir(os.path.join(path, file))])