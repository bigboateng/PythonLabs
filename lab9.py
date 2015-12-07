from __future__ import division
from math import sqrt, pow


def std_dev(x):
    """

    :param x: list of floating point numbers
    :return: standard deviation of the list of numbers
    """
    n = float(len(x))
    mu = (1//n)*sum(x)
    deviation = sqrt((1 // (n - 1)) * sum([pow((i - mu), 2) for i in x]))
    return deviation


if __name__ == '__main__':
    print(std_dev([1.0, 1.0]))