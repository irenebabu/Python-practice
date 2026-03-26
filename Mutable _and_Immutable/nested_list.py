#display list mutability with an example

matrix = [[1, 2], [3, 4]]
new = matrix
new[0][1] = 99

print("Matrix:", matrix)
print("New:",new)
