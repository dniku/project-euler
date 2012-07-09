a = sum(x * x for x in xrange(1, 101))
b = sum(xrange(1, 101))**2

print abs(a - b)