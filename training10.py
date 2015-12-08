import numpy as np


def model(t, Ti, Ta, c):
    """
    :return: T(t) = (Ti - Ta)exp(-t/c) + Ta
    """
    return (Ti - Ta)*np.exp(-t/c) + Ta
