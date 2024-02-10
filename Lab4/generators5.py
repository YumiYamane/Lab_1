def numbers(n):
    while n >= 0:
        yield n
        n -= 1 

for i in numbers(10):
    print(i)