import numpy as np
empty_array = np.empty((3, 3))
print(empty_array)

ones_array = np.ones((2, 2))
print(ones_array)

zeros_array = np.zeros((4, 4))
print(zeros_array)

random_array = np.random.rand(3, 3)
print(random_array)

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")

squeezed_array = np.squeeze(my_array)
print(squeezed_array)

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

diagonal_sum = np.trace(my_array)
print(f"Soma diagonal: {diagonal_sum}")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_linhas, num_colunas = np.shape(matriz)
print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linha_especifica = np.array([4, 5, 6])
contem_linha = np.isin(matriz, linha_especifica).all(axis=1).any()
print(f"Contém a linha específica? {contem_linha}")

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = np.transpose(matriz)
# Ou, alternativamente: matriz_transposta = matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transposta:")
print(matriz_transposta)

