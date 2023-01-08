import unittest
from mat import *

class AxisMethodTest(unittest.TestCase):
    def test_sum(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])

        self.assertEqual(a.sum(),45)
        b = Mat([12, 15, 18])
        self.assertTrue((a.sum(0)==b).all())
        b = Mat([6, 15, 24])
        self.assertTrue((a.sum(1)==b).all())

    def test_mean(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])

        self.assertEqual(a.mean(),5)
        b = Mat([4, 5, 6])
        self.assertTrue((a.mean(0)==b).all())
        b = Mat([2, 5, 8])
        self.assertTrue((a.mean(1)==b).all())


