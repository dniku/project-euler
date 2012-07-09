from acmlib import all_fibs, take_below

print sum(x for x take_below(all_fibs(), 4000000) if x % 2 == 0)