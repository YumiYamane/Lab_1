import re

txt = 'AbcDef'
x = re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).lower()
print(x)