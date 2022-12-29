import unittest
from mat import *

class BroadcastingTest(unittest.TestCase):
    def test_broadcast(self):
        a = Mat(3,3,3)
        b = a.broadcast_if_needed(Mat(3,3,1))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(Mat(3,1,3))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(Mat(1,3,1))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(Mat(1,3,3))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(Mat(3,3))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(Mat(3))
        self.assertTrue((a==b).all())
        b = a.broadcast_if_needed(0)
        self.assertTrue((a==b).all())

    def test_addition_same_shape_1d(self):
        a = Mat([1])
        b = Mat([2])
        c = Mat([3])
        self.assertTrue(((a+b)==c).all())
        
    def test_addition_same_shape_2d(self):
        a = Mat([
            [1,0.1],
            [0.01,0.001],
        ])
        b = Mat([
            [2,0.2],
            [0.02,0.002],
        ])
        c = Mat([
            [3,0.3],
            [0.03,0.003],
        ])
        d = Mat([
            [1,1],
            [1,1],
        ])*0.000001
        #TODO: Fix precision error (need to?)
        #  - Option 1: different underlying datastructure for floats
        #  - Option 2: handle within eq
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_same_shape_3d(self):
        a = Mat([
            [[1,0.1],
             [0.01,0.001],
             ],
            [[0.001,1],
             [0.1,0.01],
             ],
        ])
        b = Mat([
            [[2,0.2],
             [0.02,0.002],
             ],
            [[0.002,2],
             [0.2,0.02],
             ],
        ])
        c = Mat([
            [[3,0.3],
             [0.03,0.003],
             ],
            [[0.003,3],
             [0.3,0.03],
             ],
        ])
        d = Mat([
            [[1,1],
             [1,1],
             ],
            [[1,1],
             [1,1],
             ],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())
        
    def test_addition_same_shape_4d(self):
        a = Mat([
            [[[1,0.1],
              [0.01,0.001],
              ],
             [[0.001,1],
              [0.1,0.01],
              ],
            ],
            [[[0.01,0.001],
              [1,0.1],
              ],
             [[0.1,0.01],
              [0.001,1],
              ],
            ],
        ])
        b = Mat([
            [[[2,0.2],
              [0.02,0.002],
              ],
             [[0.002,2],
              [0.2,0.02],
              ],
            ],
            [[[0.02,0.002],
              [2,0.2],
              ],
             [[0.2,0.02],
              [0.002,2],
              ],
            ],
        ])
        c = Mat([
            [[[3,0.3],
              [0.03,0.003],
              ],
             [[0.003,3],
              [0.3,0.03],
              ],
            ],
            [[[0.03,0.003],
              [3,0.3],
              ],
             [[0.3,0.03],
              [0.003,3],
              ],
            ],
        ])
        d = Mat([
            [[[1,1],
              [1,1],
              ],
             [[1,1],
              [1,1],
              ],
             ],
            [[[1,1],
              [1,1],
              ],
             [[1,1],
              [1,1],
              ],
             ],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_0(self):
        a = Mat([
            [1,0.1],
            [2,0.2],
        ])
        b = Mat(
            [3,0.3],
        )
        c = Mat([
            [4,0.4],
            [5,0.5],
        ])
        d = Mat([
            [1,1],
            [1,1],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_1(self):
        a = Mat([
            [1,2],
            [3,4],
        ])
        b = 1
        c = Mat([
            [2,3],
            [4,5],
        ])
        d = Mat([
            [1,1],
            [1,1],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_2(self):
        a = Mat([
            [1,2],
            [3,4],
        ])
        b = Mat([[1]])
        c = Mat([
            [2,3],
            [4,5],
        ])
        d = Mat([
            [1,1],
            [1,1],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_3(self):
        a = Mat([
            [1,2],
            [3,4],
        ])
        b = Mat([1])
        c = Mat([
            [2,3],
            [4,5],
        ])
        d = Mat([
            [1,1],
            [1,1],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_4(self):
        a = Mat([
            [[1,0.1],
             [0.01,0.001],
             ],
            [[0.001,1],
             [0.1,0.01],
             ],
        ])
        b = Mat([2,0.2])
        c = Mat([
            [[3,0.3],
             [2.01,0.201],
             ],
            [[2.001,1.2],
             [2.1,0.21],
             ],
        ])
        d = Mat([
            [[1,1],
             [1,1],
             ],
            [[1,1],
             [1,1],
             ],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())

    def test_addition_diff_shape_5(self):
        a = Mat([
            [[1,0.1],
             [0.01,0.001],
             ],
            [[0.001,1],
             [0.1,0.01],
             ],
        ])
        b = Mat([
            [2,0.2],
            [0.02,0.002],
        ])
        c = Mat([
            [[3,0.3],
             [0.03,0.003],
             ],
            [[2.001,1.2],
             [0.12,0.012],
             ],
        ])
        d = Mat([
            [[1,1],
             [1,1],
             ],
            [[1,1],
             [1,1],
             ],
        ])*0.000001
        #TODO: precision error, see more: test_addition_same_shape_2d
        self.assertTrue((((a+b)-c)<d).all())
