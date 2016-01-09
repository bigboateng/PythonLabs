

def seperate(x, reverse=False):
    """
    param x      : list
    param reverse: 
    returns: tuple of two list x1, x2 such that:
            x1 = x[odd] 
            x2 = x[even] 
    """
    x1 = [x[i] for i in range(len(x)) if i % 2 != 0]
    x2 = [x[i] for i in range(len(x)) if i%2 == 0]
    if reverse:
        x2.reverse()
        x1.reverse()
        return x2, x1
    else:
        return x2, x1


def capitalise_names(name_list):
    """
    param name_list: list of names
    returns: every first letter in of item capitalized
    """
    return_names = []
    for name in name_list:
        first_letter = name[0].capitalize()
        nameAsList = list(name)
        nameAsList[0] = first_letter
        return_names.append("".join(nameAsList))
    return return_names

def capitalize_names_2(names):
    r = [name[0].capitalize()+"".join(list(name[1:])) for name in names]
    return r
        
def count(s, chars):
    """"
    param s    :string
    param chars:list of chars
    returns    :dict of num of occurences of chars in s
    """
    dictionary = {k:0 for k in chars}
    for char in s:
        if char in chars:
            dictionary[char] += 1
    return dictionary


def trap_area(xs, ys):
    """
    param xs: list of x positions
    param ys: y(x)
    returns : area under function f(x) using formula given
    """
    n = len(xs)
    a = 0.5*sum([(xs[i+1]-xs[i])*(ys[i+1]+ys[i]) for i in range(n-1)])
    return a

def intersection(line1, line2):
    """
    param line1: tuple(m1, c1)
    param line2: tuple(m2, c2)
    returns    : intersection of line1 and line2
    """
    m1, c1 = line1
    m2, c2 = line2
    x=(c2 - c1)/(m1 - m2)
    y = m1*x + c1
    return x,y

def change_unit(d, unit1, unit2):
    """
    param d    : float number to be converted
    param unit1: unit to be converted from
    param unit2: unit to be converted to
    returns    : param d converted from unit1 to unit2
    """
    units = {'meter':1, 'inch':0.0254, 'foot':0.3048}
    if units[unit1] > units[unit2]:
        return d*(units[unit1]/units[unit2])
    else:
        return d/(units[unit2]/units[unit1])

def logistic(N):
    """
    param N : list 
    returns : logistic map for N
    """
    prevY = 0.5
    logistic_map = [0.5]
    for _ in range(N):
        newY = ((11/3.0)*prevY)*(1 - prevY)
        logistic_map.append(newY)
        prevY = newY
    return logistic_map


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


def find_max():
    """
    returns: pos x of maximum of given function
    """
    from math import pi
    x = [0, pi/6, pi/3, pi/2, 2*pi/3, 5*pi/6, pi]
    y = [1, 1.15, 1.98, 14.134, 1.98, 1.15, 1]
    func = create_f(x, y)
    return max_f(func, pi/2)
    
