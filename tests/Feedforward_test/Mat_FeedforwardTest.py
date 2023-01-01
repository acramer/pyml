import unittest

from func import sigmoid
from mat import Mat

class Mat_FeedforwardTest(unittest.TestCase):
    def test_linear(self):
        x = Mat([[1,0.1]])
        # y = Mat([[1.23, 4.56]]) #TODO: batching output, ignore until backprop complete
        y = Mat([1.23, 4.56])

        w0 = Mat([
            [1.0,2.0],
            [4.0,5.0],
        ])
        b0 = Mat([0.03,0.06])

        w1 = Mat([
            [1.0,2.0],
            [4.0,5.0],
        ])
        b1 = Mat([0.03,0.06])

        p = (w0*x).sum(1)+b0
        self.assertMatEqual(p,y)

    def test_full(self):
        x = Mat([0.05,0.10])
        y = Mat([0.01,0.99])
        w0 = Mat([
            [0.15,0.20],
            [0.25,0.30],
        ])
        b0 = Mat([0.35,0.35])

        w1 = Mat([
            [0.40,0.45],
            [0.50,0.55],
        ])
        b1 = Mat([0.60,0.60])

        x = (w0*x).sum(1)+b0
        x = (w1*x).sum(1)+b1
        p = sigmoid(x)
        self.assertMatEqual(p,y)


    def assertMatEqual(self,x,y,precision=0.001):
        self.assertTrue(((x-y).abs()<precision).all())

