def div_by_three_four(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i