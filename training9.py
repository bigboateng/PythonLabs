from __future__ import division
"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    # lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    # upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    # space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.

    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print("Code is not reversible:")
        print("keys are   %s", sorted(unique_keys))
        print("values are %s", sorted(unique_vals))
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = \
    "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


def trapez(f, a, b, n):
    """

    :param f:
    :param a:
    :param b:
    :param n:
    :return: composite trapezoidal integration rule applied on f between limits a and b
    """
    a, b = float(a), float(b)
    h = (b - a)/n
    big_summation = sum([f(a + i*h) for i in range(1, n)])
    return (h/2)*(f(a) + f(b) + 2*big_summation)


def encode(code, msg):
    """ :returns ecrypts a message using the dictionary code provided"""
    msg = list(msg)
    for i in range(len(msg)):
        if msg[i] in code:
            msg[i] = code[msg[i]]
    return "".join(msg)


def reverse_dic(d):
    """
    :param d:
    :return:
    """
    return {v: k for k, v in d.items()}


def decode(code, encoded_msg):
    """
    returns the decoded version of encoded msg using the dict key
    """
    code = reverse_dic(code)
    encoded_msg = list(encoded_msg)
    for i in range(len(encoded_msg)):
        if encoded_msg[i] in code:
            encoded_msg[i] = code[encoded_msg[i]]
    return "".join(encoded_msg)

def const(x):
    return 1.

# if this file is executed on it's own, check codes given
if __name__ == "__main__":
#     f1 = lambda x:x
      f2 = lambda x:x*x
#     print(trapez(f2, 0, 1, 100))
#     print(trapez(f2, 0, 1, 1000))
      print(trapez(f2, -1, 2, 5))
#     test_codes()
#     print(range(1,1))
