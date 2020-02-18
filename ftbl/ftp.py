from mct import mct
from md import md
from util.util import line, counter
from ftbl.ftc import *

L = [4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]

dataset = counter(L)

# Frequency Table Presentation (ftp.py)
# Developed by Ignacio Aular
# ignacio345@gmail.com
# Wed Feb 15, 2020


def ftbl(data):
    n = 86
    line(n)
    titles = ['xi', 'fi', 'hi', 'Fi', 'Hi']
    fs1 = '| {0:^10} | {1:^15} | {2:^15} | {3:^15} | {4:^15} |'
    print(fs1.format(*titles))
    line(n)

    xi = cls(data)
    af = afrq(data)
    rf = rfrq(afrq(data))
    caf = cafrq(afrq(data))
    crf = crfrq(rfrq(afrq(data)))

    fs2 = '| {0:^10} | {1} | {2:^15.2f} | {3} | {4:^15.2f} |'
    for i in range(len(xi)):
        print(fs2.format(str(xi[i]).zfill(2), str(af[i]).zfill(2).center(15), rf[i],
                         str(caf[i]).zfill(2).center(15), crf[i]), sep='')
    line(n)


def desc(data):
    """ (list of number) -> None

    Show descriptive statistics that summarize the central tendency,
    dispersion and shape of a dataset's distribution.

    >>> desc([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
    -------------------------------------------------------------------------------------------------
    |   N   |  Min  |  Max  |  Mean  | Median |  Mode  | Range |  Var  | Std. Dev |
    -------------------------------------------------------------------------------------------------
    |   11  |   1    |    5     |   3.18  |     3      |     4     |     4     | 1.36 |    1.17    |
    -------------------------------------------------------------------------------------------------
    """
    n = 86
    line(n)
    titles = ['N', 'Min', 'Max', 'Mean', 'Median', 'Mode', 'Range', 'Var', 'Std. Dev']
    fs1 = '| {0:^5} | {1:^5} | {2:^5} | {3:^6} | {4:^6} | {5:^6} | {6:^5} | {7:^5} | {8:^8} |'
    print(fs1.format(*titles))
    line(n)

    fs2 = "| {0:^6}| {1:^6} | {2:^8} | {3:^8.2f}| {4:^10} | {5:^9} | {6:^10}| {7:^4.2f} | {8:^10.2f} |"
    print(fs2.format(len(data), min(data), max(data), mct.mean(data), mct.median(data),
                     mct.mode(data), md.rng(data), md.var(data), md.std(data)))
    line(n)


ftbl(dataset)
