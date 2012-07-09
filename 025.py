from acmlib import all_fibs

for i, x in enumerate(all_fibs()):
  if len(str(x)) >= 1000:
    print i + 1
    break