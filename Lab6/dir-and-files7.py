with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile: 
    for line in firstfile:
        secondfile.write(line)