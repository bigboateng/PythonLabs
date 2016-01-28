__author__ = 'Boateng'
"""
Theory of Bezier curves
"""
import numpy as np
import pylab

def bez_linear():
    """
    :return: a bezier curve between p0 and p1, this is a straight line
    B(t) = (1-t)P0 + tP1
    0 < t < 1
    """
    #control points
    a = np.array([[0,1],[1,10]])
    # generate 100 points between 0 and 1
    t = np.linspace(0, 1, 101)
    #print(t)
    # 2d array that will store the x,y coordinates of every point t,B(t)
    t_points = np.zeros([101, 2])
    for i in range(101):
        t_points[i] = (1-t[i])*a[0] + t[i]*a[1]
    #print(lin_bez)
    #print("len of x is %d" %len(lin_bez[:,0]))
    #print("len of y is %d" %len(lin_bez[:, 1]))
    pylab.plot(t_points[:,0],t_points[:,1])
    pylab.show()

def bez_quadra():
    """

    :return: quadratic bezier curve
    B(t) = (1-t)^2P0 + 2(1-t)tP1 + t^2P2
    """
    # control points
    a = np.array([[1,10] , [2,5] , [7.6863,3.9216]])
    # generate 100 values of t that lie on B(t)
    t = np.linspace(0,1,101)
    # 2d array to store x,y coordinates of every point t, B(t)
    t_points = np.zeros([101,2])
    for i in range(101):
        t_points[i] = ((1-t[i])**2)*a[0] + 2*(1-t[i])*t[i]*a[1] + t[i]**2*a[2]
    pylab.plot(t_points[:,0], t_points[:,1], 'ko')
    #pylab.show()

def choose(n, i):
    if 0 <= i <= n:
        p = 1
        for t in range(0, min(i, n-i), 1):
            p = (p * (n - t) ) // (t + 1)
        return p
    else:
        return 0


def bezier(points):
    """

    :param points: boundary for cubic bezier curve
    :return: points for th cubic bezier curve bounded by the control points
    """
    t = np.linspace(0, 1, 101)
    t_values = np.zeros([101,2])
    n = len(points)-1
    for i in range(101):
        t_values[i] = sum([choose(n, x)*((1-t[i])**(n-x))*(t[i]**x)*points[x] for x in range(n+1)])
    pylab.plot(t_values[:,0], t_values[:,1])
    pylab.show()


def rational_bezier(points, weights):
    """

    :param points:
    :param weights:
    :return: cubic bezier with n control points and n weights
    """
    t = np.linspace(0,1,101)
    t_values = np.zeros([101,2])
    n = len(points) - 1
    for i in range(101):
        top = sum([choose(n, x)*((1-t[i])**(n-x))*(t[i]**x)*points[x]*weights[x] for x in range(n+1)])
        bot = sum([choose(n, x)*((1-t[i])**(n-x))*(t[i]**x)*weights[x] for x in range(n+1)])
        t_values[i] = (top/bot)
    print(t_values)
    pylab.plot(t_values[:,0], t_values[:,1])
    pylab.show()

if __name__ == '__main__':
    #bez_linear(1,1)
    #bez_quadra()
    #print(choose(5,2))
    #pylab.plot(1,10, 'ro')
    #pylab.plot(2,5, 'ro')
    #pylab.plot(7.6863,3.9216, 'ro')
    #bezier(np.array([[1,10] , [2,5] , [7.6863,3.9216]]))
    points = np.array([[1,10] , [2,5] , [7.6863,3.9216]])
    rational_bezier(points, [1,10,1])