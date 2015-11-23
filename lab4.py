from math import sqrt


def seq_sqrt(xs):
    """

    :param xs:
    :return: returns a list of same length that containt the sqrt of
    each number in xs
    """
    return [sqrt(x) for x in xs]


def mean(xs):
    """

    :param xs:
    :return: returns arithmetic mean of sequence xs numbers
    """
    tots = 0
    for i in xs:
        tots += i
    return tots / len(xs)


def wc(filename):
    """

    :param filename:
    :return: number of words in a filename
    """
    file = open(filename, 'r')
    total_count = 0
    for line in file:
        b = line.split()
        total_count += len(b)
    file.close()
    return total_count
