from math import exp

# TODO: Add gradient computation and tracking
# TODO: Add simple functions

class negative_log_likelihood:
    def __call__(self, x):
        assert False #TODO: implement
        return x

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
        # Mean Absolute Error
        assert False #TODO: implement
        return x

class l2:
    def __call__(self, x):
        # Mean Squared Error
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

class margin_ranking_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class triplet_margin_loss:
    def __call__(self, x):
        assert False #TODO: implement
        return x

class kullback_leibler_divergence:
    def __call__(self, x):
        assert False #TODO: implement
        return x

__all__ = [
    'negative_log_likelihood',
    'cross_entropy_loss',
    'binary_cross_entropy_loss',
    'l1',
    'l2',
    'hinge_loss',
    'hubber_loss',
    'margin_ranking_loss',
    'triplet_margin_loss',
    'kullback_leibler_divergence',
]
