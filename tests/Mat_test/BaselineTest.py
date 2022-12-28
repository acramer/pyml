import unittest
from mat import *

class BaselineTest(unittest.TestCase):
    def test_creation_shape(self):
        #TODO: implement test case?
        a = Mat(1,2,3,4)

    def test_creation_object(self):
        #TODO: implement test case?
        a = Mat([
                [0,1,2],
                [3,4,5],
                [6,7,8],
            ])
            
    def test_2d_get_slice(self):
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

    def test_2d_get_index(self):
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

    def test_2d_set_slice(self):
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

    def test_2d_set_index(self):
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
        self.assertTrue((b==c).all())
            
    def test_3d_get_slice(self):
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

    def test_3d_get_index(self):
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

    def test_3d_set_slice(self):
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

    def test_3d_set_index(self):
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
        self.assertTrue((b==c).all())


if __name__ == '__main__':
    unittest.main()

