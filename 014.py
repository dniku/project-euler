from __future__ import division

def seqlen(num):
  result = 1
  while num != 1:
    result += 1
    if num % 2 == 0:
      num = num // 2
    else:
      num = num * 3 + 1
  return result

best = 0
start = 0
for x in xrange(1, 1000001):
  val = seqlen(x)
  if val > best:
    best = val
    start = x

print start