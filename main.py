#
# Module statistic.
# Released to the public domain 15-Feb-2020,
# by Ignacio Aular (ignacio_345@hotmail.com).
#
# Provided as-is; use at your own risk;
# no warranty; no promises; enjoy it!
#

from mct import mct
from md import md
from mrp import mrp
from util.util import rprint, counter
from ftbl import ftc

L = [4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
     6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]


print('Measures of Central Tendency.')
rprint('Mean:', mct.mean(L))
rprint('Median:', mct.median(L))
print('Mode:', mct.mode(L))
print()

print('Measures of Dispersion.')
rprint('Range:', md.rng(L))
rprint('Variance:', md.var(L))
rprint('Standard Deviation:', md.std(L))
print()

print('Measures of Relative Position.')
rprint('Quartile 25%:', mrp.per(L, 25))
rprint('Quartile 50%:', mrp.per(L, 50))
rprint('Quartile 75%:', mrp.per(L, 75))
rprint('Percentile 14%:', mrp.per(L, 14))
rprint('Inter-quartile:', mrp.iqr(L))
print()

dL = counter(L)

print('Frequency Table calculations.')
print('Classes:', ftc.cls(dL))
print('Abs. Frequency:', ftc.afrq(dL))
print('Rel. Frequency:', ftc.rfrq(ftc.afrq(dL)))
print('Cum. Abs. Frequency:', ftc.cafrq(ftc.afrq(dL)))
print('Cum. Rel. Frequency:', ftc.crfrq(ftc.rfrq(ftc.afrq(dL))))
