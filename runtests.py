from mat import Mat
from tests import *
import unittest

if __name__ == '__main__':
    # Space Song
    # Federer
    # Chamber of reflection
    # 
    # print(''.join(['+']*100))

    # import torch 
    # from torch import nn

    # x = torch.Tensor([
    #     [1,0.1],
    #     [2,0.2],
    # ])

    # l0 = nn.Linear(2,2)
    # l0.load_state_dict({
    #     'weight':torch.Tensor([
    #         [1.0,2.0],
    #         [4.0,5.0],
    #     ]),
    #     'bias':torch.Tensor([0.03,0.06])
    # })
    # print('x:')
    # print(x)
    # print('\nl0 weight:')
    # print(l0.weight)
    # print('\nl0 bias:')
    # print(l0.bias)
    # print('\np:')
    # print(l0(x))

    # import numpy as np
    # 
    # x = np.array([
    #     [1,0.1],
    #     [2,0.2],
    # ])
    # y = np.array([
    #     [1],
    # ])

    # w0 = np.array([
    #     [1.0,2.0],
    #     [4.0,5.0],
    # ])
    # b0 = np.array([0.03,0.06])
    # 
    # print('x:')
    # print(x)
    # print('\nl0 weight:')
    # print(w0)
    # print('\nl0 bias:')
    # print(b0)
    # print('\np:')
    # print((w0*x).sum(axis=1)+b0)

    # x = Mat([
    #     [1,0.1],
    #     [2,0.2],
    # ])

    # x = Mat([1,0.1])

    # w0 = Mat([
    #     [1.0,2.0],
    #     [4.0,5.0],
    # ])
    # b0 = Mat([0.03,0.06])
    # 
    # print('x:')
    # print(x)
    # print('\nl0 weight:')
    # print(w0)
    # print('\nl0 bias:')
    # print(b0)
    # print('\np:')
    # print(w0*x)
    # print((w0*x).sum(1)+b0)
    # from copy import deepcopy

    # x = Mat([
    #     [1,0.1],
    #     [2,0.2],
    # ])
    # w0 = Mat([
    #     deepcopy(w0),
    #     deepcopy(w0) # Repeat by number of batches
    # ])
    # # Unsqueeze by 1st dim? x = x[:,None,:]
    # x = Mat([
    #     [[1,0.1]],
    #     [[2,0.2]],
    # ])
    # print((w0*x).sum(2)+b0)

    # print(''.join(['+']*100))

    unittest.main()
