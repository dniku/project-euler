from acmlib import is_prime

best = 0
ba, bb = 0, 0
for a in xrange(-1000, 1001):
  for b in xrange(-1000, 1001):
    n = 0
    while is_prime(n * n + a * n + b):
      n += 1
    if best < n:
      best = n
      ba, bb = a, b

print ba * bb