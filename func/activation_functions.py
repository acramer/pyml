from math import exp, tanh

# TODO: Add gradient computation and tracking
# TODO: Add simple functions

def sigmoid(x):
    return 1/(1+exp(-x))

# class sigmoid:
#     def __call__(self, x):
#         return 1/(1+exp(-x))
    
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
    'sigmoid',
    'tanh',
    'relu',
    'leaky_relu',
    'swish',
]
