from itertools import permutations
from acmlib import get_nth

print ''.join(get_nth(permutations("0123456789"), 999999))