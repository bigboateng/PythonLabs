__author__ = 'Boateng'
import math
def f1(x):
    """

    :param x:
    :return: cos(2*pi*x)exp(-x^2)
    """
    return math.cos(2*math.pi*x)*math.exp(-math.pow(x, 2))

def f2(x):
    """

    :param x:
    :return: log(x + 2.1)
    """
    return math.log(x + 2.1, 10)

def positive_places(f, xs):
    """

    :param f:
    :param xs:
    :return: values for which f(x) > 0
    """
    return [f(x) for x in xs if f(x) > 0]

def reverse_dic(d):
    """

    :param d:
    :return:
    """
    return {v : k for k, v in d.items()}

if __name__ == '__main__':
    d = {1:2,2:3,3:4}
    print(reverse_dic(d))
