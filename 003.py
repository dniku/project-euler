from __future__ import division
from math import sqrt

n = 600851475143
best = 1

for d in xrange(2, int(sqrt(n)) + 1):
  while n % d == 0:
    n //= d
    best = d
  if n == 1:
    break

print best