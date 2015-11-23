from math import pi, sqrt


def swing_time(L):
    """ this function computes and returns the time T in seconds needed for a pe
    ndulum of length L to compete a single oscillation"""
    g = 9.81
    return 2*pi*(sqrt(L/g))


def range_squared(n):
    """ this returns a if squared items with length n-1"""
    return [x**2 for x in range(n)]


def count(element, seq):
    """ This returns how often a givent element appears in a list"""
    appears = 0
    for el in seq:
        if el is element:
            appears += 1
    return appears
