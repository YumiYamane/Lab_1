import os

print("Test a path exists or not:")
path = '/Users/yumi/PP2/Lab6/dir-and-files3.py'
print(os.path.exists(path))

if os.path.exists(path):
    print("File name of the path:")
    print(os.path.basename(path))

    print("Directory name of the path:")
    print(os.path.dirname(path))