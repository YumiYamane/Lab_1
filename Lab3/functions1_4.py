def is_prime(n):
    if n <= 1:
        return False    
    if n == 2 or n == 3:
        return True    
    for i in range(2, n):
        if n % i == 0:
            return False        
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))