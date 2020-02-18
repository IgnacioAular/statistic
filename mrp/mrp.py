# Measures of Relative Position
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 12, 2020


def zvalue(x, mu, sigma):
    """ (number, number, number) -> float

    Return the z value of x.

    >>> zvalue(600, 1300, 600)
    -1.1666666666666667
    """
    return (x - mu) / sigma


def per(data, perc, key=lambda x: x):
    """ (list of number) -> number

    Return the n-th percentile of the elements in data.

    >>> per([1, 2, 3, 4, 5], 25)
    2
    >>> per([1, 2, 3, 4, 5], 50)
    3
    >>> per([1, 2, 3, 4, 5], 75)
    4
    """
    import math
    data.sort()
    perc = perc / 100
    if not data:
        return None
    k = (len(data) - 1) * perc
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(data[int(k)])
    d0 = key(data[int(f)]) * (c - k)
    d1 = key(data[int(c)]) * (k - f)
    return d0 + d1


def iqr(data):
    """ (list of number) -> number

    Return the range inter-quartile of the elements in data.

    >>> iqr([1, 2, 3, 4, 5, 6])
    2.5
    """
    return per(data, 75) - per(data, 25)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
