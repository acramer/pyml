from mat import Mat
from func import sigmoid
from tests import *
import unittest

if __name__ == '__main__':
    # Space Song
    # Federer
    # Chamber of reflection

    # x = Mat([
    #         [0.05,0.10],
    #         [-0.05,-0.10],
    #     ])
    # y = Mat([
    #         [0.7513507,0.772928465],
    #         [0.7486259,0.769753154],
    #     ])
    # w0 = Mat([
    #     [0.15,0.20],
    #     [0.25,0.30],
    # ])
    # b0 = Mat([0.35,0.35])

    # w1 = Mat([
    #     [0.40,0.45],
    #     [0.50,0.55],
    # ])
    # b1 = Mat([0.60,0.60])

    # if x.rank == 2 and x.shape[0]>1:
    #     x = Mat([w0*y for y in x]).sum(2)+b0
    #     x = sigmoid(x)
    #     x = Mat([w1*y for y in x]).sum(2)+b1
    # else:
    #     x = (w0*x).sum(1)+b0
    #     x = sigmoid(x)
    #     x = (w1*x).sum(1)+b1

    # p = sigmoid(x)
    # # L1/MAE (mean absolute loss)
    # print(p)
    # E = (p-y).abs()
    # print(E)

    # 
    # print(''.join(['+']*100))

    # import torch 
    # from torch import nn
    # from torch.nn import functional as F

    # x = torch.Tensor([
    #     [0.05,0.10],
    #     [-0.05,-0.10],
    # ])

    # y = torch.Tensor([
    #     [0.7513507,0.772928465],
    #     [0.7513507,0.772928465],
    # ])

    # l0 = nn.Linear(2,2)
    # l0.load_state_dict({
    #     'weight':torch.Tensor([
    #         [0.15,0.20],
    #         [0.25,0.30],
    #     ]),
    #     'bias':torch.Tensor([0.35,0.35])
    # })
    # l1 = nn.Linear(2,2)
    # l1.load_state_dict({
    #     'weight':torch.Tensor([
    #         [0.40,0.45],
    #         [0.50,0.55],
    #     ]),
    #     'bias':torch.Tensor([0.6,0.6])
    # })
    # print(F.sigmoid(l1(F.sigmoid(l0(x)))))

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

    # a = Mat(list(range(36)))
    # print(a)
    # b = a.reshape(2,18)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(3,12)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(4,9)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(6,6)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(2,3,6)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(2,2,9)
    # print((b.flatten()==a).all(), b)
    # b = a.reshape(2,2,3,3)
    # print((b.flatten()==a).all(), b)

    unittest.main()
