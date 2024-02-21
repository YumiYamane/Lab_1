import re

txt = 'a b,c.'
x = re.sub("[ ,.]", ":", txt)
print(x)