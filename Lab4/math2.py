def area_of_trapezoid(h, b1, b2):
    S = (b1+b2)/2 * h
    return S

h = int(input())
b1 = int(input())
b2 = int(input())
print(area_of_trapezoid(h, b1, b2))