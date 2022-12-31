import unittest
from mat import *
from net import *

class BaselineTest(unittest.TestCase):
    def test_creation(self):
        a = Net(4,3)

