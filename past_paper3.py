def average_age(people):
    """
    param people: list of tuples (name, age)
    returns     : return average age of people
    """
    return sum(p[1] for p in people) / len(people)

def rectangle(p1, p2):
    """
    param p1: tuple of points
    param p2: tuple of points 
    returns : dictionary with keys area, sc, y
    """
    dx = (p2[0] - p1[0])
    dy = (p2[1] - p1[1])
    area = dx*dy
    xc = p1[0] + dx/2
    yc = p1[1] + dy/2
    return {'area':area, 'xc':xc, 'yc':yc}

def word_count(s):
    """
    param s: words
    returns: number of words in string
    """
    return len(s.split(" "))


def long_word(s):
    """
    param s: sentence
    returns: longest word in list
    """
    wordsAsList = s.split(' ')
    longestWord = wordsAsList[0]    
    for word in wordsAsList:
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord

def shift(a):
    """
    param a: list
    returns: list contsains same elements as a
             but positions have been shifted by 1 
    """
    return [a[-1]]+ [a[i] for i in range(len(a)-1)]

def rotate(a, n):
    """
    param a: list to be rotated
    param n: by how much
    returns: list a rotated n times
    """
    while n > 0:
        a = shift(a)
        n -= 1
    return a

def power(In, Vn):
    """
    param In: list of currents
    param Vn: list of voltages
    returns : list of power V*I - In[i]*Vn[i]
    """
    return [v*i for v,i in zip(In, Vn)]

def active(In, Vn):
    """
    param In: list of currents
    param Vn: list of voltages
    returns : list of indexes of regions where P=V*I < 0
    """
    powerList = power(In, Vn)
    return [powerList.index(p) for p in powerList if p < 0]

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

def T_iteration(n):
    """
    param n:
    returns:approximate solution using the iteration scheme
             and returns the list [T0, T1, ..., Tn] 
    """
    from math import exp
    results = [1.0]
    currentT = 1.0
    for k in range(0,n):
        Ti = k/n
        currentT += (1/n)*(-2*currentT + .5*exp(-Ti))
        results.append(currentT)
    return results

def T_error(n):
    """
    param n: integer
    returns: error between approximate solution and exact solution
    """
    from math import exp
    exact_equation = lambda t: (exp(-2*t)+exp(-t))/2
    approx_solutions = T_iteration(n)
    exact_solutions = [exact_equation(n) for n in range(n+1)]
    print("size of exact sols = %d" %len(exact_solutions))
    print("size of approx sols = %d" %len(approx_solutions))
    error = [i-j for i,j in zip(approx_solutions, exact_solutions)]
    print("Approx \t\t\t Exact \t\t\t Error")
    for i,j in zip(exact_solutions, approx_solutions):
        print("{} \t {} \t {}".format(i,j,j-i))
    #return max(error)
    
