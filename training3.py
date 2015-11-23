import math


def degree(x):
    """ This function will return x converted from radians to degrees """
    return x*(360/(2*math.pi))


def min_max(xs):
    """This function will return the max in min numbers in list xs"""
    if len(xs) is not 0:
        x_min = xs[1]
        x_max = xs[1]
        for x in xs:
            if x < x_min:
                x_min = x
            elif x > x_max:
                x_max = x
        return x_min, x_max
    else:
        return 0, 0


def geometric_mean(xs):
    """This function will return the geometric mean of list xs"""
    length = len(xs)
    products = 1
    for l in xs:
        products *= l
    return products ** (1.0/length)
