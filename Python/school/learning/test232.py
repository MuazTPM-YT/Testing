matrix = [[1, 2], [3, 4]]
adjoin_matrix = []

print("-"*20)
print("Matrix")
for i in range(len(matrix)):
    adjoin_matrix.append(matrix[i])
    print(matrix[i])

print("-"*20)

print("Adjoin Matrix")
adjoin_matrix = matrix
adjoin_matrix[0][0], adjoin_matrix[1][1] = adjoin_matrix[1][1], adjoin_matrix[0][0]
adjoin_matrix[0][1] *= -1
adjoin_matrix[1][0] *= -1
for j in adjoin_matrix:
    print(j)

print("-"*20)

determinant_matrix = (adjoin_matrix[0][0] * adjoin_matrix[1][1]) - (adjoin_matrix[0][1] * adjoin_matrix[1][0])
inverse_matrix = []

print("Determinant Matrix")
print(determinant_matrix)

print("-"*20)

print("Inverse Matrix")
inverse_matrix = adjoin_matrix
for k in inverse_matrix:
    for x in range(len(inverse_matrix)):
        k[x] /= determinant_matrix
    print(k)

print("-"*20)