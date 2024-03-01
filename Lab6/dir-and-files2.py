import os

print('Exist:', os.access('/Users/yumi/PP2/Lab6/dir-and-files1.py', os.F_OK))
print('Readable:', os.access('/Users/yumi/PP2/Lab6/dir-and-files1.py', os.R_OK))
print('Writable:', os.access('/Users/yumi/PP2/Lab6/dir-and-files1.py', os.W_OK))
print('Executable:', os.access('/Users/yumi/PP2/Lab6/dir-and-files1.py', os.X_OK))