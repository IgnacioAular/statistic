
# Measures of Dispersion (md.py)
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 12, 2020

import sys
import os
from mct import mct

# Change to a top level directory to import
# the mct module from the mct package.
os.chdir('../')
cwd = os.getcwd()
sys.path.append(cwd)


def rng(data):
    """ (list of number) -> number

    Return the range of the elements in data.

    >>> rng([1, 2, 3, 4, 5])
    4
    """
    return max(data) - min(data)


def var(data):
    """ (list of number) -> float

    Return the variance of the elements in data.

    >>> var([1, 2, 3, 4, 5])
    2.0

    >>> var([1, 2, 3, 4, 5, 6])
    2.9166666666666665
    """
    m = mct.mean(data)
    vr = []
    for v in data:
        vr.append((v - m) ** 2)
    return sum(vr) / len(data)


def std(data):
    """ (list of number) -> float

    Return the standard deviation of the elements in L.

    >>> std([1, 2, 3, 4, 5])
    1.4142135623730951

    >>> std([1, 2, 3, 4, 5, 6])
    1.707825127659933
    """
    return var(data) ** .5


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
