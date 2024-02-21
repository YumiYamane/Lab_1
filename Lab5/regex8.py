import re

txt = 'AbcDef'
x = re.findall('[A-Z][a-z]*', txt)
print(x)