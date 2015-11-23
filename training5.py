__author__ = 'Boateng'


def count_sub_in_file(filename, s):
    """

    :param filename:
    :param s:
    :return: the number of occurebces of s in given filename
    """
    try:
        f = open(filename, 'r').read()
        return f.count(s)
    except FileNotFoundError and IOError:
        return -1


def count_vowels(s):
    """

    :param s:
    :return: the number of times a vowel appaera in s
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    total = 0
    for v in vowels:
        total += s.count(v)
    return total