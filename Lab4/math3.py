from math import tan, pi
def area_of_polygon(n, l):
    S = n * (l**2) / (4 * tan(pi/n))
    return S

n = int(input())
l = int(input())
print(area_of_polygon(n, l))