import math


def seconds2days(seconds):
    """this function takes in a parameter in seconds
    and it returns the corresponding number of days"""
    sec_in_days = 86400.0
    return seconds/sec_in_days


def box_surface(a, b, c):
    """This function returns the surface area of a box with edges a b and c"""
    return (2*a*b) + (2*a*c) + (2*b*c)


def triangle_area(a, b, c):
    """This function computes and returns the area A of a triangle with edge -
    length a, b, c"""
    s = (a + b + c)/2
    a = math.sqrt(s*(s - a)*(s - b)*(s - c))
    return a
