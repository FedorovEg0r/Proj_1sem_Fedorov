import math

a = 7
b = 2
c = 8


def triangle_perimeter(l1=a, l2=b, l3=c):
    return l1 + l2 + l3


def triangle_area(l1=a, l2=b, l3=c):
    p = (l1 + l2 + l3)/2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
