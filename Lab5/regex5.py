import re

txt = 'abcdefb'
x = re.search('a.*b$', txt)
if x:
    print('Found a match!') 
else:
    print('Not matched!') 