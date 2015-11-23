__author__ = 'Boateng'


def positive_places(f, xs):
    """

    :param f:
    :param xs:
    :return: list whos element x of xs for which f(x) < 0
    """
    return [x for x in xs if f(x) > 0]


def eval_f_0123(f):
    """

    :param f:
    :return: return f(0), f(1), f(2), f(3)
    """
    return [f(x) for x in range(4)]
