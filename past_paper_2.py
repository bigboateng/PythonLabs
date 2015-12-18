def mult3vec(c, v):
    """
    param c: scalar
    param v: list
    returns: c * every element in v
    """
    return [c*i for i in v]

def multvec(c, v):
    """
    param c: scalar
    param v: list
    returns: c * every element in v
    """
    return [c*i for i in v]

def convert_time(t):
    """
    param t: duration in t minutes
    returns: tuple(days, hours, minutes) 
    """
    days = int(t / 1440)
    hours = int((t - days*1440)/60)
    mins = t - (days*1440 + hours*60)
    return days, hours, mins

def nearest(xs, a):
    """
    param xs: list of numbers
    param  a: element
    returns : element of xs that is nearest to a
    """
    nearest = xs[0]
    for i in xs:
        if abs(i-a) < nearest:
            nearest = i
    return nearest

def derivative(f, xs):
    """
    param f : function
    param xs: list
    returns : the approximation of the derivate of x at xs
    """
    dx = 1e-6
    return [(f(x + dx) - f(x))/ dx for x in xs]


def read(filename):
    """
    param filename: file to read data from
    returns       : tuple of x and y data in file
    """
    x, y = [], []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            if not line.count('#') > 0:
                items = line.split(',')
                x1 = items[0]
                y1 = items[1]
                x.append(float(x1))
                y.append(float(y1))
        return x,y

def isfib(F):
    """
    param F: list of numbers
    returns: true if F is a fib sequence or false otherwise
    """
    print("Length of f is %d" %len(F))
    if len(F) > 2:
        if F[len(F)-1] is (F[len(F)-2] + F[len(F)-3]):
            print(F)
            isfib(F[:-1])
        else:
            return False
    else:
        return True
        print("True")

def f_from_data(xs, ys):
    """
    param xs: x positions in list
    param ys: list of y(x) where x is in xs
    returns : f(x) where f uses linear interpoltation to find
              an estimate for y(x)
    """
    import scipy.interpolate as sc
    return (lambda x: float(sc.spline(xk=xs,yk=ys,xnew=x, order=1)))
    
