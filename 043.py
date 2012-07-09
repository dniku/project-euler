from itertools import permutations

def check(num):
  primes = (2, 3, 5, 7, 11, 13, 17)
  for i in xrange(1, 7):
    seg = ''.join(num[i:i+3])
    if int(seg) % primes[i - 1] != 0:
      return False
  return True

result = 0
for perm in permutations("0123456789"):
#  if perm[0] == '0':
#    continue
  if check(perm):
    result += int(''.join(perm))
    print ''.join(perm)

print result
