def gensquares(N):
    for i in range(N):
        yield i**2
    
g = gensquares(5)
print(next(g))