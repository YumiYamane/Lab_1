import re

txt = 'abbb'
x = re.search('ab{2,3}', txt)
if x:
    print('Found a match!') 
else:
    print('Not matched!') 