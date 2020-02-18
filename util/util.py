
# Utility functions (util.py)
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 13, 2020


def rprint(message, value):
    """ (str, number) -> None

    Show a message with a rounded floating value for 2 decimals.

    >>> rprint('2 decimals:', 43)
    2 decimals: 43.00
    """
    print(message + ' {0:.2f}'.format(value))


def counter(data):
    """ (list of number) -> dic {number:int}

    Return the elements of data as keys and their count as
    values.

    >>> counter([1, 2, 1, 3])
    {1: 2, 2: 1, 3: 1}
    """
    dic = {}
    for v in data:
        dic[v] = data.count(v)
    return dic


def line(n):
    """ (int) -> None

    Print a dashes string of length n.

    >>> line(12)
    ------------
    """
    print('-' * n)


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
