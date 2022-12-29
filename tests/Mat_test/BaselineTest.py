import unittest
from mat import *

class BaselineTest(unittest.TestCase):
    def test_creation_equality(self):
        a = Mat([
                [0,0],
                [0,0],
                [0,0],
            ])
        b = Mat(3,2)
        self.assertTrue((a==b).all())

    def test_creation_shape(self):
        #TODO: How to test?
        a = Mat(1,2,3,4)

    def test_creation_object(self):
        #TODO: How to test?
        a = Mat([
                [0,1,2],
                [3,4,5],
                [6,7,8],
            ])

    def test_creation_shape_random(self):
        #TODO: implement test case?
        pass
            
    def test_get_slice_2d(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        b = a[:2,1:]
        c = Mat([
            [2,3],
            [5,6],
        ])
        self.assertTrue((b==c).all())

    def test_get_index_2d(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        b = a[0,2]
        c = Mat([
            [3],
        ])
        self.assertTrue((b==c).all())

    def test_set_slice_2d(self):
        a = Mat([
            [1,0,0],
            [4,0,0],
            [7,8,9],
        ])
        b = Mat([
            [2,3],
            [5,6],
        ])
        c = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        a[:2,1:] = b
        self.assertTrue((a==c).all())

    def test_set_index_2d(self):
        a = Mat([
            [1,2,0],
            [4,5,6],
            [7,8,9],
        ])
        b = Mat([[3]])
        c = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        a[0,2] = b #TODO: make case for int
        self.assertTrue((a==c).all())
            
    def test_get_slice_3d(self):
        a = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        b = a[:,:2,1:]
        c = Mat([
            [[2,3],
             [5,6],
            ],
            [[12,13],
             [15,16],
            ],
        ])
        self.assertTrue((b==c).all())

    def test_get_index_3d(self):
        a = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        b = a[1,0,2]
        c = Mat([[[13]]])
        self.assertTrue((b==c).all())

    def test_set_slice_3d(self):
        a = Mat([
            [[1,0,0],
             [4,0,0],
             [7,8,9],
            ],
            [[11,0,0],
             [14,0,0],
             [17,18,19],
            ],
        ])
        
        b = Mat([
            [[2,3],
             [5,6],
            ],
            [[12,13],
             [15,16],
            ],
        ])
        c = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        a[:,:2,1:] = b
        self.assertTrue((a==c).all())

    def test_set_index_3d(self):
        a = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,0],
             [14,15,16],
             [17,18,19],
            ],
        ])

        b = Mat([[[13]]])
        c = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        a[1,0,2] = b #TODO: make case for int
        self.assertTrue((a==c).all())

