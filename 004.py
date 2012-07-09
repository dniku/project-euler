def check(num):
  snum = str(num)
  rnum = ''.join(reversed(snum))
  return snum == rnum

def solve():
  best = 0
  for x in xrange(999, 99, -1):
    for y in xrange(x, 99, -1):
      mul = x * y
      if check(mul):
        best = max(best, mul)
  return best

print solve()