import unittest

# from func import sigmoid
from mat import Mat

class Mat_FeedforwardTest(unittest.TestCase):
    def test(self):
        x = Mat([[1,0.1]])
        # y = Mat([[1.23, 4.56]]) #TODO: batching output
        y = Mat([1.23, 4.56])

        w0 = Mat([
            [1.0,2.0],
            [4.0,5.0],
        ])
        b0 = Mat([0.03,0.06])

        p = (w0*x).sum(1)+b0
        self.assertTrue(((p-y)<0.001).all())
    
