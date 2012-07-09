from acmlib import primes_below, is_prime

def check(n):
#  if not is_prime(n):
#    return False
  s = str(n)
  for i in xrange(1, len(s)):
    pre = int(s[i:])
    suf = int(s[:-i])
    if not is_prime(pre) or not is_prime(suf):
      return False
  return True

result = 0
for p in primes_below(1000000)[4:]:
  if check(p):
    result += p

print result