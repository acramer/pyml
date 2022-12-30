from copy import deepcopy
from operator import *

"""
TODO: Implement list backed Mat object
    - Constructors generate object iteratively
    - Get method creates Mat object at finish
    - Comparison methods creates Mat object at finish
"""

class Mat:
    #TODO: matrix ops: inversion, transpose, range, ones, squeeze, unsqueeze, reshape, repeat
    def __init__(self, firstElement, *args, **kwargs):
        if isinstance(firstElement, list):
            assert self.valid_matrix(firstElement), 'Invalid Matrix'
            self.set_from_list(firstElement)
        else:
            assert self.valid_shape(firstElement, *args), 'Invalid Shape'
            self.generate_mat(firstElement, *args, **kwargs)

    def valid_matrix(self, m):
        #TODO: implement
        return True

    def valid_shape(self, *shape):
        #TODO: implement
        return True

    def valid_indices(self, indices):
        return all([isinstance(i, slice) or (i >= 0 and i < s) for i, s in zip(indices, self.shape)])

    def broadcast_if_needed(self, m):
        assert not isinstance(m, list)
        if not isinstance(m, Mat):
            m = Mat([m])

        broadcast_failure_string  = 'Unnable to format shape of {} to {}'.format(m.shape, self.shape)

        # Unsqeeze to number of dims
        for _ in range(len(self.shape)-len(m.shape)):
            m = Mat([m])

        if self.shape == m.shape: return m
        assert all([x == y or y == 1 for x,y in zip(self.shape, m.shape)]), broadcast_failure_string

        def broadcast(to_shape, n):
            from_shape = n.shape
            if to_shape == from_shape:
                return n
            if to_shape[0] == from_shape[0]:
                return Mat([broadcast(to_shape[1:], o) for o in n])
            if len(from_shape) == 1:
                return Mat([n.mat[0]]*to_shape[0])
            n = broadcast(to_shape[1:], n.mat[0])
            return Mat([deepcopy(n) for _ in range(to_shape[0])])

        return broadcast(self.shape, m)

    def set_from_list(self, m):
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

    def generate_mat(self, *shape, random=False, **kwargs):
        #TODO: random
        self.shape = shape
        if len(shape) == 1:
            self.mat = [0]*shape[0]
            self.rank = 1
        else:
            self.mat = [Mat(*shape[1:])]*shape[0]
            self.rank = self.mat[0].rank + 1

    def __getitem__(self, indices):
        if not isinstance(indices, tuple):
            indices = [indices]
        assert self.valid_indices(indices), 'Invalid Indices'
        index = indices[0]
        if len(indices) > 1:
            if isinstance(index,slice):
                return Mat([m[indices[1:]] for m in self.mat[index]])
            return self.mat[index][indices[1:]]
        if isinstance(index,slice):
            return Mat(self.mat[index])
        return self.mat[index]

    def __setitem__(self, indices, M):
        if not isinstance(indices, tuple):
            indices = [indices]
        assert self.valid_indices(indices), 'Invalid Indices'
        #TODO: assert M has valid shape.  Function to generate shape from indices?
        index = indices[0]

        if isinstance(index,slice):
            if len(indices) > 1:
                for m, n in zip(self.mat[index], M):
                    m[indices[1:]] = n
            else:
                self.mat[index] = M
        else:
            if len(indices) > 1:
                self.mat[index][indices[1:]] = M
            else:
                self.mat[index] = M

    def __str__(self, inner=False):
        pad = '\n' if not inner else ''
        header = 'Mat{}'.format(self.shape) if not inner else ''
        header += '\n' if not inner and self.rank == 1 else ''
        if isinstance(self.mat[0], Mat):
            ret = pad+'['+',\n '.join([m.__str__(True) for m in self.mat])+']'+pad
        else:
            ret = str(self.mat)
        return header+ret

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

    #TODO: should this be func? privacy?
    def broadcast_op(self, m, op, bool_op=False):
        m = self.broadcast_if_needed(m)
        if not bool_op or isinstance(self.mat[0], Mat):
            return Mat([op(x,y) for x,y in zip(self.mat,m)])
        else:
            return Mat([int(op(x,y)) for x,y in zip(self.mat,m)])

    def __gt__(self, m):
        return self.broadcast_op(m, gt, True)

    def __ge__(self, m):
        return self.broadcast_op(m, ge, True)

    def __lt__(self, m):
        return self.broadcast_op(m, lt, True)

    def __le__(self, m):
        return self.broadcast_op(m, le, True)

    def __eq__(self, m):
        return self.broadcast_op(m, eq, True)

    def __ne__(self, m):
        return self.broadcast_op(m, ne, True)

    def __add__(self, m):
        return self.broadcast_op(m, add, False)

    def __sub__(self, m):
        return self.broadcast_op(m, sub, False)

    def __mul__(self, m):
        return self.broadcast_op(m, mul, False)

    def __truediv__(self, m):
        return self.broadcast_op(m, truediv, False)

    def __floordiv__(self, m):
        return self.broadcast_op(m, floordiv, False)

    def __mod__(self, m):
        return self.broadcast_op(m, mod, False)

    def __pow__(self, m):
        return self.broadcast_op(m, pow, False)

