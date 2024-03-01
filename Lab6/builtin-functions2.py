def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

s = "Hello World!"
u, l = count_upper_lower(s)
print("Number of uppercase letters:", u)
print("Number of lowercase letters:", l)