from math import sqrt

# 0 Threshold
__EPSILON__ = 0.001


def normalize(vec):
    """
    Normalizes a n dimensional vector
    """
    d = 0
    for i in len(vec):
        d += vec[i] * vec[i]

    if d < __EPSILON__:
        return vec
    else:
        d = sqrt(d)

    for j in len(vec):
        vec[j] /= d

    return vec