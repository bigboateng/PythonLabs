#training 10
import numpy as np


def model(t, Ti, Ta, c):
    """

    :param t:
    :param Ti:
    :param Ta:
    :param c:
    :return:
    """
    Ti = int(Ti)
    Ta = float(Ta)
    c = int(c)
    if type(t) != float or type(t) != int:
        return (Ti - Ta)*np.exp(-t/c) + Ta
    else:
        return np.array((Ti - Ta)*np.exp(-t/c) + Ta)
