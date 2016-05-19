import math

def area_triangle(a, b, c):
    return  math.sqrt((a + b - c) * (a - b + c) * (b - a + c) *(a + b + c)) / 4


print area_triangle(5,5,6)
