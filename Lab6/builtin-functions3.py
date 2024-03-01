def is_palindrome(s):
    s = s.lower()
    return s == ''.join(reversed(s))

s = "Anna"
if is_palindrome(s):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")