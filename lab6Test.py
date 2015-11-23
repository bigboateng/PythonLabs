import unittest
from lab6 import *
from math import sqrt
class TestLab(unittest.TestCase):

    def square(self, x):
        return x * x


    def test_positive_places(self):
        self.assertEqual(eval_f(self.square, [-1, 10, 20, 42]), [1, 100, 400, 1764])
        self.assertEqual(eval_f(sqrt, [1, 2, 4, 9]), [1.0, 1.4142135623730951, 2.0, 3.0])
        self.assertEqual()