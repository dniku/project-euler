from __future__ import division
from bisect import bisect_right
from functools import partial
from fractions import gcd
from itertools import takewhile
from math import sqrt
from operator import mul

# utilities

class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

# helper functions

def take_n(gen, n):
    for x in gen:
        if n <= 0:
            break
        n -= 1
        yield x

def take_below(gen, n):
    return takewhile(lambda x: x <= n, gen)

def get_nth(gen, n):
    for i, x in enumerate(gen):
        if i >= n:
            return x

# numbers

fibs = [1, 1]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 21]

def all_fibs():
    for val in fibs:
        yield val
    while True:
        yield fibs[-2]
        fibs.append(fibs[-2] + fibs[-1])

def lcm(a, b): 
    return (a * b) // gcd(a, b)

@memoized
def is_prime(n):
    if n <= 1:
        return False
    for d in primes_below(int(sqrt(n))):
        if n % d == 0:
            return False
    return True

def all_primes():
    global primes
    for p in primes:
        yield p
    while True:
        p += 2
        if is_prime(p):
            yield p
            primes.append(p)

def primes_below(lim):
    if lim <= 1:
        return []
    global primes
    if lim <= primes[-1]:
        pos = bisect_right(primes, lim)
        return primes[:pos]
    for p in xrange(primes[-1], lim + 1, 2):
        if is_prime(p):
            primes.append(p)
    return primes

def all_factors(n):
    result1 = []
    result2 = []
    for d in xrange(1, int(sqrt(n))):
        if n % d == 0:
            result1.append(d)
            result2.append(n // d)
    if result1 and result1[-1] == result2[-1]:
        result2.pop()
    result1.extend(reversed(result2))
    return result1

@memoized
def num_factors(n):
    if n == 1:
        return 1
    res = 2
    for p in primes_below(int(sqrt(n))):
        if n == 1:
            break
        power = 1
        while n % p != 0:
            n //= p
            power += 1
        res *= power
    return res

@memoized
def fact(n):
    return reduce(mul, xrange(2, n + 1))

def C(n, k):
    return fact(n) // (fact(k) * fact(n - k))
