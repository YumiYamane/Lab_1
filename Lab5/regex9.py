import re

txt = 'AbcDef'
x = re.sub('([a-z])([A-Z])', r'\1 \2', txt)
print(x)