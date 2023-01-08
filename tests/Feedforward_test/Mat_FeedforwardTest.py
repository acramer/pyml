import unittest

from func import sigmoid
from mat import Mat

class Mat_FeedforwardTest(unittest.TestCase):
    def test_linear(self):
        x = Mat([[1,0.1]])
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
        y = Mat([0.7513507,0.772928465])
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
        x = sigmoid(x)
        x = (w1*x).sum(1)+b1
        p = sigmoid(x)
        self.assertMatEqual(p,y)

    def test_full_batch(self):
        x = Mat([
                [0.05,0.10],
                [-0.05,-0.10],
            ])
        y = Mat([
                [0.7513507,0.772928465],
                [0.7486259,0.769753154],
            ])
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

        if x.rank == 2 and x.shape[0]>1:
            x = Mat([w0*y for y in x]).sum(2)+b0
            x = sigmoid(x)
            x = Mat([w1*y for y in x]).sum(2)+b1
        else:
            x = (w0*x).sum(1)+b0
            x = sigmoid(x)
            x = (w1*x).sum(1)+b1

        p = sigmoid(x)
        self.assertMatEqual(p,y)

    def test_error(self):
        x = Mat([
                [0.05,0.10],
                # [-0.05,-0.10],
            ])
        y = Mat([
                [0.01,0.99],
                # [0.7486259,0.769753154],
            ])
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

        if x.rank == 2 and x.shape[0]>1:
            x = Mat([w0*y for y in x]).sum(2)+b0
            x = sigmoid(x)
            x = Mat([w1*y for y in x]).sum(2)+b1
        else:
            x = (w0*x).sum(1)+b0
            x = sigmoid(x)
            x = (w1*x).sum(1)+b1

        p = sigmoid(x)
        # L2 Loss
        E = ((p-y)**2).mean()
        self.assertTrue(abs(E-0.298371109)<0.00001)

    def test_gradcalc(self):
        x = Mat([
                [0.05,0.10],
                # [-0.05,-0.10],
            ])
        y = Mat([
                [0.01,0.99],
                # [0.7486259,0.769753154],
            ])
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

        if x.rank == 2 and x.shape[0]>1:
            x = Mat([w0*y for y in x]).sum(2)+b0
            h = sigmoid(x)
            x = Mat([w1*y for y in h]).sum(2)+b1
        else:
            x = (w0*x).sum(1)+b0
            h = sigmoid(x)
            x = (w1*h).sum(1)+b1

        p = sigmoid(x)
        E = ((y-p)**2).mean()
        dEo = p-y
        # print('\ndEo')
        # print(dEo.flatten().repeat(2).transpose())
        # print('p*(1-p)')
        # print((p*(1-p)).repeat(2).transpose())
        # print('h')
        # print(h)
        dEw1 = dEo.flatten().repeat(2).transpose()*(p*(1-p)).repeat(2).transpose()*h
        # print('dEw1')
        # print(dEw1)
        # print('w1')
        # print(w1)
        # print('w1-0.5*dEw1')
        # print(w1-0.5*dEw1)
        lr = 0.5
        w1 -= lr*dEw1
        w1_prime = Mat([
            [0.35891648,0.408666186],
            [0.511301270,0.561370121],
        ])
        self.assertMatEqual(w1,w1_prime)

    # def test_backprop(self):
    #     x = Mat([0.05,0.10])
    #     y = Mat([0.7513507,0.772928465])
    #     w0 = Mat([
    #         [0.15,0.20],
    #         [0.25,0.30],
    #     ])
    #     b0 = Mat([0.35,0.35])

    #     w1 = Mat([
    #         [0.40,0.45],
    #         [0.50,0.55],
    #     ])
    #     b1 = Mat([0.60,0.60])

    #     x = (w0*x).sum(1)+b0
    #     x = sigmoid(x)
    #     x = (w1*x).sum(1)+b1
    #     p = sigmoid(x)
    #     #TODO: self.assertMatEqual(p,y)

    def assertMatEqual(self,x,y,precision=0.001):
        self.assertTrue(((x-y).abs()<precision).all())

