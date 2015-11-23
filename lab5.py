__author__ = 'Boateng'


def vector_product3(a, b):
    """

    :param a: [ax, ay, az]
    :param b: [bx, by, bz]
    :return: axb
    """
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def seq_mult_scalar(a, s):
    """

    :param a: scalar
    :param s: list
    :return: a * all items in a
    """
    return [x*s for x in a]


def powers(n, k):
    """

    :param n:
    :param k:
    :return: the list [1,n,n^2,n^3,...,n^k] where k is an integer
    """
    return [n ** i for i in range(k+1)]


def traffic_light(load):
    """

    :param load:
    :return: 'green' if load < 0.7 'amber' if >= 0.7 < 0.9 'red' if >= 0.9
    """
    if load < 0.7:
        return "green"
    if 0.7 >= load < 0.9:
        return "amber"
    if load >= 0.9:
        return "red"
