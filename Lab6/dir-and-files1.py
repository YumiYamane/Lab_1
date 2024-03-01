import os

path = '/Users/yumi/PP2/Lab6'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files:")
print([ name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name)) ])
print("All directories and files:")
print([ name for name in os.listdir(path)])