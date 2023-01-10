from copy import deepcopy
from operator import *
from math import exp
from functools import reduce

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
            assert len(args) == 0, 'Setting using iterable'
            self.set_from_list(firstElement)
        else:
            assert self.valid_shape(firstElement, *args), 'Invalid Shape'
            M = zeros(firstElement, *args, **kwargs)
            self.mat = M.mat
            self.shape = M.shape
            self.rank = M.rank

    def valid_matrix(self, m):
        #TODO: implement
        return True

    def valid_shape(self, *shape):
        #TODO: implement
        return True

    def valid_indices(self, indices):
        return all([isinstance(i, slice) or (i >= 0 and i < s) for i, s in zip(indices, self.shape)])

    def broadcast_if_needed(self, m, n):
        assert not isinstance(m, list)
        assert not isinstance(n, list)

        if not isinstance(m, Mat):
            m = Mat([m])
        if not isinstance(n, Mat):
            n = Mat([n])

        flipped = False
        if n.rank > m.rank or (n.rank == m.rank and sum(n.shape) > sum(m.shape)):
            m, n = n, m
            flipped = True

        broadcast_failure_string  = 'Unnable to format shape of {} to {}'.format(n.shape, m.shape)

        # Unsqeeze to number of dims
        for _ in range(m.rank-n.rank):
            n = Mat([n])

        if m.shape == n.shape:
            if flipped: m, n = n, m
            return m, n
        assert all([x == y or y == 1 for x,y in zip(m.shape, n.shape)]), broadcast_failure_string

        def broadcast(to_shape, o):
            from_shape = o.shape
            if to_shape == from_shape:
                return o
            if to_shape[0] == from_shape[0]:
                return Mat([broadcast(to_shape[1:], p) for p in o])
            if len(from_shape) == 1:
                return Mat([o.mat[0]]*to_shape[0])
            o = broadcast(to_shape[1:], o.mat[0])
            return Mat([deepcopy(o) for _ in range(to_shape[0])])

        n = broadcast(m.shape, n) 
        if flipped: m, n = n, m
        return m, n

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

    def abs(self):
        if isinstance(self.mat[0], Mat):
            return Mat([m.abs() for m in self.mat])
        else:
            return Mat([abs(m) for m in self.mat])

    def exp(self):
        if isinstance(self.mat[0], Mat):
            return Mat([m.exp() for m in self.mat])
        else:
            return Mat([exp(m) for m in self.mat])
    
    def sum(self,dim=None):
        if self.rank == 1:
            return sum(self.mat)
        if dim is None:
            return sum(m.sum() for m in self.mat)
        assert dim >= 0 and dim < self.rank
        sum_slice = [slice(None) for _ in range(self.rank)]
        sum_slice[dim] = 0
        ret = self.__getitem__(tuple(sum_slice))
        for i in range(1, self.shape[dim]):
            sum_slice[dim] = i
            ret += self.__getitem__(tuple(sum_slice))
        return ret

    def mean(self,dim=None):
        if self.rank == 1:
            return sum(self.mat)/len(self.mat)
        if dim is None:
            return sum(m.mean() for m in self.mat)/len(self.mat)
        assert dim >= 0 and dim < self.rank
        mean_slice = [slice(None) for _ in range(self.rank)]
        mean_slice[dim] = 0
        ret = self.__getitem__(tuple(mean_slice))
        for i in range(1, self.shape[dim]):
            mean_slice[dim] = i
            ret += self.__getitem__(tuple(mean_slice))
        return ret/self.shape[dim]

    #TODO: should this be func? privacy?
    def broadcast_op(self, n, op, bool_op=False):
        m, n = self.broadcast_if_needed(self, n)
        if not bool_op or m.rank > 1:
            return Mat([op(x,y) for x,y in zip(m,n)])
        else:
            return Mat([int(op(x,y)) for x,y in zip(m,n)])

    def flatten(self):
        #TODO: add tests
        if self.rank == 1:
            return self

        ret = []
        for m in self.mat:
            ret+=m.flatten().mat
        return Mat(ret)

    def reshape(self, *shape):
        #TODO: add tests
        #TODO: check shape is valid
        for s in shape:
            #TODO assert s is int
            #TODO assert only one wildcard (-1)
            pass

        current_power = reduce(mul, self.shape, 1)
        new_power = reduce(mul, shape, 1)
        assert new_power == current_power or (new_power < 0 and abs(new_power) <= current_power and current_power%new_power == 0)
        if new_power < 0:
            new_dim = current_power//abs(new_power)
            shape = tuple(s if s>0 else new_dim for s in shape)

        ret = self.flatten().mat
        temp = []
        for s in reversed(shape):
            for _ in range(len(ret)//s):
                temp += [Mat(ret[:s])]
                ret = ret[s:]
            ret = temp
            temp = []
        return ret[0]

    def transpose(self, axis=None):
        if axis is None:
            axis = list(range(self.rank))
            if self.rank > 1:
                axis[0], axis[-1] = axis[-1], axis[0]

        assert set(axis) == set(range(self.rank))

        shape_perm = tuple(self.shape[sidx] for sidx in axis)
        ret = Mat(*shape_perm)

        # TODO: see which way is slower
        # def recursive_for(loop, block)
        #     pass
        
        indices = [(slice(None),)]
        temp = []
        for s in self.shape[-2::-1]:
            for t in indices:
                temp += [(i,)+t for i in range(s)]
            indices = temp
            temp = []

        for idx in indices:
            ret.__setitem__(tuple(idx[sidx] for sidx in axis), self.__getitem__(idx))
        return ret
        #TODO: add tests
        # return mat([self[:,i] for i in range(self.shape[1])])

    def repeat(self, n):
        #TODO: add tests
        #TODO: check n is valid
        return Mat([deepcopy(self) for _ in range(n)])

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

    def __rgt__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m>self

    def __rge__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m>=self

    def __rlt__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m<self

    def __rle__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m<=self

    def __req__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m==self

    def __rne__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m!=self

    def __radd__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m+self

    def __rsub__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m-self

    def __rmul__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m*self

    def __rtruediv__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m/self

    def __rfloordiv__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m//self

    def __rmod__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m%self

    def __rpow__(self, m):
        if not isinstance(m, Mat):
            m = Mat([m])
        return m**self

    def __neg__(self):
        return Mat([-m for m in self.mat])

#TODO: Make static mat funcs
def zeros(*shape, **kwargs):
    return generate_mat(*shape, **kwargs)

def ones(*shape, **kwargs):
    return generate_mat(*shape, **kwargs, num=1)

def rand(*shape, **kwargs):
    return generate_mat(*shape, **kwargs, random=True)

def generate_mat(*shape, num=0, random=False, **kwargs):
    #TODO: random
    ret = Mat([0])
    ret.shape = shape
    if len(shape) == 1:
        ret.mat = [num]*shape[0]
        ret.rank = 1
    else:
        ret.mat = [generate_mat(*shape[1:], num=num, random=random, **kwargs) for _ in range(shape[0])]
        ret.rank = ret.mat[0].rank + 1
    return ret
