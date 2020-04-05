# coleções
import numpy as np

# criação da lista
lista_a = [1, 2, 3]

# criar array a partir da lista
array_a = np.array(lista_a)
print(array_a)

# precisa estar entre colchetes pois ainda é uma lista
array_b = np.array([4, 5, 6, 7])
print(array_b)

# array de n linhas (matriz)
array_c = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])

print(array_c)
print(array_c.shape)

# alterar o formato
array_c = array_c.reshape(4, 2)
print(array_c)
print(array_c.shape)

# criação automatica de arrays
array_d = np.arange(36)
print(array_d)
array_d.resize((6, 6))
print(array_d)


array_d[2, 2]
array_d[3, 3:6]
# condicional
array_d[array_d >= 30]
# alteração
array_d[array_d >= 30] = 30
array_d

# condicional
array_d[array_d >= 30] == 30
