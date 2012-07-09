import acmlib

fout = open("acmlib_test.out", 'w')

print >>fout, '\n'.join(str(val) for val in acmlib.primes_below(1000000))
exit()

for n in xrange(1, 100):
    print >>fout, n, acmlib.num_factors(n)