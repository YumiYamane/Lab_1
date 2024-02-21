import re

txt = 'abc_def'
x = re.findall('[a-z]+_[a-z]+', txt)
print(x)