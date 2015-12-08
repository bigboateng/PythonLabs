import numpy as np


def model(t, Ti, Ta, c):
    """
    :return: T(t) = (Ti - Ta)exp(-t/c) + Ta
    """
    return (Ti - Ta)*np.exp(-t/c) + Ta

def read2coldata(filename):
    """

    :param filename: name of input file
    :return: tuple of numpy array x,y where x is 1st col data and y is y col data
    """
    f = open(filename, 'r').read().split('\n')
    return np.array([float(x.split(" ")[0]) for x in f]), np.array([float(x.split(" ")[1]) for x in f])

if __name__ == '__main__':
    print(read2coldata('test_data.txt'))
