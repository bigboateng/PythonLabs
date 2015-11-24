__author__ = 'Boateng'
import numpy as np
import matplotlib.pyplot as plt
from math import cos, log, exp, pi
from scipy import optimize

f1 = lambda x: cos(2*pi*x)*exp(-x * x)
f2 = lambda x: log(x + 2.1)
f3 = lambda x: exp(x)
f4 = lambda x: cos(2*pi*x)*exp(-x * x) - log(x + 2.1)

def create_plot_data(f, xmin, xmax, n):
    """

    :param f:
    :param xmin:
    :param xmax:
    :param n:
    :return: tuple(xs,ys) where xs and ys are two sequences, each containing n numbers
    """
    xs = [(xmin + i * (xmax - xmin)/n - 1) for i in range(n)]
    ys = [f(i) for i in xs]
    return xs, ys

def myplot():
    """

    :return: plots a graph
    """
    x, y = create_plot_data(f1, -2, 2, 1001)
    x1, y1 = create_plot_data(f3, -2, 2, 1001)
    plt.title("Damped Oscillations... kinda")
    l1, = plt.plot(x, y, linewidth=2.0)
    l2, = plt.plot(x1, y1,linewidth=3.0)
    plt.legend((l1, l2), ('Oscillation', 'Exponential'), loc ='upper right', shadow = True)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig("plot.png")
    plt.savefig("plot.pdf")
    plt.show()


def find_cross():
    """

    :return: where f1 crosses f2
    """
    return optimize.brentq(f4, 0, 200)





if __name__ == '__main__':
    # print(create_plot_data(f1, -2, 2, 1001))
    myplot()
    print(find_cross())
