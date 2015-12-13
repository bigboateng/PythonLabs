

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
        
def count(s, chars):
    """"
    param s    :string
    param chars:list of chars
    returns    :dict of num of occurences of chars in s
    """
    dictionary = {k:0 for k in chars}
    for char in s:
        if char in chars:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
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
    



