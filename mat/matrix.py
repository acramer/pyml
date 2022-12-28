from copy import deepcopy

"""
TODO: Implement list backed Mat object
    - Constructors generate object iteratively
    - Get method creates Mat object at finish
    - Comparison methods creates Mat object at finish
"""

class Mat:
    #TODO: matrix ops: inversion, transpose, range
    def __init__(self, firstElement, *args, **kwargs):
        if isinstance(firstElement, list):
            assert self.validMatrix(firstElement), 'Invalid Matrix'
            self.setFromList(firstElement)
        else:
            assert self.validShape(firstElement, *args), 'Invalid Shape'
            self.generateMat(firstElement, *args, **kwargs)

    def validMatrix(self, m):
        #TODO: implement
        return True

    def validShape(self, *shape):
        #TODO: implement
        return True

    def validIndices(self, indices):
        return all([isinstance(i, slice) or (i >= 0 and i < s) for i, s in zip(indices, self.shape)])

    def setFromList(self, m):
        self.mat = []
        if isinstance(m[0], list) or isinstance(m[0], Mat):
            for n in m:
                if isinstance(n, Mat):
                    n = n.mat # Should 
                self.mat.append(Mat(n))
            self.rank = self.mat[0].rank + 1
            self.shape = (len(m), *self.mat[0].shape)
        else:
            self.mat = m
            self.rank = 1
            self.shape = (len(m), )

    def generateMat(self, *shape, random=False, **kwargs):
        #TODO: random
        self.shape = shape
        if len(shape) == 1:
            self.mat = [0]*shape[0]
            self.rank = 1
        else:
            self.mat = [Mat(*shape[1:])]*shape[0]
            self.rank = self.mat[0].rank + 1

    def __getitem__(self, indices):
        assert self.validIndices(indices), 'Invalid Indices'
        index = indices[0]
        if not isinstance(index,slice):
            index = slice(index,index+1) 
        if len(indices) > 1:
            return Mat([m[indices[1:]] for m in self.mat[index]])
        return Mat(self.mat[index])

    def __setitem__(self, indices, M):
        assert self.validIndices(indices), 'Invalid Indices'
        #TODO: assert M has valid shape.  Function to generate shape from indices?
        if len(indices) > 1:
            for m, n in zip(self.mat[indices[0]], M.mat):
                m[indices[1:]] = n
        elif isinstance(indices[0],slice):
            self.mat[indices[0]] = M.mat[:]
        else:
            self.mat[indices[0]] = M.mat[0]

    def __str__(self, inner=False):
        pad = '\n' if not inner else ''
        rankstr = '\nRank '+str(self.rank) if not inner else ''
        if isinstance(self.mat[0], Mat):
            ret = pad+'['+',\n '.join([m.__str__(True) for m in self.mat])+']'+pad
        else:
            ret = str(self.mat)
        return rankstr+ret

    def __len__(self):
        return len(self.mat)

    def __iter__(self):
        return iter(self.mat)

    def all(self):
        if isinstance(self.mat[0], Mat):
            return all([m.all() for m in self.mat])
        else:
            return all(self.mat)

    def any(self):
        if isinstance(self.mat[0], Mat):
            return any([m.any() for m in self.mat])
        else:
            return any(self.mat)

    def __gt__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x>y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x>y) for x,y in zip(self.mat,m)])

    def __ge__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x>=y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x>=y) for x,y in zip(self.mat,m)])

    def __lt__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x<y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x<y) for x,y in zip(self.mat,m)])

    def __le__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x<=y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x<=y) for x,y in zip(self.mat,m)])

    def __eq__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x==y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x==y) for x,y in zip(self.mat,m)])

    def __ne__(self, m):
        assert self.shape == m.shape, 'Matrix shapes must match'
        if isinstance(self.mat[0], Mat):
            return Mat([x!=y for x,y in zip(self.mat,m)])
        else:
            return Mat([int(x!=y) for x,y in zip(self.mat,m)])

    def __add__(self, m):
        #TODO: factor of shape?
        assert self.shape == m.shape, 'Matrix shapes must match'
        return Mat([x+y for x,y in zip(self.mat,m)])

    def __sub__(self, m):
        #TODO: factor of shape?
        assert self.shape == m.shape, 'Matrix shapes must match'
        return Mat([x-y for x,y in zip(self.mat,m)])

    def __mul__(self, m):
        #TODO: factor of shape?
        if isinstance(m,Mat):
            assert self.shape == m.shape, 'Matrix shapes must match'
            return Mat([x*y for x,y in zip(self.mat,m)])
        return Mat([x*m for x in self.mat])

    def __truediv__(self, m):
        assert(False, 'Not Implemented')
        return 0

    def __floordiv__(self, m):
        assert(False, 'Not Implemented')
        return 0

    def __mod__(self, m):
        assert(False, 'Not Implemented')
        return 0

    def __pow__(self, m):
        assert(False, 'Not Implemented')
        return 0

