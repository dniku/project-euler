def solve():
  for a in xrange(1, 1001):
    for b in xrange(1, 1001 - a):
      c = 1000 - a - b
      if a * a + b * b == c * c:
        print a, b, c
        return a * b * c

print solve()