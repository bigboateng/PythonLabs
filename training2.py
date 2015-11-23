def box_volume(a, b, c):
    """This function will return volume of cuboid with
     lengths a,b,c """
    return a * b * c
    
    
def fall_time(h):
    """ this function will return time t it takes an object to
    fall distance h"""
    g = 9.81
    return ((2 * h)/g) ** 0.5

def interval_point(a, b, x):
    """ takes three numbers and interprets a and b as 
    the start and end point of an interval, and x as a
    fraction between 0 and 1 that return how far 
    to go towards b, starting at a."""
    if x is 0:
        return a
    else:
        if a is b:
            return 0
        else:
            a *= x
            return a 
def impact_velocity(h):
    """impact_velocity(h) that return the velocity 
    (in metre per second) with which an object falling 
    from a height of h meters will hit the ground """
    g = 9.81
    return fall_time(h)*g
    
def signum(x):
    """ A function which will return 1 if x > 0
    return 0 if x is 0 
    return -1 if x < 0"""
    if x > 0:
        return 1
    elif x is 0:
        return 0
    else:
        return -1
    

        
