from math import exp, tanh

# TODO: Add gradient computation and tracking
# TODO: Add simple functions

class sigmoid:
    def __call__(self, x):
        return 1/(1+exp(-x))
    
class tanh:
    def __call__(self, x):
        return tanh(x)

class relu:
    def __call__(self, x):
        return max(0, x)

class leaky_relu:
    def __call__(self, x):
        assert False #TODO: implement
        return max(0, x)

class swish:
    def __call__(self, x):
        assert False #TODO: implement
        return max(0, x)

__all__ = [
    'cross_entropy_loss',
    'binary_cross_entropy_loss',
    'l1',
    'l2',
    'hinge_loss',
    'hubber_loss',
]
