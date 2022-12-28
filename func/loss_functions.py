from math import exp

# TODO: Add gradient computation and tracking
# TODO: Add simple functions

class cross_entropy_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x
    
class binary_cross_entropy_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class l1:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class l2:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class hinge_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class hubber_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x

__all__ = [
    'cross_entropy_loss',
    'binary_cross_entropy_loss',
    'l1',
    'l2',
    'hinge_loss',
    'hubber_loss',
]

