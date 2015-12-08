from __future__ import division
from math import sqrt, pow


def trapez(f, a, b, n):
    """

    :param f:
    :param a:
    :param b:
    :param n:
    :return: composite trapezoidal integration rule applied on f between limits a and b
    """
    a, b = float(a), float(b)
    h = (b - a)/float(n)
    big_summation = sum([f(a + i*h) for i in range(1, n)])
    return (h/2.0)*(f(a) + f(b) + 2.0*big_summation)


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
