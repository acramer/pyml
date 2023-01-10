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
            x = Mat([w0*z for z in x]).sum(2)+b0
            x = sigmoid(x)
            x = Mat([w1*z for z in x]).sum(2)+b1
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
            x = Mat([w0*z for z in x]).sum(2)+b0
            x = sigmoid(x)
            x = Mat([w1*z for z in x]).sum(2)+b1
        else:
            x = (w0*x).sum(1)+b0
            x = sigmoid(x)
            x = (w1*x).sum(1)+b1

        p = sigmoid(x)
        # L2 Loss
        E = ((p-y)**2).mean()
        self.assertTrue(abs(E-0.298371109)<0.00001)

    def test_backprop(self):
        # NOTE: test case taken from:
        # https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
        x = Mat([
                [0.05,0.10],
            ])
        y = Mat([
                [0.01,0.99],
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
            t = Mat([w0*y for y in x]).sum(2)+b0
            h = sigmoid(t)
            t = Mat([w1*y for y in h]).sum(2)+b1
        else:
            t = (w0*x).sum(1)+b0
            h = sigmoid(t)
            t = (w1*h).sum(1)+b1

        p = sigmoid(t)
        E = ((y-p)**2).mean()

        # ------------ Calculating dEw1 ------------
        dE = (p-y).flatten() # dE/d_out_o
        self.assertTrue(abs(dE[0] - 0.74136507) < 0.00001)
        self.assertEqual(dE.shape, (2,))

        dOut_dNet = p*(1-p) # derivative of activation layer wrt linear layer
        self.assertTrue(abs(dOut_dNet[0] - 0.186815602) < 0.00001)
        self.assertEqual(dOut_dNet.shape, (2,))

        deltaOut = dE * dOut_dNet
        #TODO: self.assertTrue(abs(deltaOut[0] - 0.) < 0.00001)
        self.assertEqual(deltaOut.shape, (2,))

        dEw1 = deltaOut.repeat(2).transpose() * h
        self.assertTrue(abs(dEw1[0,0] - 0.082167041) < 0.00001)
        self.assertEqual(dEw1.shape, w1.shape)

        dEb1 = deltaOut
        #TODO: self.assertTrue(abs(dEb1[0] - 0.) < 0.00001)
        self.assertEqual(dEb1.shape, b1.shape)

        # ------------ Calculating dEw0 ------------
        dEout1_dOutH1 = (deltaOut.repeat(2).transpose() * w1)[0,0]
        self.assertTrue(abs(dEout1_dOutH1 - 0.055399425) < 0.00001)

        dEout2_dOutH1 = (deltaOut.repeat(2).transpose() * w1)[1,0]
        self.assertTrue(abs(dEout2_dOutH1 - -0.019049119) < 0.00001)

        dE_dOutH1 = (deltaOut.repeat(2).transpose() * w1).sum(0)
        self.assertTrue(abs(dE_dOutH1[0] - 0.036350306) < 0.00001)
        self.assertEqual(dE_dOutH1.shape, (2,))

        dOutH1_dNetH1 = h*(1-h) # Derivative activation layer (sigmoid)
        self.assertTrue(abs(dOutH1_dNetH1[0] - 0.241300709) < 0.00001)
        self.assertEqual(dOutH1_dNetH1.shape, (2,))

        deltaHidden = dE_dOutH1 * dOutH1_dNetH1
        #TODO: self.assertTrue(abs(deltaHidden[0] - 0.) < 0.00001)
        self.assertEqual(deltaHidden.shape, (2,))

        dEw0 = deltaHidden.repeat(2).transpose() * x
        self.assertTrue(abs(dEw0[0,0] - 0.000438568) < 0.00001)
        self.assertEqual(dEw0.shape, w0.shape)

        # TODO: caclulate and test
        dEb0 = deltaHidden
        #TODO: self.assertTrue(abs( [] - 0.) < 0.00001)
        self.assertEqual(dEb0.shape, b0.shape)


        lr = 0.5
        # TODO: calculate and implement
        w0_prime = Mat([
            [0.149780716,0.19956143],
            [0.24975114,0.29950229],
        ])
        # b0_prime = Mat([0.35,0.35])
        w1_prime = Mat([
            [0.35891648,0.408666186],
            [0.511301270,0.561370121],
        ])
        # b1_prime = Mat([0.35,0.35])

        w0 -= lr*dEw0
        self.assertMatEqual(w0,w0_prime)
        # b0 -= lr*dEb0
        # self.assertMatEqual(b0,b0_prime)
        w1 -= lr*dEw1
        self.assertMatEqual(w1,w1_prime)
        # b1 -= lr*dEb1
        # self.assertMatEqual(b1,b1_prime)

    def test_backprop_batch_single(self):
        x = Mat([
                [0.05,0.10],
            ])
        y = Mat([
                [0.01,0.99],
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

        w0_prime = Mat([
            [0.149780716,0.19956143],
            [0.24975114,0.29950229],
        ])
        w1_prime = Mat([
            [0.35891648,0.408666186],
            [0.511301270,0.561370121],
        ])

        if x.rank == 2 and x.shape[0]>1:
            t = Mat([w0*y for z in x]).sum(2)+b0
            h = sigmoid(t)
            t = Mat([w1*y for z in h]).sum(2)+b1
        else:
            t = (w0*x).sum(1)+b0
            h = sigmoid(t)
            t = (w1*h).sum(1)+b1

        p = sigmoid(t)
        E = ((y-p)**2).mean()
        dE = p - y
        #TODO: replace constants in batch multi test
        self.assertTrue(abs(dE[0, 0] - 0.74136507) < 0.00001)
        self.assertEqual(dE.shape, (1, 2))

        dOut_dNet = p * (1 - p) # derivative of activation layer wrt linear layer
        self.assertTrue(abs(dOut_dNet[0] - 0.186815602) < 0.00001)
        self.assertEqual(dOut_dNet.shape, (2,))

        deltaOut = dE * dOut_dNet
        self.assertEqual(deltaOut.shape, (1, 2))

        dEw1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * h.reshape(-1,1,2)).mean(0) #TODO: batch handling
        self.assertTrue(abs(dEw1[0,0] - 0.082167041) < 0.00001)
        self.assertEqual(dEw1.shape, w1.shape)

        dEb1 = deltaOut.mean(0) #TODO: batch handling
        self.assertEqual(dEb1.shape, b1.shape)

        dEout1_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1)[0,0,0] #TODO: batch handling
        self.assertTrue(abs(dEout1_dOutH1 - 0.055399425) < 0.00001)

        dEout2_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1)[0,1,0] #TODO: batch handling
        self.assertTrue(abs(dEout2_dOutH1 - -0.019049119) < 0.00001)

        dE_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1).sum(1) #TODO: batch handling
        self.assertTrue(abs(dE_dOutH1[0, 0] - 0.036350306) < 0.00001)
        self.assertEqual(dE_dOutH1.shape, (1, 2))

        dOutH1_dNetH1 = h * (1 - h) # Derivative activation layer (sigmoid)
        self.assertTrue(abs(dOutH1_dNetH1[0] - 0.241300709) < 0.00001)
        self.assertEqual(dOutH1_dNetH1.shape, (2,))

        deltaHidden = dE_dOutH1 * dOutH1_dNetH1
        self.assertEqual(deltaHidden.shape, (1, 2))
        
        dEw0 = (Mat([d.repeat(2).transpose() for d in deltaHidden]) * x.reshape(-1,1,2)).mean(0) #TODO: batch handling
        self.assertTrue(abs(dEw0[0,0] - 0.000438568) < 0.00001)
        self.assertEqual(dEw0.shape, w0.shape)

        dEb0 = deltaHidden.mean(0) #TODO: batch handling
        self.assertEqual(dEb0.shape, b0.shape)

        lr = 0.5

        w0 -= lr*dEw0
        self.assertMatEqual(w0,w0_prime)
        w1 -= lr*dEw1
        self.assertMatEqual(w1,w1_prime)
        
    def test_backprop_batch(self):
        x = Mat([
                [0.05,0.10],
                [0.65,0.70],
                [0.75,0.80],
            ])
        y = Mat([
                [0.01,0.99],
                [0.11,0.89],
                [0.21,0.79],
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

        h, p, E = decon_forward_imp(x, y, w0, b0, w1, b1)
        dEw0, dEb0, dEw1, dEb1 = decon_backward_imp(x, y, w0, b0, w1, b1, h, p, E)

        torch_dEw1 = Mat([
            [ 0.0744,  0.0770],
            [-0.0115, -0.0117]
        ])
        torch_dEb1 = Mat([ 0.1190, -0.0189])
        torch_dEw0 = Mat([
            [0.0043, 0.0048],
            [0.0046, 0.0051]
        ])
        torch_dEb0 = Mat([0.0089, 0.0097])

        self.assertMatEqual(dEw0, torch_dEw0, should_broadcast=False)
        self.assertMatEqual(dEb0, torch_dEb0, should_broadcast=False)
        self.assertMatEqual(dEw1, torch_dEw1, should_broadcast=False)
        self.assertMatEqual(dEb1, torch_dEb1, should_broadcast=False)
 
    # def test_backprop_graph(self):
    #     # TODO: implement
    #     x = Mat([
    #             [0.05,0.10],
    #         ])
    #     y = Mat([
    #             [0.01,0.99],
    #         ])
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

    #     if x.rank == 2 and x.shape[0]>1:
    #         t = Mat([w0*y for y in x]).sum(2)+b0
    #         h = sigmoid(t)
    #         t = Mat([w1*y for y in h]).sum(2)+b1
    #     else:
    #         t = (w0*x).sum(1)+b0
    #         h = sigmoid(t)
    #         t = (w1*h).sum(1)+b1

    #     p = sigmoid(t)
    #     E = ((y-p)**2).mean()
    #     # self.assertMatEqual()

    def graph_forward_imp():
        pass

    def graph_backward_imp():
        pass

    def assertMatEqual(self, x, y, precision=0.001, should_broadcast=True):
        if not should_broadcast:
            self.assertEqual(x.shape,y.shape)
        self.assertTrue(((x-y).abs()<precision).all())

def decon_forward_imp(x, y, w0, b0, w1, b1):
    if x.rank == 2 and x.shape[0]>1:
        t = Mat([w0*y for y in x]).sum(2)+b0
        h = sigmoid(t)
        t = Mat([w1*y for y in h]).sum(2)+b1
    else:
        t = (w0*x).sum(1)+b0
        h = sigmoid(t)
        t = (w1*h).sum(1)+b1

    p = sigmoid(t)
    E = ((y-p)**2).mean()
    return h, p, E

def decon_backward_imp(x, y, w0, b0, w1, b1, h, p, E):
    dE = p - y
    dOut_dNet = p * (1 - p)
    deltaOut = dE * dOut_dNet

    dEw1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * h.reshape(-1,1,2)).mean(0)
    dEb1 = deltaOut.mean(0) #TODO: batch handling

    dE_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1).sum(1)
    dOutH1_dNetH1 = h * (1 - h)
    deltaHidden = dE_dOutH1 * dOutH1_dNetH1

    dEw0 = (Mat([d.repeat(2).transpose() for d in deltaHidden]) * x.reshape(-1,1,2)).mean(0)
    dEb0 = deltaHidden.mean(0)

    return dEw0, dEb0, dEw1, dEb1

