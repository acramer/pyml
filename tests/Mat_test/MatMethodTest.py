import unittest
from mat import *

class MatMethodTest(unittest.TestCase):
    def test_flatten(self):
        a = Mat(list(range(36)))
        b = a.reshape(2,18)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(3,12)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(4,9)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(6,6)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(2,3,6)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(2,2,9)
        self.assertMatEqual((b.flatten()==a).all())
        b = a.reshape(2,2,3,3)
        self.assertMatEqual((b.flatten()==a).all())

    def assertMatEqual(self, x, y, precision=0.001, should_broadcast=True):
        if not should_broadcast:
            self.assertEqual(x.shape,y.shape)
        self.assertTrue(((x-y).abs()<precision).all())
