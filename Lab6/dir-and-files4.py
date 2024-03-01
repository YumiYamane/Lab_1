with open("textfile.txt", 'r') as file:
    lines = len(file.readlines())
    print("Number of lines:", lines)