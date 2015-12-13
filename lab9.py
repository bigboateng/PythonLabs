from __future__ import division
from math import sqrt, pow


def trapez(f, a, b, n):
    """Approximates and returns the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    aprime = float(a)
    bprime = float(b)
    nprime = float(n)
    h = (bprime - aprime) / nprime
    s = f(aprime) + f(bprime)
    for i in range(1, n):
        s += 2 * f(aprime + i * h)
    return s * h / 2.0


def xint(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return (pow(b, 3.0) / 3.0) - (pow(a, 3.0) / 3.0)


def finderror(n):
    """

    :return: uses the trapez() function to find the error of the trapezoidal integral approximation
    """
    num_val = trapez(lambda x: x**2.0, -1.0, 2.0, n)
    a = (3.0 - num_val)
    return a


def using_quad():
    """

    :return: integral of x^2 from -1 to 2 using scipy.integrate
    """
    import scipy.integrate as i
    return i.quad(lambda x: x**2, -1, 2)


def std_dev(x):
    """

    :param x: list of floating point numbers
    :return: standard deviation of the list of numbers
    """
    n = float(len(x))
    mu = (1/n)*sum(x)
    deviation = sqrt((1 / (n - 1) * sum([pow((i - mu), 2) for i in x])))
    return deviation

if __name__ == '__main__':
    print(finderror(5))
    print(using_quad())
    print(std_dev([1.0, 1.0]))
    print(std_dev([1.0, 2.0]))
