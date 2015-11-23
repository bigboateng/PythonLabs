__author__ = 'Boateng'


def derivative(f, x, eps=1e-6):
    """

    :param f: input function f(x)
    :param x: value to evaluate function at
    :return:
    """
    return (f(x + (eps/2)) - f(x - (eps/2)))/eps


def f(x):
    return x ** 2 - 2


def newton(f,x,feps,maxit):
    """

    :param f:
    :param x:
    :param feps:
    :param maxit:
    :return: newton rhapson approximated at x
    """
    NumIterations = 0
    while abs(f(x)) > feps:
        x -= f(x)/derivative(f, x)
        NumIterations += 1
        if(NumIterations > maxit):
            raise RuntimeError("Failed after {} iterations".format(NumIterations))
    return x


def is_palindrome(s):
    """

    :param s:
    :return: if string s is a palindrom i.e ABA == ABA backwards
    """
    if len(s) == 0:
        return True
    elif len(s) is 1:
        return True
    elif s[0] is s[-1]:
        # return [s[(len(s)-1) - x] for x in range(len(s))] == list(s)
        return is_palindrome(s[1:-1])
    else:
        return False


if __name__ == '__main__':
   print(is_palindrome("rotator"))
