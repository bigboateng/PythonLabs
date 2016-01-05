import numpy as np
from scipy.optimize import curve_fit
import pylab


def model2(t, Ti, Ta, c):
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


def model(t, Ti, Ta, c):
    """
    :param t:
    :param Ti:
    :param Ta:
    :param c:
    :return:
    """
    return np.array((Ti - Ta)*np.exp(-t/c) + Ta)


def read2coldata(filename):
    """
    :param filename: name of input file
    :return: tuple of numpy array x,y
    """
    f = open(filename, 'r').read().split('\n')
    x1 = [float(a.split()[0]) for a in f]
    x2 = [float(a.split()[1]) for a in f]
    return np.array(x1), np.array(x2)


def extract_parameters(ts, Ts):
    """
    ts: numpy array of time values
    Ts: temperature values
    returns:  estimate of model parameters Ti, Ta, c (Tuple)
    """
    parameters, cov_matrix = curve_fit(model, ts, Ts, (100, 20, 200))
    return tuple(parameters)


def plot(ts, Ts, Ti, Ta, c):
    """

    param ts: data for time (ts)
    param Ts:  data for temperature (Ts)
    param Ti: model parameter for Initial Temperature
    param Ta: model paramter for Ambient Temperature
    param  c: model parameter c for the constant
    """
    pylab.plot(ts, Ts, 'o', label='data')
    fTs = model(ts, Ti, Ta, c)
    pylab.plot(ts, fTs, label='fitted')
    pylab.legend()
    pylab.savefig('testcompare.pdf')
    pylab.show()


def sixty_degree_time(Ti, Ta, c):
    """
    param Ti: Initial T
    param Ta: final T
    param c: constant
    """
    from math import log
    t = -c*log((60.0 - Ta)/(Ti - Ta))
    return t


if __name__ == '__main__':
    a, b = read2coldata('test_data.txt')
    c, d, e = extract_parameters(a, b)
    print(extract_parameters(a, b))
    plot(a, b, c, d, e)
    waittime = sixty_degree_time(c, d, e)
    print("60 degress at %s seconds = %f minutes" % (waittime, waittime / 60.))
