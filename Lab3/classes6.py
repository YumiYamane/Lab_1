def is_prime(n):
    if n <= 1:
        return False    
    if n == 2 or n == 3:
        return True    
    for i in range(2, n):
        if n % i == 0:
            return False        
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = list(filter(lambda x: is_prime(x), numbers))
print(prime)