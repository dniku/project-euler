s = open("067_triangle.txt", 'r').read()[:-1]

rows = s.split('\n')
arr = [map(int, row.split(' ')) for row in rows]

for i, row in enumerate(arr[1:]):
  row[0] += arr[i][0]
  row[-1] += arr[i][-1]
  for j, val in enumerate(row[1:-1]):
    row[j + 1] += max(arr[i][j], arr[i][j + 1])

print max(arr[-1])