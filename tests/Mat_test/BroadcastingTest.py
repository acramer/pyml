import unittest
from mat import *

class BroadcastingTest(unittest.TestCase):
    def test_addition_same_shape_1d(self):
        #TODO: implement
        a = Mat([1])
        b = Mat([2])
        c = Mat([3])
        self.assertTrue(((a+b)==c).all())
        
    def test_addition_same_shape_2d(self):
        #TODO: implement
        # self.assertTrue()
        pass

    def test_addition_same_shape_3d(self):
        #TODO: implement
        # self.assertTrue()
        pass
        
    def test_addition_same_shape_4d(self):
        #TODO: implement
        # self.assertTrue()
        pass

