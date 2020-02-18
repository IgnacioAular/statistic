
# Measures of Central Tendency (mct.py)
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 12, 2020


def mean(data):
    """ (list of number) -> float
    
    Return the average of the elements in data.
    
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """
    return sum(data) / len(data)


def median(data):
    """ (list of number) -> number
    
    Return the median of the elements in data.
    
    >>> median([1, 2, 3, 4, 5])
    3
    
    >>> median([1, 2, 3, 4, 5, 6])
    3.5
    """
    data.sort()
    n = len(data)
    i = n // 2
    if n % 2 == 0:
        return (data[i - 1] + data[i]) / 2
    return data[i]


def mode(data):
    """ (list of number) -> number
    
    Return the mode of the elements in data or a
    string if there isn't mode.
    
    >>> mode([1, 2, 3, 4, 5])
    'Not'
    
    >>> mode([1, 2, 3, 4, 5, 1])
    [1]
    
    >>> mode([1, 2, 3, 4, 5, 1, 2])
    [1, 2]
    """
    mx = max([data.count(v) for v in data])
    md = []
    for v in data:
        if data.count(v) == mx and v not in md:
            md.append(v)
    return md if len(md) != len(data) else 'Not'


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
