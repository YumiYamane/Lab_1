import re

txt = 'Abcde'
x = re.findall('[A-Z][a-z]+', txt)
print(x)