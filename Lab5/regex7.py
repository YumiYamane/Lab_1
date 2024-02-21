import re

txt = 'abc_def'
x = ''.join(i.capitalize() or '_' for i in txt.split('_'))
print(x)