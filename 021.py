from acmlib import all_factors

result = 0
for a in xrange(1, 10001):
  b = sum(all_factors(a))
  if b > a and sum(all_factors(b)) == a:
    #print a, b
    result += a + b

print result