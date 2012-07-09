def score(name):
  return sum(ord(c) - ord('A') + 1 for c in name)

with open("022_names.txt", 'r') as fh:
  names = [name[1:-1] for name in fh.read().split(',')]
  names.sort()
  print sum(score(name) * (i + 1) for i, name in enumerate(names))