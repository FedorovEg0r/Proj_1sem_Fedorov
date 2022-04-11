import math

default_radius = 5


def circle_perimeter(r=default_radius):
    return math.pi * r * 2


def circle_area(r=default_radius):
    return math.pi * (r ** 2)
