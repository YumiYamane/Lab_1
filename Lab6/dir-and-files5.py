fruits = ['apple', 'banana', 'cherry', 'melon']
with open('textfile.txt', 'w') as file:
    for item in fruits:
        file.write(str(item)+'\n')