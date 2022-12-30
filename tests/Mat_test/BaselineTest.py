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
            
    def test_get_slice_1d(self):
        #TODO: implement test case
        pass

    def test_get_index_1d(self):
        #TODO: implement test case
        pass

    def test_set_slice_1d(self):
        #TODO: implement test case
        pass

    def test_set_index_1d(self):
        #TODO: implement test case
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

        b = a[1:2,:]
        c = Mat([
            [4,5,6],
        ])
        self.assertTrue((b==c).all())

        b = a[:,1:2]
        c = Mat([[2],[5],[8]])
        self.assertTrue((b==c).all())

        b = a[:,:]
        self.assertTrue((b==a).all())
        b = a[:]
        self.assertTrue((b==a).all())

    def test_get_index_2d(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        self.assertTrue((a[:1,2:]==Mat([[3]])).all())
        self.assertTrue((a[:1,2]==Mat([3])).all())
        self.assertTrue((a[0,2:]==Mat([3])).all())
        self.assertEqual(a[0,2], 3)

    def test_set_slice_2d(self):
        a = Mat([
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ])
        b = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        c = Mat([
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ])
        
        a[:2,1:] = Mat([
            [2,3],
            [5,6],
        ])
        a[:,:1] = Mat([[1],[4],[7]])
        a[2,:] = Mat([7,8,9])
        self.assertTrue((a==b).all())

        a[:,:] = Mat([
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ])
        self.assertTrue((a==c).all())

        a[:] = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        self.assertTrue((a==b).all())

        a[:] = Mat([
            [1,2,3],
            [4,0,0],
            [7,0,9],
        ])
        a[1:2,1:] = Mat([[5,6]])
        a[2,1:2] = Mat([8])
        self.assertTrue((a==b).all())

    def test_set_index_2d(self):
        a = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])
        b = Mat([
            [1,2,0],
            [4,5,6],
            [7,8,9],
        ])
        c = Mat([
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ])

        a[:1,2:] = Mat([[0]])
        self.assertTrue((a==b).all())

        a[:1,2] = Mat([3])
        self.assertTrue((a==c).all())

        a[0,2:] = Mat([0])
        self.assertTrue((a==b).all())

        a[0,2] = 3
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

        b = Mat([
            [[2,3],
             [5,6],
            ],
            [[12,13],
             [15,16],
            ],
        ])
        self.assertTrue((a[:,:2,1:]==b).all())

        b = Mat([
            [2,3],
            [5,6],
        ])
        self.assertTrue((a[0,:2,1:]==b).all())

        b = Mat([
            [1, 4],
            [11, 14],
        ])
        self.assertTrue((a[:,:2,0]==b).all())

        b = Mat([7, 17])
        self.assertTrue((a[:,2,0]==b).all())

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
        self.assertTrue((a[:1,1:2,2:]==Mat([[[6]]])).all())
        self.assertTrue((a[0,1:2,2:]==Mat([[6]])).all())
        self.assertTrue((a[:1,1,2:]==Mat([[6]])).all())
        self.assertTrue((a[:1,1:2,2]==Mat([[6]])).all())
        self.assertTrue((a[0,1,2:]==Mat([6])).all())
        self.assertTrue((a[0,1:2,2]==Mat([6])).all())
        self.assertTrue((a[:1,1,2]==Mat([6])).all())
        self.assertEqual(a[0,1,2], 6)

    def test_set_slice_3d(self):
        a = Mat([
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
        ])
        b = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        c = Mat([
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
        ])
        
        a[:,:2,1:] = Mat([
            [[2,3],
             [5,6],
             ],
            [[12,13],
             [15,16],
             ],
        ])
        a[0,:,:1] = Mat([[1],[4],[7]])
        a[1,:2,:1] = Mat([[11],[14]])
        a[:,2:,:] = Mat([[[7,8,9]],[[17,18,19]]])
        self.assertTrue((a==b).all())

        a[:,:] = Mat([
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
            [[0,0,0],
             [0,0,0],
             [0,0,0],
            ],
        ])
        self.assertTrue((a==c).all())

        a[:] = Mat([
            [[1,2,3],
             [4,5,6],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
            ],
        ])
        self.assertTrue((a==b).all())

        a[:] = Mat([
            [[1,2,3],
             [4,0,0],
             [7,0,9],
            ],
            [[11,12,13],
             [14,0,0],
             [17,0,19],
            ],
        ])
        a[:,1:2,1:] = Mat([[[5,6]],[[15,16]]])
        a[:,2,1:2] = Mat([[8],[18]])
        self.assertTrue((a==b).all())

    def test_set_index_3d(self):
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
        b = Mat([
            [[1,2,3],
             [4,5,0],
             [7,8,9],
            ],
            [[11,12,13],
             [14,15,16],
             [17,18,19],
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

        a[:1,1:2,2:] = Mat([[[0]]])
        self.assertTrue((a==b).all())
        a[0,1:2,2:] = Mat([[6]])
        self.assertTrue((a==c).all())
        a[:1,1,2:] = Mat([[0]])
        self.assertTrue((a==b).all())
        a[:1,1:2,2] = Mat([[6]])
        self.assertTrue((a==c).all())
        a[:1,1,2] = Mat([0])
        self.assertTrue((a==b).all())
        a[0,1:2,2] = Mat([6])
        self.assertTrue((a==c).all())
        a[0,1,2:] = Mat([0])
        self.assertTrue((a==b).all())
        a[0,1,2] = 6
        self.assertTrue((a==c).all())

