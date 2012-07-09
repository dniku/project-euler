from __future__ import division
from acmlib import all_factors

for i in xrange(2, 15000):
  num = len(all_factors(i * (i + 1) // 2))
  if num > 500:
    print i, i * (i + 1) // 2, num
    break