from math import pi
def degree_to_rad(degree):
    rad = degree*(pi/180)
    return rad

degree = int(input())
print(degree_to_rad(degree))