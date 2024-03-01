import os

if os.access("/Users/yumi/PP2/Lab6/second.txt", os.F_OK):
    os.remove("second.txt")