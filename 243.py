from __future__ import division
from fractions import Fraction
import numpy as np

def print_debug(i):
  if i % 10000 == 0:
    print i

def solve(lim):
  desired = Fraction(15499, 94744)
  divs = np.arange(2, lim + 1)

  for i in xrange(2, lim // 2 + 1):
    print_debug(i)
    for j in xrange(i * 2, lim + 1, i):
      divs[j - 2] -= 1

  best = Fraction(1)
  ind = 0
  for i in xrange(2, lim + 1):
    print_debug(i)
    resil = Fraction(divs[i - 2], i)
    if resil < best:
      best = resil
      ind = i
    if resil < desired:
      return i
  print ind, best

print solve(1000000)
"""

def resilience(n):
  result = 0
  for i in xrange(1, n):
    if gcd(i, n) == 1:
      result += 1
  return Fraction(result, n)

d = 12
while True:
  d += 1
  if d % 100 == 0:
    print d
  if resilience(d) < b:
    print d
    break  
"""