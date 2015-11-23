
def eval_f(f, xs):
    """

    :param f:
    :param xs:
    :return: list with f(i) for i in xs
    """
    return [f(x) for x in xs]


def sum_f(f, xs):
    """

    :param f:
    :param xs:
    :return: sum of f(i) for i in xs
    """
    return sum([f(i) for i in xs])


def box_volume_UPS(a=13, b=11, c=2):
    """

    :param a:
    :param b:
    :param c:
    :return: volume of box with edges a, b, c
    """
    return a * b * c
