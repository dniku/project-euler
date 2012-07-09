import numpy as np
from acmlib import all_factors

def is_abundant(n):
  return sum(all_factors(n)) > n

abundants = filter(is_abundant, xrange(1, 28124))

arr = np.zeros(28123, dtype=np.bool_)

for i, a in enumerate(abundants):
  for b in abundants[i:]:
    val = a + b - 1
    if val >= len(arr):
      break
    arr[val] = True

result = 0
for i in xrange(len(arr)):
  if not arr[i]:
    result += i + 1

print result