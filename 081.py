mat = []
with open("081_matrix.txt", 'r') as fh:
  for line in fh:
    mat.append(map(int, line.split(',')))

SIZE = len(mat)

dyn = [[mat[0][0]]]

def get_elem(y, x):
  if y < 0 or x < 0:
    return 1000000000
  return dyn[y][x]

first = True
for y in xrange(SIZE):
  if not first:
    dyn.append([])
  for x in xrange(SIZE):
    if first:
      first = False
      continue
    left = get_elem(y, x - 1)
    top = get_elem(y - 1, x)
    this = mat[y][x]
    dyn[y].append(min(left, top) + this)

print dyn[-1][-1]