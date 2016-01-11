#important stuff
def create_f(xn, fn):
    """
    param xn: values of x
    paran fn: values of f(x)
    returns : function f(x) that interpolates the value of f for any position x
    """
    import scipy.interpolate as s
    import numpy as np
    return (lambda x: np.array(s.spline(xn, fn, x, 2)))
        
def max_f(f, x0):
    """
    param f : function f(x)
    param x0: intial value for downhill algorithm
    """
    import scipy.optimize as sc
    return sc.fmin((lambda x: -f(x)), x0)

def interp_V(In, Vn):
    """
    param In: list of currents
    param Vn: list of voltages
    returns : f(i) where f is a function of currents
    """
    from scipy.interpolate import interp1d
    import numpy as np
    f = interp1d(In, Vn)
    return (lambda x: np.array(f(x)))


def root(xs, ys):
    """
    param xs: list of x positions
    param ys: list of f(x) positions
    returns : value x for which y(x) is zero
    """
    from scipy.optimize import brentq
    func = f_from_data(xs, ys)
    return brentq(func, xs[0], xs[-1])



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

def myplot():
    """
    :return: plots a graph
    """
    import matplotlib.pyplot as plt
    x, y = create_plot_data(f1, -2, 2, 1001)
    x1, y1 = create_plot_data(f2, -2, 2, 1001)
    plt.title("Graph")
    l1, = plt.plot(x, y, linewidth=2.0)
    l2, = plt.plot(x1, y1, linewidth=3.0)
    plt.legend((l1, l2), ('F1', 'F2'), loc='upper right', shadow=True)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.savefig("plot.png")
    plt.savefig("plot.pdf")
    plt.show()
