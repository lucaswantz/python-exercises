#
#Faca um script em Python que leia uma matriz 5X5 e gere sua transposta. 
#A matriz transposta e obtida invertendo a matriz original, isto e, as linhas 
#tornar-se-ao colunas e as colunas tornar-se-ao linhas
#

import numpy as np

R = int(input("Numero de linhas:")) 
C = int(input("Numero de colunas")) 

# Inicializacao
matrix = [] 

# for loop para entrada de linhas
for i in range(R):		 
    #lista das colunas que serao lidas
    a =[]
    print("linha",i)
    # for loop para entrada de colunas
    for j in range(C):
        print("coluna",j)
        a.append(int(input()))
    matrix.append(a) 

print(matrix)

# Impressao da matrix
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print()
    
# Impressao da matrix transposta
for i in range(R): 
    for j in range(C): 
        print(matrix[j][i], end = " ") 
    print()

array = np.array(matrix)

print(array)

print(array.T)