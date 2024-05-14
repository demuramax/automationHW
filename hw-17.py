# There is a two-dimensional list of Latin letters. Sort the letters by columns.
# We assume that the list is rectangular.
# DO NOT use built-in functions map and zip.
import numpy as np

matrix = [['a', 'c', 'e'],
          ['f', 'b', 'a'],
          ['a', 'n', 'k'],
          ['e', 'l', 'i']]
# ->
# [['a', 'b', 'a']
#  ['a', 'c', 'e']
#  ['e', 'l', 'i']
#  ['f', 'n', 'k']]

print(len(matrix))

print(matrix[0][1])

num_rows = len(matrix)
num_cols = len(matrix[0])
print(num_cols)

# transforming matrix
matrix_transformed = []
for x in range(num_cols):
    column = []
    for y in range(num_rows):
        column.append(matrix[y][x])
    matrix_transformed.append(column)

print(matrix_transformed)
for col in matrix_transformed:
    col.sort()

print(matrix_transformed)
#transforming matrix back:
matrix_sorted = []
for x in range(num_rows):
    row = []
    for y in range(num_cols):
        row.append(matrix_transformed[y][x])
    matrix_sorted.append(row)

import numpy as np
print(np.matrix(matrix_sorted))
