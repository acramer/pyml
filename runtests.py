from mat import Mat
from func import sigmoid
from tests import *
import unittest

def torch_calc_backprop_batch():

    def printS(s, num=50, char='-'):
        spacer = ''.join([char]*num)
        print(spacer, s, spacer)

    # ============================== Torch ==============================
    import torch
    import torch.nn as nn

    printS('Torch', char='=')
    x = torch.Tensor([
            [0.05,0.10],
            [0.65,0.70],
            [0.75,0.80],
        ])
    y = torch.Tensor([
            [0.01,0.99],
            [0.11,0.89],
            [0.21,0.79],
        ])
    w0 = torch.Tensor([
        [0.15,0.20],
        [0.25,0.30],
    ])
    b0 = torch.Tensor([0.35,0.35])

    w1 = torch.Tensor([
        [0.40,0.45],
        [0.50,0.55],
    ])
    b1 = torch.Tensor([0.60,0.60])

    l0 = nn.Linear(2,2)
    l0.load_state_dict({
        'weight': w0,
        'bias': b0,
    })

    l1 = nn.Linear(2,2)
    l1.load_state_dict({
        'weight': w1,
        'bias': b1,
    })

    printS('Feed Forward')

    #TODO:
    # h = torch.sigmoid(l0(x))
    # h.requires_grad = True
    # p = torch.sigmoid(l1(h))
    # p.requires_grad = True
    p = torch.sigmoid(l1(torch.sigmoid(l0(x))))
    print('Pred:', p)

    loss = nn.MSELoss()
    E = loss(p,y)
    E.backward()
    print('Error:', E)

    printS('Backward')
    # ------------ Calculating dEw1 ------------
    #TODO: print('p',p)
    #TODO: print('h',h)
    print('dEl1w', l1.weight.grad)
    print('dEl1b', l1.bias.grad)
    print('dEl0w', l0.weight.grad)
    print('dEl0b', l0.bias.grad)

    print('\n\n')

    # ============================== Matlib ==============================
    printS('Matlib', char='=')
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

    printS('Feed Forward')
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
    print('Pred:', p)
    print('Error:', E)

    printS('Calculating Grad for w1')
    # ------------ Calculating dEw1 ------------
    #TODO: move ff and backprop logic into a method
    dE = p - y
    print('dE', dE)

    dOut_dNet = p * (1 - p) # derivative of activation layer wrt linear layer
    print('dOut_dNet', dOut_dNet)

    deltaOut = dE * dOut_dNet
    print('deltaOut', deltaOut)

    printS('',10)

    #TODO: fully implement transpose
    #TODO: determine proper way to combine matricies
    #TODO: generalize to layers
    dEw1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * h.reshape(-1,1,2)).mean(0)
    print('dEw1', dEw1)

    dEb1 = deltaOut.mean(0)
    print('dEb1', dEb1)

    printS('Calculating Grad for w0')
    # ------------ Calculating dEw0 ------------
    dEout1_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1)[0,0,0] #TODO: batch handling
    print('dEout1_dOutH1', dEout1_dOutH1)

    dEout2_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1)[0,1,0] #TODO: batch handling
    print('dEout2_dOutH1', dEout2_dOutH1)

    dE_dOutH1 = (Mat([d.repeat(2).transpose() for d in deltaOut]) * w1).sum(1) #TODO: batch handling
    print('dE_dOutH1', dE_dOutH1)

    dOutH1_dNetH1 = h * (1 - h) # Derivative activation layer (sigmoid)
    print('dOutH1_dNetH1', dOutH1_dNetH1)

    deltaHidden = dE_dOutH1 * dOutH1_dNetH1
    print('deltaHidden', deltaHidden)
    
    printS('',10)

    dEw0 = (Mat([d.repeat(2).transpose() for d in deltaHidden]) * x.reshape(-1,1,2)).mean(0)
    print('dEw0', dEw0)

    dEb0 = deltaHidden.mean(0)
    print('dEb0', dEb0)



if __name__ == '__main__':
    # Space Song
    # Federer
    # Chamber of reflection
    # torch_calc_backprop_batch()
    unittest.main()

