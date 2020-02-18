# Frequency Table Calculations (ftc.py)
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 15, 2020


def cls(d):
    """ (dic{number:int}) -> list of number

    Return the unique values as the classes in data(d).

    >>> cls({4: 9, 5: 8, 6: 9, 7: 10, 8: 8, 9: 6})
    [4, 5, 6, 7, 8, 9]
    """
    return list(d.keys())


def afrq(d):
    """ (dic{number:int}) -> list of number

    Return a the absolute frequency of the elements in data(d).

    >>> afrq({4: 9, 5: 8, 6: 9, 7: 10, 8: 8, 9: 6})
    [9, 8, 9, 10, 8, 6]
    """
    return list(d.values())


def rfrq(d):
    """ (list of int) -> list of float

    Return the relative frequency of the elements in data(d).

    >>> rfrq([9, 8, 9, 10, 8, 6])
    [0.18, 0.16, 0.18, 0.2, 0.16, 0.12]
    """
    return [v / sum(d) for v in d]


def cafrq(d):
    """ (list of int) -> list of int

    Return the cumulative absolute frequency of the elements in data(d).

    >>> cafrq([9, 8, 9, 10, 8, 6])
    [9, 17, 26, 36, 44, 50]
    """
    return [sum(d[0:i + 1]) for i in range(len(d))]


def crfrq(d):
    """ (list of float) -> list of float

    Return the cumulative relative frequency of the elements in data(d).

    >>> cafrq([0.18, 0.16, 0.18, 0.2, 0.16, 0.12])
    [0.18, 0.33999999999999997, 0.52, 0.72, 0.88, 1.0]
    """
    return cafrq(d)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
