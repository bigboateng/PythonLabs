__author__ = 'Boateng'


def count_chars(s):
    """

    :param s:
    :return: a dictionary he dictionary's keys are the set of characters that occur in string s
    """
    s_dict = {}
    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    return s_dict


def derivative(f, x, eps=1e-6):
    """

    :param f: input function f(x)
    :param x: value to evaluate function at
    :return:
    """
    return (f(x + (eps/2)) - f(x - (eps/2)))/eps
